import warnings
import pymongo
warnings.filterwarnings('ignore')


from extract import Extract
from isolation_forests import iForest


def main():

    # print(train_data)

    ext = Extract()

    train_data = ext.get_data()

    iforest_model = iForest()
    # iforest_model.train_iforest(train_data)

    iforest_model.load_model('iforest_model.joblib')

    anomalies_iforest = iforest_model.find_anomalies(train_data)
    # anomalies_iforest.to_csv('test_iso.csv')

    iforest_model.send_to_mongodb(anomalies_iforest, "mongodb+srv://sanjayparth22:sanjayP37@cluster0.r9enpld.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", "Hackathon", "Anomalies")
    # iforest_model.send_to_mongodb(anomalies_iforest, "mongodb+srv://sanjayparth22:sanjayP37@cluster0.r9enpld.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", "Hackathon", "Trial")


if __name__ == '__main__':
    main()