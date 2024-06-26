How to use:

1 - Before running the script, make sure you have installed the necessary dependencies (pytaglib and pandas).

2 - Edit the CSV file with the track list information. Each row in the CSV file should correspond to a track, and the columns should include the track number, title, artist, album, album artist, year, and publisher.

Example CSV format:

track number,title,artist,album,album artist,year,publisher

1,Track 1,Artist 1,Album Name,Various Artists,2024,Publisher Name

2,Track 2,Artist 2,Album Name,Various Artists,2024,Publisher Name

3 - Ensure that the names of the files begin with the track number followed by "-" (e.g., "1-Track1.wav", "2-Track2.wav", etc.) This ID will be used to match the files with the corresponding lines in the CSV.

4 - Write the folder path for your files in the script.

5 - Run the script. It will apply the changes to the original files.


Troubleshooting:
If you encounter permission errors when running the script, make sure that the files are not being used by other processes and that you have the necessary permissions to modify them.

Supported file types: FLAC, WAV, MP3, AIFF, OGG.
