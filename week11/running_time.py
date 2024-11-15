import time

list = []
for i in range(900000):
	list.append(i)
print('...list built...')

start = time.time()
while len(list) > 0:
	list.pop(0)
end = time.time()
print(end-start)