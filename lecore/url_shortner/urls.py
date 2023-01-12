from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('create',views.create,name='create'),
    path('<str:dynvar>',views.go,name='go') # dynvar is a dynamic url that will redirect to go function
]