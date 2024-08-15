#!/usr/bin/env python
import sys

word_counts = dict()

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    count = int(count)

    if word not in word_counts:
       word_counts[word] = count
    else:
      word_counts[word] = word_counts[word] + 1

for word, count in word_counts.items():
    print('{}\t{}'.format(word, count))