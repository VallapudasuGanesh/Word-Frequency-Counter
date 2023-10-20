def count_unique_words(file_path):
    word_freq = {}

    with open(file_path, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                word = word.strip('.,!?()[]{}"\'').lower()
                word_freq[word] = word_freq.get(word, 0) + 1

    return word_freq

def main():
    file_path = 'sample.txt'  # Replace with the actual file path

    word_freq = count_unique_words(file_path)

    for word, freq in word_freq.items():
        print(f'{word}: {freq}')

if __name__ == '__main__':
    main()
