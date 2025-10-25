from typing import Any
import cloup
from fastmcp import FastMCP


def _populate_leaves(group_or_comand, found_so_far: list[cloup.Command]):
    if isinstance(group_or_comand, cloup.Group):
        for subcommand in group_or_comand.commands.values():
            _populate_leaves(subcommand, found_so_far)
    else:
        found_so_far.append(group_or_comand)


def setup_tools(mcp: FastMCP[Any], command_or_group: cloup.Command):
    leaves: list[cloup.Command] = []
    _populate_leaves(command_or_group, leaves)

    print(f"Found {len(leaves)} commands: {leaves}")

    for leaf in leaves:
        if leaf.callback:
            mcp.tool(leaf.callback, description=leaf.get_help(cloup.Context(leaf)))
