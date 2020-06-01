import pickle

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib

from Aiplatform.app.com.rs.services.product_taxonomy.product_taxonomy_preprocess import MySimpleScaler

iris = load_iris()
print(iris)
scaler = MySimpleScaler()
X = scaler.preprocess(iris.data)
y = iris.target

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, 'model.joblib')
with open ('preprocessor.pkl', 'wb') as f:
  pickle.dump(scaler, f)

