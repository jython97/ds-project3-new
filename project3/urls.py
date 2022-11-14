from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('table/', views.index2, name='index2'),
    path('<int:id>/', views.index3, name='index3')
]