from googletrans import Translator

translator = Translator()

#using original LANGUGES is not convenient
LANGUAGES_TRANSLATED = {
    'en': {0: 'english', 1: 'английский', 2: 'inglés'},
    'ru': {0: 'russian', 1: 'русский', 2: 'ruso'},
    'es': {0: 'spanish', 1: 'испанский', 2: 'español'},
    'fr': {0: 'french', 1: 'французский', 2: 'francés'},
    'de': {0: 'german', 1: 'немецкий', 2: 'alemán'},
    'zh-cn': {0: 'chinese (simplified)', 1: 'китайский (упрощенный)', 2: 'chino (simplificado)'},
    'ja': {0: 'japanese', 1: 'японский', 2: 'japonés'},
    'it': {0: 'italian', 1: 'итальянский', 2: 'italiano'},
    'pt': {0: 'portuguese', 1: 'португальский', 2: 'portugués'},
    'uk': {0: 'ukrainian', 1: 'украинский', 2: 'ucraniano'},
    'ar': {0: 'arabic', 1: 'арабский', 2: 'árabe'},
    'hi': {0: 'hindi', 1: 'хинди', 2: 'hindi'},
    'ko': {0: 'korean', 1: 'корейский', 2: 'coreano'},
    'pl': {0: 'polish', 1: 'польский', 2: 'polaco'}
}