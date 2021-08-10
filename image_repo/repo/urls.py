from django.urls import path
from . import views
from .views import ImageCreateView, HistoryListView

urlpatterns = [
    path('', ImageCreateView.as_view(), name="home"),
    path('history/', HistoryListView.as_view(), name="history"),
    path('search/', views.imageSearch, name="imageSearch"),
    path('<int:pk>/delete/', views.imageDelete, name="imageDelete"),
]