#!/usr/bin/env python

import argparse
import helpers 

from settings import DEFAULT_LANGUAGE


if __name__ == '__main__':
  parser = argparse.ArgumentParser(prog='PyDict', description='A Python commandline dictionary')
  parser.add_argument('-l', '--language', default=DEFAULT_LANGUAGE, help='Language to search for.')
  parser.add_argument('word', help='Word to search for definition.')

  args = parser.parse_args()
  word_information = helpers.get_word_information(args.language, args.word)
  result = helpers.extract_information(word_information[0])
  
  print(result)