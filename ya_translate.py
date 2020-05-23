import requests


# переводим на яндекс переводчике текст, с исходного языка, на целевой язык, указываем ключ
def translate_it(text, lang_text, to_lang, apy_key , url=None):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param to_lang:
    :return:
    """
    URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    if not url:
        url = URL

    try:
        params = {
            'key': apy_key,
            'text': text,
            'lang': (lang_text + '-{}').format(to_lang),
        }

        response = requests.get(url, params=params)
        print(response.status_code)
        atr_json= response.__getattribute__('json')
        print(response)
        print(atr_json)
        json_ = response.json()
        #print(f'Перевели текст файла с {lang_text} на {to_lang}: {json_.get("text")[0][:40]}...')
        if json_.get('code') == 200:
            return json_.get('code'), ''.join(json_['text'])
        elif json_.get('code') == 501:
            return json_.get('code'), None
        elif json_.get('code') == 401:
            return json_.get('code'), None
        else:
            return json_.get('code'), None

    except Exception as e:
        print(f'Не удалось перевести текст: {e}')
        print(response.status_code)
        #print(f'Код ответа: {response.status_code}, {json_["code"]} - {json_["message"]}')


if __name__ == '__main__':
    api_key = ''
    print(translate_it('Hello', 'en', 'ru', api_key))
