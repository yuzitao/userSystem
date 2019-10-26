from django.urls import path
from User.views import U_P_Register
app_name = 'user'
urlpatterns = [
    path('register/', U_P_Register.as_view(), name='u_p_register'),
]