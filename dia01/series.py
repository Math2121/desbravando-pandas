# %%
import pandas as pd

# %%

# lista de idade
idade = [31,33,5,7,98,7520,2]

# print(idade)
s_idade = pd.Series(idade)
s_idade
s_idade[0]


# %%
# métodos de séries

# média
media = s_idade.mean()


# desvio padrão
desv = s_idade.std()

# variancia
vari = s_idade.var()


s_idade.describe()


# %%

# jeito antigo
nova_idade = []

for i in idade:
    if i >=30:
        nova_idade.append(i)

nova_idade


# com pandas

filtro = s_idade >= 30
s_idade[filtro]

# %%
