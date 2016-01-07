#Line sticker downloader
This is a small script that downloads Line stickers, both static and animated (where available).

I made this program because many Line stickers are unavailable due to geographic restrictions. For example, the popular sticker set gudetama is available in different countries with different language captions. Someone in America is only able to buy the gudetama pack with English text, and someone in Taiwan is only able to buy the gudetama pack with Chinese text.

With this program, users can download stickers from any region. In addition, since the stickers are in png and gif form, users are free to use the stickers in applications outside of Line.

Your stickers will be downloaded to a folder on the same level as where your script is running.

If your script is running from C:\Users\Foo\Bar\sticker-dl.py, your downloaded stickers will be in C:\Users\Foo\Bar\1234\, where 1234 is a folder.

#Finding the ID

If you know the ID, you can get a preview of the stickers and animated versions where available on http://lstk.ddns.net/Stickers.php.

The animated stickers require clicking on the static images to load.


Alternatively, if you want to search stickers by name, try http://www.line-stickers.com/.

The search result will link to a page that contains the ID.

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