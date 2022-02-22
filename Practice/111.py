# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.


print(sum(i for i in range(1000) if i % 3 == 0 or i % 5 == 0))

a = range(11)
print(type(a))
print(sum(a))

aa = []
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        aa.append(i)
print(sum(aa))


bb = []
for i in range(1000):
    if i % 3 == 0:
        bb.append(i)

    if i % 5 == 0:
        bb.append(i)

cc = set(bb)
# print(cc)
print(sum(cc))
