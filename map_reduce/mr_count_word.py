from mrjob.job import MRJob
import time

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        yield "chars", len(line)
        yield "words", len(line.split())
        yield "lines", 1

    def reducer(selfs, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    # run: python mr_count_word.py -r 'method' 'location_input_file or files'
    # e.g. python mr_count_word.py -r inline input1.txt input_2.txt (use a single Python process; just for testing)
    # e.g. use -r hadoop to run in Hadoop cluster:  python my_job.py -r hadoop hdfs://my_home/input.txt
    # e.g. use -r to run in EMR: python my_job.py -r emr s3://my-inputs/input.txt
    st = time.time()
    MRWordFrequencyCount.run()
    end = time.time()
   # print (end - st)