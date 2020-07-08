from django.urls import path
from . import views

app_name='download'
urlpatterns = [
    path('create/',views.image_create,name='create'),
]