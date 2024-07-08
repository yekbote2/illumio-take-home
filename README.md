# illumio-take-home

### Match words

A python program that reads a file and finds matches against a predefined set of words.

### How to run

Requirements:
- A working python environment is required to execute the program

Usage:
- python word_match.py <predefined_words_file_location> <input_file_location>

Program accepts both files as command line arguments

### Tests

Below scenarios have been tested:
- Predefined words file not provided or found
- Input file not provided or found
- Empty words/Numbers in the predefined words file
- 20MB input file
- 10k entries in predefined words file
- 256 word length

### Assumptions/Working

- Empty words are filtered out
- Each word is preprocessed. It is converted to lowercase, all whitespaces and punctuations are removed (Example: Large-Scale => largescale)
- Numbers are valid words (Example: 1)
- Numbers found as part of words are valid (Example: person1)
- Output is sorted in descending order of count and the processed word is printed
PS: if the original word is to be printed, a mapping between the processed word and the original word can be maintained
- Output also contains words with 0 matches
- Input file is not malformed
- Predefined words file is not malformed
- Python script is provided. Executable can be created if needed via pyinstaller. 

### Complexity

n = number of predefined words
m = number of words in the input file

Space: O(n) [store predefined words]
Time: O(n + m) + O(nlogn) => O(nlogn) [time taken to sort the words in descending order]

### Improvements
- If only top X words are needed, a min heap can be used to improve complexity to O(n + m)
- Performance can be drastically improved if Map/Reduce is used
