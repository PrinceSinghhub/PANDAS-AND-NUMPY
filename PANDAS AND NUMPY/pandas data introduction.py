import numpy as np
import pandas as pd
dic = {"name":["CODEX CODER","CODEX","PRINCE","PRINCE SINGH"],
      'marks':[90,65,80,86],
      'city':["mp",'gujrat','bihar','madhya pradesh']}
data = pd.DataFrame(dic)
print(data)
#convert data in ecel file
data.to_csv('By Pycharm data.csv')
