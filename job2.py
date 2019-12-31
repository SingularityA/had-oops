from mrjob.job import MRJob
from mrjob.protocol import TextProtocol
from statistics import mean
import re

WORD_RE = re.compile(r"\w+")


class MRAvgLengthWord(MRJob):
    OUTPUT_PROTOCOL = TextProtocol

    def mapper(self, _, line):
        for word in WORD_RE.findall(line):           
            yield None, len(word)
            
    def reducer(self, _, lengths):
        yield 'Avg', str(mean(lengths))


if __name__ == '__main__':    
    MRAvgLengthWord.run()  
