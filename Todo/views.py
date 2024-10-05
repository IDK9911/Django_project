from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.


# months=['january','feburary','march','april','may']
# challenges=['Gym membership','Book club','learn Swimming','Create Software','Happy birthday']

mydict={'january': 'Gym membership',
 'feburary': 'Book club',
 'march': 'learn Swimming',
 'april': 'Create Software',
 'may': 'Happy birthday'}


def index(request):
    res_op='<ul>'

    res_clo='</ul>'
    res=''
    for month in mydict.keys():
        link=reverse('mos_challenge',args=[month])
        res+='<li><a href={l}>{month}</a> </li>'.format(month=month.capitalize(),l=link)
    res=res_op+res+res_clo
    return HttpResponse(res)

def index(request):
    return render(request,"Todo/index.html",{"mydict":mydict})

def getMonthlyChallenge(request,month):
    print(mydict['january'])
    return HttpResponse('Goal is: '+mydict[month.lower()])