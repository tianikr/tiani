import pandas as pd
# import numpy as np

#TIANI KHUSNUL RAHMAWATI
mpg_level = []
data = pd.read_excel('mtcars.xlsx') 

df = pd.DataFrame(data, columns= ['mpg'])
for x in range(0, len(df['mpg'])):
    mpg = float(df['mpg'][x])
    if mpg < 20:
        mpg_level.append("Low")
    elif (mpg >= 20) and (mpg <= 30):
        mpg_level.append("Medium")
    elif mpg > 30:
        mpg_level.append("Hard")

df = data.insert(2, "mpg_level", mpg_level)
df = pd.DataFrame(data, columns= ['Cars','mpg', 'mpg_level'])
print(df)
