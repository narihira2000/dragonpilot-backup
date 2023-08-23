import gettext
from common.params import Params

locale_dir = "/data/openpilot/selfdrive/assets/locales"
# supported_language = ["en-US", "zh-TW", "zh-CN", "ja-JP", "ko-KR"]
supported_languages = {
  "main_zh-CHT": "zh-TW",
  "main_zh-CHS": "zh-CN",
  "main_ko": "ko-KR",
}

def events():
  locale = Params().get("LanguageSetting", encoding='utf8')
  if locale is not None:
    locale = supported_languages[locale.strip()]
  else:
    locale = "en-US"
  i18n = gettext.translation("events", localedir=locale_dir, fallback=True, languages=[locale])
  i18n.install()
  return i18n.gettext
