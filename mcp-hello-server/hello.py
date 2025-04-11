# MCP Hello server file

# fastmcp officially part of python sdk for mcp

# fastmcp is the fishing net

# with fastmcp we can create tools and resources. 


from mcp.server.fastmcp import FastMCP
# from 
from fastmcp import FastMCP

print('MCP server details')
_mcp = FastMCP 
print(_mcp)
print('new')
new = FastMCP
print(new)

mcp = FastMCP("hello-world")

# decorator

@mcp.tool() 

# tool say_hello is exposed as an external tool

async def say_hello(name: str) -> str:
    """say hello to thanga

    Args:
        name: The debusgger name

    """
    return f"Hello, {name} !"

if __name__ == "__main__":
    mcp.run(transport='stdio')    # stdio -> standard input output stream is communicating with the client.


