from . import views
from django.urls import path

app_name='blog'
urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]