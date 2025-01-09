import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
from sklearn.preprocessing import LabelEncoder

# Step 1: Load the data from CSV
# Replace 'your_data.csv' with the path to your actual CSV file
data = pd.read_csv('src/training_dataset.csv')[:10]

label_encoder = LabelEncoder()

# Assuming your target column is 'risk' and your dataframe is named 'data'
data['risk_encoded'] = label_encoder.fit_transform(data['anomaly'])

# Now, you can use 'risk_encoded' as the target (y) instead of the original 'risk'
y = data['risk_encoded']

# Step 2: Inspect the data (Optional, but helpful for understanding its structure)
print(data.head())  # Displays the first 5 rows of the dataset
print(data.info())  # Displays the data types and non-null counts

# Step 3: Preprocess the data
# Assuming the last column is the target (y) and the rest are features (X)
X = data.drop('anomaly', axis=1)  # Replace 'target_column' with the actual name of your target column

# Handle categorical variables (if any)
# If you have categorical variables, you can use one-hot encoding or label encoding
X = pd.get_dummies(X)

# Step 4: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 5: Train the Decision Tree Classifier
clf = DecisionTreeClassifier(criterion='gini', max_depth=5)  # You can adjust parameters like max_depth
clf.fit(X_train, y_train)

# Step 6: Make predictions
y_pred = clf.predict(X_test)

# Step 7: Evaluate the model
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", metrics.confusion_matrix(y_test, y_pred))

# Step 8: Plot the tree
plt.figure(figsize=(12, 8))
plot_tree(clf, filled=True, feature_names=X.columns, class_names=str(y.unique()), rounded=True)
plt.show()
