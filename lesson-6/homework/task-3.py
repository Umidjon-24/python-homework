from pathlib import Path
import re
file1 = Path("python-homework/lesson-6/homework/sample.txt")
try:
    with file1.open() as f:
        pass
except FileNotFoundError:
    with file1.open('w') as f:
        input = input("Enter a paragraph:\n")
        f.write(input)
        pass
    print("New file has created")

with open(file1, 'r') as f:
    lines = f.read()
words = re.findall(r"\b\w+\b", lines)
words = [word.lower() for word in words]
unique_words = list(set(words))


word_count = dict()
file2 = Path("python-homework/lesson-6/homework/word_count_report.txt")
with open(file2, 'a') as f:
    f.write(f"Total words: {len(unique_words)}\n")
    f.write("Top 5 common words:\n")
    print(f"Total words: {len(unique_words)}")
    print("Top 5 common words:")
    for x in range(len(unique_words)):
        counter = 0
        for y in range(len(words)):
            if unique_words[x] == words[y]:
                counter += 1
        word_count[unique_words[x]] = counter
    sorted_Word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))
    
    q = 0
    for key in sorted_Word_count.keys():
        f.write(f"{key}: {sorted_Word_count[key]}\n")
        print(f"{(key)}: {sorted_Word_count[key]} times")
        q += 1
        if q == 5:
            break
    
