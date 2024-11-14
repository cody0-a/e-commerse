from django.urls import path
from  account.views import login_view,register_views,index_views,reset_passwd


app_name = 'account'
urlpatterns = [
    path('', index_views, name='login'),
    path('login/', login_view, name='login'),
    path('register/',register_views,name='register'), 
    path('reset/',reset_passwd ,name = 'reset'),
]