#!/usr/bin/env python3
"""Copy assets/announcement.json 'message' onto the merged all-apps.json.

SideStore / AltStore show the news[] item. LCSign / Feather-style clients
also read a root 'message' field for the announcement banner.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ANNOUNCEMENT = ROOT / "assets" / "announcement.json"
ALL_APPS = ROOT / "all-apps.json"


def main() -> None:
    if not ANNOUNCEMENT.exists() or not ALL_APPS.exists():
        return
    extra = json.loads(ANNOUNCEMENT.read_text(encoding="utf-8"))
    message = extra.get("message")
    if not message:
        return
    data = json.loads(ALL_APPS.read_text(encoding="utf-8"))
    data["message"] = message
    ALL_APPS.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print("==> Injected source announcement into all-apps.json")


if __name__ == "__main__":
    main()
