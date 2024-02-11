# dessison tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv("Iris.csv")
dataset.drop("Id", axis=1, inplace=True)
# memisahkan atribut dan label
vIndependet = dataset[["Size", "Weight", "Sweetness",
                       "Crunchiness", "Juiciness", "Ripeness", "Acidity"]]
vdependent = dataset[['Species']]
# Membagi dataset menjadi data latih & data uji
X_train, X_test, y_train, y_test = train_test_split(
    vIndependet, vdependent, test_size=0.1, random_state=1)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
acc_secore = round(accuracy_score(y_pred, y_test), 3)

print('Accuracy: ', acc_secore)

# prediksi model dengan tree_model.predict([[SepalLength, SepalWidth, PetalLength, PetalWidth]])
print(model.predict([[6.2, 3.4, 5.4, 2.3]])[0])
plt.plot(vIndependet, vdependent)
plt.show()
