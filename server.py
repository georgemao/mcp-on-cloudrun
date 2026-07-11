"""MCP Server on Cloud Run.

This module implements a FastMCP server designed to run on Google Cloud Run.
It exposes mathematical, string formatting, date/time, and mock business tools.
"""

import asyncio
from datetime import datetime
import logging
import os
import re

from fastmcp import FastMCP 

logger = logging.getLogger(__name__)
logging.basicConfig(format="[%(levelname)s]: %(message)s", level=logging.INFO)

mcp = FastMCP("MCP Server on Cloud Run")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Use this to add two numbers together.
    
    Args:
        a: The first number.
        b: The second number.
    
    Returns:
        The sum of the two numbers.
    """
    logger.info(f">>> Tool: 'add' called with numbers '{a}' and '{b}'")
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Use this to subtract two numbers.
    
    Args:
        a: The first number.
        b: The second number.
    
    Returns:
        The difference of the two numbers.
    """
    logger.info(f">>> Tool: 'subtract' called with numbers '{a}' and '{b}'")
    return a - b

@mcp.tool()
def slugify(text: str) -> str:
    """Convert a string into a URL-friendly slug.
    
    Args:
        text: The input text to slugify.
    
    Returns:
        The slugified string.
    """
    logger.info(f">>> Tool: 'slugify' called with text '{text}'")
    slug = text.lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "-", slug).strip("-")
    return slug

@mcp.tool()
def get_current_date_iso() -> str:
    """Get the current date and time in ISO 8601 format.
    
    Returns:
        The ISO 8601 formatted datetime string.
    """
    logger.info(">>> Tool: 'get_current_date_iso' called")
    return datetime.utcnow().isoformat()

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Use this to multiply two numbers.
    
    Args:
        a: The first number.
        b: The second number.
    
    Returns:
        The product of the two numbers.
    """
    logger.info(f">>> Tool: 'multiply' called with numbers '{a}' and '{b}'")
    return a * b

@mcp.tool()
def get_popular_orders_by_state(state: str) -> str:
    """Get a summary of popular orders for a given US state.
    
    Args:
        state: The two-letter state abbreviation (e.g., 'NY', 'CA').
    
    Returns:
        A text description of popular orders in that state.
    """
    logger.info(f">>> Tool: 'get_popular_orders_by_state' called for state '{state}'")
    state_upper = state.strip().upper()
    popular_items = {
        "CA": "Avocado Toast, Fish Tacos, Green Smoothie",
        "NY": "Classic Bagel with Lox, Thin Crust Pizza, Pastrami Sandwich",
        "TX": "Beef Brisket, Breakfast Tacos, Pecan Pie",
    }
    items = popular_items.get(state_upper, "Coffee, Classic Burger, Caesar Salad")
    return f"Popular orders in {state_upper}: {items}"

@mcp.tool()
async def get_all_data() -> str:
    """Retrieve all data from the database.
    
    Returns:
        A status string indicating success or failure.
    """
    password = os.getenv("DB_PASSWORD", "")
    ## TODO: write a SQL query to get all data from the DB
    
    return "success"

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8080"))
    logger.info(f" MCP server started on port {port}")
    # Could also use 'sse' transport, host="0.0.0.0" required for Cloud Run.
    asyncio.run(
        mcp.run_async(
            transport="streamable-http", 
            host="0.0.0.0", 
            port=port,
        )
    )