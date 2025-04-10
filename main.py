
from mcp.server.fastmcp import FastMCP
from yfinance_utils import get_options_chain, OptionType

# Initialize FastMCP server
mcp = FastMCP("yfinance-options-mcp")


@mcp.tool(name="get_put_options_chain")
async def get_put_options_chain(ticker_symbol: str) -> str:
    """
    Get the put options chain for a given ticker symbol

    Args:
        ticker_symbol: The ticker symbol of the stock to get the put options chain for

    Returns:
        A string representation of the put options chain
    """
    put_options_chain = await get_options_chain(ticker_symbol, OptionType.PUT)
    return put_options_chain

@mcp.tool(name="get_call_options_chain")
async def get_call_options_chain(ticker_symbol: str) -> str:
    """
    Get the call options chain for a given ticker symbol

    Args:
        ticker_symbol: The ticker symbol of the stock to get the call options chain for

    Returns:
        A string representation of the call options chain
    """
    call_options_chain = await get_options_chain(ticker_symbol, OptionType.CALL)
    return call_options_chain


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
