#e1
#a = open('mbox-short.txt')
#print(a)

#e2
"""fhand = open('mbox-short.txt')
inp = fhand.read()
print(len( inp ))

print(inp[:20])
print(inp[:10])"""

#e3
"""
fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith('From'):
        print(line)
"""

#e4
"""
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()

    if not '@uct.ac.za' in line:
        continue
    print(line)
"""

#e5
"""fhand = open('mbox-short.txt')
print(fhand.readline())
"""

#e6
fhand = open('mbox-short.txt')
print(fhand.readline())
print(fhand.readline())
print(fhand.read())
















































