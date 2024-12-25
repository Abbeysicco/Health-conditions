### INTRODUCTION
> This dataset contains some nutrition facts relevant to daily meals for patients sufering from different diseases with 1698 rows and 19 columns which includes Ages, Gender, Height, Weight, Activity Level, Dietary Preference, Daily Calorie Target, Protein, Sugar, Sodium, Calories, Carbohydrates, Fiber, Fat, Breakfast Suggestion, Lunch Suggestion, Dinner Suggestion, Snack Suggestion and Disease
The dataset contains 11 Numerical columns and 8 categorical columns

### Dataset Cleaning:
There is no missing value and duplicated values in the dataset
### Exploratory Data Analysis:
Considering the Disease column which is the target column has imbalance variable where the Weight Gain has an amount which is significally high compare to other varibles. The Disesse column isa multi- label column where the multi-label target variable (e.g., diseases) are converted into a binary format using the MultiLabelBinarizer.

### Data Preprocessing:
LabelEncoder was use to encode the categoriacal values.
### Modeling
The dataset was trained using OneVsRestClassifier (OvR) with Logistic Regression, Decision Tree Clssifier and Random Forest Classifier. OvR is a useful strategy for multi-class classification problems. It essentially transforms the multi-class problem into multiple binary classification tasks. It trains one classifier for each class in the dataset. Each classifier learns to distinguish between one class and all the other classes combined (the "rest"). At the end of modelling, Logistic Regression was chosen beacuse it has best model generalization, as it shows a strong balance between performance on the training and testing data unlike the other two that scores 100% for both training and testing which might be as a result of overfitting

### Model deployment
The application is deployed for better user interaction on streamlit

# Limitation
The dataset is inbalance with Weight Gain dominating but was left lalone because it is a multi-label column

### Conclussion
The project was an end to end Supervised classification project, which give general overview on Disease/ Health Condition