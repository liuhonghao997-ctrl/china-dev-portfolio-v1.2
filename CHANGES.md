# V1.3 第二阶段质量补丁

适用仓库：liuhonghao997-ctrl/china-dev-portfolio-v1.2 （main），保留原非商业展示性质。

覆盖以下文件（只上传补丁文件，保持相对路径）：
- quote.js：严格校验数量、单价、税率，并以分为单位计算，非法时禁止打印。
- quote.html：增加可访问的错误提示元素。
- inventory.js：写入 localStorage 失败时保持已有列表不变并提示错误。
- style.css：新增 600px 以下响应式布局、焦点可见提示。
- tests/v13_quality.py：新增加载模拟数据的 Chromium 测试，包括校验、模拟存储失败、移动端横向溢出。
- .github/workflows/ci.yml：在现有 browser-regression 测试后追加 v13_quality.py。

本地检查结果：TypeScript 编译通过；4 项原单元测试通过；两份 JS 文件语法检查通过；报价逻辑 VM 测试通过；新增 Python 脚本语法通过。

注意：本环境阻止 Chromium 导航本地服务器；新增完整 Playwright 测试未在此环境通过或失败，须在 GitHub Actions 中实际运行后判断结果。原有用户已确认的线上功能保持不变。

操作：解压后，把上述文件对应地上传至仓库（不要把整个 v1.2 旧版重新上传），提交到 main，然后检查 Actions 中 verify、browser-regression 和 Pages。遇到失败请提供 Action 日志。
