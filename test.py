import re
import pandas as pd
import requests

data = pd.read_csv('test_data.csv')

BASE_URI = 'http://127.0.0.1:4300/'

for i, d in data.iterrows():
    request_body = {
        'rm': d[0],
        'lstst': d[1],
        'ptratio': d[2]
    }
    result = requests.post(BASE_URI + 'predict', request_body)
    print(BASE_URI + 'predict')
    print('Status {}'.format(result.status_code))
    print(d[0], d[1], d[2])
    print(result.raw)
    

    break