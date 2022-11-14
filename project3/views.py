from django.shortcuts import render
from .models import data
import pandas as pd
import shap
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import pickle
import numpy as np
from .ai import *
from django.http import HttpResponseRedirect
from .crawling import concat_data
from db import remake_db
from .remake_data import remake_data
import datetime

# 첫 화면 출력.
def index(request):
    # 갱신요청을 post로 받음
    if request.method=="POST":
        # 데이터 새롭게 크롤링
        concat_data()
        row_drop()

        # 새로운 모델 생성
        pro_x, y, pro_df = preprocess()
        model = boosting(pro_x, y)

        # postgres db갱신
        remake_data()
        remake_db()
        date = datetime.datetime.now()
        context = {"date" : data}
        return render(request, 'index.html', context)

    return render(request, 'index.html')

# 소환사 명을 받아서 db에서 필터링한 결과를 보내줌.
def index2(request):
    name = request.GET['summoners']
    dat = data.objects.filter(summoners=name)
    context = {"data" : dat, "name" : name}
    return render(request, 'index2.html', context)

# 두번째화면에서 클릭한 row에 해당하는 index값의 shap_plot을 생성하고 이를 출력.
def index3(request, id):
    with open('project3/model.pickle', 'rb') as fr:
        model = pickle.load(fr)
    pro_x, y, pro_df = preprocess()
    shap_plot(model, pro_df, id)
    dat = data.objects.get(id=id)
    context = {"data" : dat}
    return render(request, 'index3.html', context)