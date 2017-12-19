from django.shortcuts import render
from django.views import generic
from rest_framework import generics

from .models import Billing


class BillingDashboardView(generic.TemplateView):
  model = Billing
  context_object_name = 'billings'
  queryset = Billing.objects.all()
  template_name = 'companystats/dashboard.html'

  def get_context_data(self,*args,**kwargs):

  	ctx = super().get_context_data(*args, **kwargs)
  	ctx['billings']  = self.queryset
  	return ctx