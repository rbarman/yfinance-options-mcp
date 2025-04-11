
from mcp.server.fastmcp import FastMCP
from yfinance_utils import get_options_chain, OptionType, get_expiration_dates as _get_expiration_dates

# Initialize FastMCP server
mcp = FastMCP("yfinance-options-mcp")


@mcp.tool(name="get_put_options_chain")
async def get_put_options_chain(ticker_symbol: str, expiration_date: str = None) -> str:
    """
    Get the put options chain for a given ticker symbol

    Args:
        ticker_symbol: The ticker symbol of the stock to get the put options chain for
        expiration_date: The expiration date of the options chain to get. Optional, by default the closest expiration date is used.
    Returns:
        A string representation of the put options chain
    """
    put_options_chain = await get_options_chain(ticker_symbol, OptionType.PUT, expiration_date)
    return put_options_chain

@mcp.tool(name="get_call_options_chain")
async def get_call_options_chain(ticker_symbol: str, expiration_date: str = None) -> str:
    """
    Get the call options chain for a given ticker symbol

    Args:
        ticker_symbol: The ticker symbol of the stock to get the call options chain for
        expiration_date: The expiration date of the options chain to get. Optional, by default the closest expiration date is used.
    Returns:
        A string representation of the call options chain
    """
    call_options_chain = await get_options_chain(ticker_symbol, OptionType.CALL, expiration_date)
    return call_options_chain


@mcp.tool(name="get_expiration_dates")
async def get_expiration_dates(ticker_symbol: str) -> str:
    """
    Get the expiration dates for a given ticker symbol

    Args:
        ticker_symbol: The ticker symbol of the stock to get the expiration dates for
    Returns:
        A list of the expiration dates
    """
    expiration_dates = await _get_expiration_dates(ticker_symbol)
    return expiration_dates


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
