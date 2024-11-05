# Create your views here.
from django.shortcuts import render, redirect
from .models import Transaction, Category
from .forms import TransactionForm  # Create this form in the next step

def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'tracker/transaction_list.html', {'transactions': transactions})

def add_transaction(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    return render(request, 'tracker/add_transaction.html', {'form': form})
