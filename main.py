import pandas as pd
import os

data = {
    'Name': ['Pawan', 'Qutub', 'Randolph'],
    'Age': [19, 25, 30],
    'City': ['Surat', 'New York', 'London']
}

df = pd.DataFrame(data)

new_row = {'Name': 'Sheldon', 'Age': 27, 'City': 'CooperLand'}
df.loc[len(df.index)] = new_row

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'sample.csv')
df.to_csv(file_path, index=False)
print(f"CSV file saved to {file_path}")
