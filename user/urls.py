from django.conf.urls import url
from user import views

app_name = 'user'

urlpatterns = [
    url(r'^login/', views.login,name='user_login'),
    url(r'^register/', views.register,name='user_register'),
    url(r'^logout/', views.logout,name='user_loginout'),

]
