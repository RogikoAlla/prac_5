mport random
seq = [(random.random(), bytes(random.sample(range(5),3)),
random.randrange(1000)) for i in range(10)

with open('file','bw+')as f:
       f.write(struct.pack(seq)))


