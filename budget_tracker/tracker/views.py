from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import SignUpForm, TransactionForm
from .models import Transaction, Category

# View to display the list of transactions for the logged-in user
def transaction_list(request):
    if request.user.is_authenticated:
        transactions = Transaction.objects.filter(user=request.user)  # Filter transactions by user
    else:
        transactions = Transaction.objects.none()  # No transactions if the user is not authenticated
    
    return render(request, 'tracker/transaction_list.html', {'transactions': transactions})

# View to add a new transaction (associated with the logged-in user)
def add_transaction(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user  # Assign the logged-in user to the transaction
            transaction.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    return render(request, 'tracker/add_transaction.html', {'form': form})

# View for user registration (sign up)
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('transaction_list')  # Redirect to main page after signup
        else:
            messages.error(request, "Registration failed. Please check your details.")
    else:
        form = SignUpForm()
    return render(request, 'tracker/signup.html', {'form': form})

# View for user login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect('transaction_list')  # Redirect to main page after login
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'tracker/login.html', {'form': form})

# View to log out the user
def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('login')  # Redirect to login page after logout
