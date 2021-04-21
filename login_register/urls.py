from django.urls import path
from login_register.views import login_view, sign_view
urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', sign_view, name='signup'),
]
