import os
import pandas as pd

print(*[filename.split(".")[0] for filename in os.listdir("./opinions")], sep="\n")

product_code=input("Podaj kod produktu: ")

opinions=pd.read_json(f"./opinions/{product_code}.json")

print(opinions)
