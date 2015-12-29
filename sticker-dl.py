'''Line sticker downloader'''

'''
Page to scrape:
http://dl.stickershop.line.naver.jp/products/0/0/1/[5737]/android/productInfo.meta

ID (variable) inside []

Naver site picture at 
http://dl.stickershop.line.naver.jp/stickershop/v1/sticker/[9194627]/android/sticker.png

Gif sticker at
http://lstk.ddns.net/animg/[9194625].gif

With animation:
{"packageId":5737,"onSale":true,"validDays":0,"title":{"en":"Bac Bac\u0027s Diary: It\u0027s Winter!","es":"El diario de Bac Bac: Â¡ya es invierno!","in":"Bac Bac\u0027s Diary di Musim Dingin!","ja":"Bac Bac\u0027s Diary: It\u0027s Winter!","ko":"Bac Bac\u0027s Diary: ì‹ ë‚˜ëŠ” ê²¨ìš¸!","th":"Bac Bac\u0027s Diary à¸¤à¸”à¸¹à¸«à¸™à¸²à¸§à¸¡à¸²à¹à¸¥à¹‰à¸§à¸ˆà¹‰à¸²!","zh_CN":"ç™½ç™½æ—¥è®°ï¼šå†¬å¤©æ¥äº†ï¼","zh_TW":"ç™½ç™½ï¼Œå†¬å¤©äº†!"},
"author":{"en":"Daryl Cheung","ja":"Daryl Cheung"},
"price":[{"country":"@@","currency":"NLC","symbol":"NLC","price":100.0},{"country":"HK","currency":"HKD","symbol":"HK$","price":15.0},{"country":"JP","currency":"JPY","symbol":"ï¿¥","price":200.0},{"country":"KR","currency":"KRW","symbol":"â‚©","price":2000.0},{"country":"SG","currency":"SGD","symbol":"S$","price":2.58},{"country":"TW","currency":"TWD","symbol":"NT$","price":60.0},{"country":"US","currency":"USD","symbol":"ï¼„","price":1.99}],
"stickers":[{"width":275,"id":9194624,"height":204},{"width":269,"id":9194625,"height":198},{"width":278,"id":9194626,"height":197},
{"width":260,"id":9194627,"height":206},{"width":269,"id":9194628,"height":225},{"width":278,"id":9194629,"height":140},
{"width":206,"id":9194630,"height":225},{"width":273,"id":9194631,"height":210},{"width":266,"id":9194632,"height":218},
{"width":275,"id":9194633,"height":183},{"width":264,"id":9194634,"height":216},{"width":248,"id":9194635,"height":221},
{"width":266,"id":9194636,"height":213},{"width":270,"id":9194637,"height":201},{"width":278,"id":9194638,"height":206},
{"width":233,"id":9194639,"height":225},{"width":263,"id":9194640,"height":200},{"width":240,"id":9194641,"height":203},
{"width":240,"id":9194642,"height":225},{"width":240,"id":9194643,"height":221},{"width":272,"id":9194644,"height":213},
{"width":248,"id":9194645,"height":212},{"width":270,"id":9194646,"height":159},{"width":260,"id":9194647,"height":147}],
"hasAnimation":true}

Without animation:
{"packageId":5736,"onSale":true,"validDays":0,"title":{"en":"Psalms of Planets Eureka seveN","es":"Psalms of Planets Eureka seveN","in":"Psalms of Planets Eureka seveN","ja":"交響詩篇エウレカセブン","ko":"교향시편 유레카 7","th":"Psalms of Planets Eureka seveN","zh_CN":"交响诗篇","zh_TW":"交響詩篇艾蕾卡7"},"author":{"en":"BANDAI NAMCO Entertainment Inc.","ja":"バンダイナムコエンターテインメント","ko":"BANDAI NAMCO Entertainment Inc.","zh_CN":"BANDAI NAMCO Entertainment Inc.","zh_TW":"BANDAI NAMCO Entertainment Inc."},"price":[{"country":"@@","currency":"NLC","symbol":"NLC","price":100.0},{"country":"HK","currency":"HKD","symbol":"HK$","price":15.0},{"country":"JP","currency":"JPY","symbol":"￥","price":200.0},{"country":"KR","currency":"KRW","symbol":"₩","price":2000.0},{"country":"SG","currency":"SGD","symbol":"S$","price":2.58},{"country":"TW","currency":"TWD","symbol":"NT$","price":60.0},{"country":"US","currency":"USD","symbol":"＄","price":1.99}],
"stickers":[{"width":231,"id":9194496,"height":225},{"width":242,"id":9194497,"height":225},{"width":242,"id":9194498,"height":227},
{"width":248,"id":9194499,"height":233},{"width":239,"id":9194500,"height":225},{"width":239,"id":9194501,"height":225},
{"width":249,"id":9194502,"height":225},{"width":242,"id":9194503,"height":227},{"width":248,"id":9194504,"height":233},
{"width":246,"id":9194505,"height":230},{"width":240,"id":9194506,"height":225},{"width":236,"id":9194507,"height":225},
{"width":240,"id":9194508,"height":225},{"width":233,"id":9194509,"height":225},{"width":240,"id":9194510,"height":225},
{"width":240,"id":9194511,"height":225},{"width":242,"id":9194512,"height":227},{"width":242,"id":9194513,"height":227},
{"width":233,"id":9194514,"height":227},{"width":239,"id":9194515,"height":224},{"width":243,"id":9194516,"height":231},
{"width":242,"id":9194517,"height":225},{"width":237,"id":9194518,"height":227},{"width":248,"id":9194519,"height":234},
{"width":240,"id":9194520,"height":225},{"width":242,"id":9194521,"height":225},{"width":221,"id":9194522,"height":231},
{"width":248,"id":9194523,"height":233},{"width":251,"id":9194524,"height":225},{"width":252,"id":9194525,"height":227},
{"width":240,"id":9194526,"height":227},{"width":240,"id":9194527,"height":227},{"width":240,"id":9194528,"height":225},
{"width":236,"id":9194529,"height":227},{"width":261,"id":9194530,"height":240},{"width":240,"id":9194531,"height":224},
{"width":242,"id":9194532,"height":225},{"width":224,"id":9194533,"height":243},{"width":240,"id":9194534,"height":225},
{"width":248,"id":9194535,"height":233}]}



'''

import requests, sys

def main():
    pack_id = int(input("Enter the sticker pack ID: "))
    pack_url = "http://dl.stickershop.line.naver.jp/products/0/0/1/{}/android/productInfo.meta".format(pack_id)
    pack_meta = get_pack_meta(pack_url).text

    print(pack_meta)

    if """"hasAnimation":true""" in pack_meta:
        pack_ext = input("Animated stickers available! Enter png, gif, or both: ")


    



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

'''