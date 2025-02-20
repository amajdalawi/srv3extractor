import ebooklib
from bs4 import BeautifulSoup
from pathlib import Path


class EpubFile:
    '''
    This class will hold information regarding the epub file to be aligned, its gonna hold
    stuff like: metadata about the novel if it exists, a sorted list of chapters (that will be fed to a spacy sentenizer)
    
    '''