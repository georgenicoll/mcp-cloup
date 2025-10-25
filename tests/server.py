from fastmcp import FastMCP
from mcp_cloup import setup_tools
from .cli import main


mcp = FastMCP("mcp_cloup")


setup_tools(mcp, main)


if __name__ == "__main__":
    mcp.run()