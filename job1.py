from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"\w+")


class MRMaxLengthWord(MRJob):

    def mapper(self, _, line):
        for word in WORD_RE.findall(line):           
            yield len(word), word
        
    def combiner(self, word_length, words):
        yield None, (word_length, ' '.join(words))
        
    def reducer(self, _, word_length_pairs):
        yield max(word_length_pairs)


if __name__ == '__main__':    
    MRMaxLengthWord.run()  
