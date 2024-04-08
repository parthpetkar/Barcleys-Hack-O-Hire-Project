from yahoo_fin.stock_info import get_data
import pandas as pd
import yahoo_fin.stock_info as si
from yahoo_fin.stock_info import get_quote_table
from pymongo import MongoClient
import yfinance as yf

from typing import Dict
import yfinance as yf


def get_ticker_metadata(ticker: str) -> Dict[str, str]:
    result = {"company_name": "not_found",
              "market_cap": "not_found"}
    try:
        info = yf.Ticker(ticker).info
        if info:
            if 'longName' in info:
                result["company_name"] = info['longName']
            if "marketCap" in info:
                result["market_cap"] = str(round((info['marketCap']/1000000000), 2))
    except Exception as e:
        print(e)

    return result

tickerCommunications = ["GOOG","META","VZ","CHTR","ADTN","HIVE","AUDC","ALLT","AVNW","ATEN","AMPG","AKTS","BOSC","HEAR","NOK","CIEN","INFN","CALX","SATS","COMM","KN","CMTL","CLRO","TCCO","OCC","CRNT","CLFD","ZSTN","FEIM","ELST","FKWL","GILT","HLIT","MFON","QCOM","MSI","NTGR","KVHI","VSAT","VIAV","RITT","NTIP","WSTL"]
tickerIndustrial = ["CAT","GE","UNP","ETN","ARLP","AOS","AMSC","AIN","HOLI","ASM","AIT","AUMN","APWC","AUSI","AGIN","ASPW","AMNL","AMLM","BTU","BHP","B","BGC","BLDP","BDC","BVN","SVBL","BW","EMR","FAST","CMCT","CLF","PH","MNR","CCJ","MSM","TRNO","MTRN","CMP","LEU","DNN","TRS","FELE","CHNR","PZG","SXI"]
tickerEstate = ["PLD","SPG","WELL","PSA","BAM","ALEX","NEN","GRBK","XIN","JOE","MLP","CTO","FOR","LGIH","INN","MMI","STRS","IRS","TPL","ROII","PRSI"]
tickerHealth=["LLY","UNH","JNJ","MRK","AFL","AIZ","AMED","ADUS","FMS","ACHC","PAHC","AMS","AMEH","CVS","CI","CNC","CNO","SBRA","CHE","GLRE","PRA","CPSI","DVA","DOC","DIGP","EIG","EVH","UNH","GEO","UNM","HCP","HUM","OHI","HR","MOH","NHI","HSTM","INOV","STRM","UHT","MRGE","HQY","PFHO","VTR","LTC","MPW","VEEV","OMCL","TDOC"]
tickerTechnology = ["NVDA","DLO","YMM","GTLB","AMGN","ACN","ADSK","ACAD","ARRY","FOLD","ACOR","ACIW","AGIO","AVXL","ALNY","LIFE","ADXS","ACM","AGEN","SAIC","ANTH","AMPE","ARWR","AKBA","AEZS","ACST","AMBS","ARDX","ANIK","ATNM","ANIP","DGLY","ADMA","JAGX","HMNY","AMRC","ABIO","TEAM","ADAP","ALDX","ABUS","AXON","ASND","AFMD","AFFY","DYSL","AERG","SIGL","ALSE","ARNI","PSSR","CRYO","IBM","BIIB","BMRN","PACB","PBYI","EBS","BLUE","BCRX","NWBO","SGMO","BMI","TECH","NAVB","CALA","CANF","PLX"]

tickers = [tickerCommunications,tickerIndustrial,tickerEstate,tickerHealth,tickerTechnology]

sector_mapping = {}
for ticker in tickerCommunications:
    sector_mapping[ticker] = "Communications"
for ticker in tickerIndustrial:
    sector_mapping[ticker] = "Industrial"
for ticker in tickerEstate:
    sector_mapping[ticker] = "Real Estate"
