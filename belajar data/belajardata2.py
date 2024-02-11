import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
dt = pd.read_csv('Iris.csv')
df = pd.DataFrame(dt)
df.drop("Id", axis=1, inplace=True)
x = df.drop("Species", axis=1)
y = df['Species']

# memisahkan data uji dan data testing
x_uji, x_testing, y_uji, y_testing = train_test_split(
    x, y, test_size=0.1, random_state=42)
# membuat model
model = KNeighborsClassifier()
model.fit(x_testing, y_testing)

uji_model = model.predict(x_uji)
acc = round(accuracy_score(uji_model, y_uji), 3)

print(model.predict([[6.2, 3.4, 5.4, 2.3]])[0])
