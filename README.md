# Ada Liu · Personal Portfolio

单页个人主页，聚焦 AI SaaS 产品经理定位。

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

## 更新线上版本（网页上传）

1. 打开 GitHub 仓库 → 进入要更新的文件（如 `index.html`）→ **Edit**
2. 用本地最新文件内容替换 → **Commit changes**
3. 或 **Add file → Upload files** 拖入覆盖
4. 等 1～2 分钟刷新主页

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
