from sticker_dl import *

def main():

    # http://stackoverflow.com/questions/4020539/process-escape-sequences-in-a-string-in-python
    # 2 hours of searching. Python why.
    pack_meta = get_pack_meta(5737).text
    name_string = """"ko":"""
    pack_name = get_pack_name(name_string, pack_meta)
    p1 = bytes(pack_name, 'utf-8').decode('unicode_escape')
    print(pack_name)
    print(p1)

    pack_meta = get_pack_meta(5737).text
    name_string = """"en":"""
    pack_name = get_pack_name(name_string, pack_meta)
    print(pack_name)
    p1 = bytes(pack_name, 'utf-8').decode('unicode_escape')
    print(p1)


if __name__ == '__main__':
    main()