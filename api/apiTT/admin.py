from django.contrib import admin
from .models import Cidade
from .models import Ponto
from .models import Info
from .models import PontoFisico
from .models import Contato
from .models import Slide

class PontoInline(admin.TabularInline):
    model = Ponto

class CidadeAdmin(admin.ModelAdmin):
    inlines = [PontoInline]


admin.site.register(Cidade, CidadeAdmin)
admin.site.register(Info)
admin.site.register(PontoFisico)
admin.site.register(Contato)
admin.site.register(Slide)

