# Make sure your files begin with the track number followed by "-" so they can be matched to the correct line of data.
# Edit the csv file, specify the folder path and run.

# Supported file types: FLAC, WAV, MP3, AIFF, OGG.

import os
import pandas as pd
import taglib

# Read metadata from CSV
metadata_df = pd.read_csv("metadata.csv") 

# Define folder path
source_folder = "Insert folder path here"


# Tag and Rename function
def tag(file_name,metadata_df,source_folder,file_extension):
        track_number = int(file_name.split("-")[0])  # Extract track number from filename
        track_metadata = metadata_df[metadata_df["track number"] == track_number]
        
        if not track_metadata.empty:
            track_metadata = track_metadata.iloc[0]  # Assuming there's only one match
            audio_file = os.path.join(source_folder, file_name)
            
            # Load audio file
            audio = taglib.File(audio_file)
            
            # Add metadata
            audio.tags['TRACKNUMBER'] = str(track_metadata["track number"]) 
            audio.tags['TITLE'] = track_metadata["title"]  
            audio.tags['ARTIST'] = track_metadata["artist"] 
            audio.tags['ALBUM'] = track_metadata["album"] 
            audio.tags['ALBUMARTIST'] = track_metadata["album artist"] 
            audio.tags['DATE'] = str(track_metadata["year"])  
            audio.tags['PUBLISHER'] = track_metadata["publisher"]  

            # Save modified metadata
            audio.save()
            audio.close()
            
            # Rename file
            new_file_name = f"{track_metadata['track number']} - {track_metadata['artist']} - {track_metadata['title']}{file_extension}"
            new_file_path = os.path.join(source_folder, new_file_name)
            os.rename(audio_file, new_file_path)
            
            print(f"Metadata updated and file renamed: {file_name} -> {new_file_name}")
        else:
            print(f"No metadata found for {file_name}")


# Process audio files
for file_name in os.listdir(source_folder):
    if file_name.endswith(".wav"):
        tag(file_name,metadata_df,source_folder,file_extension='.wav')
    elif file_name.endswith(".flac"):
        tag(file_name,metadata_df,source_folder,file_extension='.flac')
    elif file_name.endswith(".mp3"):
        tag(file_name, metadata_df, source_folder, file_extension='.mp3')
    elif file_name.endswith(".aiff") or file_name.endswith(".aif"):
        tag(file_name, metadata_df, source_folder, file_extension='.aiff')
    elif file_name.endswith(".ogg"):
        tag(file_name, metadata_df, source_folder, file_extension='.ogg')
