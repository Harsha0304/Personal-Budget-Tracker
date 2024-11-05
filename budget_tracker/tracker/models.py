# Create your models here.
from django.db import models

# class Category(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

class Category(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('entertainment', 'Entertainment'),
        ('transportation', 'Transportation'),
        ('utilities', 'Utilities'),
        ('healthcare', 'Healthcare'),
        ('others', 'Others'),
    ]
    
    name = models.CharField(max_length=50, choices=CATEGORY_CHOICES, unique=True)

    def __str__(self):
        return self.get_name_display()  # This will display the readable name in templates


class Transaction(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.amount} - {self.category.name}"

class Budget(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Budget for {self.category.name}: {self.amount}"
