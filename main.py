from pytube import YouTube
import os
import shutil

Urls = []
ruta = './audioMp4'

def AgregarALista(input):
    Urls.append(input)

def Menu():
    print(Urls)
    print("Youtube Url:")
    UrlInput = str(input())
    print("1) Agregar ")
    print("2) Descargar ")
    inputMenu = str(input('Ingrese:'))
    AgregarALista(UrlInput)
    if inputMenu == '1':
        Menu()
    if inputMenu == '2':
        Descargar()
def Descargar():
    print('Iniciando descargas')
    for url in Urls:
        yt = YouTube(url).streams.filter(abr="128kbps",type="audio").first()
        donwloadFileMp4Audio = yt.download(output_path=ruta)
        print("Done: " + YouTube(url).title)
    Convertir()
def Convertir():
    print('Convertir a mp3')
    listMp4 = os.listdir(path=ruta)
    comandoEntrarCaparteMp4 = 'cd ' + ruta + "\n"
    for itemMp4 in listMp4:
        itemMp3 = itemMp4.replace(".mp4",".mp3")
        comandoConvertir = "ffmpeg -i '" + itemMp4 + "' '" + itemMp3 +"'\n"
        os.system(comandoEntrarCaparteMp4 + comandoConvertir)
        os.system(comandoEntrarCaparteMp4 + "rm '" + itemMp4 + "'")
    print('Listo')
    Mover()
def Mover():
    print('Moviendo')
    listMp3 =  os.listdir(path=ruta)
    for mp3 in listMp3:
        fileMp3Route = "./audioMp4/" + mp3
        shutil.move(fileMp3Route, 'mp3/')
    print('TODO CORRECTO, files listos /mp3/')


def Main():
    Menu()
Main()