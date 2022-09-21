from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# TODO: Create your views here.
def show_mywatchlist(request):
    data_barang_mywatchlist = MyWatchList.objects.all()
    context = {
        'list_movies': data_barang_mywatchlist,
        'nama': 'Hayfa Najma', 
        'npm' : '2106653754',
        'text': show_message()
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_message():
    watched = MyWatchList.objects.filter(watched=True).count()
    not_watched = MyWatchList.objects.filter(watched = False).count()
    if(watched >= not_watched):
        return("Selamat, kamu sudah banyak menonton!")
    else:
        return("Wah, kamu masih sedikit menonton!")

