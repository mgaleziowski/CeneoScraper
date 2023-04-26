import os
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

print(*[filename.split(".")[0] for filename in os.listdir("./opinions")], sep="\n")

product_code="96875119"

opinions=pd.read_json(f"./opinions/{product_code}.json")
opinions_count=opinions.shape[0]
pros_count=sum([False if len(p)==0 else True for p in opinions.pros])
cons_count=sum([False if len(c)==0 else True for c in opinions.cons])
opinions.score=opinions.score.map(lambda x: float(x[:-2].replace(",",".")))
avg_score=opinions.score.mean()

print(f"\n\nDla produktu o kodzie [{product_code}] dostępnych jest {opinions_count} opinii\nDla {pros_count} opinii dostępna jest lista zalet a dla {cons_count} opinii dostępna jest lista wad\nŚrednia liczba gwiazdek to {(round(2*avg_score))/2}")
score=opinions.score.value_counts().reindex(list(np.arange(0,5.5,0.5)),fill_value=0)
score.plot.bar()
plt.title("histogram ocen")
plt.xlabel("liczba gwiazdek")
plt.ylabel("liczba opinii")
plt.xticks(rotation=0)
for index,value in enumerate(score):
    plt.text(index,value+0.5,str(value),ha="center")
plt.show()
try:
    os.mkdir("./plots")
except FileExistsError:
    pass
plt.savefig(f"./plots/{product_code}_score.png")
plt.close