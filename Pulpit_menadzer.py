import os
import shutil

Scieszka='C:/Users/PC/Desktop'

#funkcja tworzenia folderów
def folder(foldery):
    #to łączy w jedną sicieszkę
    pelna_sciezka = os.path.join(Scieszka, foldery)

    if not os.path.exists(pelna_sciezka):
        os.mkdir(pelna_sciezka)

    else:
        print('Juz istnieje')  
    return pelna_sciezka


lista_plikow=os.listdir(Scieszka)

#print(lista_plikow)

folder("Pliki_tekstowe")
folder("Foldery")
folder("Programy")

for pliki in lista_plikow:
    pelna_sciezka = os.path.join(Scieszka, pliki)
    nazwa, rozszerzenie = os.path.splitext(pliki)

    if rozszerzenie.lower() == '.txt' or rozszerzenie.lower() == '.pdf' or rozszerzenie.lower() == '.docx' or rozszerzenie.lower() == '.rtf':
        shutil.move(os.path.join(Scieszka,pliki), os.path.join(Scieszka, "Pliki_tekstowe"))
    if rozszerzenie.lower() == '.jpg':
        shutil.move(os.path.join(Scieszka,pliki), 'C:/Users/PC/Obrazy')
    if rozszerzenie.lower() == '.exe':
        shutil.move(os.path.join(Scieszka,pliki), os.path.join(Scieszka, "Programy"))
    if pliki not in  ["Foldery","Nowy folder (3)","Pliki_tekstowe","Programy" ]:
        if os.path.isdir(pelna_sciezka):
        
            shutil.move(os.path.join(Scieszka,pliki), os.path.join(Scieszka, "Foldery"))
    