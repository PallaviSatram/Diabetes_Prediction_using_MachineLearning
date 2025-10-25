# Diabetes_Prediction_using_MachineLearning
Diabetes Prediction using Machine Learning is a project designed to predict the likelihood of diabetes in patients based on medical attributes such as Glucose, BMI, Blood Pressure, Insulin levels, Age, and more.

This project uses a Support Vector Machine (SVM) classifier to train on the PIMA Indians Diabetes Dataset, achieving reliable accuracy in distinguishing between diabetic and non-diabetic cases. The workflow includes data exploration, preprocessing (scaling and normalization), model training, evaluation, and prediction for new patient data.

🧠 Tech Stack
- **Language:** Python 🐍  
- **Libraries:** NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn  
- **Algorithm:** Support Vector Machine (SVM)  
- **Environment:** Google Colab / Jupyter Notebook

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

🔮 Future Improvements

-Experiment with ensemble models like Random Forest or XGBoost
-Hyperparameter tuning using GridSearchCV
-Build a web app using Flask or Streamlit for interactive predictions
-Implement cross-validation for more robust evaluation

This project is ideal for beginners and intermediate learners looking to understand end-to-end ML project development, from data processing to deployment-ready predictive models.
