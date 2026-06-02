#!/usr/bin/env python3
"""Fetch public market intel snippets for career.html (radar + scout)."""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone, timedelta
from pathlib import Path

SCRIPT = Path(__file__).resolve()
if SCRIPT.parent.name == "scripts":
    REPO_ROOT = SCRIPT.parents[2]
    DATA = SCRIPT.parents[1] / "data"
else:
    REPO_ROOT = SCRIPT.parent
    DATA = REPO_ROOT / "career" / "data"

RADAR_QUERIES = [
    ("深圳", "深圳 AI产品经理 招聘 月薪 2025 2026"),
    ("深圳", "深圳 大模型 产品经理 BOSS 薪资"),
    ("远程", "remote AI product manager job LLM SaaS"),
    ("新加坡", "Singapore AI product manager iGaming fintech"),
]

SCOUT_QUERIES = [
    ("AI SaaS", "AI SaaS startup funding round 2025 2026"),
    ("AI客服", "AI customer service startup 融资 创业"),
    ("iGaming AI", "iGaming AI tools market trend"),
    ("副业", "AI product manager side project consulting"),
]


def now_cst() -> str:
    cst = timezone(timedelta(hours=8))
    return datetime.now(cst).strftime("%Y-%m-%dT%H:%M:%S+08:00")


def norm_url(url: str) -> str:
    u = (url or "").strip()
    if u.startswith("//"):
        return "https:" + u
    return u


def search_ddg_html(query: str, max_results: int = 4) -> list[dict]:
    import re
    import urllib.parse
    import urllib.request

    url = "https://html.duckduckgo.com/html/?" + urllib.parse.urlencode({"q": query})
    req = urllib.request.Request(url, headers={"User-Agent": "AdaCareerOS/1.0"})
    try:
        html = urllib.request.urlopen(req, timeout=20).read().decode("utf-8", errors="ignore")
    except Exception as e:
        return [{"title": "网络抓取失败", "snippet": str(e)[:200], "url": ""}]

    items = []
    for m in re.finditer(
        r'class="result__a"[^>]*href="([^"]+)"[^>]*>([^<]+)</a>.*?class="result__snippet"[^>]*>(.*?)</a>',
        html,
        re.DOTALL,
    ):
        link, title, snip = m.group(1), re.sub(r"<[^>]+>", "", m.group(2)), re.sub(r"<[^>]+>", "", m.group(3))
        items.append({"title": title.strip(), "snippet": snip.strip()[:280], "url": norm_url(link.strip())})
        if len(items) >= max_results:
            break
    return items


def search(query: str, max_results: int = 4) -> list[dict]:
    try:
        from duckduckgo_search import DDGS

        items = []
        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=max_results):
                items.append({
                    "title": (r.get("title") or "").strip(),
                    "snippet": (r.get("body") or "").strip()[:280],
                    "url": norm_url((r.get("href") or "").strip()),
                })
        if items:
            return items
    except Exception:
        pass
    return search_ddg_html(query, max_results)


def dedupe(items: list[dict]) -> list[dict]:
    seen: set[str] = set()
    out = []
    for it in items:
        key = re.sub(r"\s+", "", (it.get("title") or "") + (it.get("url") or ""))[:120]
        if not key or key in seen:
            continue
        seen.add(key)
        out.append(it)
    return out


def run_radar() -> dict:
    raw: list[dict] = []
    for region, q in RADAR_QUERIES:
        for hit in search(q, 3):
            raw.append({**hit, "region": region, "tags": ["AI PM", region]})
    items = dedupe(raw)[:12]
    return {
        "type": "radar",
        "updated": now_cst(),
        "source": "github-actions",
        "cadence": "每周一自动更新",
        "items": items or [{"region": "-", "title": "本轮无结果", "snippet": "下周再试或 Cursor 跑市场雷达", "url": "", "tags": []}],
        "disclaimer": "公开摘要，投递前请核实 JD 与薪资",
    }


def run_scout() -> dict:
    raw: list[dict] = []
    for cat, q in SCOUT_QUERIES:
        for hit in search(q, 3):
            raw.append({
                **hit,
                "category": cat,
                "suggestion": "观察",
            })
    items = dedupe(raw)[:10]
    return {
        "type": "scout",
        "updated": now_cst(),
        "source": "github-actions",
        "cadence": "每周五自动更新",
        "items": items or [{"category": "-", "title": "本轮无结果", "snippet": "Cursor 说「创业风口」补跑", "url": "", "suggestion": "观察"}],
        "disclaimer": "不构成投资建议；默认求职优先于副业",
    }


def write_json(path: Path, data: dict) -> None:
    text = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    # flat copy at repo root — GitHub 网页上传不用建子文件夹
    if path.name in ("radar-latest.json", "scout-latest.json"):
        (REPO_ROOT / path.name).write_text(text, encoding="utf-8")
    # archive copy
    stamp = data["updated"][:10]
    kind = data["type"]
    archive = DATA.parent / ("market-radar" if kind == "radar" else "opportunity-scout") / f"{stamp}.json"
    archive.parent.mkdir(parents=True, exist_ok=True)
    archive.write_text(text, encoding="utf-8")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("mode", choices=["radar", "scout", "all"], default="all", nargs="?")
    args = p.parse_args()

    if args.mode in ("radar", "all"):
        write_json(DATA / "radar-latest.json", run_radar())
        print("wrote radar-latest.json")

    if args.mode in ("scout", "all"):
        write_json(DATA / "scout-latest.json", run_scout())
        print("wrote scout-latest.json")


if __name__ == "__main__":
    main()
