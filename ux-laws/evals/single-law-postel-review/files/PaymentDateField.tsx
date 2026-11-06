import { useState } from "react";

// Used on the "Schedule a transfer" screen. The parsed date is sent to the
// payments API as the execution date of the transfer.
const DATE_RE = /^\d{2}\/\d{2}\/\d{4}$/;

export function PaymentDateField({ onChange }: { onChange: (d: Date) => void }) {
  const [value, setValue] = useState("");
  const [error, setError] = useState<string | null>(null);

  function commit(raw: string) {
    if (!DATE_RE.test(raw)) {
      setValue("");                // clear what the user typed
      setError("Invalid input");
      return;
    }
    const [dd, mm, yyyy] = raw.split("/").map(Number);
    setError(null);
    onChange(new Date(yyyy, mm - 1, dd)); // silently read as DD/MM/YYYY
  }

  return (
    <div>
      <label htmlFor="pay-date">Payment date</label>
      <input
        id="pay-date"
        placeholder="dd/mm/yyyy"
        value={value}
        onChange={(e) => setValue(e.target.value)}
        onBlur={(e) => commit(e.target.value.trim())}
      />
      {error && <span className="error">{error}</span>}
    </div>
  );
}
