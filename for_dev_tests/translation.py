from modeltranslation.translator import translator, TranslationOptions
from for_dev_tests.models import SimpleTranslationModel as STM

class STMTranslationOptions(TranslationOptions):
    fields = ('title', 'body_text',)

translator.register(STM, STMTranslationOptions)