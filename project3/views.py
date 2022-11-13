from django.shortcuts import render
from .models import data
import pandas as pd
import shap
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import pickle
import numpy as np
from .ai import preprocess, shap_plot

# Create your views here.
def index(request):
    return render(request, 'index.html')

def index2(request, summoners):
    dat = data.objects.get(summoners=summoners)
    context = {"data" : dat}
    return render(request, 'index2.html', context)

def index3(request, id):
    with open('model.pickle', 'rb') as fr:
        model = pickle.load(fr)
    pro_x, y, pro_df = preprocess()
    shap_plot(model, pro_df, id)
    return render(request, 'index3.html')