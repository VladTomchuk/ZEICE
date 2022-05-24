from modeltranslation.translator import translator, TranslationOptions
from .models import ZeBarTools, IceType


class ZeBarToolsTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


class IceTypeTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


translator.register(ZeBarTools, ZeBarToolsTranslationOptions)
translator.register(IceType, IceTypeTranslationOptions)
