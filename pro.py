import csv
import dataclasses
import pandas as pd
import csv

data = pd.read_csv("brown_dwarf_stars.csv")

df = data[data['Mass'].notna()]
df = data[data['Radius'].notna()]
df = data[data['Distance'].notna()]
df = data[data['Star_name'].notna()]
print(df)

Mass = float(data.Mass*0.000954588)
Radius = float(data.Radius*0.102763)


