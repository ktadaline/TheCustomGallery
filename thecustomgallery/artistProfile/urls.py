from django.urls import path
from . import views
urlpatterns = [
    path('api/lead/', views.artistProfileListCreate.as_view() ),
]