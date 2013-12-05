# Natural Language Toolkit: Corpus Readers
#
# Copyright (C) 2001-2013 NLTK Project
# Author: Edward Loper <edloper@gmail.com>
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT

# [xx] this docstring isnt' up-to-date!
"""
NLTK corpus readers.  The modules in this package provide functions
that can be used to read corpus files in a variety of formats.  These
functions can be used to read both the corpus files that are
distributed in the NLTK corpus package, and corpus files that are part
of external corpora.

Available Corpora
=================

Please see http://nltk.googlecode.com/svn/trunk/nltk_data/index.xml
for a complete list.  Install corpora using nltk.download().

Corpus Reader Functions
=======================
Each corpus module defines one or more "corpus reader functions",
which can be used to read documents from that corpus.  These functions
take an argument, ``item``, which is used to indicate which document
should be read from the corpus:

- If ``item`` is one of the unique identifiers listed in the corpus
  module's ``items`` variable, then the corresponding document will
  be loaded from the NLTK corpus package.
- If ``item`` is a filename, then that file will be read.

Additionally, corpus reader functions can be given lists of item
names; in which case, they will return a concatenation of the
corresponding documents.

Corpus reader functions are named based on the type of information
they return.  Some common examples, and their return types, are:

- words(): list of str
- sents(): list of (list of str)
- paras(): list of (list of (list of str))
- tagged_words(): list of (str,str) tuple
- tagged_sents(): list of (list of (str,str))
- tagged_paras(): list of (list of (list of (str,str)))
- chunked_sents(): list of (Tree w/ (str,str) leaves)
- parsed_sents(): list of (Tree with str leaves)
- parsed_paras(): list of (list of (Tree with str leaves))
- xml(): A single xml ElementTree
- raw(): unprocessed corpus contents

For example, to read a list of the words in the Brown Corpus, use
``nltk.corpus.brown.words()``:

    >>> from nltk.corpus import brown
    >>> print(", ".join(brown.words()))
    The, Fulton, County, Grand, Jury, said, ...

"""

import re

from nltk.tokenize import RegexpTokenizer
from nltk.corpus.util import create_lazy_corpus_loader
from nltk.corpus.reader import *

abc = create_lazy_corpus_loader(
    'abc', PlaintextCorpusReader, r'(?!\.).*\.txt', encoding=[
            ('science', 'latin_1'),
            ('rural', 'utf8')])
alpino = create_lazy_corpus_loader(
    'alpino', AlpinoCorpusReader, tagset='alpino')
brown = create_lazy_corpus_loader(
    'brown', CategorizedTaggedCorpusReader, r'c[a-z]\d\d',
    cat_file='cats.txt', tagset='brown', encoding="ascii")
cess_cat = create_lazy_corpus_loader(
    'cess_cat', BracketParseCorpusReader, r'(?!\.).*\.tbf',
    tagset='unknown', encoding='ISO-8859-2')
cess_esp = create_lazy_corpus_loader(
    'cess_esp', BracketParseCorpusReader, r'(?!\.).*\.tbf',
    tagset='unknown', encoding='ISO-8859-2')
cmudict = create_lazy_corpus_loader(
    'cmudict', CMUDictCorpusReader, ['cmudict'])
comtrans = create_lazy_corpus_loader(
    'comtrans', AlignedCorpusReader, r'(?!\.).*\.txt')
conll2000 = create_lazy_corpus_loader(
    'conll2000', ConllChunkCorpusReader,
    ['train.txt', 'test.txt'], ('NP','VP','PP'),
    tagset='wsj', encoding='ascii')
conll2002 = create_lazy_corpus_loader(
    'conll2002', ConllChunkCorpusReader, '.*\.(test|train).*',
    ('LOC', 'PER', 'ORG', 'MISC'), encoding='utf-8')
conll2007 = create_lazy_corpus_loader(
    'conll2007', DependencyCorpusReader, '.*\.(test|train).*', encoding=[
        ('eus', 'ISO-8859-2'),
        ('esp', 'utf8')])
dependency_treebank = create_lazy_corpus_loader(
    'dependency_treebank', DependencyCorpusReader, '.*\.dp',
    encoding='ascii')
floresta = create_lazy_corpus_loader(
    'floresta', BracketParseCorpusReader, r'(?!\.).*\.ptb', '#',
    tagset='unknown', encoding='ISO-8859-15')
framenet = create_lazy_corpus_loader(
    'framenet_v15', FramenetCorpusReader, ['frRelation.xml','frameIndex.xml','fulltextIndex.xml','luIndex.xml','semTypes.xml'])
gazetteers = create_lazy_corpus_loader(
    'gazetteers', WordListCorpusReader, r'(?!LICENSE|\.).*\.txt',
    encoding='ISO-8859-2')
