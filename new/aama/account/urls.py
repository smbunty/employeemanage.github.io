from django.urls import path
from . import views

urlpatterns = [
    path('',views.ndex),
    path('signup',views.signup,name='signup'),
    path("signupage",views.signupage,name='signupage'),
    path('signin',views.signin,name='signin'),
    path('signinpage',views.signinpage,name='signinpage'),
    path('user',views.user,name='user'),
    path('logout',views.logout,name='logout')
]
   
