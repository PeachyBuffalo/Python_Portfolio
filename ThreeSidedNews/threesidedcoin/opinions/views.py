from django.shortcuts import render
from .models import Article, OpinionPoll


# Create your views here.
def home(request):
    polls = OpinionPoll.objects.all()  # Adjust query as needed
    return render(request, 'home.html', {'polls': polls})
