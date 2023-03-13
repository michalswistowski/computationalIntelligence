import pandas as pd
import matplotlib.pyplot as plt

miasta = pd.read_csv('./miasta.csv')

row = {'Rok': 2010, 'Gdansk':460, 'Poznan':555, 'Szczecin':405}

miasta.loc[len(miasta.index)] = row
print(miasta)

miasta = pd.DataFrame(miasta)

miasta.plot(x='Rok', ylabel='ludnosc[w tys]', marker='o')

plt.title(label='ludnosc w miastach polski')
plt.show() 

#e
miasta_standarized = miasta[['Gdansk', 'Poznan', 'Szczecin']].copy()
mean_before = miasta_standarized.values.mean()
std_before = miasta_standarized.values.std()
print("srednia poczatkowa: " + str(mean_before))
print("odchylenie standardowe poczatkowe: " + str(std_before))
miasta_standarized['Gdansk'] = (miasta_standarized['Gdansk'] - mean_before) / std_before
miasta_standarized['Poznan'] = (miasta_standarized['Poznan'] - mean_before) / std_before
miasta_standarized['Szczecin'] = (miasta_standarized['Szczecin'] - mean_before) / std_before
mean_after = miasta_standarized.values.mean()
std_after = miasta_standarized.values.std()
print(miasta_standarized.values)
print("srednia po standaryzacji: " + str(mean_after))
print("odchylenie standardowe po standaryzacji: " + str(miasta_standarized.values.std()))
#f
miasta_normalized = miasta[['Gdansk', 'Poznan', 'Szczecin']].copy()
min_before = miasta_normalized.values.min()
max_before = miasta_normalized.values.max()
print("min poczatkowe: " + str(min_before) + " max poczatkowe: " + str(max_before))
miasta_normalized['Gdansk'] = (miasta_normalized['Gdansk'] - min_before) / (max_before - min_before)
miasta_normalized['Poznan'] = (miasta_normalized['Poznan'] - min_before) / (max_before - min_before)
miasta_normalized['Szczecin'] = (miasta_normalized['Szczecin'] - min_before) / (max_before - min_before)
print(miasta_normalized)
min_after = miasta_normalized.values.min()
max_after = miasta_normalized.values.max()
print("min po normalizacji: " + str(min_after))
print("max po normalizacji: " + str(max_after))