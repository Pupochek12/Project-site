from django.http import HttpResponse
from django.shortcuts import render

import matplotlib.pyplot as plt
import numpy as np
import pandas



def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')

def geography(request):
    return render(request, 'main/geograf.html')