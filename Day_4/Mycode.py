import pandas as pd
import os

data = {"name": ["Ali", "Reza", "Sina", "Sara", "Zahra"],
        "age": [20, 21, 22, 23, 24],
        "city": ["Tehran", "Mashhad", "Shiraz", "Tabriz", "Yazd"]}

df = pd.DataFrame(data)

print(df)


data_dir = 'Day_4'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'data.csv')

df.to_csv(file_path, index=False)

print(f"Data saved to {file_path}")








