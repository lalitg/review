import heapq
from datetime import datetime

class Review:
    def __init__(self, comment, date):     
        self.comment=comment
        self.count=1
        self.date = date
    def increment(self):
        self.count+=1
    def printcount(self):
        print (self.count)
    def __cmp__(self, other):
        return cmp(self.count, other.count)
revheap = {}# a dictionary of heap
for x in range(11):
    revheap[x] = list()
    heapq.heapify(revheap[x])
f = open("review.txt","r")
data = f.readlines()
alldict = list()# list of dictionary for each month to store comment vs review instance
for x in range(11):
    alldict.append({})
for x in data:
    comment = x.split(" ")[0]
    date_obj = datetime.strptime(x.split(" ")[1].split("\n")[0], "%d-%m-%y")
    month = date_obj.month-1
    if(comment in alldict[month].keys()):
        rev = alldict[month][comment]
        rev.increment()
        heapq.heapify(revheap[month])
    else:
        rev = Review(comment, date_obj)
        heapq.heappush(revheap[month],rev)
        alldict[month][comment]=rev
for x in revheap.keys():
    print("month "+str(x+1))
    for y in heapq.nlargest(10, revheap[x]):
        print(y.comment)
