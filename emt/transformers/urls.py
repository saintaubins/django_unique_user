from django.urls import path
from transformers import views

urlpatterns = [
	path('transformers/', views.transformer_list, name = 'transformer-list'),
	path('transformers/<int:pk>/', views.transformer_detail, name = 'transformer-detail'),
	path('usersdata/<str:obj>/', views.usersData, name = 'usersdata'),
	path('usersdatadetail/<str:obj>/<int:pk>/', views.usersDataDetail, name = 'usersdatadetail')
]
