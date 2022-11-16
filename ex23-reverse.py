import sys

script, encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        out_file = open("languages-bytes.txt", "w")
        out_file.write(line)
        out_file.close()
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)

    print(next_lang, "<===>", raw_bytes)


languages = open("languages.txt", encoding="utf-8")
main(languages, encoding, error)
