from django.shortcuts import render, HttpResponse
import os
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def index(request):
    context= {
        }
    return render(request, "base.html", context)

