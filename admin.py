from django.contrib import admin

from .models import Centre , Produit , Client , Fournisseur , Employe ,Matiere_premiere ,Achat,Reglement,Vente,paiementcredit,Transfert,Stock

admin.site.register(Centre)
admin.site.register(Produit)
admin.site.register(Client)
admin.site.register(Fournisseur)
admin.site.register(Employe)
admin.site.register(Matiere_premiere)
admin.site.register(Achat)
admin.site.register(Reglement)
admin.site.register(Vente)
admin.site.register(paiementcredit)
admin.site.register(Transfert)
admin.site.register(Stock)
