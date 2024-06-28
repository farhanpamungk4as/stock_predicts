from django.shortcuts import render, redirect, get_object_or_404, reverse


def index(request):
    return render(request, 'home.html')