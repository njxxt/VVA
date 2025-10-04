import matplotlib.pyplot as plt

plt.figure(figsize=(14, 10))

countries = ['USSR/Ru', 'USA', 'Chi', 'Eu', 'In', 'Ja', 'Ano']
programs = [45, 38, 22, 18, 12, 10, 15]
plt.gcf().set_facecolor('#8B0000')
plt.pie(programs, labels=countries, autopct='%1.f%%', textprops={'fontsize': 13, 'weight': 'bold', 'color': 'white'})

plt.title('Spaces programs of counties', fontsize=16, fontweight='bold')

forle = [f'{c}: {pro}' for c, pro in zip(countries, programs)]
plt.legend(forle)

plt.tight_layout()
plt.show()
