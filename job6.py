from mrjob.job import MRJob
from mrjob.protocol import TextProtocol
import re


class MROneDotAbbr(MRJob):

    OUTPUT_PROTOCOL = TextProtocol
    PATTERN_RE = re.compile(r'(?:[А-Яа-яA-za-z] )?[А-Яа-яA-Za-z]\. ?[а-яa-z]\.')
    THRESH = 0.01

    def mapper(self, _, line):
        for match in self.PATTERN_RE.findall(line):
            yield match.lower(), 1
                        
    def combiner(self, word, counts):
        yield None, (sum(counts), word)

    def reducer(self, _, pairs):
        sp = sorted(pairs)
        for counts, word in sp:
            per = counts/len(sp)
            if per > self.THRESH:
                yield word, str(per)
        

if __name__ == "__main__":
    MROneDotAbbr.run() 
