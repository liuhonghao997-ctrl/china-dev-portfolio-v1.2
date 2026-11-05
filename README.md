# 中文 IT 开发作品集（个人非商业 Demo）

![CI](https://img.shields.io/badge/TypeScript-checked-blue)
**当前版本：v1.2**（中文作品集 + TypeScript 库存管理 Demo）

本仓库是个人非商业技术展示项目，使用模拟数据，不用于真实企业业务。目前不提供收费服务；如未来考虑商业化，会先确认适用规定及雇主政策。

## 本地预览

需要 Node.js 22+ 和 Python 3（用于本地静态服务器）。

```bash
npm install
npm run check
npm run serve
```

访问 http://localhost:8000/ 。注意：库存 Demo 采用 ES module 导入，**请使用本地 HTTP 服务器访问**，不要直接双击 `inventory.html`。

如只需浏览其它静态页面，直接打开 HTML 文件也可以。

## 演示功能

- `index.html`：中文作品集首页，强调为个人技术演示。
- `inventory.html`：库存新增、编辑、删除、搜索、分类、库存预警、CSV 导入导出和 localStorage 保存。
- `csv-tool.html`：双 CSV 联合匹配 `id` / `subid`，导出匹配结果。
- `quote.html`：简单报价单计算和浏览器打印/PDF。

## 技术实现和自动测试

- `src/inventory-core.ts`：纯 TypeScript 库存校验、库存统计、CSV 状态机解析、导入导出逻辑。
- `dist/`：编译后的浏览器可用 JavaScript 文件（随项目包提供，保证不安装工具也能用静态 HTTP 服务预览）。
- `inventory.js`：浏览器交互层，使用 TypeScript 核心输出。
- `tests/`：Node 原生测试，包括 CSV 特殊字符、数据校验、重复 SKU、导入/导出往返。
- `.github/workflows/ci.yml`：push / pull request 后在 GitHub Actions 上安装依赖、构建并运行测试。

```bash
npm run build   # 编译 TypeScript
npm test        # 执行 Node 自动测试（需要先 build）
npm run check  # 构建并测试
```

> 这**不是 Angular 项目**，而是 Angular 迁移前的 TypeScript 业务逻辑抽取。Angular UI 改造需要另一个开发阶段，不应在个人作品集中宣传为 Angular 已实现。

## 公开展示与限制

- 本项目仅是模拟数据和技术 Demo，不含正式账户系统、服务器数据库、权限、多用户、支付或审计日志。
- 数据保存在当前浏览器 localStorage，清除浏览器数据会丢失。
- CSV 导入采取**覆盖**模式，上传前应备份；目前最大 2MB / 1000 行，UTF-8 优先。
- 程序性自动测试通过不等于完整端到端、兼容性或安全测试完成。
- 本项目仅用于非商业技术展示，不接受付费订单，也不用于真实客户或企业数据。开始任何收费服务前，应先确认适用规定及雇主政策。

详情见 `LEGAL_AND_LAUNCH.md`。

## GitHub 仓库与线上演示（检查于 2026-11-05）

- GitHub 仓库：<https://github.com/liuhonghao997-ctrl/china-dev-portfolio-v1.2>
- 默认分支：`main`；仓库为公开仓库。
- 在线作品集：<https://liuhonghao997-ctrl.github.io/china-dev-portfolio-v1.2/>
- TypeScript CI：[运行记录](https://github.com/liuhonghao997-ctrl/china-dev-portfolio-v1.2/actions/runs/41986096528)，检查时已通过。
- GitHub Pages 部署：[运行记录](https://github.com/liuhonghao997-ctrl/china-dev-portfolio-v1.2/actions/runs/41986096656)，检查时已成功。

Actions 状态可能随新提交变化，请以仓库中的最新运行记录为准。

### 最快捷发布

1. 解压项目包，确保 `index.html`、`inventory.html`、`src/`、`dist/`、`.github/` 等位于仓库根目录，而不是外层同名文件夹。
2. 登录 GitHub，进入 `https://github.com/liuhonghao997-ctrl/china-dev-portfolio-v1.2`，通过 **Add file → Upload files** 上传解压后的文件（网页上传时务必保留子目录结构；推荐使用 GitHub Desktop 以避免漏传 `.github` 等隐藏目录）。
3. 如果电脑装有 Git，可在解压后的 `china-dev-portfolio` 目录执行：

```bash
git init
git add .
git commit -m "feat: add Chinese portfolio demos and CI"
git branch -M main
git remote add origin https://github.com/liuhonghao997-ctrl/china-dev-portfolio-v1.2.git
git push -u origin main
```

4. 在 GitHub 仓库 **Settings → Pages → Build and deployment → Source** 选择 **GitHub Actions**。推送 main 后，`.github/workflows/pages.yml` 将尝试构建并发布静态站点。站点预计使用 `https://liuhonghao997-ctrl.github.io/china-dev-portfolio-v1.2/`，以 Pages 实际显示的地址为准，首次发布前不能视为可用。
5. 在仓库的 **Actions** 中查看 `TypeScript CI` 和 `Deploy static portfolio to GitHub Pages` 是否都成功。如果失败，先查看失败日志。

### 本地测试

```bash
npm install
npm run check
python3 -m http.server 8000
```

可选浏览器端到端测试（本次封装环境限制 Chromium 访问 `localhost`，未能完成浏览器验收）：

```bash
python3 -m pip install playwright
python3 -m playwright install chromium
python3 tests/browser_smoke.py
```

**当前页面由原生 HTML/JS 和 TypeScript 核心构成，并非完整 Angular 项目；不得宣传为已经完成 Angular 迁移。**
