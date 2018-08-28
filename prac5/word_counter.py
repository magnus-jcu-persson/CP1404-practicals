text = input('text: ').lower()

words = text.split(' ')
words_count = {}
for word in words:
    if word not in words_count:
        words_count[word] = 1
    else:
        words_count[word] += 1

length = max(len(word) for word in words)

for word in sorted(words_count.keys()):
    print("{0:{2}s}: {1}".format(word, words_count[word], length))

