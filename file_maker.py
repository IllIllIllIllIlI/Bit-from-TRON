import pandas as pd

df1 = pd.read_csv('tron_dataset_plus200.csv')
df2 = pd.read_csv('tron_data_set_v4.csv')

merger = pd.concat([df1, df2], ignore_index=True)


print(f"before: {len(merger)}")
merger = merger.drop_duplicates()
print(f"After: {len(merger)}")

file_path = "tron_dataset.csv"

merger.to_csv(file_path, index=False)
