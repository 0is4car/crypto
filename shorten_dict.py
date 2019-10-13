import random
dictionary = []
i=0
with open('./english_words.txt') as f:
    with open('./shorten.txt', 'w') as h:
        for line in f:
            if i%200 == 1:
                h.write(line)
            i += 1


