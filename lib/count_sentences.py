#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self._value = value

    def get_value(self):
        return self._value

    def set_value(self, value):
        if not isinstance(value, str):
            print("The value must be a string.")

        else:
            self._value = value

    def is_sentence(self):
        if self._value == None:
            return False
        else:
            return self._value.endswith(".")

    value = property(get_value, set_value)

    def is_question(self):
        if self._value == None:
            return False
        else:
            return self._value.endswith("?")

    def is_exclamation(self):
        if self._value == None:
            return False
        else:
            return self._value.endswith("!")

    def count_sentences(self):
        if self._value is None:
            return 0

        normalized_text = self._value.replace('!', '.').replace('?', '.')

        sentences = normalized_text.split('.')

        return len([sentence for sentence in sentences if sentence.strip() != ""])


daniel = MyString("Daniel")

daniel.value = 'Daniel'
print(daniel.value)
