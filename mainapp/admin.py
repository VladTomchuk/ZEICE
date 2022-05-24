from django.contrib import admin
from .models import *


# Register your models here.


class ClientImagesInline(admin.StackedInline):
    model = ClientImages


class ClientImagesAdmin(admin.ModelAdmin):
    pass


class IceTypeImagesInline(admin.StackedInline):
    model = IceTypeImages


class ClientsAdmin(admin.ModelAdmin):
    inlines = [ClientImagesInline]

    class Meta:
        model = Clients


class IceTypeAdmin(admin.ModelAdmin):
    inlines = [IceTypeImagesInline]
    exclude = ['title', 'description']

    class Meta:
        model = IceType


class ZeBarToolsImagesInline(admin.StackedInline):
    model = ZeBarToolsImages


class ZeBarToolsAdmin(admin.ModelAdmin):
    inlines = [ZeBarToolsImagesInline]
    exclude = ['title', 'description']

    class Meta:
        model = ZeBarTools


admin.site.register(IceType, IceTypeAdmin)
admin.site.register(ZeBarTools, ZeBarToolsAdmin)
admin.site.register(Distributor)
admin.site.register(Clients, ClientsAdmin)
