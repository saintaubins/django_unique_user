from django.urls import path
from transformers import views

urlpatterns = [
	path('transformers/',
		views.transformer_list,
		name = 'transformer'),
	path('transformers/<int:pk>/',
		views.transformer_detail,
		name = 'transformer'),
]
