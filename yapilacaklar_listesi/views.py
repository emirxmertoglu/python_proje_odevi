from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import yapilacaklarListesi
from .forms import yapilacaklarListesiForm, yeniYapilacaklarListesiForm

def index(request):
  liste = yapilacaklarListesi.objects.order_by('id')
  #form = yapilacaklarListesiForm()
  yeniyapilacakform = yeniYapilacaklarListesiForm()
  context = {'liste' : liste, 'form' : yeniyapilacakform}
  return render(request, 'yapilacaklar_listesi/index.html', context)

@require_POST
def yapilacakEkle(request):
  #form = yapilacaklarListesiForm(request.POST)
  yeniyapilacakform = yeniYapilacaklarListesiForm(request.POST)
  if yeniyapilacakform.is_valid():
    #yeni_yapilacak = yapilacaklarListesi(yazi=form.cleaned_data['yazi'])
    #yeni_yapilacak.save()
    yeni_yapilacak = yeniyapilacakform.save()
  return redirect('index')

def yapilacakTamamlama(request, yapilacak_id):
  yapilacak = yapilacaklarListesi.objects.get(pk=yapilacak_id)
  yapilacak.tamamlama = True
  yapilacak.save()
  return redirect('index')

def tamamlanmislariSil(request):
  yapilacaklarListesi.objects.filter(tamamlama__exact=True).delete()
  return redirect('index')

def hepsiniSil(request):
  yapilacaklarListesi.objects.all().delete()
  return redirect('index')
