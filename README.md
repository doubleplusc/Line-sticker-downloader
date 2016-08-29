#Line sticker downloader
This is a Python script that downloads Line stickers, both static and animated (where available).

For Windows 7 64-bit users, a standalone executable is available on the releases page. Its compatibility with Windows 8 and 10 are not guaranteed. For other operating systems, please consult https://docs.python.org/3.5/using/index.html for installing and using Python.

Many Line stickers are unavailable due to geographic restrictions. For example, the popular sticker set gudetama is available in different countries with different language captions. Users in America are only able to buy the gudetama pack with English text, and users in Taiwan are only able to buy the gudetama pack with Chinese text. Additionally, limited time/expired/promotional sticker packs will no longer be available for use after their offering periods.

With this program, users can download stickers from any region and from expired packs. Downloads are in png and gif form, users are free to use the stickers in applications outside of Line. NOTE: Animated "popup" stickers with sound are not currently supported. This will be fixed in the next version.

There are some limitations to this program that are beyond my control:

1. Line will only support static images through the photo upload feature, even if the sticker is animated. Line does not support inline animated images, unlike programs like Wechat.

2. You have to directly transfer the downloaded stickers from your computer to your phone. There are plenty of programs out there that make device transfers less painful.

Your stickers will be downloaded to a folder on the same level as where your script is running.

If your script is running from C:\Users\Foo\sticker_dl.py, and you download a sticker pack named Bar, your downloaded stickers will be in C:\Users\Foo\Bar\.

#Finding the ID

To search for stickers by name, try http://www.line-stickers.com/.

The search result will link to a page that contains the ID.

This site is not necessarily up to date, and you may need to search by release date and ID on http://lstk.ddns.net/Stickers.php.

![](/images/Line_sticker_-_search_by_name.png?raw=true)

You can also find the ID through your Line app's sticker preview page and pressing the Share button. If you share to a program that transmits text, the ID and link will be pasted. (Note that your mobile app's page only contains region-locked and unexpired results.)

![](/images/Line_sticker_-_ID_share_button.png?raw=true)

![](/images/Line_sticker_-_ID_from_app.png?raw=true)

After getting the ID, you can get a preview of the stickers and animated versions where available on http://lstk.ddns.net/Stickers.php. This site is also handy for browsing the entire Line archive of available stickers, most recent shown first. Click on the thumbnails to load the preview page. Packs with animations require clicking on the static images to load.

![](/images/Line_sticker_-_search_by_ID.png?raw=true)


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

Next release: support animated "popup" stickers. Script only downloads static versions for now.

Allow program to take input from a text file for batch downloading.

Add a GUI to make program less offensive looking.

Allow inline previewing of image?

Line store seems to have .apng files, an uncommon format. Should add option for that.

Unlikely, but on the wishlist: inline search of sticker packs, removing need to separately go on other sites to find ID; database for sticker descriptions? Also figure out how sound stickers are implemented.



DISCLAIMER: I take no responsibility for what users do with this program.