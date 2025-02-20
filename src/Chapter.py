import ebooklib

class Chapter:
    '''
    This class will hold the text that is inside each section, and it will also hold 
    '''
    def __init__(self, list_of_paragraphs: List[str]):
        self.list_of_paragraphs = list_of_paragraphs
        self._split_paragraphs()

    def _split_paragraphs(self):
        ...

    
    