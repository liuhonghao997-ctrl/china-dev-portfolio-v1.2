# 项目状态（2026-11-05）

- 项目包：V1.2.0，含中文作品集、库存 Demo、CSV 匹配、报价工具、TypeScript 库存核心、4 项单元测试及两个 GitHub Actions 工作流。
- GitHub 仓库：`liuhonghao997-ctrl/gpt123`，公开，默认分支 `main`。
- 最近检查到的远端提交：`60dd28c`（网页上传）。
- 该远端提交目前缺少 `src/`、`dist/`、`tests/`、`.github/workflows/`。因此库存 Demo 的核心模块缺失，CI/Pages 工作流也未运行。
- 本地单元测试：4 项通过（基于已打包的 `dist/inventory-core.js`）；GitHub Actions 结果待补齐目录后确认。
- Pages 设置及线上页面未能通过当前连接核实。预期地址 `https://liuhonghao997-ctrl.github.io/gpt123/` 尚未确认可访问。
- Angular UI 迁移：未完成。当前项目是原生 HTML/JavaScript + TypeScript 核心。
- 商业接单：暂不启动；公开内容保持为非商业技术演示，不收款、不签约、不使用真实客户数据。

## 下一步

1. 将 V1.2.0 包中的 `src/`、`dist/`、`tests/`、`.github/workflows/` 同步到远端仓库。
2. 查看 GitHub Actions 中 CI 和 Pages 部署结果。
3. 如准备公开非商业网站，在 Settings → Pages 中把 Source 设为 GitHub Actions，再验证实际网址。
4. 后续再安排 Angular UI 迁移与真实浏览器端到端验收。
