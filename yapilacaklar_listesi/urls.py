from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ekle', views.yapilacakEkle, name='ekle'),
    path('tamamlama/<yapilacak_id>', views.yapilacakTamamlama, name='tamamlama'),
    path('tamamlanmislarisil', views.tamamlanmislariSil, name='tamamlanmislarisil'),
    path('hepsinisil', views.hepsiniSil, name='hepsinisil')
]