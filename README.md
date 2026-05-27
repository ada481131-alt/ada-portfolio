# Ada Liu · Personal Portfolio

单页个人主页，聚焦**海外游戏**场景的 AI 产品（玩家客服 / AI 外呼 / AI 营销）。

## 上线前可改（约 1 分钟）

打开 `index.html`，搜索 `const SITE`：

```javascript
const SITE = {
  siteUrl: "https://你的用户名.github.io/ada-portfolio/",
  email: "你的邮箱",
  wechat: "你的微信号",
  xiaohongshu: "", // 有小红书主页再填
};
```

作品弹窗里的 `outcomes` 数组可改成你的真实数据（脱敏后）。

**简历**：`resume.html` 可浏览器打印为 PDF；改经历后同步更新 `index.html` 与 `resume.html`，再上传到 GitHub。

## 交互演示页

| 文件 | 说明 |
|------|------|
| `demo-ai-support.html` | AI 玩家客服（充值/提现/玩法 · RAG + 转人工） |
| `demo-metrics.html` | 玩家客服指标看板（读取本机 Demo 数据） |
| `prd.html` | 五个项目的 PRD 摘要（海外游戏业务语境） |
| `demo-prompt-lab.html` | Prompt A/B 对比与检查项打分 |
| `demo-knowledge-base.html` | 玩家 FAQ 知识库切片 / metadata / 检索预览 |
| `demo-hr-rag.html` | AI 外呼脚本检索（市场 / 分群 / 活动版本） |
| `demo-marketing.html` | AI 营销分群看板 + 增收策略建议 |
| `demo-agent-workbench.html` | 人工坐席工作台（实时对话 / 监控 / 配置） |
| `demo-resume-assistant.html` | AI PM 简历助手（JD 匹配 / 面试题 / 薪资） |
| `moments.html` | 生活向 · 朋友圈原型（非主案例） |

各 Demo 已对齐海外游戏：支付/玩法双库客服、外呼拉新召回、营销 ROI 分群等。

## 更新线上版本（网页上传）

打开 [GitHub 上传页](https://github.com/ada481131-alt/ada-portfolio/upload)（把用户名换成你的），**可以一次拖入下面全部文件**覆盖旧版，然后点 **Commit changes**。等 1～2 分钟强刷页面（`Cmd+Shift+R`）。

### 建议上传的完整文件清单（共 15 个）

| 文件 | 说明 |
|------|------|
| `index.html` | 主页（横滑作品、弹窗、PRD/看板入口） |
| `resume.html` | 简历页 |
| `avatar.jpg` | 头像（约 650KB，必传） |
| `demo-ai-support.html` | 玩家客服 Demo |
| `demo-metrics.html` | 客服指标看板 |
| `demo-prompt-lab.html` | Prompt 对比 |
| `demo-knowledge-base.html` | 知识库治理 |
| `demo-hr-rag.html` | AI 外呼脚本 Demo |
| `demo-marketing.html` | AI 营销分群 Demo |
| `demo-agent-workbench.html` | 人工坐席工作台 Demo |
| `demo-resume-assistant.html` | AI PM 简历助手 |
| `moments.html` | 朋友圈原型（可选） |
| `prd.html` | 五项目 PRD 摘要（完善版） |
| `README.md` | 说明文档 |
| `.nojekyll` | GitHub Pages 需要（空文件即可） |

**不必上传**：`.git` 文件夹、`.DS_Store`。

上传后自检：

- 主页 → 作品横滑 → 点「PRD 摘要」「指标看板」
- `prd.html?p=1` 能打开且章节完整
- `moments.html` 封面、发动态正常

## 本地预览

```bash
cd /Users/liuyao/Desktop/Ada-portfolio
python3 -m http.server 8080
```

浏览器打开：http://localhost:8080

## 部署到 GitHub Pages（免费）

### 1. 创建 GitHub 仓库

1. 打开 https://github.com/new
2. 仓库名建议：`ada-portfolio`（或任意名称）
3. 选 **Public**，不要勾选 README（本地已有）
4. 创建仓库

### 2. 推送代码

在终端执行（把 `YOUR_USERNAME` 换成你的 GitHub 用户名）：

```bash
cd /Users/liuyao/Desktop/Ada-portfolio
git init
git add index.html avatar.jpg README.md .gitignore .nojekyll
git commit -m "Publish Ada Liu portfolio"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ada-portfolio.git
git push -u origin main
```

### 3. 开启 Pages

1. 进入仓库 → **Settings** → **Pages**
2. **Source** 选 `Deploy from a branch`
3. **Branch** 选 `main`，文件夹选 `/ (root)`
4. 保存，等待 1–2 分钟

站点地址：`https://YOUR_USERNAME.github.io/ada-portfolio/`

（若仓库名是 `YOUR_USERNAME.github.io`，则主页在根路径 `https://YOUR_USERNAME.github.io/`）

## 文件说明

| 文件 | 说明 |
|------|------|
| `index.html` | 主页（文案 + 交互 + 站点配置） |
| `avatar.jpg` | 头像 |
| `.nojekyll` | 让 GitHub Pages 正确托管静态资源 |
