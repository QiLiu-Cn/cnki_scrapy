# -*- codeing = utf-8 -*-
import pandas
import pandas as pd

f = pd.read_csv(r'5.csv',names=['title','url','download'])
url = f['url'].values.tolist()
print(len(url))
for i in range(len(url)):
    print(url(i))
# print(url)
print(type(url))
