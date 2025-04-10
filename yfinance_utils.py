from enum import Enum
import pandas as pd
import yfinance as yf

class OptionType(Enum):
    PUT = "PUT"
    CALL = "CALL"

# TODO: add expiration date to the options chain, by default yfinance returns the closest expiration date
# ticker.option_chain(date=expiration_date)


# async def _get_put_options_chain(ticker_symbol: str) -> pd.DataFrame:
#     ticker = yf.Ticker(ticker_symbol)
#     option_chain = ticker.option_chain().puts
#     return option_chain

# async def _get_call_options_chain(ticker_symbol: str) -> pd.DataFrame:
#     ticker = yf.Ticker(ticker_symbol)
#     option_chain = ticker.option_chain().calls
#     return option_chain

def format_options_chain(options_chain: pd.DataFrame) -> str:
    # keep only the columns that are needed
    df =  options_chain[["strike", "lastPrice", "change", "percentChange", "volume", "openInterest", "impliedVolatility", "inTheMoney"]]
    df.columns = ["strike", "price", "change", "percent_change", "volume", "open_interest", "implied_volatility", "in_the_money"]
    return df.to_string()

async def get_options_chain(ticker_symbol: str, type: OptionType) -> str:
    ticker = yf.Ticker(ticker_symbol)
    if type == OptionType.PUT:
        chain = ticker.option_chain().puts
    elif type == OptionType.CALL:
        chain = ticker.option_chain().calls
    return format_options_chain(chain)

if __name__ == "__main__":
    import asyncio

    async def main():
        ticker_symbol = "GOOG"
        put_options_chain = await get_options_chain(ticker_symbol, OptionType.CALL)
        print(put_options_chain)

    asyncio.run(main())