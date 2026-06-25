# AIDroidRun — 项目指引

## 项目概述

Android 自动化测试 Agent，基于 [mobilerun](https://mobilerun.ai) SDK 驱动 Android 设备执行任务。

## 参考文档

- [mobilerun 官方文档](https://docs.mobilerun.ai/framework/quickstart)
- [mobilerun GitHub 仓库](https://github.com/droidrun/mobilerun)
- [mobilerun-portal GitHub 仓库](https://github.com/droidrun/mobilerun-portal)
- [Agent config_example.yaml](https://github.com/droidrun/mobilerun/blob/main/mobilerun/config_example.yaml)
- [credentials_example.yaml](https://github.com/droidrun/mobilerun/blob/main/mobilerun/config/credentials_example.yaml)

## 技术栈

- **语言**: Python >= 3.11
- **包管理**: `uv`（见 `uv.lock`，非 pip）
- **核心依赖**: `mobilerun`（外部 SDK，连接智谱 GLM 系列模型）
- **无** lint/format/typecheck/test 配置

## 关键命令

```bash
# 安装依赖
uv sync

# 运行 agent
uv run python src/main.py

# 如需先激活 venv
.venv\Scripts\activate
```

## 安装 mobilerun CLI

```bash
# 仅安装 CLI
uv tool install mobilerun

# 安装 CLI + Python 库
uv pip install mobilerun

# 安装 Deepseek 扩展
uv tool install 'mobilerun[anthropic,deepseek]'

# 安装 Portal APK 到设备并启用无障碍服务
mobilerun setup

# 测试连接
mobilerun ping
```

## CLI 使用示例

```bash
# 默认配置（Google Gemini）
mobilerun run "Open the settings app and tell me the Android version"

# 指定 provider 和 model
mobilerun run "Check the battery level" --provider OpenAI --model gpt-4o

# 启用视觉模式（发送截图给 LLM）
mobilerun run "What app is currently open?" --vision

# 启用推理模式（Manager-Executor 工作流）
mobilerun run "Find a contact named John and send him an email" --reasoning
```

### CLI 常用标志

| 标志 | 说明 |
|------|------|
| `--provider` | LLM 提供商（GoogleGenAI、OpenAI、Anthropic 等） |
| `--model` | 模型名称（如 `gemini-3.1-flash-lite-preview`、`gpt-4o`） |
| `--vision` | 启用截图处理 |
| `--reasoning` | 启用多智能体规划 |
| `--steps N` | 最大执行步数（默认：15） |
| `--debug` | 详细日志 |

## 环境变量（可选）

```bash
# Google Gemini（默认）
export GOOGLE_API_KEY=your-api-key-here

# OpenAI
export OPENAI_API_KEY=your-api-key-here

# Anthropic Claude
export ANTHROPIC_API_KEY=your-api-key-here
```

## Python 脚本使用

```python
import asyncio
from mobilerun import MobileAgent, MobileConfig

async def main():
    config = MobileConfig()
    agent = MobileAgent(
        goal="Open Settings and check battery level",
        config=config,
    )
    result = await agent.run()
    print(f"Success: {result.success}")
    print(f"Reason: {result.reason}")
    print(f"Steps: {result.steps}")

asyncio.run(main())
```

## 项目结构

```
src/
├── main.py              # 入口：创建 MobileAgent 并运行
├── config.yaml          # 所有配置（agent、LLM、device、MCP...）
├── .env                 # API Key（不要提交到 git！）
├── config/
│   └── credentials.yaml # 凭据存储
└── utils/               # 预留工具模块（空）
```

## 关键注意事项

### 配置方式

- `config.yaml` 是唯一配置源，通过 `MobileConfig.from_yaml("config.yaml")` 加载
- **不**使用 pyproject.toml 的项目元数据做运行时配置
- 所有文件路径（prompt/app_cards 等）相对于 `src/` 目录

### LLM

- 所有 LLM 走 OpenAILike provider，base_url = `https://open.bigmodel.cn/api/paas/v4/`
- 多个模型分角色配置：manager/executor/fast_agent/app_opener/structured_output
- API Key 读取顺序：`.env` → 环境变量（`auto` 模式）

### 安全

- **`src/.env` 和 `src/config/credentials.yaml` 均已提交到 git**，包含真实 API Key
- 如推送到远端，务必先清理 git 历史并添加 `.env`、`credentials.yaml` 到 `.gitignore`
- 无 `.gitignore` 文件，`.venv/` 和 `.idea/` 默认被 git 全局规则忽略但未显式配置

### 设备

- 目标设备: Android（serial: `RFCR3153BKL`）
- `auto_setup: true` 会自动安装 Portal APK 并启用无障碍服务
- 默认控件坐标使用绝对像素（`use_normalized_coordinates: false`）

### 开发注意

- 项目非常早期（仅 2 个 commit），无测试、无 CI、无 lint
- 如需调试，修改 `config.yaml` 中 `logging.debug: true`
- 轨迹记录: `save_trajectory: step` + `trajectory_gifs: true` 会生成 GIF
