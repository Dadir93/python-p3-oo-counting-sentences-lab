#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        if not isinstance(value, str):
            print("The value must be a string.")
            raise ValueError("The value must be a string.")
        self.value = value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        if not self.value:
            return 0

        sentence_endings = ['.', '?', '!']
        sentence_count = 0
        previous_char = ''

        for char in self.value:
            if char in sentence_endings and previous_char not in sentence_endings:
                sentence_count += 1
            previous_char = char

        return sentence_count
