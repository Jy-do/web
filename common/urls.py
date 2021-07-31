from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('ranking/', views.rankingpage, name='rankingpage'),
    path('introduction/', views.introductionpage, name='introductionpage'),
    path('calendar/', views.calendarpage, name='calendarpage'),
    path('mypage/', views.mypage, name='mypage'),

]