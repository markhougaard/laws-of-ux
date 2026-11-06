#!/usr/bin/env bash
# Install the ux-laws skill for one or more agent harnesses.
#
#   scripts/install.sh [options]
#
#   -H, --harness LIST   comma-separated: claude, codex, opencode, agents, all
#                        (default: all = claude + agents)
#                          claude    ~/.claude/skills            .claude/skills
#                          codex     ~/.agents/skills            .agents/skills
#                          agents    same as codex; the shared Agent Skills
#                                    location, also read by OpenCode
#                          opencode  ~/.config/opencode/skills   .opencode/skills
#   -p, --project [DIR]  install into a project (default: current directory)
#                        instead of the user's home
#   -d, --dir DIR        install into DIR/ux-laws instead (any other agent)
#   -l, --link           symlink to this checkout instead of copying, so
#                        a git pull updates the installed skill
#   -f, --force          replace an existing install
#   -u, --uninstall      remove the skill from the chosen locations
#   -a, --agents-md FILE also add (or refresh) a block in FILE (an AGENTS.md
#                        or similar) telling agents without skill support
#                        where the skill is and when to use it
#   -h, --help
#
# Copies exclude evals/ (test fixtures, not needed at run time).
# Works with bash 3.2+ (macOS default) and Linux.
set -euo pipefail

SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/ux-laws"
NAME="ux-laws"
harnesses="all"; project=""; dir=""; link=0; force=0; uninstall=0; agents_md=""

die() { echo "install.sh: $*" >&2; exit 1; }
usage() { sed -n '2,/^set -euo/p' "${BASH_SOURCE[0]}" | sed '$d' | sed 's/^# \{0,1\}//'; exit "${1:-0}"; }

while [ $# -gt 0 ]; do
  case "$1" in
    -H|--harness) [ $# -ge 2 ] || die "$1 needs a value"; harnesses="$2"; shift 2 ;;
    -p|--project)
      if [ $# -ge 2 ] && [ "${2#-}" = "$2" ]; then project="$2"; shift 2; else project="."; shift; fi ;;
    -d|--dir) [ $# -ge 2 ] || die "$1 needs a value"; dir="$2"; shift 2 ;;
    -l|--link) link=1; shift ;;
    -f|--force) force=1; shift ;;
    -u|--uninstall) uninstall=1; shift ;;
    -a|--agents-md) [ $# -ge 2 ] || die "$1 needs a value"; agents_md="$2"; shift 2 ;;
    -h|--help) usage 0 ;;
    *) echo "install.sh: unknown option $1" >&2; usage 1 ;;
  esac
done

[ -f "$SRC/SKILL.md" ] || die "can't find $SRC/SKILL.md"

# Resolve target skills directories (one per line).
targets=""
add() { case $'\n'"$targets"$'\n' in *$'\n'"$1"$'\n'*) ;; *) targets="${targets:+$targets$'\n'}$1" ;; esac; }
if [ -n "$dir" ]; then
  add "$dir"
else
  if [ -n "$project" ]; then base="$(cd "$project" && pwd)"; else base="$HOME"; fi
  IFS=',' read -r -a list <<< "$harnesses"
  for h in "${list[@]}"; do
    case "$h" in
      all)          add "$base/.claude/skills"; add "$base/.agents/skills" ;;
      claude)       add "$base/.claude/skills" ;;
      codex|agents) add "$base/.agents/skills" ;;
      opencode)     if [ -n "$project" ]; then add "$base/.opencode/skills"; else add "${XDG_CONFIG_HOME:-$HOME/.config}/opencode/skills"; fi ;;
      *) die "unknown harness '$h' (use claude, codex, opencode, agents or all)" ;;
    esac
  done
fi

# Only ever delete something that is a ux-laws install (or a link to one).
is_ours() { [ -L "$1" ] || { [ -f "$1/SKILL.md" ] && grep -q "^name: $NAME\$" "$1/SKILL.md"; }; }

remove() {
  local t="$1"
  if [ -L "$t" ]; then rm "$t"
  elif [ -e "$t" ]; then
    is_ours "$t" || die "$t exists and isn't a $NAME skill; not touching it"
    rm -rf "$t"
  fi
}

installed=""
while IFS= read -r skills_dir; do
  t="$skills_dir/$NAME"
  if [ "$uninstall" = 1 ]; then
    if [ -e "$t" ] || [ -L "$t" ]; then remove "$t"; echo "removed   $t"; else echo "absent    $t"; fi
    continue
  fi
  if [ -e "$t" ] || [ -L "$t" ]; then
    [ "$force" = 1 ] || die "$t already exists (use --force to replace it)"
    remove "$t"
  fi
  mkdir -p "$skills_dir"
  if [ "$link" = 1 ]; then
    ln -s "$SRC" "$t"; echo "linked    $t -> $SRC"
  else
    mkdir "$t"
    (cd "$SRC" && tar cf - --exclude ./evals .) | (cd "$t" && tar xf -)
    echo "installed $t"
  fi
  installed="${installed:-$t}"
done <<< "$targets"

if [ -n "$agents_md" ] && { [ "$uninstall" = 0 ] || [ -f "$agents_md" ]; }; then
  start="<!-- ux-laws:start -->"; end="<!-- ux-laws:end -->"
  tmp="$(mktemp)"
  if [ -f "$agents_md" ]; then
    awk -v s="$start" -v e="$end" '$0==s{skip=1} !skip{print} $0==e{skip=0}' "$agents_md" > "$tmp"
  fi
  if [ "$uninstall" = 0 ]; then
    path="${installed:-$SRC}"
    # In a project, write a project-relative path so the file can be committed.
    if [ -n "$project" ]; then path="${path#"$base"/}"; fi
    # strip trailing blank lines before appending
    if [ -s "$tmp" ]; then printf '%s\n\n' "$(cat "$tmp")" > "$tmp"; fi
    cat >> "$tmp" <<EOF
$start
## UX laws

For UX or usability advice, UI design or front-end guidance, or a review of a design, screenshot, prototype or UI diff, read \`$path/SKILL.md\` and follow it. Paths in that skill are relative to \`$path\`.
$end
EOF
  fi
  mv "$tmp" "$agents_md"
  if [ "$uninstall" = 1 ]; then echo "updated   $agents_md (block removed)"; else echo "updated   $agents_md"; fi
fi
