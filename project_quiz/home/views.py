from django.shortcuts import render
from question.models import Quest

# Create your views here.
def home(request):
    quest = {
        'quest': Quest.objects.all()
    }
    print(Quest.objects.all())
    return render(request,'home_page/index.html', quest)

