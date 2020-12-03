class Decode:
    def __init__(self, input_text: str, method, key=3):
        self.value = input_text
        self.key = key
        self.method = method

    def __str__(self):
        if self.method == 1:
            return ''.join(chr(ord(letter) + self.key) for letter in self.value)
        elif self.method == 2:
            return ''.join(chr(int(ord(letter) / self.key)) for letter in self.value)
