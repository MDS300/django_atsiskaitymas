from django.contrib import admin
from .models import Projektas, Klientas, Darbuotojas, Darbas, Saskaita


class ProjektasAdmin(admin.ModelAdmin):
    list_display = ("pavadinimas", "klientas", "atsakingasis", "pabaigos_data")
    search_fields = ("pavadinimas", "atsakingasis")
    list_filter = ("pradzios_data", )


class KlientasAdmin(admin.ModelAdmin):
    list_display = ("vardas", "pavarde", "imone")


class DarbasAdmin(admin.ModelAdmin):
    list_display = ("pavadinimas", "pastabos")


class SaskaitaAdmin(admin.ModelAdmin):
    list_display = ("israsymo_data", "suma")


admin.site.register(Projektas, ProjektasAdmin)
admin.site.register(Klientas, KlientasAdmin)
admin.site.register(Darbuotojas)
admin.site.register(Darbas, DarbasAdmin)
admin.site.register(Saskaita, SaskaitaAdmin)
