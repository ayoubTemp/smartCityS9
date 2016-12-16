import csv
import json


separator = ";"
IndexToDelete = []
ColumnsToDelete = []


ColumnsToDelete.append("Debut d'evenement")
ColumnsToDelete.append("Type d'evenement")
ColumnsToDelete.append("Lieu de l'evenement")
ColumnsToDelete.append("Nom Organisme")
ColumnsToDelete.append("Type d'organisme")
ColumnsToDelete.append("Identifiant")
ColumnsToDelete.append("Style")
ColumnsToDelete.append("Genre")
ColumnsToDelete.append("Texte Debut")
ColumnsToDelete.append("Texte Fin")
ColumnsToDelete.append("Departement")
ColumnsToDelete.append("Code INSEE")
ColumnsToDelete.append("Code Postal")
ColumnsToDelete.append("Tarif Mention Payant")
ColumnsToDelete.append("Tarif General")
ColumnsToDelete.append("Tarif Autre")
ColumnsToDelete.append("Age Minimum")


myCsvFilePath = "C:\Users\media\Documents\SmartCityFile\Agenda_culturel_out2.csv"
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


#########################################################
#nettoyage csv model_nouri
myCsvFilePath = "C:\Users\media\Documents\SmartCityFile\model_nouri.csv"
myTempOutputFile = myCsvFilePath.replace(".csv", "_out.csv")



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

#########################################################
#nettoyage csv ghanem_model
myCsvFilePath = "C:\Users\media\Documents\SmartCityFile\ghanem_model.csv"
myTempOutputFile = myCsvFilePath.replace(".csv", "_out.csv")


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


#########################################################
#nettoyage csv Bahssou_model
myCsvFilePath = "C:\Users\media\Documents\SmartCityFile\Bahssou_model.csv"
myTempOutputFile = myCsvFilePath.replace(".csv", "_out.csv")


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


#########################################################
#nettoyage csv Ftouhi_out
myCsvFilePath = "C:\Users\media\Documents\SmartCityFile\Ftouhi.csv"
myTempOutputFile = myCsvFilePath.replace(".csv", "_out.csv")


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


#csv to json
#model_hajar
csvfile = open('C:\Users\media\Documents\SmartCityFile\model_nouri_out.csv', 'r')
jsonfile = open('C:\Users\media\Documents\SmartCityFile\model_nouri.json', 'w')
reader = csv.reader( csvfile,delimiter=separator )
keys = ( "categorie","titre","texteMilieu","commune","latitude","longitude","jourMin","jourMax")
out = []
out = [dict(zip(keys, property)) for property in reader]
print json.dumps(out)
jsonfile.write(json.dumps(out))

#model_ghanem
csvfile = open('C:\Users\media\Documents\SmartCityFile\ghanem_model_out.csv', 'r')
jsonfile = open('C:\Users\media\Documents\SmartCityFile\model_ghanem.json', 'w')
reader = csv.reader( csvfile,delimiter=separator )
keys = ( "categorie","titre","texteMilieu","commune","latitude","longitude","jourMin","jourMax")
out = []
out = [dict(zip(keys, property)) for property in reader]
print json.dumps(out)
jsonfile.write(json.dumps(out))

#model_ayouh
csvfile = open('C:\Users\media\Documents\SmartCityFile\Bahssou_model_out.csv', 'r')
jsonfile = open('C:\Users\media\Documents\SmartCityFile\model_bahssou.json', 'w')
reader = csv.reader( csvfile,delimiter=separator )
keys = ( "categorie","titre","texteMilieu","commune","latitude","longitude","jourMin","jourMax")
out = []
out = [dict(zip(keys, property)) for property in reader]
print json.dumps(out)
jsonfile.write(json.dumps(out))

#model_ftouhi
csvfile = open('C:\Users\media\Documents\SmartCityFile\Ftouhi_out.csv', 'r')
jsonfile = open('C:\Users\media\Documents\SmartCityFile\model_ftouhi.json', 'w')
reader = csv.reader( csvfile,delimiter=separator )
keys = ( "categorie","titre","texteMilieu","commune","latitude","longitude","jourMin","jourMax")
out = []
out = [dict(zip(keys, property)) for property in reader]
print json.dumps(out)
jsonfile.write(json.dumps(out))