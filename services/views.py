from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'services/index.html')

def about(request):
    return render(request, 'services/about.html')

def vision(request):
    return render(request, 'services/vision.html')

def ind_str(request):
    return render(request, 'services/industry_str.html')

def contact(request):
    return render(request, 'services/contact.html')

# schemes views
def saving(request):
    return render(request, 'services/schemes/saving.html')

def recurring(request):
    return render(request, 'services/schemes/recurring.html')

def monthly(request):
    return render(request, 'services/schemes/monthly.html')

def fixed(request):
    return render(request, 'services/schemes/fixed.html')

def daily(request):
    return render(request, 'services/schemes/daily.html')

# Loan views
def gold(request):
    return render(request, 'services/loans/gold.html')

def group(request):
    return render(request, 'services/loans/group.html')

def loanagainstdeposit(request):
    return render(request, 'services/loans/loanagainstdeposit.html')

def loanagainstgovtsec(request):
    return render(request, 'services/loans/loanagainstgovtsec.html')

def mortgage(request):
    return render(request, 'services/loans/mortgage.html')

def personal(request):
    return render(request, 'services/loans/personal.html')
