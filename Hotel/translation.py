from .models import RoomType
from modeltranslation.translator import TranslationOptions, register


@register(RoomType)
class HotelTranslationOptions(TranslationOptions):
    fields = ('name', 'description')