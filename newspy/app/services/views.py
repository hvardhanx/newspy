from django.shortcuts import render
from .crawler import HNCrawler

def hn_post(request):
    hn_crawler = HNCrawler()
    top_stories = hn_crawler.get_top()
    return render(request, 'hn.html', {'stories': top_stories})