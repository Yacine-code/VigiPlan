from django.urls import path
from .views import PrestationListView, PrestationCreateView, PrestationUpdateView, PrestationDeleteView

urlpatterns = [
    path('', PrestationListView.as_view(), name='prestation-list'),
    path('create/', PrestationCreateView.as_view(), name='prestation-create'),
    path('<int:pk>/update/', PrestationUpdateView.as_view(), name='prestation-update'),
    path('<int:pk>/delete/', PrestationDeleteView.as_view(), name='prestation-delete'),
]
