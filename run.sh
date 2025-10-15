#!/bin/bash

# NBA开拓者队数据分析系统启动脚本

echo "🏀 NBA开拓者队数据分析系统"
echo "=============================="
echo ""

# 检查API密钥
if [ -z "$LAZYLLM_KIMI_API_KEY" ]; then
    echo "⚠️  警告: 未设置 LAZYLLM_KIMI_API_KEY 环境变量"
    echo "AI分析功能将无法使用"
    echo ""
    echo "请设置API密钥："
    echo "export LAZYLLM_KIMI_API_KEY='your_api_key_here'"
    echo ""
    echo "按Enter继续运行（仅展示数据，不含AI分析）..."
    read
fi

# 启动应用
echo "正在启动应用..."
uv run python nba_app.py
