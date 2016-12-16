'''
Created on 8 nov. 2016

@author: media
'''
import csv


myCsvFilePath = "C:\Users\media\Documents\SmartCityFile\Agenda_culturel.csv"
myTempOutputFile = myCsvFilePath.replace(".csv", "_out2.csv")

separator = ";"
IndexToDelete = []
ColumnsToDelete = []

ColumnsToDelete.append("Ident Type")
ColumnsToDelete.append("Ident Organisme")
ColumnsToDelete.append("Etat")
ColumnsToDelete.append("Theme")
ColumnsToDelete.append("Ident Genre")
ColumnsToDelete.append("Jour 1")
ColumnsToDelete.append("Jour 2")
ColumnsToDelete.append("Jour 3")
ColumnsToDelete.append("Jour Du")
ColumnsToDelete.append("Jour Au")
ColumnsToDelete.append("Tarif Mention Gratuit")
ColumnsToDelete.append("Tarif Reduit")
ColumnsToDelete.append("Photo 1 Chemin")
ColumnsToDelete.append("Photo 2 Chemin")
ColumnsToDelete.append("Photo 3 Chemin")
ColumnsToDelete.append("Photo 1 Legende")
ColumnsToDelete.append("Photo 1 Credit")
ColumnsToDelete.append("Photo 2 Legende")
ColumnsToDelete.append("Photo 2 Credit")
ColumnsToDelete.append("Photo 3 Legende")
ColumnsToDelete.append("Photo 3 Credit")
ColumnsToDelete.append("Age Maximum")
ColumnsToDelete.append("Duree")
ColumnsToDelete.append("Mention Complet")
ColumnsToDelete.append("Liens Sons")
ColumnsToDelete.append("Liens Dossiers de Presse")
ColumnsToDelete.append("Tags")
ColumnsToDelete.append("Groupes")
ColumnsToDelete.append("Texte Libre Court")
ColumnsToDelete.append("Texte Libre Long")
ColumnsToDelete.append("Mention Accessible Handicap")
ColumnsToDelete.append("Liens Billeteries")
ColumnsToDelete.append("Liens Videos")

#indices des colonnes a supprimer
for columnToDeleteName in ColumnsToDelete:
    inFile = open(myCsvFilePath)        
    inCSV = csv.reader(inFile, delimiter=separator)
    # On commence par rechercher le numero de la colonne  supprimer
    firstRow = inCSV.next()
    #columnIndex = firstRow.index(columnToDeleteName)
    IndexToDelete.append(firstRow.index(columnToDeleteName))
    inFile.close()

#trier le tableau des indices
flag=1
while flag==1 :
    i=0       
    j=0 
    flag=0
    while i<len(IndexToDelete)-1  :
        if IndexToDelete[i]<(IndexToDelete[i+1]):
            j=IndexToDelete[i]
            IndexToDelete[i]=IndexToDelete[i+1]
            IndexToDelete[i+1]=j
            flag=1
        i=i+1


inFile = open(myCsvFilePath)        
inCSV = csv.reader(inFile, delimiter=separator)

outFile = file(myTempOutputFile, 'wb')        
outCSV = csv.writer(outFile, delimiter=separator,quoting=csv.QUOTE_NONNUMERIC)

#suppression des colonnes et la reecriture dans le fichier out
for row in inCSV:
    # Ici, petite feinte pk Python copie par reference,donc on prend la valeur de la ligne et non la ligne directement
    currentRow = row[:]
    for columnIndex in IndexToDelete:
        currentRow.pop(columnIndex)    
    outCSV.writerow(currentRow)

inFile.close()
outFile.close()


