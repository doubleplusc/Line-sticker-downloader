'''Line sticker downloader'''


import requests, sys, os



def main():
    pack_id = int(input("Enter the sticker pack ID: "))
    pack_url = "http://dl.stickershop.line.naver.jp/products/0/0/1/{}/android/productInfo.meta".format(pack_id)
    pack_meta = get_pack_meta(pack_url).text


    
    if """"hasAnimation":true""" in pack_meta:
        pack_ext = input("Animated stickers available! Enter png, gif, or both, anything else to exit: ")
    else:
        pack_ext = input("Only static stickers available! y to continue, anything else to exit")
    

    id_string = """"id":"""
    list_ids = []

    current_id, start_index = 0, 0  # [4] Why have start_index included

    while start_index != -1:
        start_index, current_id, pack_meta = get_ids(id_string, pack_meta)  # "Passing by assignment" something mutable vs. immutables. SO answers are handwavey and fail to give useful explanation to a newcomer
        list_ids.append(current_id)

    list_ids.pop()  # [4] Why pop


    # [3] A less ugly way of checking menu values
    menu = {'gif': get_gif, 'png': get_png, 'both': [get_gif, get_png]}
    menu.setdefault()
    if choice in menu[pack_ext]:  # there isn't really a good way to set the default return value if key doesn't exist without setdefault() on all of them
        choice(list_ids, pack_id)
    else:
        sys.exit()

    print("Done! Program exiting...")
    sys.exit()

def get_ids(id_string, pack_meta):
    start_index = pack_meta.find(id_string)
    end_index = pack_meta.find(",", start_index + 1)
    sticker_id = pack_meta[start_index+len(id_string):end_index]
    return start_index, sticker_id, pack_meta[end_index:]


def get_gif(list_ids, pack_id):
    os.makedirs(pack_id, exist_ok = True)  # exist_ok = True doesn't raise exception if directory exists. Files already in directory are not erased
    for x in list_ids:
        url = 'http://lstk.ddns.net/animg/{}.gif'.format(x)

def get_png(list_ids, pack_id):
    os.makedirs(pack_id, exist_ok = True)
    for x in list_ids:
        url = 'http://dl.stickershop.line.naver.jp/stickershop/v1/sticker/{}/android/sticker.png'.format(x)
        

def get_pack_meta(pack_url):
    pack_meta = requests.get(pack_url)

    # http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html Status codes
    # It seems that normal request gives 200. Not sure what it means for program if non200 code is given. Will work with 200 for now.


    if pack_meta.status_code == 200:
        return pack_meta
        '''
        f = open('dump.txt', 'w+b')  # [2] write mode
        f.write(pack_meta.content)  # [1] UnicodeEncodeError
        f.close()
        '''
    else:
        print("{} did not return 200 status code. Program exiting...".format(pack_id))
        sys.exit()


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
[4] Originally had a conditional in the while state to check if the start_index was -1 to make sure it doesn't get added.
But a single pop at the end is much better than the if check in every loop iteration.
'''
