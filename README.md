# 中文 IT 开发作品集（个人非商业 Demo）

**当前版本：V1.2.0**

本仓库展示个人技术练习和模拟数据 Demo，不接收订单、不展示虚构客户案例，也不处理真实客户数据。它目前不是商业服务，也不是完整生产系统。

## 本地预览

需要 Node.js 22+ 和 Python 3：

```bash
npm install
npm run check
npm run serve
```

访问 http://localhost:8000/。库存 Demo 使用 ES module，请通过本地 HTTP 服务器打开，不要直接双击 `inventory.html`。

## 演示项目

- `index.html`：中文开发作品集首页。
- `inventory.html`：商品新增、编辑、删除、搜索、分类、库存预警、CSV 导入导出，以及浏览器本地保存。
- `csv-tool.html`：根据 `id` 和 `subid` 联合匹配两张 CSV，并导出结果。
- `quote.html`：报价明细和金额计算，可通过浏览器打印或保存 PDF。

## 技术实现

- `src/inventory-core.ts`：TypeScript 库存校验、统计和 CSV 导入导出逻辑。
- `dist/`：浏览器运行所需的编译产物。
- `tests/`：Node 原生单元测试，覆盖数据校验、CSV 特殊字符、重复 SKU 和导入导出往返。
- `.github/workflows/ci.yml`：GitHub Actions 构建和单元测试。
- `.github/workflows/pages.yml`：GitHub Pages 静态网站部署流程。

此项目尚未迁移成 Angular 应用。它使用原生 HTML/JavaScript 与 TypeScript 库存核心。

## 数据和使用限制

- 库存数据只保存在当前浏览器的 `localStorage`；清除浏览器数据会丢失。
- CSV 导入会覆盖当前库存；导入前请备份。限制为 2 MB / 1000 行，优先使用 UTF-8。
- 项目没有服务器数据库、账号权限、多用户协作、支付或审计功能，不能用作真实库存系统。
- 自动化单元测试不等于完整的浏览器兼容性、安全或生产验收。

## 非商业状态

在确认适用的工作许可、雇主规定和税务要求前，不开展收费服务、签约或客户数据处理。个人合规材料应保存在私密位置，不放入公开仓库。此项目不构成法律或税务意见。

## GitHub 检查记录（2026-11-05）

目标仓库为 [liuhonghao997-ctrl/gpt123](https://github.com/liuhonghao997-ctrl/gpt123)，默认分支为 `main`。最近检查到的提交是 `60dd28c`（网页上传）。该提交包含根目录页面和文档，但缺少 `src/`、`dist/`、`tests/` 与 `.github/workflows/`，所以当时库存页面引用的模块无法在远端加载，GitHub Actions 也没有工作流运行记录。

本 V1.2.0 项目包包含上述缺失目录。将完整项目同步到仓库后，先查看 Actions 中的构建与 Pages 部署运行结果；若要启用 Pages，在仓库 **Settings → Pages → Build and deployment → Source** 选择 **GitHub Actions**。预期网址是 https://liuhonghao997-ctrl.github.io/gpt123/，需以成功部署和实际访问结果为准。

## 本地检查

```bash
npm run build
npm test
npm run check
```

库存核心的 4 项单元测试已在本地预编译产物上通过。GitHub Actions 和线上页面仍需在代码同步后确认。
