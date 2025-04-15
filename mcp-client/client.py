import asyncio
from contextlib import AsyncExitStack
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    server_script_path = "/Users/thangaraj/Documents/projects/MCP/MCP_fahd/mcp-hello-server/hello.py"

    server_params = StdioServerParameters(
        command="python",
        args=[server_script_path],
        env=None
    )

    async with AsyncExitStack() as stack:
        stdio_transport = await stack.enter_async_context(stdio_client(server_params))
        session = await stack.enter_async_context(ClientSession(*stdio_transport))

        await session.initialize()
        result = await session.call_tool("say_hello", {"name" : "Thanga MCP"})

        print(result.content.text)

asyncio.run(main())        


