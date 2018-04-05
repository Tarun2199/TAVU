
import os
import shutil

##############################################################################
#                                                                            #
#                           By Tarun Kumar                                   #
#                                                                            #
##############################################################################

# Disclaimer: Writen by Tarun kumar ;)
print("                                ==================================================    ")
print("                             |||              _____                                |||")
print("                             |||              ----- /\ \  / |  |                   |||")
print("                             |||                |  /  \ \/  |__|                   |||")
print("                             |||                                                   |||")
print("                                ==================================================    ")

if(input("                                         || press any key to continue ||")):
    os.system('cls' if os.name=='nt' else 'clear')
    print("                                  --------------------------------------")
    print("                                            Choose Language-")
    print("                                  --------------------------------------")
    lan_choice=int(input('                                    1>>ENGLISH 2>SPANISH 3>RUSSIAN'))
    os.system('cls')
    if(lan_choice==1):
        print("                                 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("                                     Enter path location for arranging")
        path=input("                                 ----").strip()
##        list_dict=os.listdir(path)
        try:
            list_dict=os.listdir(path)
        except:
            print("                                 XXXXXXXXXX Invalid Input XXXXXXXXX")
        else:
            for files in list_dict:
               
               if '.png' in files or '.jpeg' in files and not os.path.exists(path+'Images/'+files):
                    if not os.path.exists(path+'Images'):
                       os.makedirs(path+'Images')
                    shutil.move(path+files,path+'Images/'+files)
               if '.txt' in files and not os.path.exists(path+'Documents/Text/'+files):
                   if not os.path.exists(path+'Documents/Text'):
                       os.makedirs(path+'Documents/Text')
                   shutil.move(path+files,path+'Documents/Text/'+files)
               if '.docx' in files and not os.path.exists(path+'Documents/Word/'+files):
                   if not os.path.exists(path+'Documents/Word'):
                       os.makedirs(path+'Documents/Word')
                   shutil.move(path+files,path+'Documents/Word/'+files)
               if '.pdf' in files and not os.path.exists(path+'Documents/Pdf/'+files):
                   if not os.path.exists(path+'Documents/Pdf'):
                       os.makedirs(path+'Documents/Pdf')
                   shutil.move(path+files,path+'Documents/Pdf/'+files)
               if '.pptx' in files and not os.path.exists(path+'Documents/Powerpoint/'+files):
                   if not os.path.exists(path+'Documents/Powerpoint'):
                       os.makedirs(path+'Documents/Powerpoint')
                   shutil.move(path+files,path+'Documents/Powerpoint/'+files)
               if '.xlsx' in files and not os.path.exists(path+'Documents/Excel/'+files):
                   if not os.path.exists(path+'Documents/Excel'):
                       os.makedirs(path+'Documents/Excel')
                   shutil.move(path+files,path+'Documents/Excel/'+files)
               if '.mp3' in files and not os.path.exists(path+'Musics/'+files):
                   if not os.path.exists(path+'Musics'):
                       os.makedirs(path+'Musics')
                   shutil.move(path+files,path+'Musics/'+files)
               if '.mp4'in files or '.mkv'in files or '.wmv'in files or '.avi'in files or '.flv'in files or '.mov' in files and not os.path.exists(path+'Videos/'+files):
                   if not os.path.exists(path+'Videos'):
                       os.makedirs(path+'Videos')
                   shutil.move(path+files,path+'Videos/'+files)
            print("                                     --------------------------------------")
            print("                                               Successful arrange")      
            print('\n')
            print("                                            ++++++++++++++++++++++")
            input("                                                   Thank You")
    


            
    if(lan_choice==2):
        print("                                 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("                                     Ingrese la ubicación de la ruta para organizar")
        path=input("                                 ----").strip()
        try:
            list_dict=os.listdir(path)
        except:
            print("                                 XXXXXXXXXX entrada inválida XXXXXXXXX")
            
        else:
            for files in list_dict:
               if '.png' in files or '.jpeg' in files and not os.path.exists(path+'Imágenes/'+files):
                    if not os.path.exists(path+'Imágenes'):
                       os.makedirs(path+'Imágenes')
                    shutil.move(path+files,path+'Imágenes/'+files)
               if '.txt' in files and not os.path.exists(path+'Documentos/TextFile/'+files):
                   if not os.path.exists(path+'Documentos/TextFile'):
                       os.makedirs(path+'Documentos/TextFile')
                   shutil.move(path+files,path+'Documentos/TextFile/'+files)
               if '.docx' in files and not os.path.exists(path+'Documentos/WordFile/'+files):
                   if not os.path.exists(path+'Documentos/WordFile'):
                       os.makedirs(path+'Documentos/WordFile')
                   shutil.move(path+files,path+'Documentos/WordFile/'+files)
               if '.pdf' in files and not os.path.exists(path+'Documentos/Pdf/'+files):
                   if not os.path.exists(path+'Documentos/Pdf'):
                       os.makedirs(path+'Documentos/Pdf')
                   shutil.move(path+files,path+'Documentos/Pdf/'+files)
               if '.pptx' in files and not os.path.exists(path+'Documentos/Powerpoint/'+files):
                   if not os.path.exists(path+'Documentos/Powerpoint'):
                       os.makedirs(path+'Documentos/Powerpoint')
                   shutil.move(path+files,path+'Documentos/Powerpoint/'+files)
               if '.xlsx' in files and not os.path.exists(path+'Documentos/Excel/'+files):
                   if not os.path.exists(path+'Documentos/Excel'):
                       os.makedirs(path+'Documentos/Excel')
                   shutil.move(path+files,path+'Documentos/Excel/'+files)
               if '.mp3' in files and not os.path.exists(path+'Musica/'+files):
                   if not os.path.exists(path+'Musica'):
                       os.makedirs(path+'Musica')
                   shutil.move(path+files,path+'Musica/'+files)
               if '.mp4'in files or '.mkv' in files or '.wmv' in files or '.avi' in files or '.flv'in files or '.mov' in files and not os.path.exists(path+'Videos/'+files):
                   if not os.path.exists(path+'Videos'):
                       os.makedirs(path+'Videos')
                   shutil.move(path+files,path+'Videos/'+files)
               else:
                   continue
            print("                                     --------------------------------------")
            print("                                               Arreglos exitosos")
            print('\n')
            print("                                            ++++++++++++++++++++++")
            input("                                                  Gracias ")

    if(lan_choice==3):
        print("                                 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("                                     Введите путь для размещения")
        path=input("                                 ----").strip()
        try:
            list_dict=os.listdir(path)
        except:
            print("                                 XXXXXXXXXX неправильный ввод XXXXXXXXX")
            
        else:
            for files in list_dict:
               if '.png' in files or '.jpeg' in files and not os.path.exists(path+'Изображений/'+files):
                    if not os.path.exists(path+'Изображений'):
                       os.makedirs(path+'Изображений')
                    shutil.move(path+files,path+'Изображений/'+files)
               if '.txt' in files and not os.path.exists(path+'документы/Text/'+files):
                   if not os.path.exists(path+'документы/Text'):
                       os.makedirs(path+'документы/Text')
                   shutil.move(path+files,path+'документы/Text/'+files)
               if '.docx' in files and not os.path.exists(path+'документы/Word/'+files):
                   if not os.path.exists(path+'документы/Word'):
                       os.makedirs(path+'документы/Word')
                   shutil.move(path+files,path+'документы/Word/'+files)
               if '.pdf' in files and not os.path.exists(path+'документы/Pdf/'+files):
                   if not os.path.exists(path+'документы/Pdf'):
                       os.makedirs(path+'документы/Pdf')
                   shutil.move(path+files,path+'документы/Pdf/'+files)
               if '.pptx' in files and not os.path.exists(path+'документы/Powerpoint/'+files):
                   if not os.path.exists(path+'документы/Powerpoint'):
                       os.makedirs(path+'документы/Powerpoint')
                   shutil.move(path+files,path+'документы/Powerpoint/'+files)
               if '.xlsx' in files and not os.path.exists(path+'документы/Excel/'+files):
                   if not os.path.exists(path+'документы/Excel'):
                       os.makedirs(path+'документы/Excel')
                   shutil.move(path+files,path+'документы/Excel/'+files)
               if '.mp3' in files or '.wav' in files and not os.path.exists(path+'Гурджиева/'+files):
                   if not os.path.exists(path+'Гурджиева'):
                       os.makedirs(path+'Гурджиева')
                   shutil.move(path+files,path+'Гурджиева/'+files)
               if '.mp4'in files or '.mkv' in files or '.wmv' in files or '.avi' in files or '.flv'in files or '.mov' in files and not os.path.exists(path+'видео/'+files):
                   if not os.path.exists(path+'видео'):
                       os.makedirs(path+'видео')
                   shutil.move(path+files,path+'видео/'+files)
               else:
                   continue
            print("                                     --------------------------------------")
            print("                                               Успешная организация")
            print('\n')
            print("                                            ++++++++++++++++++++++")
            input("                                                   Спасибо")
