import pandas as pd
import os

data = {"name": ["Ali", "Reza", "Sina", "Sara", "Zahra"],
        "age": [20, 21, 22, 23, 24],
        "city": ["Tehran", "Mashhad", "Shiraz", "Tabriz", "Yazd"]}

df = pd.DataFrame(data)

# Add a new row using pd.concat (modern approach)
new_row = {'name': 'Hassan', 'age': 25, 'city': 'Tehran'}
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

print(df)


data_dir = 'data'

file_path = os.path.join(data_dir, 'data.csv')

df.to_csv(file_path, index=False)

print(f"Data saved to {file_path}")








