from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def projects(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Here are some projects!")

def project(request:HttpRequest,pk:str)->HttpResponse:
    return HttpResponse(f"Single project {pk}")
