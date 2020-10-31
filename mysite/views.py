from django.shortcuts import render
# Cody when request from Browser ....
from django.http import HttpResponse
import random

def index(request):
    lucky_no = random.randint(1, 42)
    # return HttpResponse("<h1>Hello</h1>")   
    # return HttpResponse("<h3> Your Lucky # is {}</h3>".format(lucky_no))
    numbers = list()
    for i in range(6):
        numbers.append(random.randint(1, 42))
    return render (request, "index.html", locals())
