"""Append-only hash-chained provenance ledger (the governance spine).

Each entry commits to: its payload + the previous entry's hash.
Tamper with any byte -> verify() reports the exact break point.
Accumulate-not-replace: entries are only ever appended.

Entry layout:
  {seq, ts, kind, payload, prev_hash, entry_hash}
"""

from __future__ import annotations

import hashlib
import json
import os
import time

GENESIS_HASH = "0" * 64


def _canonical(obj) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")


def _hash(prev_hash: str, seq: int, ts: str, kind: str, payload: dict) -> str:
    h = hashlib.sha256()
    h.update(prev_hash.encode("utf-8"))
    h.update(_canonical({"seq": seq, "ts": ts, "kind": kind, "payload": payload}))
    return h.hexdigest()


class Ledger:
    def __init__(self, path: str):
        self.path = path
        os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
        if not os.path.exists(path):
            open(path, "w", encoding="utf-8").close()

    def _read_raw(self):
        entries = []
        with open(self.path, "r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if line:
                    entries.append(json.loads(line))
        return entries

    def append(self, kind: str, payload: dict) -> dict:
        entries = self._read_raw()
        prev = entries[-1]["entry_hash"] if entries else GENESIS_HASH
        entry = {
            "seq": len(entries),
            "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "kind": kind,
            "payload": payload,
        }
        entry["prev_hash"] = prev
        entry["entry_hash"] = _hash(prev, entry["seq"], entry["ts"], kind, payload)
        with open(self.path, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(entry, sort_keys=True) + "\n")
        return entry

    def read_all(self):
        return self._read_raw()

    def verify(self) -> dict:
        """Re-hash the full chain. Returns {ok, checked, break_at}."""
        entries = self._read_raw()
        prev = GENESIS_HASH
        for i, e in enumerate(entries):
            if e.get("prev_hash") != prev:
                return {"ok": False, "checked": i, "break_at": i,
                        "reason": "prev_hash link broken"}
            expect = _hash(e["prev_hash"], e["seq"], e["ts"], e["kind"], e["payload"])
            if e.get("entry_hash") != expect:
                return {"ok": False, "checked": i, "break_at": i,
                        "reason": "entry_hash mismatch (payload tampered?)"}
            prev = e["entry_hash"]
        return {"ok": True, "checked": len(entries), "break_at": None, "reason": None}
