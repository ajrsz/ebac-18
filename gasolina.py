
import pandas as pd
import csv 
import seaborn as sns
import matplotlib.pyplot as plt

    
data = pd.read_csv('gasolina.csv', delimiter=',', decimal='.')
gasolina = data

plt.figure(figsize=(8, 5))

sns.set_style("darkgrid")
graph = sns.lineplot(x="dia", y="venda", data=gasolina, marker='o')

plt.title('Preço da Gasolina por Dia', fontsize=15)
plt.xlabel('Dia', fontsize=13)
plt.ylabel('Preço', fontsize=12)

plt.savefig("gasolina.png")
plt.show()
