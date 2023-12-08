from django.urls import path
from . import views

app_name = 'UserApp'

urlpatterns = [
    path('register/',views.register,name = 'register')
]