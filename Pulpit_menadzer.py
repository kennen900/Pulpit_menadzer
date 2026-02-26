import os
import shutil
from pathlib import Path

Desktop = Path.home() / "Desktop"
Obrazy_systemowe = Path.home() / "Pictures"   
Programy_folder = Desktop / "Programy"
Teksty_folder = Desktop / "Pliki_tekstowe"

Kategorie = {
    Teksty_folder: ['.txt', '.pdf', '.docx', '.rtf'],
    Obrazy_systemowe: ['.jpg', '.png', '.jpeg'],
    Programy_folder: ['.exe', '.lnk'],
}


for folder in [Teksty_folder, Programy_folder]:
    folder.mkdir(exist_ok=True)

for plik in Desktop.iterdir():
    if plik.is_file():
        for folder_docelowy, rozszerzenia in Kategorie.items():
            if plik.suffix.lower() in rozszerzenia:
                shutil.move(str(plik), str(folder_docelowy / plik.name))
                break