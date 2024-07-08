import string
import sys


def preprocess_word(word: str):
    word = word.strip().lower()

    punctuation = set(string.punctuation)
    processed_word = ''
    for char in word:
        if char in punctuation:
            continue

        processed_word = processed_word + char

    return processed_word


def get_predefined_words(predefined_words_file: str) -> set:
    predefined_words = set()
    with open(predefined_words_file, 'r') as file:
        for word in file:
            word = preprocess_word(word)
            if word is None or len(word) == 0:
                continue

            predefined_words.add(word)

    return predefined_words


def count_words(input_file: str, predefined_words: set) -> dict:
    word_count = {word: 0 for word in predefined_words}

    with open(input_file, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = preprocess_word(word)
                if word in predefined_words:
                    word_count[word] = word_count.get(word, 0) + 1
    
    return word_count


def output_results(word_count: dict):
    sorted_words = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
    
    print("Predefined word \t Match count")
    for word, count in sorted_words:
        print(f"{word} \t {count}")


def main(predefined_words_file: str, input_file: str):
    predefined_words = get_predefined_words(predefined_words_file)

    if predefined_words is None or len(predefined_words) == 0:
        raise Exception("No predefined words found")
    
    word_count = count_words(input_file, predefined_words)
    
    output_results(word_count)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise Exception("Usage: python3 word_match.py <predefined_words_file_location> <input_file_location>")

    predefined_words_file = sys.argv[1]
    input_file = sys.argv[2]

    main(predefined_words_file, input_file)
