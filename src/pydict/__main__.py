import argparse

from pydict import helpers 
from pydict.settings import DEFAULT_LANGUAGE


def main():
  parser = argparse.ArgumentParser(prog='PyDict', description='A Python commandline dictionary')
  parser.add_argument('-l', '--language', default=DEFAULT_LANGUAGE, help='Language to search for.')
  parser.add_argument('word', help='Word to search for definition.')

  args = parser.parse_args()
  word_information = helpers.get_word_information(args.language, args.word)
  result = helpers.extract_information(word_information[0])
  print(result)

if __name__ == '__main__':
  main()