import pandas as pd


df = pd.read_csv("vendas_padaria.csv")

print(df.head()) #amostra dos 5 primeiros
print(df.tail()) #amostra dos 5 últimos
print(df.info()) #informações principais