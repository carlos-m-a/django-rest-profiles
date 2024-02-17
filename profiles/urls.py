from django.urls import path, include
from . import views

app_name = 'profiles'

urlpatterns = [
    # For API - rest framework
    path('mymodel/', views.MyModelListApiView.as_view()),
    path('mymodel/<int:mymodel_id>/', views.MyModelDetailApiView.as_view()),

    # For templates rendered pages
    path("my_model_list/", views.MyModelListView.as_view(), name="my_model_list"),
    path("my_model_create/", views.MyModelCreateView.as_view(), name="my_model_create"),
]