from typing import Any, Optional
import click.core as clic_core
import cloup
from fastmcp import FastMCP


def _populate_leaves(
    prefix: str,
    group_or_command: clic_core.Command,
    found_so_far: list[tuple[str, clic_core.Command]]
):
    if isinstance(group_or_command, cloup.Group):
        for subcommand in group_or_command.commands.values():
            if subcommand.name:
                new_prefix = f"{prefix}_{subcommand.name}" if prefix else subcommand.name
                _populate_leaves(new_prefix, subcommand, found_so_far)
    else:
        found_so_far.append((prefix, group_or_command))


def setup_mcp_tools(mcp: FastMCP[Any], group_or_command: cloup.Command):
    leaves: list[tuple[str, clic_core.Command]] = []
    _populate_leaves('', group_or_command, leaves)

    print(f"Found {len(leaves)} commands: {leaves}")

    for name, command in leaves:
        if command.callback:
            mcp.tool(command.callback, name=name, description=command.get_help(cloup.Context(command)))
