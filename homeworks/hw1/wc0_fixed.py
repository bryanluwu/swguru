#!/usr/bin/env python3 -B

# A03 Created a config dict to hold constants as to not hardcode them
CONFIG = {
    "STOPWORDS": {
        "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for",
        "of", "is", "was", "are", "were", "be", "been", "with"
    },
    "TOP_N": 10,
    "PUNCTUATION": '.,!?;:"()[]'
}

# A02 Added file opening to its own function
def open_file(file):
  text = ""
  with open(file) as f:
    for line in f: # A04 read line by line rather than all at once
      text += line
  return text

# A02 A04 Print header in its own function
def print_header(file):
  print(f"\n{'='*50}")
  print(f"WORD FREQUENCY ANALYSIS - {file}")
  print(f"{'='*50}\n")
  
# A02 A04 Clean the input of any unwanted characters in its own function
def clean(text):
    result = []
    words = text.lower().split()
    for word in words:
        word = word.strip(CONFIG["PUNCTUATION"])
        if word:
          result.append(word)
    return result

# A02 Count the frequencies in its own function
def count(words, STOPWORDS):
  counts = {}
  for word in words:
    if word and word not in STOPWORDS:
      counts[word] = counts.get(word, 0) + 1
  return counts

# A02 Sorting done in its own function
def sort_counts(counts):
  return sorted(counts.items(), key=lambda x: x[1], reverse=True)

# A01 A02 Separate the formatting of the output from the code 
def format_output(word, count, rank):
  bar = "*" * count
  return f"{rank:2}. {word:15} {count:3} {bar}"

# A01 A02 Separate computation from prints
def sum_counts(counts):
  return sum(counts.values())

# A01 A02 Separate unique word count from prints
def unique_word_count(counts):
  return len(counts)

# A02 Printing results in its own function
def print_results(counts, sorted_words, TOP_N):
  print(f"Total words (after removing stopwords): {sum_counts(counts)}") # A01 summation function call to separate computation
  print(f"Unique words: {unique_word_count(counts)}\n") # A01 unique word count function call to separate computation
  print(f"Top {TOP_N} most frequent words:\n") # A03 top_n used as a constant
  for i, (word, count) in enumerate(sorted_words[:TOP_N], 1):
    print(format_output(word, count, i)) # A01 print the formatted output using a function call

# A04 Main function to structure the flow
def count_words(file="essay.txt"):
  text = open_file(file)
  print_header(file)
  words = clean(text)
  counts = count(words, CONFIG["STOPWORDS"])
  sorted_words = sort_counts(counts)
  print_results(counts, sorted_words, CONFIG["TOP_N"])
  print() # added to match the original output format

# A04 Added main guard
if __name__ == "__main__":
  count_words("essay.txt")