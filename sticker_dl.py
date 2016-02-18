'''Line sticker downloader'''


import requests
import sys
import os
import re
import codecs


def main():
    pack_id = int(input("Enter the sticker pack ID: "))
    pack_meta = get_pack_meta(pack_id).text

    name_string = """"en":"""  # folder name will take pack's English title
    pack_name = get_pack_name(name_string, pack_meta)
    pack_name = decode_escapes(pack_name)
    print("\nThis pack contains stickers for", pack_name)

    if """"hasAnimation":true""" in pack_meta:
        pack_ext = input("\nAnimated stickers available! \nEnter png, gif, or both, anything else to exit: ")
    else:
        pack_ext = input("\nOnly static stickers available! \ny to download, anything else to exit: ")

    id_string = """"id":"""
    list_ids = []

    current_id, start_index = 0, 0  # [4] Why have start_index included

    while start_index != -1:
        start_index, current_id, pack_meta = get_ids(id_string, pack_meta)  # "Passing by assignment" mutable vs. immutable. Any reassignments done in called function will not reflect on return. But manipulating the parameter will reflect.
        list_ids.append(current_id)

    list_ids.pop()  # [4] Why pop

    # [3] A less ugly way of checking menu values
    menu = {'gif': (get_gif,), 'png': (get_png,), 'y': (get_png,), 'both': (get_gif, get_png)}  # D'OH! Originally said tuples wouldn't work, which was strange. Thanks to doing MIT problems, I realized I used (var) instead of (var,). Former will not be considered a tuple.
    if pack_ext in menu:
        for choice in menu[pack_ext]:
            choice(list_ids, pack_name)
    else:
        print("Nothing done. Program exiting...")
        sys.exit()

    print("\nDone! Program exiting...")

    sys.exit()


def get_pack_name(name_string, pack_meta):
    start_index = pack_meta.find(name_string)
    end_index = pack_meta.find(',', start_index + 1)
    sticker_name = pack_meta[start_index+len(name_string)+1:end_index-1]  # lower bound needs +1 to exclude the beginning " mark. -1 to make upper bound the , which is excluded from the range
    return sticker_name


def get_ids(id_string, pack_meta):
    start_index = pack_meta.find(id_string)
    end_index = pack_meta.find(",", start_index + 1)
    sticker_id = pack_meta[start_index+len(id_string):end_index]
    return start_index, sticker_id, pack_meta[end_index:]


def validate_savepath(pack_name):
    decoded_name = decode_escapes(pack_name)
    save_name = "".join(i for i in decoded_name if i not in r'\/:*?"<>|')
    os.makedirs(str(save_name), exist_ok = True)  # exist_ok = True doesn't raise exception if directory exists. Files already in directory are not erased
    return save_name


def get_gif(list_ids, pack_name):
    pack_name = validate_savepath(pack_name)
    for x in list_ids:
        save_path = os.path.join(str(pack_name), str(x) + '.gif')
        url = 'http://lstk.ddns.net/animg/{}.gif'.format(x)
        image = requests.get(url, stream = True)
        with open(save_path, 'wb') as f:
            for chunk in image.iter_content(chunk_size = 10240):
                if chunk:
                    f.write(chunk)


def get_png(list_ids, pack_name):
    pack_name = validate_savepath(pack_name)
    for x in list_ids:
        save_path = os.path.join(str(pack_name), str(x) + '.png')
        url = 'http://dl.stickershop.line.naver.jp/stickershop/v1/sticker/{}/android/sticker.png'.format(x)
        image = requests.get(url, stream = True)
        with open(save_path, 'wb') as f:  # http://stackoverflow.com/questions/16694907/how-to-download-large-file-in-python-with-requests-py Understood! with construct is a fancy way of try/catch that cleans up, even with exceptions thrown
            for chunk in image.iter_content(chunk_size = 10240):  # chunk_size is in bytes
                if chunk:
                    f.write(chunk)


def get_pack_meta(pack_id):

    pack_url = "http://dl.stickershop.line.naver.jp/products/0/0/1/{}/android/productInfo.meta".format(pack_id)
    pack_meta = requests.get(pack_url)

    # http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html Status codes
    # It seems that normal request gives 200. Not sure what it means for program if non200 code is given. Will work with 200 for now.

    if pack_meta.status_code == 200:
        return pack_meta
    else:
        print("{} did not return 200 status code, possibly invalid sticker ID. Program exiting...".format(pack_id))
        sys.exit()

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


if __name__ == '__main__':
    main()


'''
[1] http://stackoverflow.com/questions/11435331/python-requests-and-unicode
Solve Unicode with r.content instead of r.text
[2] w+ creates file if it doesn't exist, truncates if it exists. b is for binary, Windows is picky. Never hurts to add b for platform friendliness
[3] http://stackoverflow.com/questions/3260057/how-to-check-variable-against-2-possible-values-python
leads to http://stackoverflow.com/questions/13186542/functions-in-python-dictionary
For multiple functions per key: http://stackoverflow.com/questions/9205081/python-is-there-a-way-to-store-a-function-in-a-list-or-dictionary-so-that-when
How clever.
http://stackoverflow.com/a/9139961 If I didn't have a check for key in dict, this would've been another way.
[4] Originally had a conditional in the while state to check if the start_index was -1 to make sure it doesn't get added.
But a single pop at the end is much better than the if check in every loop iteration.
[5] http://stackoverflow.com/questions/4020539/process-escape-sequences-in-a-string-in-python
Regular expression saves the day.
'''
