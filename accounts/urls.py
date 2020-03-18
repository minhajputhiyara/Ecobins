
from django.urls import path
from accounts.views import SignUpView,LogoutView,LoginView

urlpatterns = [
    path('signup/',SignUpView,name="signup"),
    path('logout/',LogoutView,name='logout'),
    path('login/', LoginView,name="login"),

]
