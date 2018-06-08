# MAKE SURE YOU HAVE INSTALLED pdftotext IN YOUR LINUX MACHINE

import unicodedata
import os
import argparse
 
# ELIMINATE TILDES FROM TEXT
def elimina_tildes(cadena):
    s = ''.join((c for c in unicodedata.normalize('NFD',cadena) if unicodedata.category(c) != 'Mn'))
    return s
 
 
# CREATES NEW FILE WITH CLEAN TEXT
def cleanTXT(txtFileName, pdfFilesPath):
 
    # CREAMOS DIRECTORIO PARA ALMACENAR LOS TXT LIMPIOS
    if not os.path.exists(pdfFilesPath + 'limpios/'):
        os.makedirs(pdfFilesPath + 'limpios/')
 
    file = open(txtFileName, 'r')
    if pdfFilesPath == "":
        new_name = txtFileName[4:-4]+'_clean.txt'
    else:
        new_name = txtFileName[len(pdfFilesPath)+4:-4]+'_clean.txt'
        #new_name = txtFileName[14:-4]+'_clean.txt'
    new_file = open(pdfFilesPath + 'limpios/' + new_name, 'w')
 
    lines = file.readlines()
    for line in lines:
        # ELIMINATE SPACES
        while True:
            line = line.replace("  ", " ")
            if "  " not in line:
                break
 
        # ELIMINATE TILDES
        elimina_tildes(line)
 
        # APPEND NEW CLEAN LINE TO new_file
        new_file.write(line)
 
    new_file.close()
    file.close()

 
def pdf2text(pdfFilesPath):
 
    for pdfFile in os.listdir(pdfFilesPath):
        if pdfFilesPath == None:
            pdfFilesPath = ""
        # CREAMOS DIRECTORIO PARA ALMACENAR LOS TXT LIMPIOS
        if not os.path.exists(pdfFilesPath+'txt/'):
            os.makedirs(pdfFilesPath+'txt/')
        if pdfFile[-4:] == ".pdf":
            txt_name = pdfFilesPath + "txt/" + pdfFile[:-4]+'.txt'
            os.system('pdftotext -layout '+ pdfFilesPath + pdfFile + ' ' + txt_name)
            cleanTXT(txt_name, pdfFilesPath)
 
 
if __name__ == '__main__':
 
    parser = argparse.ArgumentParser()
 
    ##POSITIONAL ARGUMENT --> PATH
    parser.add_argument('--path', nargs=1, help='python3 pdf2text.py --path [PATH/] ## by default current path is set ## Example: python3.5 pdf2text.py --path filesPath/', type=str)
 
    args = parser.parse_args()
 
    if not args.path:
        pdf2text(None)
    else:
        pdf2text(args.path[0])
