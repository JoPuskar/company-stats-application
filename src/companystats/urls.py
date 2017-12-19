from django.conf.urls import url, include
from django.views.generic import ListView

from . import views
from .views import BillingDashboardView

urlpatterns = [
    url(r'^dashboard', views.BillingDashboardView.as_view(), name='dashboard'),
]