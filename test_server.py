"""Test client for MCP Server on Cloud Run.

This module contains test routines to programmatically verify and exercise
the registered tools on the running MCP server.
"""

import asyncio

from fastmcp import Client

async def test_server():
    """Client test routine that connects to the local FastMCP server and calls tools."""
    # Test the MCP server using streamable-http transport.
    # Use "/sse" endpoint if using sse transport.
    async with Client("http://localhost:8080/mcp") as client:
        # List available tools
        tools = await client.list_tools()
        for tool in tools:
            print(f">>> Tool found: {tool.name}")
        
        # Call add tool
        print(">>>  Calling add tool for 1 + 2")
        result = await client.call_tool("add", {"a": 1, "b": 2})
        print(f"<<<  Result: {result[0].text}")
        
        # Call subtract tool
        print(">>>  Calling subtract tool for 10 - 3")
        result = await client.call_tool("subtract", {"a": 10, "b": 3})
        print(f"<<< Result: {result[0].text}")

        # Call multiply tool
        print(">>>  Calling multiply tool for 6 * 7")
        result = await client.call_tool("multiply", {"a": 6, "b": 7})
        print(f"<<< Result: {result[0].text}")

        # Call slugify tool
        print(">>>  Calling slugify tool for 'Hello World! Super_Cool_Feature'")
        result = await client.call_tool("slugify", {"text": "Hello World! Super_Cool_Feature"})
        print(f"<<< Result: {result[0].text}")

        # Call get_current_date_iso tool
        print(">>>  Calling get_current_date_iso tool")
        result = await client.call_tool("get_current_date_iso", {})
        print(f"<<< Result: {result[0].text}")

        # Call get_popular_orders_by_state tool
        print(">>>  Calling get_popular_orders_by_state tool for 'NY'")
        result = await client.call_tool("get_popular_orders_by_state", {"state": "NY"})
        print(f"<<< Result: {result[0].text}")

if __name__ == "__main__":
    asyncio.run(test_server())