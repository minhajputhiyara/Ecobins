
from django.urls import path
from accounts.views import SignUpView
urlpatterns = [
    path('signup/',SignUpView,name="signup"),
]
