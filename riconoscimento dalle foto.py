import face_recognition as riconoscimento
from glob import glob
from shutil import move

immagine_da_riconoscere = riconoscimento.load_image_file("") #nelle virgolette mettere la foto da far riconoscere
encoding_da_riconoscere = riconoscimento.face_encodings(immagine_da_riconoscere)[0]

for foto in glob(""): #percorso della cartella es fotodariconoscere/*.png
    print(foto)
    immagine = riconoscimento.load_image_file(foto)
    encoding = riconoscimento.face_encodings(immagine)[0]
    match = riconoscimento.compare_faces([encoding_da_riconoscere], encoding)[0]
    if match:
        move(foto, "") #creare una cartella e "" mettere il percorso della cartella