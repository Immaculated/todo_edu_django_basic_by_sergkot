from django.urls import path
from registration.views import registration_view, login_view

app_name = 'registration'

urlpatterns = [
    path('', registration_view, name='registration'),
    path('login/', login_view, name='login'),
]
