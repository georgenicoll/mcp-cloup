from fastmcp import Client
import pytest
import asyncio
from .server import mcp


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
        assert any(tool.name == "operations_add" for tool in tools)
        assert any(tool.name == "operations_subtract" for tool in tools)
        assert any(tool.name == "operations_advanced_square" for tool in tools)
        assert any(tool.name == "other-operations_add" for tool in tools)
        assert any(tool.name == "other-operations_subtract" for tool in tools)


@pytest.mark.asyncio
async def test_call_tool_operations_add():
    async with Client(mcp) as client:
        result = await client.call_tool("operations_add", {"x": 5, "y": 3})
        assert int(result.content[0].text) == 8  # Assuming text response


@pytest.mark.asyncio
async def test_call_tool_operations_subtract():
    async with Client(mcp) as client:
        result = await client.call_tool("operations_subtract", {"x": 20, "y": 7})
        assert int(result.content[0].text) == 13


@pytest.mark.asyncio
async def test_call_tool_operations_advanced_square():
    async with Client(mcp) as client:
        result = await client.call_tool("operations_advanced_square", {"x": 12})
        assert int(result.content[0].text) == 144


@pytest.mark.asyncio
async def test_call_tool_other_operations_add():
    async with Client(mcp) as client:
        result = await client.call_tool("other-operations_add", {"x": 5.1, "y": 3.2})
        assert float(result.content[0].text) == pytest.approx(8.3)


@pytest.mark.asyncio
async def test_call_tool_other_operations_subtract():
    async with Client(mcp) as client:
        result = await client.call_tool("other-operations_subtract", {"x": 20.1, "y": 7.2})
        assert float(result.content[0].text) == pytest.approx(12.9)

