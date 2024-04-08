import datetime
import pandas as pd
from pymongo import MongoClient

class Extract:
    def get_data(self):
        client = MongoClient('mongodb+srv://sanjayparth22:sanjayP37@cluster0.r9enpld.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
        db = client['Hackathon']
        collection = db['Live-Stock-Data']
        # collection = db['Stock-Data-Final']

        cursor = collection.find()

        # Convert MongoDB cursor to pandas DataFrame
        ticker_data = pd.DataFrame(list(cursor))
        # print(ticker_data)
        # Dropping '_id' column
        ticker_data = ticker_data.drop(columns=['_id'])

        # Setting 'Date' column as index
        ticker_data['Date'] = pd.to_datetime(ticker_data['Date'])
        ticker_data.set_index('Date', inplace=True)
        # ticker_data = ticker_data.drop(columns = ['Adj Close'])
        # ticker_data = ticker_data.drop(columns = ['Capital Gains'])
        print(ticker_data)
        return ticker_data
