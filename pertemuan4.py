# #konsep FIFO(First In, First Out)
# #queue kayak antrian
# #enqueue menambah data ke queue
# #dequeue merngerlluarkan data dari queue
# #Front data paling depan
# #rear data paling belakang
# #isEmpty ngecek queue kosong apa engga

queue = []
#enqueue
queue.append("jeremy")
print("queue:", queue)

queue.append("rachell")
print("queue:", queue)

queue.append("pieter")
print("queue:", queue)

#dequeue
out = queue.pop(0)
print("data keluar:", out)
print("data yang tersisa:", queue)

#front
print("front:", queue[0])

#rear
print("rear:", queue[-1])

#isEmpty
print("apakah queue kosong?",len(queue) == 0)

queue = ["a","b","c"]
print("apakah queue kosong?",len(queue) == 0)
print(queue.pop())
print(queue.pop(0))
print(queue)