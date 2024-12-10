import json
from jinja2 import Template


class Translate:
    @staticmethod
    def get_phrase(user, code, **kwargs):
        language_prefix = user.tg_user_json_dict.get('language_code', 'ru')
        locale_file = f'locale/{language_prefix}.json'
        try:
            with open(locale_file, 'r') as f:
                locale_data = json.load(f)
        except FileNotFoundError:
            # Если файл не найден, пробуем взять файл по умолчанию (ru)
            locale_file = 'locale/ru.json'
            try:
                with open(locale_file, 'r') as f:
                    locale_data = json.load(f)
            except FileNotFoundError:
                print(f'Locale file {locale_file} not found')
                return ''

        phrase = locale_data.get(code)
        if not phrase:
            print(f'Phrase {code} not found in locale file {locale_file}')

        template = Template(phrase)
        return template.render(**kwargs)
