import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

file_path = 'dataset/3_dataset_tafu_2000.csv'
df = pd.read_csv(file_path)
print('ข้อมูลตัวอย่าง:')
print(df.head())


print('\nMissing values ต่อคอลัมน์:')
print(df.isnull().sum())
print('\nประเภทข้อมูล:')
print(df.dtypes)

df = df.fillna(df.median(numeric_only=True))

if df['label'].dtype == 'O':
    le = LabelEncoder()
    df['label'] = le.fit_transform(df['label'])

X = df.drop('label', axis=1)
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


models = {
    'LogisticRegression': LogisticRegression(max_iter=1000),
    'RandomForest': RandomForestClassifier(),
    'SVC': SVC(),
    'KNN': KNeighborsClassifier()
}
accuracies = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    accuracies[name] = acc
    print(f'{name} accuracy: {acc:.4f}')

selected = [name for name, acc in accuracies.items() if acc > 0.9]
if selected:
    best_name = max(selected, key=lambda n: accuracies[n])
    best_model = models[best_name]
    print(f'\nเลือกโมเดล: {best_name} (accuracy = {accuracies[best_name]:.4f})')
    # 8. แสดง confusion matrix
    y_pred = best_model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot(cmap='Blues')
    plt.title(f'Confusion Matrix: {best_name}')
    plt.show()
else:
    print('ไม่มีโมเดลใดที่ accuracy > 90%')