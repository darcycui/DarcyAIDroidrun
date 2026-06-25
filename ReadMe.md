
## 参考文档

[官网文档 mobilerun](https://docs.mobilerun.ai/framework/quickstart)

[Github仓库 mobilerun](https://github.com/droidrun/mobilerun)

[Github仓库 mobilerun-portal](https://github.com/droidrun/mobilerun-portal)

[Agent config_example.yaml](https://github.com/droidrun/mobilerun/blob/main/mobilerun/config_example.yaml)

[ApiKey credentials_example.yaml](https://github.com/droidrun/mobilerun/blob/main/mobilerun/config/credentials_example.yaml)

## 是什么
基于AI + Android无障碍服务实现的UI自动化项目

## 怎么使用
运行脚本 main.py

#### 安装 UV 软件
项目使用uv管理依赖，请根据需要安装。

```shell
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### 安装 droidrun 仅CLI

```shell
uv tool install mobilerun
```

#### 安装 droidrun CLI 和 Python

```shell
uv pip install mobilerun
```

#### 安装Deepseek扩展

```shell
uv tool install 'mobilerun[anthropic,deepseek]'
```

#### 安装门户 APK 

```shell
mobilerun setup
```

命令自动执行：

1. 下载最新的 Portal 应用程序包
2. 将其安装在您的连接设备上。
3. 启用无障碍服务

#### 测试连接

```shell
mobilerun ping

# 显示如下输出即成功
Portal is installed and accessible. You're good to go!
```

#### 设置大模型
```shell
mobilerun configure
```

#### 设置环境变量(可选)

```shell
# For Google Gemini (default)
export GOOGLE_API_KEY=your-api-key-here

# For OpenAI
export OPENAI_API_KEY=your-api-key-here

# For Anthropic Claude
export ANTHROPIC_API_KEY=your-api-key-here
```

#### 用自然语言 通过CLI来控制：

```shell
# Using default configuration (Google Gemini)
mobilerun run "Open the settings app and tell me the Android version"

# Override provider and model
mobilerun run "Check the battery level" --provider OpenAI --model gpt-4o

# Enable vision mode (sends screenshots to LLM)
mobilerun run "What app is currently open?" --vision

# Enable reasoning mode (uses Manager-Executor workflow for complex tasks)
mobilerun run "Find a contact named John and send him an email" --reasoning
```

常见的 CLI 标志：

- `--provider`- 语言模型提供商（如 GoogleGenAI、OpenAI、Anthropic 等）
- `--model`- 模型名称（如 gemini-3.1-flash-lite-preview、gpt-4o 等）
- `--vision`- 启用截图处理功能
- `--reasoning`- 启用多智能体规划模式
- `--steps N`- 最大执行步数（默认：15）
- `--debug`- 启用详细日志记录功能

#### 用自然语言 通过脚本控制

直接运行脚本 main.py 即可。
