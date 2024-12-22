def count_words(string):
  return len(string.split())

def count_characters(string):
  char_count = {}
  for char in string.lower():
    if char.isalpha():
      if char in char_count:
        char_count[char] += 1
      else:
        char_count[char] = 1
  return char_count

def main():
  file_name = "books/frankenstein.txt"
  with open(file_name) as f:
    file_contents = f.read()
    word_count = count_words(file_contents)
    char_count = count_characters(file_contents)

    print(f"--- Begin report of {file_name} ---")
    print(f"{word_count} words found in the document\n")

    for char, count in sorted(char_count.items()):
      print(f"The {char} character was found {char_count[char]} times")
    
    print("--- End report ---")


main()