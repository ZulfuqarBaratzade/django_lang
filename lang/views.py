from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.utils.translation import get_language,activate,gettext
# Create your views here.

def home(request):
    trans = translate(language='az')
    return render(request,'home.html',{'trans':trans})
def translate(language):
    cur_language = get_language()
    try:
        activate(language)
        text = gettext("Salam")
    finally:
        activate(cur_language)