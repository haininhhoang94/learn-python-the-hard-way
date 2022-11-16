"""
Some important things to note
- If you have raw BYTES, then you must use .decode() to get the string
- If you have a string and want to send it, store it, share it, or do some
    operation, you need to encode the string back to BYTES
=> Decode Bytes, Encode Strings
"""

# Setup the command line usage and argument
import sys

script, encoding, error = sys.argv


def main(language_file, encoding, errors):
    """
    Explanation:
        - In this case, line use the function readline() which is the following
        readline() will normally return a string contain a line, however, if
        it reached the end of the file, or the file is empty, it will return
        false => make the following if else statement stop printing
    """
    line = language_file.readline()

    if line:
        # This function is describe in the below
        print_line(line, encoding, errors)
        # This is calling main inside main. Technically, this is how you create
        # while loop (alternative way). The things can be described like this
        # while (line):
        # print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):

    """
    Explanation:
        - Decode Bytes, Encode Strings. We need to remember that anything read
        in readline() method is a string, and it should be encode into bytes
        - After that, we need to decode this TRUE bytes again
    """
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)

    cooked_string = raw_bytes.decode(encoding, errors=errors)
    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")
main(languages, encoding, error)
