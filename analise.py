import pandas as pd

df = pd.read_csv("dados.csv")
df["faturamento"] = df["preco"] * df["quantidade"]

print(df)
print("Total:", df["faturamento"].sum())
