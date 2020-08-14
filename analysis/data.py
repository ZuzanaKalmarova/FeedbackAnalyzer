import os
import pandas as pd
from pymongo import MongoClient
from datetime import datetime, timedelta
import numpy as np

def connect_mongo(db='feedback_db'):
    MONGO_URI = os.environ.get('MONGO_URI')
    conn = MongoClient(MONGO_URI)
    return conn[db]

def get_data(collection='feedbacks', query={}):
    db = connect_mongo()
    cursor = db[collection].find(query)
    df = pd.DataFrame(list(cursor))
    
    # process df: drop _id column, convert rating column to float,
    # convert blank text in feedback column to NaN
    df.drop(['_id'], axis=1, inplace=True)
    df['rating'] = df['rating'].astype(float)
    df.loc[df['feedback']=='', 'feedback'] = np.NaN
    return df



#query_date = datetime.today() - timedelta(weeks=4)

#query = {"date": { '$gte' : query_date}}

def get_statistics(data, report_to_date):
    data1 = data[data['date'] > (report_to_date - timedelta(weeks=1))]
    data2 = data[data['date'] > (report_to_date - timedelta(weeks=2))]
    dfs = [data1, data2, data]
    mins = [np.nanmin(df.rating) for df in dfs]
    maxs = [np.nanmax(df.rating) for df in dfs]
    medians = [np.nanmedian(df.rating) for df in dfs]
    means = [np.nanmean(df.rating) for df in dfs]
    counts = [len(df.rating) for df in dfs]
    counts_with_rating = [np.sum(df.rating.notnull()) for df in dfs]
    counts_with_feedback = [np.sum(df.feedback.notnull()) for df in dfs]
    statistics = pd.DataFrame({'minimum': mins, 'maximum': maxs, 'median': medians, 'mean': means, 'count': counts,
                               'count_with_rating': counts_with_rating, 'count_with_feedback': counts_with_feedback},
                               index=['last_week', 'last_two_weeks', 'last_four_weeks'])
    return statistics

