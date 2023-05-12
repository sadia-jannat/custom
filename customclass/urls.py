from django.urls import path
from customclass import views

urlpatterns = [
    path('custompage/', views.customclass_list),
    path('custompageid/<int:pk>/', views.customclass_detail),
]