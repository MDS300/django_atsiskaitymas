from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Klientas(models.Model):
    vardas = models.CharField("Vardas", max_length=50)
    pavarde = models.CharField("Pavardė", max_length=50)
    imone = models.CharField("Įmonė", max_length=50)
    tel_nr = models.CharField("Telefono numeris", max_length=20)
    el_pastas = models.CharField("El. paštas", max_length=50)

    def __str__(self):
        return f"{self.vardas} {self.pavarde}, {self.imone}, {self.tel_nr}"

    class Meta:
        verbose_name = 'Klientas'
        verbose_name_plural = 'Klientai'


class Darbuotojas(models.Model):
    vardas = models.CharField("Vardas", max_length=50)
    pavarde = models.CharField("Pavardė", max_length=50)
    pareigos = models.CharField("Pareigos", max_length=50)

    def __str__(self):
        return f"{self.vardas} {self.pavarde} - {self.pareigos}"

    class Meta:
        verbose_name = 'Darbuotojas'
        verbose_name_plural = 'Darbuotojai'


class Darbas(models.Model):
    pavadinimas = models.CharField("Pavadinimas", max_length=50)
    pastabos = models.TextField("Pastabos", max_length=100)

    def __str__(self):
        return f"{self.pavadinimas}, {self.pastabos}"

    class Meta:
        verbose_name = 'Darbas'
        verbose_name_plural = 'Darbai'


class Saskaita(models.Model):
    israsymo_data = models.DateField("Išrašymo data", auto_now_add=True, blank=True)
    suma = models.FloatField("Suma", max_length=10)

    def __str__(self):
        return f"{self.israsymo_data} {self.suma}"

    class Meta:
        verbose_name = 'Sąskaita'
        verbose_name_plural = 'Sąskaitos'


class Projektas(models.Model):
    pavadinimas = models.CharField("Pavadinimas", max_length=50)
    pradzios_data = models.DateField("Pradžios data", max_length=20)
    pabaigos_data = models.DateField("Pabaigos data", max_length=20)
    klientas = models.ForeignKey(Klientas, on_delete=models.SET_NULL, null=True)
    atsakingasis = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    darbuotojai = models.ManyToManyField(Darbuotojas)
    darbai = models.ManyToManyField(Darbas)
    saskaitos = models.ForeignKey(Saskaita, on_delete=models.SET_NULL, null=True)
    aprasymas = HTMLField("Tekstas")
    nuotrauka = models.ImageField("Nuotrauka", upload_to='nuotraukos', null=True)

    def __str__(self):
        return f"{self.pavadinimas} {self.klientas} {self.atsakingasis} {self.pabaigos_data}"

    class Meta:
        verbose_name = 'Projektas'
        verbose_name_plural = 'Projektai'
        ordering = ['pavadinimas']
