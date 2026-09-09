#push

#pop
#pop()

#peek(melihat data terakhir atau paling atas)

#isEmpty(mengecek apakah stack kosong true atau tidak false)

tumpukan = [1, 2, 3]
print("data awal:", tumpukan)

#push
tumpukan.append(4)
print("Data setelah push:", tumpukan)

#pop
out = tumpukan.pop()
print("data setelah pop:", out)
print("data sekarang:", tumpukan)

#peek
print("data paling atas:", tumpukan[-1])

#isEmpty
tumpukan = []
print("data isEmpty:", len(tumpukan)==0)

stack = []

stack.append("A")
stack.append("B")
stack.append("C")


print(stack.pop())
stack.append("D")
print(stack[-1])
print(stack)