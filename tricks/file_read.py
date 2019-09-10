#bad way
f = open('/home/soundaryagajjam/a.txt')
text = f.read()
for line in text.split('\n'):
    print(line)
f.close()

#good way
f = open('/home/soundaryagajjam/a.txt')
for line in f:
    print(line)
f.close()

#better way
with open('/home/soundaryagajjam/a.txt') as f:
    for line in f:
        print(line)