# 🏀 NBA开拓者队智能数据分析系统

> 🇨🇳 专注中国球员杨瀚森的NBA数据追踪与AI智能分析平台

![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![LazyLLM](https://img.shields.io/badge/LazyLLM-0.6.2+-green.svg)
![Kimi AI](https://img.shields.io/badge/Kimi-AI-orange.svg)
![NBA](https://img.shields.io/badge/NBA-Data-red.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📖 项目简介

这是一个基于 **LazyLLM框架** 和 **Kimi AI大模型** 构建的NBA数据分析系统，实时追踪波特兰开拓者队（Portland Trail Blazers）的比赛数据，特别关注中国球员 **杨瀚森（Yang Hansen）** 的表现。

**为什么做这个项目？**
- 🇨🇳 作为中国球迷，想实时追踪中国球员在NBA的表现
- 🤖 探索AI在体育数据分析领域的应用
- 📊 打造一个专业、美观的数据可视化平台
- 🚀 实践LazyLLM框架的实战应用

---

## ✨ 核心功能

### 🎯 1. 实时数据追踪
- ✅ **自动抓取NBA官方API数据**
- ✅ 开拓者队战绩、比赛日程
- ✅ 杨瀚森个人数据（场均得分、篮板、助攻等）
- ✅ 最近10场比赛详细表现
- ✅ 投篮命中率、三分球、正负值等15+统计指标

### 🤖 2. AI智能分析
- ✅ **Kimi大模型深度分析**
- ✅ 球员表现趋势解读
- ✅ 球队战术分析
- ✅ 数据对比和预测建议
- ✅ 中文专业解说

### 🎨 3. 专业级界面
- ✅ **NBA官方风格设计**
- ✅ 开拓者队经典红黑配色
- ✅ 左右分栏布局（主数据 + AI分析）
- ✅ NBA官方球员头像展示
- ✅ 动态进度条、动画效果
- ✅ 响应式设计，支持手机/平板/电脑

### 📊 4. 丰富数据展示
- ✅ **球队数据**: 战绩、胜率、场均得分/失分
- ✅ **球员数据**: 出场次数、场均时间、得分、篮板、助攻、盖帽
- ✅ **投篮数据**: 命中率、罚球率、三分球
- ✅ **比赛细节**: 抢断、失误、犯规、正负值
- ✅ **历史记录**: 近期比赛表现追踪

---

## 🖼️ 界面展示

### 主页布局
```
┌──────────────────────────────────────────────────────┬─────────────────────┐
│                                                      │                     │
│  🏀 PORTLAND TRAIL BLAZERS                           │   🤖 AI智能分析      │
│  波特兰开拓者队 数据分析中心                            │                     │
│                                                      │   Kimi AI实时分析    │
│  ┌─────────────┬─────────────┐                      │   球员表现数据...    │
│  │ 🏆 球队战绩  │ 📊 球队数据  │                      │                     │
│  │ 战绩: 5-2   │ 场均得分     │                      │   (固定右侧栏)       │
│  │ 胜率: 71.4% │ 98.1分      │                      │   (独立滚动)         │
│  └─────────────┴─────────────┘                      │                     │
│                                                      │                     │
│  ┌──────────────────────────────────────┐           │                     │
│  │  👤 杨瀚森 YANG HANSEN                │           │                     │
│  │  [NBA官方头像] 位置:C | 背号:#99      │           │                     │
│  │  身高:7-3 | 体重:280 | 🇨🇳中国        │           │                     │
│  └──────────────────────────────────────┘           │                     │
│                                                      │                     │
│  ┌───────────┬───────────┬───────────┐             │                     │
│  │🏀场均数据  │📈技术统计  │🎯投篮效率  │             │                     │
│  │出场:7场   │场均篮板   │命中率     │             │                     │
│  │时间:7.3分 │4.9个      │38.2%     │             │                     │
│  │得分:10.3分│助攻:0.7   │罚球率     │             │                     │
│  └───────────┴───────────┴───────────┘             │                     │
│                                                      │                     │
│  📅 最近比赛 (完整赛程表)                              │                     │
│  🎮 杨瀚森最近比赛表现 (详细统计)                       │                     │
│                                                      │                     │
└──────────────────────────────────────────────────────┴─────────────────────┘
```

### 特色亮点

#### 🎯 1. AI分析固定在右侧
- 打开页面即可看到AI分析，无需滚动
- 独立滚动区域，不影响主内容浏览
- 宽度450px，提供舒适的阅读体验

#### 🖼️ 2. NBA官方球员头像
- 自动加载高清球员照片
- 智能降级：加载失败时显示国旗
- 圆形头像+白色边框，专业设计

#### 📊 3. 数据可视化
- 胜率/命中率用进度条展示
- 重要数据红色高亮
- 悬停动画效果

#### ⚡ 4. 流畅动画
- 页面加载滑入动画
- 卡片悬停上浮效果
- AI图标脉冲呼吸
- 数字更新平滑过渡

---

## 🚀 快速开始

### 环境要求

```bash
Python 3.12+
LazyLLM 0.6.2+
Kimi API密钥
```

### 安装步骤

#### 1️⃣ 克隆项目
```bash
git clone https://github.com/Minokun/nba-yhs-stats.git
cd nba-yhs-stats
```

#### 2️⃣ 安装依赖
```bash
# 使用uv包管理器（推荐）
uv sync

# 或使用pip
pip install -r requirements.txt
```

#### 3️⃣ 配置API密钥
```bash
# 设置Kimi API密钥
export LAZYLLM_KIMI_API_KEY="your_kimi_api_key_here"
```

💡 **如何获取Kimi API密钥？**
- 访问 [Kimi开放平台](https://platform.moonshot.cn/)
- 注册账号并创建API密钥
- 复制密钥并设置到环境变量

#### 4️⃣ 启动服务
```bash
# 方式1：使用启动脚本
bash run.sh

# 方式2：直接运行
uv run python nba_app.py

# 方式3：使用Python
python nba_app.py
```

#### 5️⃣ 访问系统
```
🌐 主页面: http://localhost:23456
📊 数据API: http://localhost:23456/api/data
🤖 AI分析: http://localhost:23456/api/analysis
```

---

## 🛠️ 技术架构

### 技术栈

| 技术 | 说明 | 版本 |
|------|------|------|
| **Python** | 后端开发语言 | 3.12+ |
| **LazyLLM** | AI应用开发框架 | 0.6.2+ |
| **Kimi AI** | 大语言模型 | kimi-k2-0905-preview |
| **Flask** | Web框架 | 3.0.0+ |
| **Requests** | HTTP库 | 2.31.0+ |
| **BeautifulSoup4** | 网页解析 | 4.12.0+ |

### 系统架构

```
┌─────────────────────────────────────────────────────────┐
│                      用户浏览器                           │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│                  Flask Web服务器                         │
│  ┌─────────────┐  ┌──────────────┐  ┌───────────────┐  │
│  │  路由控制   │  │  数据接口    │  │  AI分析接口   │  │
│  └─────────────┘  └──────────────┘  └───────────────┘  │
└──────────┬───────────────────┬──────────────┬──────────┘
           │                   │              │
           ▼                   ▼              ▼
┌──────────────────┐  ┌────────────────┐  ┌──────────────┐
│ NBA数据抓取模块   │  │  数据处理层    │  │ LazyLLM+Kimi │
│                  │  │                │  │  AI分析引擎   │
│ • 球队数据       │  │ • 数据清洗     │  │              │
│ • 球员数据       │  │ • 统计计算     │  │ • 数据解读   │
│ • 比赛记录       │  │ • JSON生成     │  │ • 趋势分析   │
└──────────────────┘  └────────────────┘  └──────────────┘
           │
           ▼
┌──────────────────────────────────────────────────────────┐
│              NBA中国官方API (api.nba.cn)                   │
│  • 球员比赛数据  • 球队信息  • 实时比分                      │
└──────────────────────────────────────────────────────────┘
```

### 核心模块

#### 1. `nba_data_fetcher.py` - 数据抓取层
```python
class NBADataFetcher:
    """NBA数据获取器 - 从NBA中国官网API抓取真实数据"""
    
    def get_blazers_players()      # 获取球员名单
    def get_blazers_schedule()     # 获取比赛日程
    def get_yang_hansen_stats()    # 获取杨瀚森数据
    def get_team_stats()           # 获取球队统计
    def get_all_data()             # 获取全部数据
```

#### 2. `nba_app.py` - Web服务层
```python
# Flask路由
@app.route('/')                    # 主页面
@app.route('/api/data')            # 数据API
@app.route('/api/analysis')        # AI分析API

# LazyLLM集成
chat = lazyllm.OnlineChatModule(
    source='kimi',
    model='kimi-k2-0905-preview'
)
```

#### 3. `templates/index.html` - 前端界面
- HTML5 + CSS3 + JavaScript
- 响应式设计
- 动画效果
- 数据可视化

---

## 📊 数据说明

### 数据来源

✅ **真实NBA官方数据**

所有数据均来自 **NBA中国官方API** (api.nba.cn)，确保数据的准确性和实时性。

**API端点：**
```
球员比赛数据: https://api.nba.cn/sib/v2/players/{playerId}/games
球员列表:    https://api.nba.cn/sib/v2/players/list
球员新闻:    https://api.nba.cn/cms/v2/news/list
```

### 数据字段

#### 球队数据
```json
{
  "team_name": "Portland Trail Blazers",
  "record": "5-2",
  "wins": 5,
  "losses": 2,
  "win_percentage": 0.714,
  "points_per_game": 98.1,
  "opponent_points_per_game": 101.9,
  "point_differential": -3.7
}
```

#### 杨瀚森个人数据
```json
{
  "player_name": "杨瀚森",
  "number": "99",
  "position": "C",
  "height": "7-3",
  "weight": "280",
  "season_stats": {
    "games_played": 7,
    "minutes_per_game": 7.3,
    "points_per_game": 10.3,
    "rebounds_per_game": 4.9,
    "assists_per_game": 0.7,
    "blocks_per_game": 0.7,
    "field_goal_percentage": 0.382,
    "free_throw_percentage": 0.0
  }
}
```

#### 比赛详细数据
```json
{
  "date": "10月15日",
  "opponent": "GSW",
  "opponent_full": "勇士",
  "minutes": 20.2,
  "points": 9,
  "rebounds": 6,
  "assists": 1,
  "blocks": 1,
  "steals": 0,
  "turnovers": 1,
  "fouls": 4,
  "plus_minus": -12,
  "fg_made": 4,
  "fg_attempted": 11,
  "fg_pct": 36.4,
  "three_made": 1,
  "three_attempted": 4,
  "is_starter": false
}
```

---

## 🎯 特色功能详解

### 1️⃣ 实时数据追踪

**自动数据更新**
- 每次访问页面自动获取最新数据
- 真实的NBA比赛数据
- 精确到分钟的统计

**多维度数据**
- 球队层面：战绩、得失分
- 球员层面：场均数据、投篮效率
- 比赛层面：单场表现、对手信息

### 2️⃣ AI智能分析

**Kimi大模型能力**
- 📖 **数据解读**: 理解复杂的篮球统计数据
- 📈 **趋势分析**: 发现球员表现的趋势和规律
- 🎯 **优劣势分析**: 指出球员的强项和待提升领域
- 💡 **建议提供**: 给出专业的改进建议

**分析示例**
```
🤖 AI分析：杨瀚森近期表现分析

根据最近7场比赛数据，杨瀚森展现出以下特点：

✅ 优势：
• 场均10.3分表现稳定，作为新秀已展现出不错的得分能力
• 篮板能力出色，场均4.9个篮板显示出良好的内线卡位意识
• 盖帽数据场均0.7个，说明防守端有一定威慑力

⚠️ 待提升：
• 罚球命中率较低，需要加强罚球训练
• 场均时间7.3分钟偏少，需要争取更多上场机会
• 助攻数据0.7次，传球意识还需加强

📊 趋势：
从最近的比赛来看，随着适应NBA节奏，出场时间有所增加...
```

### 3️⃣ 专业界面设计

**设计理念**
- 🎨 **NBA官方风格**: 参考NBA.com的设计规范
- 🔴 **球队配色**: 开拓者队经典红黑配色
- 📱 **响应式**: 完美适配各种设备尺寸
- ⚡ **流畅动画**: 提升用户体验

**布局创新**
- 左右分栏设计，主数据 + AI分析并列显示
- AI分析固定右侧，打开即见
- 独立滚动区域，互不干扰

### 4️⃣ 数据可视化

**进度条展示**
```
胜率: ████████████████████░░ 71.4%
投篮命中率: ███████████░░░░░░░░░ 38.2%
```

**颜色编码**
- 🟢 绿色：胜利、正向数据
- 🔴 红色：失败、负向数据、重要强调
- ⚪ 白色：中性数据

---

## 🔧 配置说明

### 环境变量

```bash
# Kimi AI API密钥（必需）
export LAZYLLM_KIMI_API_KEY="your_api_key"

# 服务器端口（可选，默认23456）
export NBA_PORT=23456
```

### 修改配置

#### 更换AI模型
编辑 `nba_app.py`:
```python
chat = lazyllm.OnlineChatModule(
    api_key=kimi_api_key,
    source='kimi',  # 可改为其他模型
    model='kimi-k2-0905-preview'  # 模型版本
)
```

#### 更改端口
编辑 `nba_app.py`:
```python
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=23456)  # 修改端口
```

#### 自定义球员
编辑 `nba_data_fetcher.py`:
```python
self.yang_hansen_id = "1642905"  # 更改球员ID
```

---

## 📈 使用场景

### 适用人群

- 🏀 **NBA球迷**: 追踪喜欢的球队和球员
- 🇨🇳 **中国球迷**: 关注中国球员的NBA表现
- 📊 **数据分析师**: 学习体育数据分析
- 🤖 **AI开发者**: 探索AI在体育领域的应用
- 💻 **Web开发者**: 学习LazyLLM框架实战

### 使用案例

**1. 日常球迷追踪**
```
每天打开系统查看：
✅ 昨晚比赛结果
✅ 杨瀚森表现如何
✅ AI对表现的专业分析
```

**2. 数据研究**
```
导出数据用于：
📊 制作数据报告
📈 趋势分析图表
🎯 球员对比研究
```

**3. 自媒体创作**
```
获取素材用于：
✍️ 撰写球评文章
📹 制作视频内容
📱 社交媒体分享
```

---

## 🎓 技术亮点

### 1. LazyLLM框架应用

**为什么选择LazyLLM？**
- ✅ 简化AI应用开发流程
- ✅ 统一的API接口
- ✅ 支持多种AI模型
- ✅ 完善的中文支持

**代码示例**
```python
# 只需3行代码集成AI
chat = lazyllm.OnlineChatModule(
    source='kimi',
    model='kimi-k2-0905-preview'
)

# 直接调用AI分析
analysis = chat(prompt)
```

### 2. 真实数据接入

**API集成技术**
- HTTP请求与响应处理
- JSON数据解析
- 错误处理与重试机制
- 数据缓存策略

### 3. 前后端分离

**架构优势**
- Flask提供RESTful API
- 前端独立渲染
- 便于扩展和维护
- 支持多客户端

### 4. 响应式设计

**适配方案**
```css
@media (max-width: 1200px) {
    /* 移动端布局调整 */
    .layout { flex-direction: column; }
    .ai-sidebar { width: 100%; }
}
```

---

## 🚧 未来规划

### 短期目标 (1-2个月)

- [ ] 🔔 **数据推送通知**: 比赛结束后自动推送战报
- [ ] 📊 **数据导出功能**: 支持导出Excel/CSV格式
- [ ] 🎨 **多主题切换**: 支持其他NBA球队配色
- [ ] 📱 **移动端App**: 开发原生移动应用

### 中期目标 (3-6个月)

- [ ] 📈 **数据可视化增强**: 添加图表、走势图
- [ ] 🤖 **AI功能扩展**: 
  - 比赛预测
  - 球员对比分析
  - 战术建议
- [ ] 👥 **多球员追踪**: 同时追踪多个球员
- [ ] 🌐 **国际化**: 支持英文界面

### 长期目标 (6个月+)

- [ ] 🎮 **互动功能**: 用户评论、讨论区
- [ ] 📹 **视频集锦**: 自动获取比赛精彩片段
- [ ] 🏆 **历史数据**: 完整赛季历史数据库
- [ ] 🔄 **实时更新**: WebSocket实时推送数据

---

## 🤝 贡献指南

欢迎各种形式的贡献！

### 如何贡献

1. **Fork本项目**
2. **创建特性分支** (`git checkout -b feature/AmazingFeature`)
3. **提交更改** (`git commit -m 'Add some AmazingFeature'`)
4. **推送到分支** (`git push origin feature/AmazingFeature`)
5. **提交Pull Request**

### 贡献方向

- 🐛 **Bug修复**: 发现并修复问题
- ✨ **新功能**: 添加有用的功能
- 📝 **文档完善**: 改进文档说明
- 🎨 **界面优化**: 提升用户体验
- 🧪 **测试覆盖**: 增加测试用例

---

## 📞 联系方式

### 问题反馈

- 🐛 **Bug报告**: 通过GitHub Issues提交
- 💡 **功能建议**: 在Issues中讨论新想法
- 📧 **邮件联系**: [your-email@example.com]

### 社交媒体

- 🐦 Twitter: [@yourhandle]
- 📱 微博: [@你的微博]
- 💬 微信公众号: [公众号名称]

---

## 📄 许可证

本项目采用 **MIT License** 开源协议。

```
MIT License

Copyright (c) 2025 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

详见 [LICENSE](LICENSE) 文件。

---

## 🙏 致谢

感谢以下项目和服务：

- **[LazyLLM](https://github.com/LazyAGI/LazyLLM)** - 优秀的AI应用开发框架
- **[Kimi AI](https://kimi.moonshot.cn/)** - 强大的中文大语言模型
- **[NBA中国](https://china.nba.cn/)** - 提供官方数据API
- **[Flask](https://flask.palletsprojects.com/)** - 轻量级Web框架
- **所有开源贡献者** - 为开源社区做出的贡献

---

## ⭐ Star History

如果这个项目对你有帮助，请给个 **Star** ⭐ 支持一下！

```
⭐ Star数量增长图表（待添加）
```

---

## 📸 更多截图

### 主页全貌
```
[待添加实际截图]
```

### AI分析详情
```
[待添加实际截图]
```

### 移动端展示
```
[待添加实际截图]
```

---

<div align="center">

### 🏀 让数据说话，用AI洞察！

**Made with ❤️ by NBA Fans**

*最后更新: 2025年10月15日*

</div>

---

## 🔖 标签

`#NBA` `#开拓者` `#杨瀚森` `#AI` `#LazyLLM` `#Kimi` `#数据分析` `#Python` `#Flask` `#体育科技`
