class Encode:
    def __init__(self, input_text: str, key = 3):
        self.value = input_text
        self.key = key

    def __str__(self):
        return ''.join(chr(ord(letter) - self.key) for letter in self.value)
