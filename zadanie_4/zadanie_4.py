import numpy as np
import pandas as pd
from pymcdm.methods import TOPSIS, SPOTIS
from pymcdm.normalizations import minmax_normalization
from pymcdm.helpers import rankdata

# ----- 1. Przygotowanie danych -----

# Macierz decyzyjna: 4 alternatywy, 3 kryteria
# Przykład: [zysk, koszt, ryzyko]
matrix = np.array([
    [250, 16, 12],
    [200, 20, 8],
    [300, 14, 16],
    [275, 18, 11]
])

# Wagi kryteriów (suma = 1)
weights = np.array([0.5, 0.3, 0.2])

# Typy kryteriów: 1 = maksymalizacja, -1 = minimalizacja
criteria_types = [1, -1, -1]

# ----- 2. Normalizacja danych dla TOPSIS -----
normalized_matrix = minmax_normalization(matrix, criteria_types)

# ----- 3. TOPSIS -----
topsis = TOPSIS()
topsis_scores = topsis(normalized_matrix, weights, criteria_types)
topsis_ranking = rankdata(topsis_scores, reverse=True)

# ----- 4. SPOTIS (potrzebuje granic) -----
# Granice dla SPOTIS: min i max dla każdej kolumny
bounds = [[min(col), max(col)] for col in matrix.T]

spotis = SPOTIS(bounds)
spotis_scores = spotis(matrix, weights, criteria_types)
spotis_ranking = rankdata(spotis_scores, reverse=False)

# ----- 5. Prezentacja wyników -----
alternatives = [f"A{i+1}" for i in range(matrix.shape[0])]
results_df = pd.DataFrame({
    "Alternatywa": alternatives,
    "TOPSIS Score": np.round(topsis_scores, 4),
    "TOPSIS Ranking": topsis_ranking,
    "SPOTIS Score": np.round(spotis_scores, 4),
    "SPOTIS Ranking": spotis_ranking
})

print("\n=== Wyniki analizy MCDM ===\n")
print(results_df)
