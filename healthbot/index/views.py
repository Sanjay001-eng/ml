from django.shortcuts import render
import joblib
#import pickle
#import pandas as pd
#from sklearn import svm
# Create your views here.
def index(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'services.html')

def predictheart(request):
    return render(request, 'predictheart.html')


def predictdiabetes(request):
    return render(request, 'predictdiabetes.html')


def predictparkinson(request):
    return render(request, 'predictparkinson.html')

def diabetesresults(request):
    #cls = pickle.load(open('diabetes_model.sav', 'rb'))
    cls = joblib.load('diabetes_model.sav')
    lis = []
    # Pregnancies Glucose	BloodPressure SkinThickness Insulin BMI DiabetesPedigreeFunction Age
    lis.append(float(request.GET['Pregnancies']))
    lis.append(float(request.GET['Glucose']))
    lis.append(float(request.GET['BloodPressure']))
    lis.append(float(request.GET['SkinThickness']))
    lis.append(float(request.GET['Insulin']))
    lis.append(float(request.GET['BMI']))
    lis.append(float(request.GET['DiabetesPedigreeFunction']))
    lis.append(float(request.GET['Age']))
    # print(lis)
    ans = cls.predict([lis])

    return render(request, 'results.html', {'ans': ans})

def heartresults(request):
    #cls = pickle.load(open('diabetes_model.sav', 'rb'))
    cls = joblib.load('heart_disease_model.sav')
    lis = []
      #age sex cp trestbps chol fbs restecg thalach exang oldpeak slope ca thal target

    lis.append(float(request.GET['age']))
    lis.append(float(request.GET['sex']))
    lis.append(float(request.GET['cp']))
    lis.append(float(request.GET['trestbps']))
    lis.append(float(request.GET['chol']))
    lis.append(float(request.GET['fbs']))
    lis.append(float(request.GET['restecg']))
    lis.append(float(request.GET['thalach']))
    lis.append(float(request.GET['exang']))
    lis.append(float(request.GET['oldpeak']))
    lis.append(float(request.GET['slope']))
    lis.append(float(request.GET['ca']))
    lis.append(float(request.GET['thal']))
    # print(lis)
    ans = cls.predict([lis])

    return render(request, 'results.html', {'ans': ans})

def parkinsonresults(request):
    #cls = pickle.load(open('diabetes_model.sav', 'rb'))
    cls = joblib.load('parkinsons_model.sav')
    lis = []

    lis.append(float(request.GET['MDVP:Fo(Hz)']))
    lis.append(float(request.GET['MDVP:Fhi(Hz)']))
    lis.append(float(request.GET['MDVP:Flo(Hz)']))
    lis.append(float(request.GET['MDVP:Jitter(%)']))
    lis.append(float(request.GET['MDVP:Jitter(Abs)']))
    lis.append(float(request.GET['MDVP:RAP']))
    lis.append(float(request.GET['MDVP:PPQ']))
    lis.append(float(request.GET['Jitter:DDP']))
    lis.append(float(request.GET['MDVP:Shimmer']))
    lis.append(float(request.GET['Shimmer:APQ3']))
    lis.append(float(request.GET['Shimmer:APQ5']))
    lis.append(float(request.GET['MDVP:APQ']))
    lis.append(float(request.GET['Shimmer:DDA']))
    lis.append(float(request.GET['NHR']))
    lis.append(float(request.GET['HNR']))
    lis.append(float(request.GET['status']))
    lis.append(float(request.GET['RPDE']))
    lis.append(float(request.GET['DFA']))
    lis.append(float(request.GET['spread1']))
    lis.append(float(request.GET['spread2']))
    lis.append(float(request.GET['D2']))
    lis.append(float(request.GET['PPE']))
    # print(lis)
    ans = cls.predict([lis])

    return render(request, 'results.html', {'ans': ans})