from rest_framework import routers

from . import viewsets

router = routers.DefaultRouter()
router.register(r'billing', viewsets.BillingViewSet, base_name='billing')
router.register(r'company', viewsets.CompanyViewSet, base_name='company')