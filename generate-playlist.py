import os

def generate_playlist():
    audio_extensions = {'.mp3', '.wma', '.wav'}
    file_list = []
    
    current_dir = os.getcwd()
    parent_folder = os.path.basename(current_dir)
    
    for root, _, files in os.walk(current_dir):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in audio_extensions:
                full_path = os.path.join(root, file)
                file_list.append(full_path)
    
    # Sort by folder structure first, then filename
    file_list.sort(key=lambda x: (
        # Split the relative path into directory components
        tuple(os.path.normpath(os.path.relpath(x, current_dir)).split(os.sep)[:-1]),
        # Then sort by filename (case-insensitive)
        os.path.basename(x).lower()
    ))
    
    playlist_name = f"{parent_folder}.m3u"
    
    with open(playlist_name, 'w', newline='\r\n') as f:
        f.write('\n'.join(file_list))

if __name__ == '__main__':
    generate_playlist()