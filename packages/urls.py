from django.urls import path
from .views import PackageListView, PackageCreateView


app_name = 'packages'

urlpatterns = [
    path('package-list/', PackageListView.as_view(), name='package-list'),
    path('package-create/', PackageCreateView.as_view(), name='package-create'),
]