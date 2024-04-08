'''
Isolation Forest:
after training the model, the output will be either *j
    -1 : outlier 
    1  : inlier
'''
import datetime
import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder
import pymongo

class iForest:

    def send_to_mongodb(self, outlier_data, db_url, db_name, collection_name):
        client = pymongo.MongoClient(db_url)
        db = client[db_name]
        collection = db[collection_name]

        # Convert DataFrame to list of dictionaries for easier insertion
        outlier_data_dict = outlier_data.to_dict(orient='records')

        # Insert outlier_data into the MongoDB collection
        collection.insert_many(outlier_data_dict)

        client.close()

    def train_iforest(self, train_data):
        train_data = train_data.drop(columns=['Sector', 'Capital'])
        le= LabelEncoder()
        train_data['Ticker'] = le.fit_transform(train_data['Ticker'])
        train_data_for_scaling = train_data.drop(columns=['Ticker'])
        scaler = StandardScaler()
        train_data_scaled = scaler.fit_transform(train_data_for_scaling)
        train_data_scaled = pd.DataFrame(train_data_scaled, columns=train_data_for_scaling.columns, index=train_data_for_scaling.index)
        train_data_scaled['Ticker'] = train_data['Ticker']
        iso_model = IsolationForest(n_estimators=300,max_samples='auto',contamination=float(0.1))
        iso_model.fit(train_data_scaled)

        joblib.dump(iso_model, 'iforest_model.joblib')  # Save the model as 'iforest_model.joblib'

    def load_model(self, model_path):
        self.iso_model = joblib.load(model_path)
        

    def find_anomalies(self, data):
        iso_model = self.iso_model
        outlier_data = data.copy()
        # Assuming 'data' is your DataFrame
        data.index = data.index.strftime('%Y-%m-%d')

        test_data = data.drop(columns=['Sector', 'Capital'])
        le = LabelEncoder()
        test_data['Ticker'] = le.fit_transform(test_data['Ticker'])
        train_data_for_scaling = test_data.drop(columns=['Ticker'])
        scaler = StandardScaler()
        print(test_data)
        print(test_data.info())
        train_data_scaled = scaler.fit_transform(train_data_for_scaling)
        train_data_scaled = pd.DataFrame(train_data_scaled, columns=train_data_for_scaling.columns, index=train_data_for_scaling.index)
        train_data_scaled['Ticker'] = test_data['Ticker']
        # new_column_order = ['Ticker', 'Volume', 'Low', 'High', 'Average', 'Open', 'Close', 'CategoryId']
        # train_data_scaled = train_data_scaled.reindex(columns=new_column_order)

        print(train_data_scaled)
        results = iso_model.predict(train_data_scaled)

        outlier_data['Outlier'] = results
        # print(outlier_data)

        # See how many outliers
        print(outlier_data['Outlier'].value_counts())

        # Determine intensity of outliers
        intensity = iso_model.decision_function(train_data_scaled) 
        outlier_data['Outlier_Intensity'] = intensity
        # print(outlier_data)

        # Filter outliers based on specified conditions
        neg_data = outlier_data[outlier_data['Outlier'] == -1]
        pos_data = outlier_data[outlier_data['Outlier'] == 1]
        mean = pos_data['Volume'].mean()

        for _, row in neg_data.iterrows():
            cat_id = row['CategoryId']
            volume_average = row['Volume'] * row['Average']
            if cat_id == 1:
                if not (volume_average >= mean + mean * 0.1) and not (volume_average <= mean - mean * 0.1):
                    outlier_data.loc[outlier_data.index == row.name, 'Outlier'] = 1
            elif cat_id == 2:
                if not (volume_average >= mean + mean * 0.25) and not (volume_average <= mean - mean * 0.25):
                    outlier_data.loc[outlier_data.index == row.name, 'Outlier'] = 1
            else:
                if not (volume_average >= mean + mean * 0.4) and not (volume_average <= mean - mean * 0.4):
                    outlier_data.loc[outlier_data.index == row.name, 'Outlier'] = 1

        # After filtering, print the count of outliers
        print(outlier_data['Outlier'].value_counts())
        return outlier_data
