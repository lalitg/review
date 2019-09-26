""" 
    This module calculate the top 10 rated values per months based on comment values
"""
import heapq
import psycopg2
from datetime import datetime

class Review:
    """
        This class stored the comment with time and frequency of that comment on different time
    """
    def __init__(self, comment):     
        self.comment=comment
        self.count=1
    def increment(self):
        """
            This function increase the value by 1
        """
        self.count+=1
    def __cmp__(self, other):
        """
            This function used by heapify to compare the comments based on their frequency
        """
        return cmp(self.count, other.count)

revheap = {}# a dictionary of heap

for x in range(12):# 12 for number of months
    revheap[x] = list()
    heapq.heapify(revheap[x])

alldict = list()# list of dictionary for each month to store comment vs review instance
for x in range(12):
    alldict.append({})

def getData():
    """
        Reading from local postgres db
        database name : review
        user : postgres
        password : root
        table : usercomments(comments  character varying(20),  postdate  date)
    """
    conn = psycopg2.connect("dbname=review user=postgres password=root")
    cur = conn.cursor()
    cur.execute('select * from usercomments;')
    data = cur.fetchall()
    return data

data = getData()

for x in data:
    comment = x[0] 
    date_obj = x[1]
    month = date_obj.month-1
    if(comment in alldict[month].keys()):
        rev = alldict[month][comment]
        rev.increment()
        heapq.heapify(revheap[month])
    else:
        rev = Review(comment)
        heapq.heappush(revheap[month],rev)
        alldict[month][comment]=rev
for x in revheap.keys():
    print("month "+str(x+1))
    for y in heapq.nlargest(10, revheap[x]):
        print(y.comment)
