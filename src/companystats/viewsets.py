from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.response import Response
from . models import Billing, Company, Department

from .serializers import BillingSerializer, CompanySerializer

class BillingViewSet(viewsets.ModelViewSet):
	model = Billing
	serializer_class = BillingSerializer

	def get_queryset(self):
		queryset = Billing.objects.all()
		return queryset.order_by('payment_date')

	def retrieve(self, request, *args, **kwargs):
		# company_id = kwargs.get('id', None)
		# company = Company.objects.get(id=company_id)
		self.queryset = Billing.objects.filter(company='Merojob')
		return super(BillingViewSet, self).retrieve(request, *args, **kwargs)

		
class CompanyViewSet(viewsets.ModelViewSet):
	model = Company
	queryset = Company.objects.all()
	serializer_class = CompanySerializer
	lookup_field = 'id'

	def get_queryset(self):
		queryset = Company.objects.all()
		return queryset.order_by('company_name')

	def retrieve(self, request, *args, **kwargs):
		company_id = kwargs.get('id', None)
		company = Company.objects.get(id=company_id)
		self.queryset = Billing.objects.filter(company=company).distinct()
		return super(CompanyViewSet, self).retrieve(request, *args, **kwargs)

	# def get_queryset(self):
	# 	c3 = Company.objects.get(id=3)
	# 	serializer = CompanySerializer(instance=c3)
	# 	Response(serializer.data)