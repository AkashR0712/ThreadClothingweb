from django.shortcuts import render
from .models import MenOversizedTshirt
# Create your views here.
def home(request): 
    return render(request,"homepage.html",{}) 


#when we click oversized t-shirt on homepage
def oversizedfilter(request):
    ob1=MenOversizedTshirt.objects.all()
    print(len(ob1))
    return render(request,"filter.html",{'ob1':ob1})