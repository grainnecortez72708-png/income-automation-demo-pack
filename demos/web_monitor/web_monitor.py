#!/usr/bin/env python3
import argparse, hashlib, json, re, sys, time
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


def fetch_text(url: str) -> str:
    req = Request(url, headers={"User-Agent": "Mozilla/5.0 web-monitor-mini/1.0"})
    with urlopen(req, timeout=20) as r:
        raw = r.read().decode("utf-8", errors="ignore")
    text = re.sub(r"<script[\s\S]*?</script>", " ", raw, flags=re.I)
    text = re.sub(r"<style[\s\S]*?</style>", " ", text, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text[:200000]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--url", required=True)
    p.add_argument("--state", default="state.json")
    args = p.parse_args()
    state_path = Path(args.state)
    old = json.loads(state_path.read_text("utf-8")) if state_path.exists() else {}
    try:
        text = fetch_text(args.url)
        h = hashlib.sha256(text.encode()).hexdigest()
        previous = old.get(args.url)
        state = {**old, args.url: {"hash": h, "checked_at": int(time.time()), "preview": text[:500]}}
        state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2), "utf-8")
        if previous and previous.get("hash") != h:
            print(json.dumps({"changed": True, "url": args.url, "old_hash": previous.get("hash"), "new_hash": h, "preview": text[:500]}, ensure_ascii=False))
        elif previous:
            print(json.dumps({"changed": False, "url": args.url, "hash": h}, ensure_ascii=False))
        else:
            print(json.dumps({"changed": None, "url": args.url, "hash": h, "message": "baseline saved"}, ensure_ascii=False))
    except (HTTPError, URLError, TimeoutError) as e:
        print(json.dumps({"error": str(e), "url": args.url}, ensure_ascii=False), file=sys.stderr)
        sys.exit(2)

if __name__ == "__main__":
    main()
