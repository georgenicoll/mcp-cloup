# Bridge between cloup and mcp

## Introduction

This library provides the `setup_mcp_tools()` function that automatically converts cloup CLI commands into MCP tools.
`setup_mcp_tools()` traverses your cloup command groups and registers each command as an MCP tool with FastMCP,
making your CLI functions available as tools for AI assistants.

## Build

```shell
uv sync
uv build
```

## Example usage

See [server.py](tests/server.py) in tests.
