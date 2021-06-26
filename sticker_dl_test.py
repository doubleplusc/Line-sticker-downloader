import sticker_dl

import re
import codecs

ESCAPE_SEQUENCE_RE = re.compile(r'''
    ( \\U........      # 8-digit hex escapes
    | \\u....          # 4-digit hex escapes
    | \\x..            # 2-digit hex escapes
    | \\[0-7]{1,3}     # Octal escapes
    | \\N\{[^}]+\}     # Unicode characters by name
    | \\[\\'"abfnrtv]  # Single-character escapes
    )''', re.UNICODE | re.VERBOSE)


def decode_escapes(s):
    def decode_match(match):
        return codecs.decode(match.group(0), 'unicode-escape')

    return ESCAPE_SEQUENCE_RE.sub(decode_match, s)


def main():

    # http://stackoverflow.com/questions/4020539/process-escape-sequences-in-a-string-in-python
    # 2 hours of searching. Python why.
    pack_meta = sticker_dl.get_pack_meta(5737).text
    name_string = """"ko":"""
    pack_name = sticker_dl.get_pack_name(name_string, pack_meta)
    decoded_name = decode_escapes(pack_name)
    file_name = "".join(i for i in decoded_name if i not in r'\/:*?"<>|')  # https://en.wikipedia.org/wiki/Filename#Reserved_characters_and_words  # noqa: E501
    print(file_name)

    pack_meta = sticker_dl.get_pack_meta(5737).text
    name_string = """"en":"""
    pack_name = sticker_dl.get_pack_name(name_string, pack_meta)
    decoded_name = decode_escapes(pack_name)
    file_name = "".join(i for i in decoded_name if i not in r'\/:*?"<>|')
    print(file_name)


if __name__ == '__main__':
    main()


def test_dummy():
    assert 0 == 0
