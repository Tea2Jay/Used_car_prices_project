# %%
import seaborn as sns
import pandas as pd

df_cars_mixed = pd.read_csv("carsclean.csv")
print(df_cars_mixed.info())
df_cars_mixed

# %%
df_used_only = pd.read_csv("used_car_cleaned.csv")
print(df_used_only.info())
df_used_only

# %%
df_cars_mixed = df_cars_mixed[df_cars_mixed['condition'] == 'Used']

df_cars_mixed.drop(columns=['city', 'condition',
                   'fuel', 'pay_method', 'color'], inplace=True)
df_cars_mixed
# %%
df_cars_mixed = df_cars_mixed.reindex(
    columns=['car_maker', 'model', 'kilometers', 'transmission', 'year', 'price'])
df_cars_mixed

# %%
mixed_col = df_cars_mixed.columns.tolist()
only_col = df_used_only.columns.tolist()

df_cars_mixed.rename(
    columns={mixed_col[i]: only_col[i] for i in range(6)}, inplace=True)
# %%
df_merged = [df_cars_mixed, df_used_only]

df_merged = pd.concat(df_merged)

# %%
df_merged.drop_duplicates(ignore_index=True, inplace=True)


# %%
sns.boxplot(x=df_merged['car_price'])

# %%
df_merged.to_csv("merged_dataset.csv", index=False)
# %%
# df_merged = df_merged[df_merged['car_price'] < 50000000]
# df_merged = df_merged[df_merged['car_price'] != 123]

# %%
# df_merged[df_merged['car_price']>= 1000000]
max_threshold = df_merged['car_price'].quantile(0.90)
max_threshold

# %%

df_merged[df_merged['car_price']>max_threshold]

# %%
min_threshold = df_merged['car_price'].quantile(0.05)
min_threshold

# %%
df_test = df_merged[df_merged['car_price']>min_threshold]
df_test = df_test[df_test['car_price']<max_threshold]
df_test

# %%
sns.boxplot(x=df_test['car_price'])
print(df_test['car_price'].mean())
print(df_test['car_price'].std())

# %%
df_test.to_csv("merged_dataset.csv", index=False)

# %%
df_test = pd.get_dummies(df_test, columns=['car_model', 'car_brand'])
df_test = df_test[df_test['car_transmission'] != 'CVT']
df_test['car_transmission'] = df_test['car_transmission'].replace(
    {'Automatic': 1, 'Manual': 0})

# %%
df_test.to_csv('merged_dataset_dummies.csv', index=False)
df_test.dtypes
