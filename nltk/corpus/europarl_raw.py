# Natural Language Toolkit: Europarl Corpus Readers
#
# Copyright (C) 2001-2013 NLTK Project
# Author:  Nitin Madnani <nmadnani@umiacs.umd.edu>
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT

import re
from nltk.corpus.util import create_lazy_corpus_loader
from nltk.corpus.reader import *

# Create a new corpus reader instance for each European language
danish = create_lazy_corpus_loader(
    'europarl_raw/danish', EuroparlCorpusReader, r'ep-.*\.da', encoding='utf-8')

dutch = create_lazy_corpus_loader(
    'europarl_raw/dutch', EuroparlCorpusReader, r'ep-.*\.nl', encoding='utf-8')

english = create_lazy_corpus_loader(
    'europarl_raw/english', EuroparlCorpusReader, r'ep-.*\.en', encoding='utf-8')

finnish = create_lazy_corpus_loader(
    'europarl_raw/finnish', EuroparlCorpusReader, r'ep-.*\.fi', encoding='utf-8')

french = create_lazy_corpus_loader(
    'europarl_raw/french', EuroparlCorpusReader, r'ep-.*\.fr', encoding='utf-8')

german = create_lazy_corpus_loader(
    'europarl_raw/german', EuroparlCorpusReader, r'ep-.*\.de', encoding='utf-8')

greek = create_lazy_corpus_loader(
    'europarl_raw/greek', EuroparlCorpusReader, r'ep-.*\.el', encoding='utf-8')

italian = create_lazy_corpus_loader(
    'europarl_raw/italian', EuroparlCorpusReader, r'ep-.*\.it', encoding='utf-8')

portuguese = create_lazy_corpus_loader(
    'europarl_raw/portuguese', EuroparlCorpusReader, r'ep-.*\.pt', encoding='utf-8')

spanish = create_lazy_corpus_loader(
    'europarl_raw/spanish', EuroparlCorpusReader, r'ep-.*\.es', encoding='utf-8')

swedish = create_lazy_corpus_loader(
    'europarl_raw/swedish', EuroparlCorpusReader, r'ep-.*\.sv', encoding='utf-8')
