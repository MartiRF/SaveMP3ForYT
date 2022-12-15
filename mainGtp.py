from pytube import YouTube
import os
import shutil

ruta = './audioMp4'

def menu(urls):
    print("Youtube Url:")
    UrlInput = str(input())
    print("1) Agregar ")
    print("2) Descargar ")
    inputMenu = str(input('Ingrese:'))
    urls.append(UrlInput)
    if inputMenu == '1':
        menu(urls)
    if inputMenu == '2':
        descargar(urls)

def descargar(urls):
    print('Iniciando descargas')
    for url in urls:
        yt = YouTube(url).streams.filter(abr="128kbps",type
def convertir():
    print('Convertir a mp3')
    for itemMp4 in os.listdir(path=ruta):
        itemMp3 = itemMp4.replace(".mp4",".mp3")
        os.system('cd ' + ruta + "\n" +
                  "ffmpeg -i '" + itemMp4 + "' '" + itemMp3 +"'\n" +
                  "rm '" + itemMp4 + "'")
    print('Listo')
    mover()

def mover():
    print('Moviendo')
    for mp3 in os.listdir(path=ruta):
        shutil.move("./audioMp4/" + mp3, 'mp3/')
    print('TODO CORRECTO, files listos /mp3/')

def main():
    urls = []
    menu(urls)

main()
# En resumen, se han movido las funciones al principio del código, se ha eliminado la lista global Urls y se ha pasado como parámetro a las funciones que lo necesiten, se ha eliminado la función AgregarALista(), se ha simplificado la función Descargar() utilizando ciclos for, se han mejorado la legibilidad y la simplicidad de las funciones Convertir() y Mover() utilizando ciclos for y comillas simples en lugar de comillas dobles, y se ha agregado una función main() que inicializa el programa.