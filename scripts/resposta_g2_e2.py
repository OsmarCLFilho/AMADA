import func_etapa2_g2 as fe
import pandas as pd

df = pd.read_csv("spo_lyr_data.csv")

print("######  QUESTÃO 1  ######\n")

dicionario = fe.concatenar_elementos_coluna(df, 'album')
dicionario = fe.remove_contracoes(dicionario)
dicionario = fe.remove_caracteres(dicionario)
dicionario = fe.remove_irrelevantes(dicionario)
dicionario = fe.freq_elementos(dicionario)

print("10 palavras mais comuns nos títulos dos álbuns:\n")
print(dicionario['Todas'].head(10))

print("\n\n")


print("######  QUESTÃO 2  ######\n")

dicionario = fe.concatenar_elementos_coluna(df, 'name')
dicionario = fe.remove_contracoes(dicionario)
dicionario = fe.remove_caracteres(dicionario)
dicionario = fe.remove_irrelevantes(dicionario)
dicionario = fe.freq_elementos(dicionario)

print("10 palavras mais comuns nos títulos das músicas:\n")
print(dicionario['Todas'].head(10))

print("\n\n")


print("######  QUESTÃO 3  ######\n")

dicionario = fe.concatenar_elementos_coluna(df, 'lyrics', 'album')
dicionario = fe.remove_contracoes(dicionario)
dicionario = fe.remove_caracteres(dicionario)
dicionario = fe.remove_irrelevantes(dicionario)
dicionario = fe.freq_elementos(dicionario)

print("10 palavras mais comuns nas letras das músicas por álbum:\n")

for key in dicionario.keys():
    print(key,":")
    print(dicionario[key].head(10))
    print("\n")

print("\n\n")

print("######  QUESTÃO 4  ######\n")

dicionario = fe.concatenar_elementos_coluna(df, 'lyrics')
dicionario = fe.remove_contracoes(dicionario)
dicionario = fe.remove_caracteres(dicionario)
dicionario = fe.remove_irrelevantes(dicionario)
dicionario = fe.freq_elementos(dicionario)

print("10 palavras mais comuns nas letras das músicas:\n")
print(dicionario['Todas'].head(10))

print("\n\n")

print("######  QUESTÃO 5  ######\n")

dicionario = fe.concatenar_elementos_coluna(df, 'lyrics', 'album')
dicionario = fe.relevancia(dicionario)

print("Quantidade de vezes que o nome dos álbuns aparece nas letras de suas músicas:\n")

for ind in sorted(dicionario, key = dicionario.get, reverse=True):
    print(ind, ": ", dicionario[ind])

print("\n\n")


print("######  QUESTÃO 6  ######\n")

dicionario = fe.concatenar_elementos_coluna(df, 'lyrics', 'name')
dicionario = fe.relevancia(dicionario)

print("Quantidade de vezes que o nome das músicas aparecem nas suas letras:\n")

for ind in sorted(dicionario, key = dicionario.get, reverse=True):
    print(ind, ": ", dicionario[ind])

