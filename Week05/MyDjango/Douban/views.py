from django.shortcuts import render

# Create your views here.
from .models import Douban

def moive_short(request):
    shorts = Douban.objects.all()
    # 星级筛选
    queryset = Douban.objects.values('star','comment')
    condtions = {'star__gt': 3}
    star_plus = queryset.filter(**condtions)



    # return render(request, 'douban.html', locals())
    return render(request, 'index.html', locals())