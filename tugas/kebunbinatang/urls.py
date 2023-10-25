from django.urls import path
from . import views

urlpatterns = [
    path('kebunbinatang/', views.kebunbinatang, name='kebunbinatang'),
]