import face_recognition as fr
from glob import glob
from shutil import move

# Load the image to be recognized
image_to_recognize = fr.load_image_file("path/to/image.jpg")  # Insert the path to the image to be recognized within the quotes

# Encode the image to be recognized
encoding_to_recognize = fr.face_encodings(image_to_recognize)[0]

# Loop through all images in the specified folder
for photo in glob("folder_path/*.png"):  # Replace "folder_path" with the path to the folder containing the images to be recognized
    print(photo)
    # Load the current image
    image = fr.load_image_file(photo)
    
    # Encode the current image
    encoding = fr.face_encodings(image)[0]
    
    # Compare the encodings of the current image and the image to be recognized
    match = fr.compare_faces([encoding_to_recognize], encoding)[0]
    
    # If a match is found, move the image to a specified folder
    if match:
        move(photo, "destination_folder_path/")  # Replace "destination_folder_path" with the path to the destination folder
