'''
from google.colab import files
import pandas as pd

uploaded = files.upload()

df = pd.read_excel("products_50_rows.xlsx")
print(df)

print(df.shape)
print(df.columns)
print(df.info())


print(df.head(5))
print(df.tail(5))

print(df.iloc[4])
print(df.iloc[8])
print(df['Product'])


print(df)
print(df.loc[2, "Brand"])
print(df.loc[3, "Product"])
print(df.loc[12, "Stock"])
print(df.iloc[4, 0])
print(df.iloc[2, 1])
print(df.iloc[3, 3])

df_dropped = df.drop(columns=["Stock"])
#df_dropped = df.drop(columns=["Stock"],inplace=True)
print("After Dropping 'Stock' Column:\n", df_dropped)

df_renamed = df.rename(columns={"Price": "Cost"})
print(df_renamed)
#df.rename(columns={"Product": "Product  name"}, inplace=True)

print(df)
print("*************Using loc************************\n", df.loc[df['BestSeller']==True])
print("*************Using loc************************\n", df.loc[df['Stock']<40])
print("*************Using loc************************\n", df.loc[df['Price']<10000])


df_grouped = df.groupby("Brand").agg({"Price": "mean", "Stock": "sum"})
print(df_grouped)

grouped=df.groupby("Brand").agg({"Price": ["mean", "max", "min","sum"]})
print(grouped)

grouped = df.groupby("Brand")["Price"].mean()
print(grouped)

data2 = {
    "Brand": ["SoundMax", "TechNova", "ByteCore", "TimeTrack", "EchoBoom"],
    "Rating": [4.2, 4.5, 4.0, 4.1, 3.9],
    'discount':[28,40,16,10,5]
}

df_ratings = pd.DataFrame(data2)
print(df_ratings)

df_merged = df.merge(df_ratings, on="Brand")
print("Merged DataFrame (Adding Ratings):\n", df_merged)

new_data = {
    "Product": ["Tablet"],
    "Brand": ["SmartWare"],
    "Price": [12999],
    "Stock": [25],
    "BestSeller":[True]
}
df_new = pd.DataFrame(new_data)
print(df_new)

df_concat = pd.concat([df, df_new], ignore_index=True)
print("Concatenated DataFrame:\n", df_concat)

print(df[["Product", "Price","Stock"]])

df["Rank"] = df["Price"].rank(ascending=False)
print(df)
print(df.sort_values(by="Rank", ascending=True))
print(df.sort_values(by="Rank", ascending=False))

df.pivot_table(values="Price", index="Brand", columns="Stock", aggfunc="max")

pd.crosstab(df["Brand"], df["Stock"])

import pandas as pd
import numpy as np

data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, np.nan, 5],
    'C': [10, np.nan, np.nan, 40, 50]
}

df = pd.DataFrame(data)
print("Original DataFrame with Missing Values:")
print(df)


df_interpolate = df.interpolate()
print("\nDataFrame after filling NaN values using interpolation:")
print(df_interpolate)

df_dropna = df.dropna()
print("\nDataFrame after dropping rows with NaN values:")
print(df_dropna)

df_fillna = df.fillna(9)
print("\nDataFrame after filling NaN values with 0:")
print(df_fillna)
'''