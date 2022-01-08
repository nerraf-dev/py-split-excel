import pandas as pd
data_df = pd.read_excel('./data/PCHub.xlsx')
grouped_df = data_df.groupby('CATEGORY')

for data in grouped_df.CATEGORY:
  grouped_df.get_group(data[0]).to_excel("./output/" + data[0]+".xlsx")
  # print(data)
  print(grouped_df.get_group(data[0]))
