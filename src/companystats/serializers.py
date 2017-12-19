from rest_framework import serializers
import datetime
from datetime import date

from .models import Company, Department, Billing


class BillingSerializer(serializers.ModelSerializer):
	company_name = serializers.SerializerMethodField()	
	department_name = serializers.SerializerMethodField()
	remaining_days = serializers.SerializerMethodField()

	class Meta:
		model = Billing
		fields = ('company_name', 'department_name', 'expenditure_point', 'amount', 'payment_date', 'remaining_days','status')

	def get_company_name(self, instance):
		self.company_name = instance.company.company_name
		return self.company_name


	def get_department_name(self, instance):
		self.department_name = instance.department.department_name
		return self.department_name

	def get_remaining_days(self, instance):
		if instance.status == 'PAID':
			self.remaining_days = "-"
			return self.remaining_days
		delta = instance.payment_date - datetime.date.today()
		self.remaining_days = delta.days
		return self.remaining_days


class CompanySerializer(serializers.ModelSerializer):
	billings = BillingSerializer(many=True)

	class Meta:
		model = Company
		fields = ('company_name', 'billings')

	def create(self, validated_data):
		billings_data = validated_data.pop('billings')
		company = Company.objects.create(**validated_data)
		for billing_data in billings_data:
			Billing.objects.create(company=company, **billing_data)
		return company