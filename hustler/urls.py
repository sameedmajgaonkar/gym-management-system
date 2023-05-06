from django.urls import path
from hustler import views
app_name = "hustler"

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('autobot/', views.autobot, name='autobot'),
    path('download/', views.download_file, name='download_file'),
]
