import pandas as pd
df = pd.read_html('https://www.sharesansar.com/today-share-price')
c = df[0]
c.to_csv("newdf1.csv")
print(c)
