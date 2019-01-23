# LINE-sticker-downloader
Simple code to easily download LINE sticker packs. Download and process sticker packs. Opti
mised for using downloaded content as WhatsApp stickers.

## Currently only for Linux/Ubuntu

<b> Prerequisites</b>: python3, apng2gif

sudo apt install python3  
sudo apt install apng2gif  

<b>How to use:</b>  
  Clone this repository. 
  Navigate into the folder.  
  Write the line sticker codes in the "numbers.txt" file, each on separate line (Contains few codes already for demo).  
  Save the txt file.  
  Open terminal in this folder.  
  Run command: python3 linkgen.py  
After the process completes, there will be two folders <i>"_animated"</i> and <i>"_static"</i> with respective content.
