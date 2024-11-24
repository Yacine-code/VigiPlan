from django.urls import path
from .views import SiteListView, SiteCreateView, SiteUpdateView, SiteDeleteView

urlpatterns = [
    path('', SiteListView.as_view(), name='site-list'),
    path('create/', SiteCreateView.as_view(), name='site-create'),
    path('<int:pk>/update/', SiteUpdateView.as_view(), name='site-update'),
    path('<int:pk>/delete/', SiteDeleteView.as_view(), name='site-delete'),
]
