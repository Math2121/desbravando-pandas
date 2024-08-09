# %%
import pandas as pd
# %%

data = {
    "nome": ["math", "jose", "mario"],
    "idade": [20,56,63],
"cor": ["preto","verde","roxo"],
"renda": [3500,1354,432]
}


df = pd.DataFrame(data)
df["idade"]

# %%
df.describe()
df[['idade', 'renda']].mean()

# %%
