from django.shortcuts import render, HttpResponse

my_model = "I am world"
def home(request):
    return HttpResponse(my_model)