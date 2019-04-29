from django.db import models

class yapilacaklarListesi(models.Model):
  yazi = models.CharField(max_length=40)
  tamamlama = models.BooleanField(default=False)

  def __str__(self):
    return self.yazi
