import pandas as pd
df = pd.read_json (r'.\orders_data.json')
df.to_csv (r'.\data_file.csv', index = None)
