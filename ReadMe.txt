Problem Statement: Calculate the top 10 rated values per month based on the comment value.

Solutions:

assumption: 
1) comments are alphabests i.e. A, B
2) calculating the frequency of each  comments per month
3) assuming data set is low and can adjust in the avilable memory
4) calculating for 12 months of a particular year

data structure: 

Review class: each instance for one comment type and have method for increment frequency and __cmp__ which is used by python heapq 
revheap: a dictionary which contains month as key (integer ranges from 0 to 11) and value contains list of review instances which are stored as a heap usig python heapq. 
alldict: a list which contains 12 dictionary for each month. each dictionary object contains comment as key and value as review instances. Maintaining it to fast lookup of review instances.

Algorithm 
1) data read from data base and stored in one variable.
2) reading each tuple from the data and calculating the month value.
3) based on the month check it is first occerance of comment or not in the alldict. Month value (integer 0 to 11) used as index of list.
4) if it is second occerance it will get the review instance and increment the frequency and heapify it.
5) else it will create a new review instance and added into alldict and into revheap

Printing output
1) after parsing all data rows it call nlargest method of heapq for each month from revheap. 


