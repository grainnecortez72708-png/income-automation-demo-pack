#!/usr/bin/env python3
import argparse, csv, re
from pathlib import Path

KEYWORDS = {
    "urgent": ["urgent", "asap", "today", "马上", "紧急", "今天"],
    "sales": ["price", "quote", "buy", "budget", "报价", "购买", "预算"],
    "support": ["bug", "issue", "error", "not working", "报错", "不能用", "问题"],
    "automation": ["automate", "workflow", "n8n", "zapier", "make", "自动化", "流程"],
}


def classify(text):
    t = text.lower()
    labels = [k for k, words in KEYWORDS.items() if any(w in t for w in words)]
    priority = "high" if "urgent" in labels or ("sales" in labels and "automation" in labels) else "normal"
    if not labels:
        labels = ["general"]
    return ",".join(labels), priority


def main():
    p = argparse.ArgumentParser()
    p.add_argument("input")
    p.add_argument("output")
    args = p.parse_args()
    chunks = [x.strip() for x in re.split(r"\n---+\n", Path(args.input).read_text("utf-8")) if x.strip()]
    with Path(args.output).open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["message", "labels", "priority"])
        w.writeheader()
        for msg in chunks:
            labels, priority = classify(msg)
            w.writerow({"message": msg[:500], "labels": labels, "priority": priority})
    print(f"classified={len(chunks)} output={args.output}")

if __name__ == "__main__":
    main()
