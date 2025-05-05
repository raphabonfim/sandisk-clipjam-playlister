# sandisk-clipjam-playlister
A python script to generate working playlists for the Sandisk ClipJAM MP3 player regardless of Operational System.

## How to use this script
Run the script in the directory you want to create a playlist. This script can also be used in the parent directory of the files (in the case of double records or multi-disc releases). 

The script automatically: 

1. lists all of your .mp3, .wma, .wav files in the current directory and all children
2. Sorts the file names by folder and
3. adds them to a playlist in the .m3u format using the `CRLF` newline standard from Windows and DOS. 

You should open the resulting playlist and remove the `/Volume/ClipJAM/` or `E:\ClipJAM\` from it as the MP3 player won’t work with absolute filepaths.

This should make the playlists work. Enjoy your MP3 player :) 