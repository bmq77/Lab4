from django.shortcuts import render

tax = 15


def index(request):
  
  return render(request, 'index.html')



def taxrate(request):
  
  return render(request, 'taxrate.html', context={"taxrate":10})


def taxCalc(request, num):
  total = num + num*tax/100
  
  return render(request, 'taxCalc.html', context={"total":total, "initial":num, "tax":tax})



