"""
What was the max amount of snow per date?
"""
from mrjob.job import MRJob
import mrjob


class Snow_days(MRJob):
    INPUT_PROTOCOL = mrjob.protocol.RawProtocol

    def mapper(self, key, line):
        all_data = line.split(",")
        yield "key",key
        if all_data[4] and float(all_data[4]) > 0:
            yield all_data[3], float(all_data[4])

    def reducer(self, date, snow):
        if str(date) != "key":
            tl,ts=0,0
            alldata=[]
            for i in snow:
                tl+=1
                ts+=i
                alldata.append(i)
            yield "avg snow on "+date, ts/tl
            yield "avg snow on "+date, sum(alldata)/len(alldata)
            yield "max snow on "+date, max(alldata)
            # yield "max", "by date"
            # yield date, max(snow)
        else:
            yield "key",list(snow)

if __name__ == "__main__":
    Snow_days.run()
