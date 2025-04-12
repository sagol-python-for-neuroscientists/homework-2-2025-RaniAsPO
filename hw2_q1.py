MORSE_CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
              'D': '-..',    'E': '.',      'F': '..-.',
              'G': '--.',    'H': '....',   'I': '..',
              'J': '.---',   'K': '-.-',    'L': '.-..',
              'M': '--',     'N': '-.',     'O': '---',
              'P': '.--.',   'Q': '--.-',   'R': '.-.',
              'S': '...',    'T': '-',      'U': '..-',
              'V': '...-',   'W': '.--',    'X': '-..-',
              'Y': '-.--',   'Z': '--..',

              '0': '-----',  '1': '.----',  '2': '..---',
              '3': '...--',  '4': '....-',  '5': '.....',
              '6': '-....',  '7': '--...',  '8': '---..',
              '9': '----.',

              '.': '.-.-.-', ',': '--..--', ':': '---...',
              "'": '.----.', '-': '-....-',
              }


def english_to_morse(
    input_file: str = "lorem.txt",
    output_file: str = "lorem_morse.txt"
):
    """Convert an input text file to an output Morse code file.

    Notes
    -----
    This function assumes the existence of a MORSE_CODE dictionary, containing a
    mapping between English letters and their corresponding Morse code.

    Parameters
    ----------
    input_file : str
        Path to file containing the text file to convert.
    output_file : str
        Name of output file containing the translated Morse code. Please don't change
        it since it's also hard-coded in the tests file.
    """
    with open(input_file, 'r') as infile:
        text = infile.read().upper()  # Convert the text to uppercase

    # Replace each word with its Morse code equivalent
    #words = text.text()  # Split text into words
    #morse_words = [''.join(MORSE_CODE.get(char, '') for char in word) for word in words]  # Join Morse letters tightly without spaces

    # Write each Morse word into the output file on a new line
    #with open(output_file, 'w') as outfile:
    #   outfile.write('\n'.join(morse_words))  # Write each Morse word on a new line    
    #return f"Morse code successfully written to {output_file}"

    # Process each line separately and join words with spaces in Morse
     # Process each line separately
    lines = text.splitlines()  # Split text into lines
    morse_lines = [
        '\n'.join(''.join(MORSE_CODE.get(char, '') for char in word) for word in line.split())
        for line in lines
    ]


    # Write the Morse code lines back to the file with line breaks preserved
    with open(output_file, 'w') as outfile:
        outfile.write('\n'.join(morse_lines))  # Write each Morse line on a new line

    return f"Morse code successfully written to {output_file}"



if __name__ == '__main__':
    # Question 1
    param1 = "/workspaces/homework-2-2025-RaniAsPO/lorem.txt"  # Input file
    param2 = "/workspaces/homework-2-2025-RaniAsPO/lorem_morse.txt"  # Output file
    return_value = english_to_morse(param1, param2)
    print(f"Question 1 solution: {return_value}")