from googletrans import Translator

translator = Translator()
print(translator.translate('이 문장은 예시 문장입니다.'))

#src = 번역 전 언어, dest = 번역 후 언어, text = 번역 결과, pronounciation = 번역 결과의 발음(영어 base)

print(translator.translate('안녕').text)

print(translator.translate('안녕', src='ko', dest='ja'))

print(translator.detect('안녕'))

print(translator.detect('veritas lux mea'))

# 언어만 확인
print(translator.detect('안녕').lang)