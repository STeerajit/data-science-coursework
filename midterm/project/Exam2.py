import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline

# Load dataset
file_path = 'dataset/2_Mall_Customers_Adj.csv'
df = pd.read_csv(file_path)

# แปลงชื่อคอลัมน์ให้เหมาะสม
columns = ['CustomerID', 'Gender', 'Age', 'AnnualIncome', 'SpendingScore']
df.columns = columns

# แปลง Gender เป็นตัวเลข
le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])

# แสดงข้อมูลตัวอย่าง
print(df.head())

# Correlation plot
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()

# แสดง Correlation Matrix
corr_matrix = df.corr()
print('\nCorrelation Matrix:')
print(corr_matrix)

# Features และ Target
X = df[['Gender', 'Age', 'AnnualIncome']]
y = df['SpendingScore']

# แบ่งข้อมูล train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ทดสอบ Polynomial Regression หลาย degree
degrees = [1, 2, 3, 4, 5]
mse_list = []
for degree in degrees:
    poly = PolynomialFeatures(degree=degree)
    X_train_poly = poly.fit_transform(X_train)
    X_test_poly = poly.transform(X_test)
    model = LinearRegression()
    model.fit(X_train_poly, y_train)
    y_pred = model.predict(X_test_poly)
    mse = mean_squared_error(y_test, y_pred)
    mse_list.append(mse)
    print(f'Degree {degree}: MSE = {mse:.2f}')
    if degree == 2:  # แสดงรายละเอียดของ degree ที่เหมาะสม
        print(f'\nPolynomial Degree 2 Coefficients:')
        print(model.coef_)
        print(f'Intercept: {model.intercept_}')
        print('\nตัวอย่างค่าทำนาย (y_pred) เทียบกับจริง (y_test):')
        compare_df = pd.DataFrame({"y_true": y_test.values, "y_pred": y_pred})
        print(compare_df.head(10))

# Plot MSE vs Degree
plt.figure(figsize=(6,4))
plt.plot(degrees, mse_list, marker='o')
plt.xlabel('Polynomial Degree')
plt.ylabel('Mean Squared Error (MSE)')
plt.title('Model Complexity vs. Prediction Error')
plt.show()

# เลือก degree ที่เหมาะสมที่สุด (MSE ต่ำสุด)
best_degree = degrees[np.argmin(mse_list)]
print(f'\nแนะนำให้ใช้ Polynomial Degree = {best_degree} สำหรับการทำนาย Spending Score')

# Pairplot
sns.pairplot(df)
plt.suptitle('Pairplot of All Attributes', y=1.02)
plt.show()

# --- Polynomial Regression Visualization ---
# ใช้ feature AnnualIncome กับ SpendingScore เพื่อแสดงเส้น polynomial regression

# เลือก degree ที่เหมาะสมที่สุด
best_degree = degrees[np.argmin(mse_list)]

# Fit polynomial regression กับข้อมูลทั้งหมด (AnnualIncome -> SpendingScore)
X_plot = df[['AnnualIncome']].values
X_plot_range = np.linspace(X_plot.min(), X_plot.max(), 200).reshape(-1, 1)
poly_model = make_pipeline(PolynomialFeatures(degree=best_degree), LinearRegression())
poly_model.fit(X_plot, y)
y_plot = poly_model.predict(X_plot_range)

plt.figure(figsize=(8,6))
plt.scatter(df['AnnualIncome'], df['SpendingScore'], color='blue', label='Actual Data', alpha=0.5)
plt.plot(X_plot_range, y_plot, color='red', linewidth=2, label=f'Polynomial Regression (degree={best_degree})')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score')
plt.title(f'Polynomial Regression Fit (degree={best_degree})')
plt.legend()
plt.show()
