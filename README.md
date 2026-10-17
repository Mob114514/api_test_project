# Python API 自动化测试项目

本项目是一个基于 Python + Pytest + Requests 的接口自动化测试框架实践，旨在通过企业级的工程化思维，验证公开 API 的功能及稳定性。

## 🛠️ 技术栈
- **编程语言**: Python 3.12
- **测试框架**: Pytest
- **HTTP 请求**: Requests
- **断言校验**: JSONSchema (结构校验)
- **测试报告**: pytest-html
- **持续集成**: GitHub Actions

## 📂 项目结构
- `test_api.py`: 核心接口测试用例脚本（包含正常路径与异常路径校验）
- `requirements.txt`: 项目依赖清单
- `.github/workflows/pytest.yml`: GitHub Actions CI 流水线配置

## 🚀 如何运行
1. 安装依赖: `pip install -r requirements.txt`
2. 执行测试并生成报告: `pytest test_api.py -v --html=report.html`

## 🤖 CI 自动化流水线
配置了 GitHub Actions 后，每次 `git push` 到 `main` 分支，都会自动触发云端测试流水线。可以在仓库的 `Actions` 标签页下查看最新的自动化测试结果及下载测试报告。
