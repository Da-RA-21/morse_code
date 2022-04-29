morse_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
              'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
              '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-',
              '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'}


def translate(string):
    sentence_list = []
    for char in string:
        if char.isalpha():
            char = char.upper()
            code = morse_dict[char]
            sentence_list.append(code)
        elif char.isdigit():
            code = morse_dict[char]
            sentence_list.append(code)
        else:
            try:
                code = morse_dict[char]
                sentence_list.append(code)
            except KeyError:
                sentence_list.append('error')

    sentence = ' '.join(sentence_list)
    return sentence
