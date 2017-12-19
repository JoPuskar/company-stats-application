from django.db import models

class Company(models.Model):
	company_name = models.CharField(max_length=120, unique=True)

	class Meta:
		verbose_name_plural = "Companies"

	def __str__(self):
		return self.company_name

class Department(models.Model):
	department_name = models.CharField(max_length=120, unique=True)

	def __str__(self):
		return self.department_name

class Billing(models.Model):
	PAYMENT_STATUSES = (
		('PAID', 'Paid'),
		('UNPAID', 'Unpaid'),
	)
	company = models.ForeignKey(Company, related_name='billings', on_delete=models.CASCADE)
	department = models.ForeignKey(Department, related_name='billings', on_delete=models.CASCADE)
	expenditure_point = models.CharField(max_length=120)
	amount = models.PositiveIntegerField()
	payment_date = models.DateField()
	status = models.CharField(max_length=6, default='UNPAID', choices=PAYMENT_STATUSES)

	class Meta:
		unique_together = ('company', 'department', 'expenditure_point')
		ordering = ['payment_date']

	def __str__(self):
		return '%s %s %s' % (self.expenditure_point, self.department, self.company)