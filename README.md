#Line sticker downloader
This is a small script that downloads Line stickers, both static and animated (where available).
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