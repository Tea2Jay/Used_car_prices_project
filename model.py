# %%
import sklearn
from sklearn.model_selection import train_test_split
import autosklearn.regression
import pandas as pd
from joblib import dump,load
import pickle
import sklearn.metrics
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LogisticRegression

# %%
df = pd.read_csv('merged_dataset_dummies.csv')
# data = df.values
x, y = df.drop(columns='car_price'), df['car_price']

X_train, X_test, y_train, y_test = train_test_split(
    x, y, test_size=0.25, random_state=1)
# %%
automl = autosklearn.regression.AutoSklearnRegressor(
    time_left_for_this_task=120,
    per_run_time_limit = 30,
    output_folder='done',
    metric=autosklearn.metrics.mean_squared_error

)
automl.fit(X_train,y_train,dataset_name='Used_cars_prices')


dump(automl,'automl_test.joblib')
# %%
print(automl.sprint_statistics())
print(automl.show_models())
# %%
y_pred = automl.predict(X_test)

# %%
print("Mean score", sklearn.metrics.mean_squared_error(y_test, y_pred))

# %%
print(automl.get_models_with_weights())
# %%

lr = DecisionTreeRegressor()
lr.fit(X_train,y_train)
# %%
y_pred = lr.predict(X_test)
print("Mean score", sklearn.metrics.mean_squared_error(y_test, y_pred))
