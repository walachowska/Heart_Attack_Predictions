import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

data = pd.read_csv('heart.csv')
print(data.shape)
# Nazwy kolumn
print(f'Column names:\n {data.columns.tolist()}')
# Wyświetlenie pierwszych kilku wierszy, aby sprawdzić, czy dane zostały poprawnie wczytane
print(data.head())

px.imshow(df.corr(),title="Correlation Plot Heat-map")



