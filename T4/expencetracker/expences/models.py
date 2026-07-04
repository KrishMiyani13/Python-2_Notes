from django.db import models

# Create your models here.

class Expense(models.Model):
    CATEGORY_CHOICES = [
        
            ("Food","Food"),
            ("Travel","Travel"),
            ("Shopping","Shopping")
    ]
    title = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50,choices=CATEGORY_CHOICES)
    expense_date = models.DateField()