genesis = create_lazy_corpus_loader(
    'genesis', PlaintextCorpusReader, r'(?!\.).*\.txt', encoding=[
        ('finnish|french|german', 'latin_1'),
        ('swedish', 'cp865'),
        ('.*', 'utf_8')])
gutenberg = create_lazy_corpus_loader(
    'gutenberg', PlaintextCorpusReader, r'(?!\.).*\.txt', encoding='latin1')
# corpus not available with NLTK; these lines caused help(nltk.corpus) to break
#hebrew_treebank = create_lazy_corpus_loader(
#    'hebrew_treebank', BracketParseCorpusReader, r'.*\.txt')
ieer = create_lazy_corpus_loader(
    'ieer', IEERCorpusReader, r'(?!README|\.).*')
inaugural = create_lazy_corpus_loader(
    'inaugural', PlaintextCorpusReader, r'(?!\.).*\.txt', encoding='latin1')
# [XX] This should probably just use TaggedCorpusReader:
indian = create_lazy_corpus_loader(
    'indian', IndianCorpusReader, r'(?!\.).*\.pos',
    tagset='unknown', encoding='utf8')
ipipan = create_lazy_corpus_loader(
    'ipipan', IPIPANCorpusReader, r'(?!\.).*morph\.xml')
jeita = create_lazy_corpus_loader(
    'jeita', ChasenCorpusReader, r'.*\.chasen', encoding='utf-8')
knbc = create_lazy_corpus_loader(
    'knbc/corpus1', KNBCorpusReader, r'.*/KN.*', encoding='euc-jp')
lin_thesaurus = create_lazy_corpus_loader(
    'lin_thesaurus', LinThesaurusCorpusReader, r'.*\.lsp')
mac_morpho = create_lazy_corpus_loader(
    'mac_morpho', MacMorphoCorpusReader, r'(?!\.).*\.txt',
    tagset='unknown', encoding='latin-1')
machado = create_lazy_corpus_loader(
    'machado', PortugueseCategorizedPlaintextCorpusReader,
    r'(?!\.).*\.txt', cat_pattern=r'([a-z]*)/.*', encoding='latin-1')
movie_reviews = create_lazy_corpus_loader(
    'movie_reviews', CategorizedPlaintextCorpusReader,
    r'(?!\.).*\.txt', cat_pattern=r'(neg|pos)/.*',
    encoding='ascii')
names = create_lazy_corpus_loader(
    'names', WordListCorpusReader, r'(?!\.).*\.txt', encoding='ascii')
nps_chat = create_lazy_corpus_loader(
    'nps_chat', NPSChatCorpusReader, r'(?!README|\.).*\.xml', tagset='wsj')
pl196x = create_lazy_corpus_loader(
    'pl196x', Pl196xCorpusReader, r'[a-z]-.*\.xml',
    cat_file='cats.txt', textid_file='textids.txt', encoding='utf8')
ppattach = create_lazy_corpus_loader(
    'ppattach', PPAttachmentCorpusReader, ['training', 'test', 'devset'])
ptb = create_lazy_corpus_loader( # Penn Treebank v3: WSJ and Brown portions
    'ptb', CategorizedBracketParseCorpusReader, r'(WSJ/\d\d/WSJ_\d\d|BROWN/C[A-Z]/C[A-Z])\d\d.MRG',
    cat_file='allcats.txt', tagset='wsj')
qc = create_lazy_corpus_loader(
    'qc', StringCategoryCorpusReader, ['train.txt', 'test.txt'], encoding='ISO-8859-2')
reuters = create_lazy_corpus_loader(
    'reuters', CategorizedPlaintextCorpusReader, '(training|test).*',
    cat_file='cats.txt', encoding='ISO-8859-2')
rte = create_lazy_corpus_loader(
    'rte', RTECorpusReader, r'(?!\.).*\.xml')
senseval = create_lazy_corpus_loader(
    'senseval', SensevalCorpusReader, r'(?!\.).*\.pos')
shakespeare = create_lazy_corpus_loader(
    'shakespeare', XMLCorpusReader, r'(?!\.).*\.xml')
sinica_treebank = create_lazy_corpus_loader(
    'sinica_treebank', SinicaTreebankCorpusReader, ['parsed'],
    tagset='unknown', encoding='utf-8')
state_union = create_lazy_corpus_loader(
    'state_union', PlaintextCorpusReader, r'(?!\.).*\.txt',
    encoding='ISO-8859-2')
stopwords = create_lazy_corpus_loader(
    'stopwords', WordListCorpusReader, r'(?!README|\.).*', encoding='utf8')
