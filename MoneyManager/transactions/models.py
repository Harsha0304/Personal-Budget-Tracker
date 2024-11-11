from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.name

class Transaction(models.Model):
    BORROWED = 'borrowed'
    LENT = 'lent'
    
    TRANSACTION_TYPE_CHOICES = [
        (BORROWED, 'Borrowed'),
        (LENT, 'Lent')
    ]
    
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.transaction_type.title()} - {self.amount} with {self.person.name}"

class ScheduledPayment(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    frequency = models.CharField(max_length=50)  # e.g., "monthly"
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"Scheduled {self.amount} to {self.person.name} every {self.frequency}"
