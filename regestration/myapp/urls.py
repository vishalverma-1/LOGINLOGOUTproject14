from django.urls import path
from . import views
urlpatterns = [
    path('',views.reg,name='reg'),
    path('login/',views.log,name='login'),
    path('home/',views.home,name="home"),
    path('logout/',views.logout,name="logout"),
]
