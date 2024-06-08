from pyexpat.errors import messages
from django.shortcuts import render
from django.shortcuts import render
import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Create your views here.
def diabitic(request):
    if request.method == "POST":
            age = request.POST.get('n1')
            sex = request.POST.get('n2')
            highchol = request.POST.get('n3')
            cholcheck = request.POST.get('n4')
            bmi = request.POST.get('n5')
            smoker = request.POST.get('n6')
            heartdiseage = request.POST.get('n7')
            physactivity = request.POST.get('n8')
            fruit = request.POST.get('n9')
            veggies = request.POST.get('n10')
            alcohal = request.POST.get('n11')
            genhlt = request.POST.get('n12')
            mental = request.POST.get('n13')
            physical = request.POST.get('n14')
            diffwalk = request.POST.get('n15')
            stroke = request.POST.get('n16')
            highbp = request.POST.get('n17')
            age=int(age)
            sex=int(sex)
            highchol=int(highchol)
            cholcheck=int(cholcheck)
            bmi=int(bmi)
            smoker=int(smoker)
            heartdiseage=int(heartdiseage)
            physactivity=int(physactivity)
            fruit=int(fruit)
            veggies=int(veggies)
            alcohal=int(alcohal)
            genhlt=int(genhlt)
            mental=int(mental)
            physical=int(physical)
            diffwalk=int(diffwalk)
            stroke=int(stroke)
            highbp=int(highbp)
            print(age,sex,highchol,cholcheck,bmi,smoker,heartdiseage,physactivity,fruit,veggies,alcohal,genhlt,mental,physical,diffwalk,stroke,highbp)
            data = [age,sex,highchol,cholcheck,bmi,smoker,heartdiseage,physactivity,fruit,veggies,alcohal,genhlt,mental,physical,diffwalk,stroke,highbp]
            accuracy,result= diabetes_prediction(data)
            print(accuracy,result)
            context = {
                'result':result
            }
            if result == "Diabetic":
            #   messages.success(request, 'The user is not diabetic')
              return render(request,"diabeticresult.html",context)
            elif result == "Non-Diabetic":
                #  messages.error(request, 'The user is diabetic')
                 return render(request,"diabeticresult.html",context)

    return render(request,'diabeticform.html')


def diabetes_prediction(in_data):
  
    data = pd.read_csv('static\diabetes_data.csv') 
    X = data.drop('Diabetes', axis=1) 
    y = data['Diabetes']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    logreg = LogisticRegression(max_iter=100000)  
    logreg.fit(X_train, y_train)
    y_pred = logreg.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred) * 100
    user_data = np.array([in_data]) 
    user_prediction = logreg.predict(user_data)
    print(user_prediction)

    if user_prediction == 0:
        user_category = "Non-Diabetic"
    elif user_prediction == 1:
        user_category = "Diabetic"
    
    return accuracy, user_category

def resultl(request):
     return render(request,"diabeticresult.html")


def bloodpressure(request):
     if request.method == "POST":
            Hemoglobin = request.POST.get('n1')
            Genetic = request.POST.get('n2')
            Age = request.POST.get('n3')
            bmi = request.POST.get('n4')
            sex = request.POST.get('n5')
            Pregnancy = request.POST.get('n6')
            Smoking = request.POST.get('n7')
            Physical = request.POST.get('n8')
            salt = request.POST.get('n9')
            alcohol = request.POST.get('n10')
            stress = request.POST.get('n11')
            kidney = request.POST.get('n12')
            thyroid = request.POST.get('n13')

            Hemoglobin=int(Hemoglobin)
            Genetic=int(Genetic)
            Age=int(Age)
            bmi=int(bmi)
            sex=int(sex)
            Pregnancy=int(Pregnancy)
            Smoking=int(Smoking)
            Physical=int(Physical)
            salt=int(salt)
            alcohol=int(alcohol)
            stress=int(stress)
            kidney=int(kidney)
            thyroid=int(thyroid)
            
            print(Hemoglobin,Genetic,Age,bmi,sex,Pregnancy,Smoking,Physical,salt,alcohol,stress,kidney,thyroid)
            data = [Hemoglobin,Genetic,Age,bmi,sex,Pregnancy,Smoking,Physical,salt,alcohol,stress,kidney,thyroid]
            accuracy,result= blood_prediction(data)
            print(accuracy,result)
            context = {
                'result':result
            }
            if result == "Don't have a blood pressure":
            #   messages.success(request, 'The user is not diabetic')
              return render(request,"diabeticresult.html",context)
            elif result == "User have a blood pressure":
                #  messages.error(request, 'The user is diabetic')
                 return render(request,"diabeticresult.html",context)
     return render(request,"bloodpressure.html")

def blood_prediction(in_data):
     
    data = pd.read_csv('static\data.csv')  # Update path as necessary

    # Drop the Patient_Number column
    data = data.drop(columns=['Patient_Number'])

    # Check for missing values and fill if necessary
    # Here we fill missing values with the mean of the respective columns
    data = data.fillna(data.mean())

    # Extract features and target variable
    X = data.drop('Blood_Pressure_Abnormality', axis=1)  # Assuming the target column name is 'Blood_Pressure_Abnormality'
    y = data['Blood_Pressure_Abnormality']

    # Split the data into training/testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.6, random_state=42)

    # Create logistic regression object with increased max_iter
    logreg = LogisticRegression(max_iter=1000)  # Increase max_iter value as needed

    # Train the model using the training sets
    logreg.fit(X_train, y_train)

    # Make predictions using the testing set
    y_pred = logreg.predict(X_test)

    # Calculate accuracy percentage
    accuracy = accuracy_score(y_test, y_pred) * 100

    # Example user data with all features except Patient_Number (Ensure the order matches the dataset)
    user_data = np.array([in_data])   # Replace with actual feature values as necessary

    # Ensure user_data has the correct shape
    if user_data.shape[1] != X_train.shape[1]:
        raise ValueError("Number of features in user_data does not match the training data")

    # Predict the class for the user data
    user_prediction = logreg.predict(user_data)

    if user_prediction == 0:
        user_category = "Don't have a blood pressure"
    elif user_prediction == 1:
        user_category = "User have a blood pressure"
    else:
        user_category = "Unknown"  # In case there are more categories

    return accuracy, user_category


def recipe(request):
    return render(request,'recipe.html')

def Chicken_on_Sweetcorn_Puree(request):
    return render(request,'Chicken_on_Sweetcorn_Puree.html')