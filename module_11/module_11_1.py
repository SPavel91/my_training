import requests

r = requests.get('https://www.flickr.com/services/api/')
print(r.text)

import pandas as pd
import matplotlib.pyplot as plt

players = pd.DataFrame({"Имя": ["Иван", "Петр", "Елена", "Дмитрий", "Яна"],
        "Возраст": [22, 20, 25, 18, 30],
        "Пол": ["мужской", "мужской", "женский", "мужской", "женский"],})

print(players["Возраст"].max())
print(players["Имя"].str.lower())
players.to_excel("players.xlsx")

fig, ax = plt.subplots()
ax.plot(players.index, players["Возраст"], color ="red")
ax.set_title(r'Возраст участников', fontsize=20)

for i, (name, age) in enumerate(zip(players["Имя"], players["Возраст"])):
    ax.annotate(f'{name}, {age}', xy=(i, age), xytext=(i, age + 1), ha='center', fontsize=10,
                arrowprops=dict(arrowstyle='->', color='black'))
plt.show()