swadesh = create_lazy_corpus_loader(
    'swadesh', SwadeshCorpusReader, r'(?!README|\.).*', encoding='utf8')
switchboard = create_lazy_corpus_loader(
    'switchboard', SwitchboardCorpusReader, tagset='wsj')
timit = create_lazy_corpus_loader(
    'timit', TimitCorpusReader)
timit_tagged = create_lazy_corpus_loader(
    'timit', TimitTaggedCorpusReader, '.+\.tags',
    tagset='wsj', encoding='ascii')
toolbox = create_lazy_corpus_loader(
    'toolbox', ToolboxCorpusReader, r'(?!.*(README|\.)).*\.(dic|txt)')
treebank = create_lazy_corpus_loader(
    'treebank/combined', BracketParseCorpusReader, r'wsj_.*\.mrg',
    tagset='wsj', encoding='ascii')
treebank_chunk = create_lazy_corpus_loader(
    'treebank/tagged', ChunkedCorpusReader, r'wsj_.*\.pos',
    sent_tokenizer=RegexpTokenizer(r'(?<=/\.)\s*(?![^\[]*\])', gaps=True),
    para_block_reader=tagged_treebank_para_block_reader, encoding='ascii')
treebank_raw = create_lazy_corpus_loader(
    'treebank/raw', PlaintextCorpusReader, r'wsj_.*', encoding='ISO-8859-2')
udhr = create_lazy_corpus_loader(
    'udhr', UdhrCorpusReader)
udhr2 = create_lazy_corpus_loader(
    'udhr2', PlaintextCorpusReader, r'.*\.txt', encoding='utf8')
verbnet = create_lazy_corpus_loader(
    'verbnet', VerbnetCorpusReader, r'(?!\.).*\.xml')
webtext = create_lazy_corpus_loader(
    'webtext', PlaintextCorpusReader, r'(?!README|\.).*\.txt', encoding='ISO-8859-2')
wordnet = create_lazy_corpus_loader(
    'wordnet', WordNetCorpusReader)
wordnet_ic = create_lazy_corpus_loader(
    'wordnet_ic', WordNetICCorpusReader, '.*\.dat')
words = create_lazy_corpus_loader(
    'words', WordListCorpusReader, r'(?!README|\.).*', encoding='ascii')
ycoe = create_lazy_corpus_loader(
    'ycoe', YCOECorpusReader)
# defined after treebank
propbank = create_lazy_corpus_loader(
    'propbank', PropbankCorpusReader,
    'prop.txt', 'frames/.*\.xml', 'verbs.txt',
    lambda filename: re.sub(r'^wsj/\d\d/', '', filename),
    treebank) # Must be defined *after* treebank corpus.
nombank = create_lazy_corpus_loader(
    'nombank.1.0', NombankCorpusReader,
    'nombank.1.0', 'frames/.*\.xml', 'nombank.1.0.words',
    lambda filename: re.sub(r'^wsj/\d\d/', '', filename),
    treebank) # Must be defined *after* treebank corpus.
propbank_ptb = create_lazy_corpus_loader(
    'propbank', PropbankCorpusReader,
    'prop.txt', 'frames/.*\.xml', 'verbs.txt',
    lambda filename: filename.upper(),
    ptb) # Must be defined *after* ptb corpus.
nombank_ptb = create_lazy_corpus_loader(
    'nombank.1.0', NombankCorpusReader,
    'nombank.1.0', 'frames/.*\.xml', 'nombank.1.0.words',
    lambda filename: filename.upper(),
    ptb) # Must be defined *after* ptb corpus.
semcor = create_lazy_corpus_loader(
    'semcor', SemcorCorpusReader, r'brown./tagfiles/br-.*\.xml',
    wordnet) # Must be defined *after* wordnet corpus.

def demo():
    # This is out-of-date:
    abc.demo()
    brown.demo()
#    chat80.demo()
    cmudict.demo()
    conll2000.demo()
    conll2002.demo()
    genesis.demo()
    gutenberg.demo()
    ieer.demo()
    inaugural.demo()
    indian.demo()
    names.demo()
    ppattach.demo()
    senseval.demo()
    shakespeare.demo()
    sinica_treebank.demo()
    state_union.demo()
    stopwords.demo()
    timit.demo()
    toolbox.demo()
    treebank.demo()
    udhr.demo()
    webtext.demo()
    words.demo()
#    ycoe.demo()

if __name__ == '__main__':
    #demo()
    pass

# ** this is for nose **
# unload all corpus after tests
def teardown_module(module=None):
    import nltk.corpus
    for name in dir(nltk.corpus):
        obj = getattr(nltk.corpus, name, None)
        if isinstance(obj, CorpusReader) and hasattr(obj, '_unload'):
            obj._unload()
