#!/bin/bash
cd "$(dirname "$0")"
PORT=8080
echo "=========================================="
echo "  Ada Portfolio 本地预览"
echo "  主页:     http://localhost:$PORT/"
echo "  竞品Agent: http://localhost:$PORT/demo-competitor-agent.html"
echo "  PRD:      http://localhost:$PORT/prd.html?p=8"
echo "  按 Ctrl+C 停止"
echo "=========================================="
if command -v open >/dev/null 2>&1; then
  open "http://localhost:$PORT/demo-competitor-agent.html"
fi
python3 -m http.server "$PORT"
