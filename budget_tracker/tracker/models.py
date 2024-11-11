from django.db import models
from django.contrib.auth.models import User

def get_default_user():
    return User.objects.get(username='default_user')  # Make sure this user exists

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
        return self.get_name_display()

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_default_user)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.amount} - {self.category.name} ({self.user.username})"

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_default_user)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Budget for {self.category.name}: {self.amount} ({self.user.username})"
