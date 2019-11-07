from modeltranslation.translator import translator, TranslationOptions
from .models import TextInfoBlock as TIB, LotlTeamMember, VideoLink, Tour, Musician, Album
from .models import Event, TextMaterial, News, Article

class TIBTO(TranslationOptions):
    fields = ('name', 'text',)
translator.register(TIB, TIBTO)

class LotlTeamMemberTO(TranslationOptions):
    fields = ('comment',)
translator.register(LotlTeamMember, LotlTeamMemberTO)

class VideoLinkTO(TranslationOptions):
    fields = ('title', 'description', )
translator.register(VideoLink, VideoLinkTO)

class TourTO(TranslationOptions):
    fields = ('description',)
translator.register(Tour, TourTO)

class MusicianTO(TranslationOptions):
    fields = ('name', 'role', 'info',  )
translator.register(Musician, MusicianTO)

class AlbumTO(TranslationOptions):
    fields = ('description', )
translator.register(Album, AlbumTO)

class EventTO(TranslationOptions):
    fields = ('title', 'anons', )
translator.register(Event, EventTO)
"""
class TextMaterialTO(TranslationOptions):
    fields = ('title', 'text_short', 'text_full', )
translator.register(TextMaterial, TextMaterialTO)
"""
translator.register(TextMaterial)
class NewsTO(TranslationOptions):
    fields = ('title', 'text_short', 'text_full', )
translator.register(News, NewsTO)

class ArticleTO(TranslationOptions):
    fields = ('title', 'text_short', 'text_full', )
translator.register(Article, ArticleTO)
