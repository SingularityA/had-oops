from mrjob.job import MRJob
from mrjob.protocol import TextProtocol
import re

WORD_RE = re.compile(r"\w+")

class MROftenUpperCase(MRJob):
    OUTPUT_PROTOCOL = TextProtocol

    def mapper(self, _, line):
        for word in WORD_RE.findall(line):
            yield word.lower(), word[0].isupper()
        
    def reducer(self, word, marks):
        upper_count, number_count = 0, 0
        for mark in marks:
            number_count += 1
            if mark:
                upper_count += 1
        if number_count > 10 and upper_count > number_count / 2:
            yield str(number_count), word 


if __name__ == '__main__':    
    MROftenUpperCase.run()  
