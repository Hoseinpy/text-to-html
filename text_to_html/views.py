from django.shortcuts import render
from .forms import TextToHtmlForm


def convert_view(request):
    form = TextToHtmlForm()
    return render(request, 'text_to_html/main.html', {'form':form})