from fastmcp import Client
import pytest
import asyncio
from .server import mcp  # Import your FastMCP instance


@pytest.fixture
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.mark.asyncio
async def test_list_tools():
    async with Client(mcp) as client:  # In-memory connection
        tools = await client.list_tools()
        assert len(tools) >= 1
        assert any(tool.name == "add" for tool in tools)
        assert any(tool.name == "subtract" for tool in tools)
        assert any(tool.name == "addf" for tool in tools)
        assert any(tool.name == "subtractf" for tool in tools)


@pytest.mark.asyncio
async def test_call_tool_add():
    async with Client(mcp) as client:
        result = await client.call_tool("add", {"x": 5, "y": 3})
        assert int(result.content[0].text) == 8  # Assuming text response


@pytest.mark.asyncio
async def test_call_tool_subtract():
    async with Client(mcp) as client:
        result = await client.call_tool("subtract", {"x": 20, "y": 7})
        assert int(result.content[0].text) == 13


@pytest.mark.asyncio
async def test_call_tool_addf():
    async with Client(mcp) as client:
        result = await client.call_tool("addf", {"x": 5.1, "y": 3.2})
        assert float(result.content[0].text) == pytest.approx(8.3)  # Assuming text response


@pytest.mark.asyncio
async def test_call_tool_subtractf():
    async with Client(mcp) as client:
        result = await client.call_tool("subtractf", {"x": 20.1, "y": 7.2})
        assert float(result.content[0].text) == pytest.approx(12.9)

