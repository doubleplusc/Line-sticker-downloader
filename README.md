#Line sticker downloader
This is a small script that downloads Line stickers, both static and animated (where available).

Many Line stickers are unavailable due to geographic restrictions. For example, the popular sticker set gudetama is available in different countries with different language captions. Someone in America is only able to buy the gudetama pack with English text, and someone in Taiwan is only able to buy the gudetama pack with Chinese text. Additionally, limited time/expired/promotional sticker packs will no longer be available for use after their offering periods.

With this program, users can download stickers from any region and from expired packs. In addition, since the stickers are in png and gif form, users are free to use the stickers in applications outside of Line.

There are some limitations to this program that are beyond my current control:
1. Line will only support static images through the photo upload feature, even if the sticker is animated. Line does not support inline animated images, unlike programs like Wechat.
2. You have to directly transfer the downloaded stickers from your computer to your phone. There are plenty of programs out there that make device transfers less painful.

Your stickers will be downloaded to a folder on the same level as where your script is running.

If your script is running from C:\Users\Foo\sticker_dl.py, and you download a sticker pack named Bar, your downloaded stickers will be in C:\Users\Foo\Bar\.

#Finding the ID

Alternatively, if you want to search stickers by name, try http://www.line-stickers.com/.

The search result will link to a page that contains the ID.

You can also find the ID through your Line app's sticker preview page and pressing the Share button. If you share to a program that transmits text, the ID and link will be pasted. (Note that your mobile app's page only contains region-locked and unexpired results.)

After getting the ID, you can get a preview of the stickers and animated versions where available on http://lstk.ddns.net/Stickers.php. Packs with animations require clicking on the static images to load.


#Using the Program
When you open the program, you will be prompted

```Enter the sticker pack ID:```

Enter the ID you found from the previous step.

You will be notified whether animated stickers are available, and prompted for your desired download.

#Download options
png: static stickers only.

y: static stickers only.

gif: animated stickers only.

both: both static and animated stickers will be downloaded.

Anything else: exit the program without downloading.


#TODO

Allow program to take input from a text file for batch downloading.

Add a GUI to make program less offensive looking.

Allow inline previewing of image?

Line store seems to have .apng files, an uncommon format. Should add option for that.

Unlikely, but on the wishlist: inline search of sticker packs, removing need to separately go on other sites to find ID; database for sticker descriptions? Also figure out how sound stickers are implemented.



DISCLAIMER: I am not responsible for what users do with this program. This program was written purely for learning purposes.