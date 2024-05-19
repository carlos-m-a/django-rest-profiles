from django.urls import path, include
from . import views

app_name = 'profiles'

urlpatterns = [
    # For API - rest framework
    path('mymodel/', views.MyModelListApiView.as_view()),
    path('mymodel/<int:mymodel_id>/', views.MyModelDetailApiView.as_view()),
]