from . import views
from django.urls import path


app_name = "userApp"

urlpatterns = [
    path('',views.login,name = 'mainLogin'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name = 'signup'),
    path('home/',views.home,name='home'),
    path('chat/<str:username>/',views.chat,name = 'chat'),
    path('getMES/<str:username>/',views.getData,name="getMES"),
    path('logout/',views.Logout,name = 'logout'),
    path('Del/',views.Del,name= "Del"),
]
