from django.db import models

class FinancialData(models.Model):
    label = models.CharField(max_length=255)  
    description = models.TextField()
    units = models.CharField(max_length=50)  
    end_date = models.DateField()
    value = models.IntegerField()
    accn = models.TextField()
    fiscal_year = models.IntegerField()
    filing_form = models.CharField(max_length=20)  
    filed_date = models.DateField()
    frame = models.TextField()
