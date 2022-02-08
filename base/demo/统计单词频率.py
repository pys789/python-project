line = 'New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.'
freq = {}
for word in line.split():
    freq[word] = freq.get(word, 0) + 1
words = sorted(freq.keys())

for w in words:
    print('%s:%d' % (w, freq[w]))
