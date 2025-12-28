# Diabetes_Prediction_using_MachineLearning
Diabetes Prediction using Machine Learning is a project designed to predict the likelihood of diabetes in patients based on medical attributes such as Glucose, BMI, Blood Pressure, Insulin levels, Age, and more.

This project uses a Support Vector Machine (SVM) classifier to train on the PIMA Indians Diabetes Dataset, achieving reliable accuracy in distinguishing between diabetic and non-diabetic cases. The workflow includes data exploration, preprocessing (scaling and normalization), model training, evaluation, and prediction for new patient data.

🧠 Tech Stack
- **Language:** Python 🐍  
- **Libraries:** NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn  
- **Algorithm:** Support Vector Machine (SVM)  
- **Environment:** Google Colab / Jupyter Notebook
- **Deployment:** Streamlit

📊 Dataset
- Dataset used: **PIMA Indians Diabetes Dataset**  
- Source: [Kaggle - Diabetes Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)  
- Features include:
  - Pregnancies  
  - Glucose  
  - Blood Pressure  
  - Skin Thickness  
  - Insulin  
  - BMI  
  - Diabetes Pedigree Function  
  - Age  
  - Outcome (0 = Non-Diabetic, 1 = Diabetic)
 
⚙️ Project Workflow
1. Import Dependencies  
2. Load and Explore the Dataset (EDA)  
3. Data Preprocessing (Scaling, Cleaning)  
4. Train-Test Split  
5. Model Training using SVM  
6. Model Evaluation (Accuracy Score)  
7. Predictive System Development  
8. Deployment / Integration (optional)

📈 Model Performance
Accuracy ~77-78%

🚀 How to Run the Project
  pip install -r requirements.txt
  streamlit run Diabetes_Pred_App.py 

**Future Improvements**

- Experiment with ensemble models such as Random Forest and XGBoost
- Perform hyperparameter tuning using GridSearchCV
- Implement cross-validation for better generalization
- Enhance the Streamlit UI for improved user experience
- Deploy the application on Streamlit Cloud or Render

**Key Learning Outcomes**

- Understanding of end-to-end machine learning workflow
- Hands-on experience with data preprocessing and model evaluation
- Practical implementation of SVM for binary classification
- Introduction to deploying ML models using Streamlit
