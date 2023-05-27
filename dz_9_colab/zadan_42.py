import pandas as pd

data = pd.read_csv('sample_data/california_housing_train.csv')

min_population = data['population'].min()

filtered_data = data[data['population'] == min_population]

max_households = filtered_data['households'].max()

print(f"Максимальное значение households в зоне минимального значения population: {max_households}")