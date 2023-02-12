from pytube import YouTube
import os
import glob
import shutil

def menu():
    os.system('cls')
    print("Youtube Url:")
    url = str(input())
    descargar(url)

def descargar(url):
    print('Iniciando descargas')
    yt = YouTube(url).streams.filter(abr="128kbps",type="audio").first()
    yt.download()
    print("Done: " + YouTube(url).title)
    convertir()

def convertir():
    ruta = os.path.join(os.path.dirname(__file__), "*.mp4")
    mp4 = glob.glob(ruta)

    for archivo in mp4:
        nombreMp4 = os.path.basename(archivo)
        nombreMp3 = nombreMp4.replace(".mp4", ".mp3")
        convertir = 'ffmpeg -i "' + nombreMp4 + '" -y "' + nombreMp3 + '"'
        print(convertir)
        os.system(convertir)
        os.remove(nombreMp4)
        mover(nombreMp3)

def mover(nombre):
    print('sexo')
    shutil.move(nombre, "mp3/")
    main()

def main():
    menu()
main()