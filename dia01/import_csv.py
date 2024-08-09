# %%
import pandas as pd

#%%

df = pd.read_csv("../data/customers.csv", sep=";")
df
# %%

# Atributos

df.columns


# %%
df.shape
# %%

df.index
# %%
df.info(memory_usage='deep')
# %%

df.dtypes


# %%

df.head()
# %%
df.tail()
# %%
# dados aleatórios
df.sample(5)
# %%

df[["UUID","Name"]].head()
df.columns.tolist()

# %%

df_sample = df.sample(100)
df_sample.head()
# %%

# posição do dataframe (linhas)
df_sample.iloc[0:4]
df_sample.iloc[[0,2,5]]

# %%

# pega os índices
df.loc[33:66]["Name"]
# %%
