morse_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
              'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
              '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-',
              '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'}


def translate(string):
    """
    This method takes a string as an argument and translates it into morse code; putting spaces in between letters and
    slashes in between words. This method can handle letters and numbers plus some special characters: ,.?/-()
    :param string: this parameter is the string that is passed into the method
    :return: a string that contains the translated phrase with appropriate spaces and slashes
    """
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
