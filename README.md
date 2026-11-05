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

访问 http://localhost:8000/ 。库存 Demo 使用 ES module 导入，请通过本地 HTTP 服务器访问，不要直接双击 `inventory.html`。

## 演示功能

- `index.html`：中文作品集首页，展示个人技术 Demo。
- `inventory.html`：库存新增、编辑、删除、搜索、分类、库存预警、CSV 导入导出和 localStorage 保存。
- `csv-tool.html`：通过 `id` / `subid` 联合匹配两个 CSV，并导出匹配结果。
- `quote.html`：报价单计算和浏览器打印/PDF。

## 技术实现与自动测试

- `src/inventory-core.ts`：库存校验、库存统计、CSV 解析及导入导出逻辑。
- `dist/`：编译后的浏览器 JavaScript 文件。
- `inventory.js`：库存页面交互层，使用 TypeScript 核心逻辑。
- `tests/`：Node 原生自动测试，覆盖 CSV 特殊字符、数据校验、重复 SKU 和导入导出往返。
- `.github/workflows/ci.yml`：在 push 和 pull request 后运行构建与测试。

```bash
npm run build   # 编译 TypeScript
npm test        # 执行自动测试（需要先 build）
npm run check   # 构建并执行测试
```

**本项目不是 Angular 项目。** 当前实现由原生 HTML/JavaScript 和 TypeScript 业务核心构成；Angular UI 迁移属于后续工作，完成前不应宣传为已实现。

## 展示限制

- 本项目仅使用模拟数据，不含正式账户系统、服务器数据库、多用户权限、支付或审计日志。
- 库存数据保存在当前浏览器的 localStorage 中；清除浏览器数据会导致数据丢失。
- CSV 导入采用覆盖模式，导入前请备份数据；目前限制为 2 MB / 1000 行，优先使用 UTF-8 编码。
- 自动化测试通过不代表完整的端到端、兼容性或安全测试均已完成。
- 本项目仅用于非商业技术展示，不接受付费订单，也不用于真实客户或企业数据。开始收费服务前，应先确认适用规定及雇主政策。

更多项目边界说明见 `LEGAL_AND_LAUNCH.md`。

## GitHub 仓库与线上演示

- GitHub 仓库：<https://github.com/liuhonghao997-ctrl/china-dev-portfolio-v1.2>
- 默认分支：`main`；仓库为公开仓库。
- 在线作品集：<https://liuhonghao997-ctrl.github.io/china-dev-portfolio-v1.2/>
- TypeScript CI：[最新检查记录](https://github.com/liuhonghao997-ctrl/china-dev-portfolio-v1.2/actions/runs/41987679192)，检查时已通过。
- GitHub Pages 部署：[最新部署记录](https://github.com/liuhonghao997-ctrl/china-dev-portfolio-v1.2/actions/runs/41987679057)，检查时已成功。

Actions 状态可能随新提交变化，请以仓库中的最新运行记录为准。

## 可选浏览器端测试

如需运行浏览器端测试，可按项目脚本要求安装 Playwright 和 Chromium：

```bash
python3 -m pip install playwright
python3 -m playwright install chromium
python3 tests/browser_smoke.py
```