for ticker in tickerHealth:
    sector_mapping[ticker] = "Healthcare"
for ticker in tickerTechnology:
    sector_mapping[ticker] = "Technology"

def get_sector(ticker):
    return sector_mapping.get(ticker)

desired_columns = ['Date','ticker', 'Sector', 'volume','Capital', 'low','high', 'mid', 'open',   'close', 'adjclose','CategoryId']

data_list = []

for i in range(0, 5):
    for j in range(0, len(tickers[i])):
        ticker = yf.Ticker(tickers[i][j])
        todays_data = pd.DataFrame(ticker.history(period='1d'))

        todays_data['Date'] = todays_data.index
        todays_data["Ticker"] = tickers[i][j]
        todays_data["Sector"] = todays_data["Ticker"].apply(get_sector)
        cap = get_ticker_metadata(tickers[i][j])['market_cap']

        todays_data['Capital'] = cap
        todays_data.drop(columns=["Dividends", "Stock Splits"], inplace=True)

        if cap != 'not_found':
            cap_float = float(cap)
            if cap_float > 10 :
                todays_data['CategoryId'] = 3
            elif 2 < cap_float < 10:
                todays_data['CategoryId'] = 2
            elif cap_float < 2:
                todays_data['CategoryId'] = 1

        # Reindexing columns - Commented out for now
        # todays_data = todays_data.reindex(columns=desired_columns)

        # Renaming columns
        todays_data.rename(columns={
            'Open': 'Open',
            'High': 'High',
            'Low': 'Low',
            'Close': 'Close',
            'Adj Close': 'Adj Close',
            'Volume': 'Volume',
            'Ticker': 'Ticker',
            'Capital': 'Capital',
            'CategoryId': 'CategoryId',
            'mid': 'Average'
        }, inplace=True)

        todays_data["Average"] = (todays_data['High'] + todays_data['Low']) / 2
        todays_data = todays_data[todays_data["Capital"] != 'not_found']

        todays_data.reset_index(drop=True, inplace=True)


        todays_data["Capital"] = todays_data["Capital"].astype(float)

        data_list.append(todays_data)

# Concatenate all DataFrames in data_list into a single DataFrame
todays_data = pd.concat(data_list, ignore_index=True)

# Print the resulting DataFrame
print(todays_data)

data_list = []

for i in range(0, 5):
    for j in range(0, len(tickers[i])):
        ticker = yf.Ticker(tickers[i][j])
        data = pd.DataFrame(ticker.history(period='1d'))
        data['Ticker'] = tickers[i][j]  # Add a column for the ticker symbol
        market_cap = get_ticker_metadata(tickers[i][j])['market_cap']
        data.loc[data['Ticker'] == tickers[i][j], 'Capital'] = market_cap

        if(market_cap != 'not_found'):
          if float(market_cap) > 10 :
            data.loc[data['Ticker'] == tickers[i][j], 'CategoryId'] = 3
          elif 2 < float(market_cap) < 10:
            data.loc[data['Ticker'] == tickers[i][j], 'CategoryId'] = 2
          elif float(market_cap) < 2:
            data.loc[data['Ticker'] == tickers[i][j], 'CategoryId'] = 1
          data_list.append(data)

# Concatenate all DataFrames in data_list into a single DataFrame
newData = pd.concat(data_list)

# Add 'Date' and 'Sector' columns
newData['Date'] = newData.index
newData['Sector'] = newData['Ticker'].apply(get_sector)

# Drop unnecessary columns
newData.drop(columns=["Dividends", "Stock Splits"], inplace=True)

list_of_dicts = newData.to_dict(orient='records')

client = MongoClient("mongodb+srv://sanjayparth22:sanjayP37@cluster0.r9enpld.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Access the database
db = client["Hackathon"]

# Access the collection
collection = db["Live-Stock-Data"]

collection.insert_many(list_of_dicts)


client.close()