import requests

from settings import DEFAULT_LANGUAGE, DICTIONARY_API_URL


def get_word_information(language, word):
  language if language == DEFAULT_LANGUAGE else DEFAULT_LANGUAGE
  try:
    r = requests.get(f'{DICTIONARY_API_URL}/{language}/{word}')
  except requests.exceptions.ConnectionError:
    print('Connection Error: Please check your internet connection.')
  else:
    return r.json()


def aggregate_meanings(meanings):
  result = ''
  for meaning in meanings:
    part_of_speech = meaning['partOfSpeech']
    definitions = [f'- {definition["definition"]}' for definition in meaning['definitions']]
    formated_def = '\n'.join(definitions)
    result += f'[{part_of_speech.upper()}]\n{formated_def}\n\n'
  else:
    return result


def extract_information(information):
    meanings = aggregate_meanings(information['meanings'])
    result = f"""---
WORD: {information['word']}\n
{meanings}"""
    return result
