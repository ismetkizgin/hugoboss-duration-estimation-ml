import pandas as pd
from sklearn.linear_model import LinearRegression
from datetime import datetime
import requests
import json
import datetime
import csv
import pickle

def dataMap(productionFlow):
    productionTime = (datetime.datetime.strptime(productionFlow['endDate'], '%Y-%m-%dT%H:%M:%S+00:00') - datetime.datetime.strptime(productionFlow['startDate'], '%Y-%m-%dT%H:%M:%S+00:00')).total_seconds() / 60.0
    return { 'productId': productionFlow['productId'], 'factoryId': productionFlow['factoryId'], 'amount': productionFlow['amount'], 'productionTime': productionTime }

query= """query getProductionFlows {
  production_flows {
    productId
    startDate
    factoryId
    endDate
    amount
  }
}"""
response = requests.post('https://api.hugoboss.ismetkizgin.com.tr/v1/graphql', json={'query': query}, headers={"x-hasura-admin-secret":"J!#LSC4#/x.n4uVt"})
productionFlows = response.json()['data']['production_flows']

df = pd.DataFrame(list(map(dataMap, productionFlows)))

x = df.iloc[:,0:3].values
y = df.iloc[:,3:4].values.reshape(-1,1)

model = LinearRegression()
model.fit(x,y)


pickle.dump(model, open('model.pkl','wb'))