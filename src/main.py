import asyncio
from mobilerun import MobileAgent, MobileConfig, LLMProfile

async def main():
    # Use default configuration with built-in LLM profiles
    # 自定义配置 https://docs.mobilerun.ai/framework/sdk/droid-agent

    config = MobileConfig.from_yaml("../config.yaml")

    # Create agent
    # LLMs are automatically loaded from config.llm_profiles
    agent = MobileAgent(
        goal="Open Settings and check battery level",
        config=config,
    )

    # Run agent
    result = await agent.run()

    # Check results (result is a ResultEvent object)
    print(f"Success: {result.success}")
    print(f"Reason: {result.reason}")
    print(f"Steps: {result.steps}")

if __name__ == "__main__":
    asyncio.run(main())
