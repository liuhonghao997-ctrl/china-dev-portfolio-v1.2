# V1.3 GitHub Actions 浏览器回归测试补丁

目标仓库：https://github.com/liuhonghao997-ctrl/china-dev-portfolio-v1.2

此次只需添加/替换两个文件，**不要覆盖项目其他文件**：

1. 将 `tests/browser_regression.py` 添加到对应路径（使用此前已在 Windows 本地输出 `BROWSER_REGRESSION_OK` 的测试脚本）。
2. 将 `.github/workflows/ci.yml` 替换为本补丁中的版本（保留原 TypeScript 测试，并新增 Playwright 浏览器回归测试 job）。
3. 将两项变更作为一个 Git 提交推送到 `main`，或通过 Pull Request 合并。
4. 检查 https://github.com/liuhonghao997-ctrl/china-dev-portfolio-v1.2/actions/workflows/ci.yml 。应出现 `verify` 和 `browser-regression` 两个 job，均成功才算本次 CI 通过。

## 本地运行

```sh
npm install
npm run build
python -m pip install playwright==1.56.0
python -m playwright install chromium
python tests/browser_regression.py
```

说明：本补丁仅做过 Python 语法检查。之前的测试通过是用户在 Windows 本地针对 V1.2 的运行结果。本补丁尚未运行 GitHub Actions，不能宣称 CI 已通过。
