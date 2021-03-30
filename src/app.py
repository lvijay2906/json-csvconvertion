import pandas as pd
df = pd.read_json (r'.\json\orders_data.json')
df.to_csv (r'.\csv\data_file.csv', index = None)
