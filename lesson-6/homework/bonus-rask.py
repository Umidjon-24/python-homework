from pathlib import Path
import re
from collections import Counter
file1 = Path("python-homework/lesson-6/homework/sample.txt")

word_count = Counter()
with file1.open() as f:
    for line in f:
        words = re.findall(r"\b\w+\b", line.lower())
        word_count.update(words)

i = int(input("How many top common words you want to see: "))

print(f"Total unique words: {len(word_count)}")
print(f"Top {i} common words:")
for word, count in word_count.most_common(i):
    print(f"{word}: {count} times")
    
