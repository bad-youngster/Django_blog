from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    # string = u'this is my news Djanog'
    # return render(request,'home.html',{'string': string})
    # TutorialList = ["HTML","v","CSS", "jQuery", "Python", "Django"]
    # return render(request,'home.html',{'TutorialList' : TutorialList})

    List = map(str,range(100))
    return render(request,'home.html',{'List' : List})