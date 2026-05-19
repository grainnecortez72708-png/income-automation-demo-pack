#!/usr/bin/env python3
import argparse, csv
from pathlib import Path


def clean_value(v):
    return " ".join((v or "").strip().split())


def main():
    p = argparse.ArgumentParser()
    p.add_argument("input")
    p.add_argument("output")
    p.add_argument("--dedupe", help="column name for dedupe")
    args = p.parse_args()

    inp, out = Path(args.input), Path(args.output)
    with inp.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
        fields = rows[0].keys() if rows else []

    seen = set()
    cleaned = []
    for row in rows:
        r = {k: clean_value(v) for k, v in row.items()}
        if args.dedupe:
            key = r.get(args.dedupe, "").lower()
            if key and key in seen:
                continue
            if key:
                seen.add(key)
        cleaned.append(r)

    with out.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(fields))
        w.writeheader()
        w.writerows(cleaned)
    print(f"cleaned_rows={len(cleaned)} output={out}")

if __name__ == "__main__":
    main()
