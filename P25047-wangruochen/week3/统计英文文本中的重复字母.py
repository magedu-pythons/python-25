wenjian = "d e d f s a a a a d s a f d s f s a"
new = wenjian.split(" ")
print(new)
counter = 0
for i in new:
    if 'a' == i:
        counter += 1
print(counter)