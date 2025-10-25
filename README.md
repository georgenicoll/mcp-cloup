# Bridge between cloup and mcp

## Introduction

This library provides `setup_tools()` function that automatically converts cloup CLI commands into MCP tools. It traverses your cloup command groups and registers each command as an MCP tool with FastMCP, making your CLI functions available as tools for AI assistants.

## Build

```shell
uv sync
uv build
```

## Example usage

See [server.py](tests/server.py) in tests.
