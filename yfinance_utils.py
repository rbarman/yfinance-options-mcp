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

async def get_options_chain(ticker_symbol: str, type: OptionType, expiration_date: str = None) -> str:
    ticker = yf.Ticker(ticker_symbol)
    if type == OptionType.PUT:
        chain = ticker.option_chain(date=expiration_date).puts
    elif type == OptionType.CALL:
        chain = ticker.option_chain(date=expiration_date).calls
    return format_options_chain(chain)

async def get_expiration_dates(ticker_symbol: str) -> list[str]:
    ticker = yf.Ticker(ticker_symbol)
    ticker._download_options()
    return list(ticker._expirations.keys())

if __name__ == "__main__":
    import asyncio

    async def main():
        ticker_symbol = "GOOG"
        
        # get expiration dates
        expiration_dates = await get_expiration_dates(ticker_symbol)
        print(f"Expiration dates for {ticker_symbol}:")
        for i, expiration_date in enumerate(expiration_dates):
            print(f"{i+1}. {expiration_date}")

        # get options chain for the first expiration date
        expiration_date = expiration_dates[1]
        print(f"Options chain for {ticker_symbol} at expiration date {expiration_date}:")
        put_options_chain = await get_options_chain(ticker_symbol, OptionType.CALL, expiration_date)
        print(put_options_chain)

    asyncio.run(main())