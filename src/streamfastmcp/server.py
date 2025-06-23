# server.py
from fastmcp import FastMCP # type: ignore

mcp = FastMCP(name="MyServer")

@mcp.tool()
def greet(name: str) -> str:
    """Greet a user by name."""
    return f"Hello, {name}!"

if __name__ == "__main__":

    mcp.run(transport="streamable-http", 
            host="127.0.0.1", 
            port=8000)