# Pfm/views.py

from django.shortcuts import render, redirect
from .models import Expense, Budget, FinancialGoal
from .forms import ExpenseForm, BudgetForm, GoalForm

def home(request):
    return render(request, 'home.html')

def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)
    return render(request, 'expense_list.html', {'expenses': expenses})

def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'add_expense.html', {'form': form})

# Similarly create views for budgets and financial goals
