from mrjob.job import MRJob
from mrjob.protocol import TextProtocol
import re
import pymorphy2

WORD_RE = re.compile(r"[\w']+")


class MRNamesSearch(MRJob):
    OUTPUT_PROTOCOL = TextProtocol
    THRESH =  0.55
    
    morph = pymorphy2.MorphAnalyzer()
    
    def mapper(self, _, line):
        for word in WORD_RE.findall(line):
            yield word, 1
            
    def combiner(self, word, counts):
        yield None, word

    def reducer(self, _, words):
        for word in words:
            for result in self.morph.parse(word):
                if 'Name' in result.tag and result.score >= self.THRESH:
                    yield word, str(result.score)
        
        
if __name__ == '__main__':
    MRNamesSearch.run() 
