from django.urls import path
from pages_content.views import explore
urlpatterns = [
    path('', explore, name='explore'),
]
