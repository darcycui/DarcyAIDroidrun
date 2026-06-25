import asyncio
import os
from pathlib import Path
from dotenv import load_dotenv
from mobilerun import MobileAgent, MobileConfig

async def main():
    os.chdir(Path(__file__).parent)
    load_dotenv(".env")

    config = MobileConfig.from_yaml("config.yaml")

    # Create agent
    # LLMs are automatically loaded from config.llm_profiles
    agent = MobileAgent(
        goal="打开设置，查看手机电量剩余百分比",
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
