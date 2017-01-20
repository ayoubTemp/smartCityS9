'''
Created on 18 nov. 2016

@author: Gihane G
'''
import json
import csv
from pyspark import SparkConf, SparkContext, SQLContext
from _sqlite3 import Row


# encoding=utf8

sparkConf = SparkConf().setAppName("mapreduce").setMaster("local")
sc = SparkContext(conf = sparkConf)

textFile = sc.textFile("C:\Users\Gihane G\workspace\SmartCity\Agenda_culturel_out2.csv")

fProfils = "C:\Users\Gihane G\workspace\SmartCity\Profils.csv"
fileprofils = open(fProfils, "rb")
readerP = csv.reader(fileprofils, delimiter=";")

row_ghanem=[]
row_nouri=[]
row_bahssou=[]
row_ftouhi=[]


for row in readerP:
    if row[0]=="ghanem":
        row_ghanem = row
    if row[0]=="nouri":
        row_nouri = row
    if row[0]=="bahssou":
        row_bahssou = row
    if row[0]=="ftouhi":
        row_ftouhi = row
        
    




data = textFile.map(lambda line: line.split(";"))




if int(row_ghanem[2])<16 :
    dataghanem = data.filter(lambda line : "jeunes" in line[7]).filter(lambda line : row_ghanem[5] in line[21])
    cpt_ghanem = data.filter(lambda line: "jeunes" in line[7]).filter(lambda line : row_ghanem[5] in line[21]).count()

elif row_ghanem[4]=="handicape" :
    dataghanem = data.filter(lambda line :
                            "handicap" in line[23]
                             or "handicap" in line[11]
                            or "handicap" in line[12]
                            or "handicap" in line[3]).filter(lambda line : row_ghanem[5] in line[21])
    cpt_ghanem = data.filter(lambda line:"handicap" in line[23]
                              or "handicap" in line[12]
                             or "handicap" in line[11]
                             or "handicap" in line[3]).filter(lambda line : row_ghanem[5] in line[21]).count()

else:   
    dataghanem = data.filter(lambda line:   
                          row_ghanem[3] in line[7]
                          or row_ghanem[3] in line[6]).filter(lambda line : row_ghanem[5] in line[21])
                          
    cpt_ghanem = data.filter(lambda line: 
                          row_ghanem[3] in line[7]
                          or row_ghanem[3] in line[6]).filter(lambda line : row_ghanem[5] in line[21])
                          
                          
if row_ghanem[5]=="oui":
     dataghanem = dataghanem.filter(lambda line :
                             line[22] <= "\"" + row_ghanem[6] + "\"" )
     cpt_ghanem = dataghanem.filter(lambda line:
                            line[22] <= "\""  + row_ghanem[6]+"\"" ).count()
    


if int(row_bahssou[2])<16 :
    databahssou = data.filter(lambda line : "jeunes" in line[7]).filter(lambda line : row_bahssou[5] in line[21])
    cpt_bahssou = data.filter(lambda line: "jeunes" in line[7]).filter(lambda line : row_bahssou[5] in line[21]).count()
    
elif row_bahssou[4]=="handicape" :
    databahssou = data.filter(lambda line : "handicap" in line[23]
                                             or "handicap" in line[12]
                                            or "handicap" in line[3]
                                            or "handicap" in line[11]).filter(lambda line : row_bahssou[5] in line[21])
    cpt_bahssou = data.filter(lambda line: "handicap" in line[23]
                               or "handicap" in line[12]
                                or "handicap" in line[3]
                                or "handicap" in line[11]).filter(lambda line : row_bahssou[5] in line[21]).count()

else:               
    databahssou = data.filter(lambda line:   
                          row_bahssou[3] in line[7]
                          or row_bahssou[3] in line[6]).filter(lambda line : line[7] != "Animation loisirs jeunes").filter(lambda line : row_bahssou[5] in line[21])
    cpt_bahssou = data.filter(lambda line: 
                          row_bahssou[3] in line[7]
                          or row_bahssou[3] in line[6]).filter(lambda line : line[7] != "Animation loisirs jeunes").filter(lambda line : row_bahssou[5] in line[21]).count()                

if row_bahssou[5]=="oui":
     databahssou = databahssou.filter(lambda line :
                             line[22] <= "\"" + row_bahssou[6] + "\"" )
     cpt_bahssou = databahssou.filter(lambda line:
                            line[22] <= "\"" + row_bahssou[6] + "\"" ).count()                          



if int(row_nouri[2])<16 :
    datanouri = data.filter(lambda line : "jeunes" in line[7]).filter(lambda line : row_nouri[5] in line[21])
    cpt_nouri = data.filter(lambda line: "jeunes" in line[7]).filter(lambda line : row_nouri[5] in line[21]).count()
    
elif row_nouri[4]=="handicape" :
    datanouri = data.filter(lambda line : "handicap" in line[23]
                                 or "handicap" in line[12]
                                 or "handicap" in line[3]
                                          or "handicap" in line[11]).filter(lambda line : row_nouri[5] in line[21])
    cpt_nouri = data.filter(lambda line: "handicap" in line[23]
                                 or "handicap" in line[12]
                                or "handicap" in line[3]
                                or "handicap" in line[11]).filter(lambda line : row_nouri[5] in line[21]).count()


else:
    datanouri = data.filter(lambda line: 
                            row_nouri[3] in line[7]
                           or row_nouri[3] in line[6]).filter(lambda line : row_nouri[5] in line[21])
    cpt_nouri = data.filter(lambda line: row_nouri[3] in line[7]
                           or row_nouri[3] in line[6]).filter(lambda line : row_nouri[5] in line[21]).count()
    
if row_nouri[5]=="oui":
     datanouri = datanouri.filter(lambda line :
                             line[22] <= "\"" + row_nouri[6]+"\""  )
     cpt_nouri = datanouri.filter(lambda line:
                            line[22] <= "\"" + row_nouri[6]+"\""  ).count()    
                       

if int(row_ftouhi[2])<16 :
    dataftouhi = data.filter(lambda line : "jeunes" in line[7]).filter(lambda line: row_ftouhi[5] in line[21])
    cpt_ftouhi = data.filter(lambda line: "jeunes" in line[7] ).filter(lambda line: row_ftouhi[5] in line[21]).count()

elif row_ftouhi[4]=="handicape" :
    dataftouhi = data.filter(lambda line : "handicap" in line[23]
                                          or "handicap" in line[11]
                                           or "handicap" in line[12]
                                or "handicap" in line[3]).filter(lambda line: row_ftouhi[5] in line[21])
    cpt_ftouhi = data.filter(lambda line: "handicap" in line[23]
                                or "handicap" in line[11]
                                 or "handicap" in line[12]
                                or "handicap" in line[3]).filter(lambda line: row_ftouhi[5] in line[21]).count()

else:                         
    dataftouhi = data.filter(lambda line: row_ftouhi[3] in line[7]
                           or row_ftouhi[3] in line[6]).filter(lambda line: row_ftouhi[5] in line[21])

    cpt_ftouhi = data.filter(lambda line: row_ftouhi[3] in line[7]
                             or row_ftouhi[3] in line[6] ).filter(lambda line: row_ftouhi[5] in line[21]).count()

if row_ftouhi[5]=="oui":
     dataftouhi = dataftouhi.filter(lambda line :
                             line[22] <= "\"" + row_ftouhi[6]+"\""  )
     cpt_ftouhi = dataftouhi.filter(lambda line:
                            line[22] <= "\"" + row_ftouhi[6]+"\""  ).count()

fname = "C:\Users\Gihane G\workspace\SmartCity\ghanem_model.csv"
file = open(fname, "wb")
writer = csv.writer(file, delimiter=";", quoting=csv.QUOTE_NONE,quotechar='')



for i in range(0, cpt_ghanem):
    writer.writerow([dataghanem.collect()[i][0], dataghanem.collect()[i][1].encode("utf-8"), dataghanem.collect()[i][2].encode("utf-8"), dataghanem.collect()[i][3].encode("utf-8"), dataghanem.collect()[i][4].encode("utf-8"),  dataghanem.collect()[i][5].encode("utf-8"),   dataghanem.collect()[i][6].encode("utf-8"), dataghanem.collect()[i][7].encode("utf-8"),  dataghanem.collect()[i][8].encode("utf-8"), dataghanem.collect()[i][9].encode("utf-8"), dataghanem.collect()[i][10].encode("utf-8"), 
                     dataghanem.collect()[i][11].encode("utf-8"), dataghanem.collect()[i][12].encode("utf-8"), 
                     dataghanem.collect()[i][13].encode("utf-8"), dataghanem.collect()[i][14].encode("utf-8"), 
                     dataghanem.collect()[i][15].encode("utf-8"),   dataghanem.collect()[i][16].encode("utf-8"), 
                     dataghanem.collect()[i][17].encode("utf-8"),  dataghanem.collect()[i][18].encode("utf-8"),
                     dataghanem.collect()[i][19].encode("utf-8"), dataghanem.collect()[i][20].encode("utf-8"),
                      dataghanem.collect()[i][21].encode("utf-8"), dataghanem.collect()[i][22].encode("utf-8"),
                      dataghanem.collect()[i][23].encode("utf-8"), dataghanem.collect()[i][24].encode("utf-8")
                     ])
    

fname2 = "C:\Users\Gihane G\workspace\SmartCity\Bahssou_model.csv"
file2 = open(fname2, "wb")
writer2 = csv.writer(file2, delimiter=";", quoting=csv.QUOTE_NONE,quotechar='')

for i in range(0, cpt_bahssou):
    writer2.writerow([databahssou.collect()[i][0], databahssou.collect()[i][1].encode("utf-8"), databahssou.collect()[i][2].encode("utf-8"), databahssou.collect()[i][3].encode("utf-8"), databahssou.collect()[i][4].encode("utf-8"),  databahssou.collect()[i][5].encode("utf-8"),   databahssou.collect()[i][6].encode("utf-8"), databahssou.collect()[i][7].encode("utf-8"),  databahssou.collect()[i][8].encode("utf-8"), databahssou.collect()[i][9].encode("utf-8"), databahssou.collect()[i][10].encode("utf-8"), 
                     databahssou.collect()[i][11].encode("utf-8"), databahssou.collect()[i][12].encode("utf-8"), 
                     databahssou.collect()[i][13].encode("utf-8"), databahssou.collect()[i][14].encode("utf-8"), 
                     databahssou.collect()[i][15].encode("utf-8"),   databahssou.collect()[i][16].encode("utf-8"), 
                     databahssou.collect()[i][17].encode("utf-8"),  databahssou.collect()[i][18].encode("utf-8"),
                     databahssou.collect()[i][19].encode("utf-8"), databahssou.collect()[i][20].encode("utf-8"),
                      databahssou.collect()[i][21].encode("utf-8"), databahssou.collect()[i][22].encode("utf-8"),
                      databahssou.collect()[i][23].encode("utf-8"), databahssou.collect()[i][24].encode("utf-8")
                     ])


fname1 = "C:\Users\Gihane G\workspace\SmartCity\model_nouri.csv"
file1 = open(fname1, "wb")
writer1 = csv.writer(file1, delimiter=";", quoting=csv.QUOTE_NONE,quotechar='')


for i in range(0, cpt_nouri):

    writer1.writerow([datanouri.collect()[i][0], datanouri.collect()[i][1].encode("utf-8"), datanouri.collect()[i][2].encode("utf-8"), datanouri.collect()[i][3].encode("utf-8"), datanouri.collect()[i][4].encode("utf-8"),  datanouri.collect()[i][5].encode("utf-8"),   datanouri.collect()[i][6].encode("utf-8"), datanouri.collect()[i][7].encode("utf-8"),  datanouri.collect()[i][8].encode("utf-8"), datanouri.collect()[i][9].encode("utf-8"), datanouri.collect()[i][10].encode("utf-8"), 
                     datanouri.collect()[i][11].encode("utf-8"), datanouri.collect()[i][12].encode("utf-8"), 
                     datanouri.collect()[i][13].encode("utf-8"), datanouri.collect()[i][14].encode("utf-8"), 
                     datanouri.collect()[i][15].encode("utf-8"),   datanouri.collect()[i][16].encode("utf-8"), 
                     datanouri.collect()[i][17].encode("utf-8"),  datanouri.collect()[i][18].encode("utf-8"),
                     datanouri.collect()[i][19].encode("utf-8"), datanouri.collect()[i][20].encode("utf-8"),
                      datanouri.collect()[i][21].encode("utf-8"), datanouri.collect()[i][22].encode("utf-8"),
                      datanouri.collect()[i][23].encode("utf-8"), datanouri.collect()[i][24].encode("utf-8")
                     ])
    
    
fname3 = "C:\Users\Gihane G\workspace\SmartCity\Ftouhi.csv"
file3 = open(fname3, "wb")
writer3 = csv.writer(file3, delimiter=";", quoting=csv.QUOTE_NONE,quotechar='')


for i in range(0, cpt_ftouhi):

    writer3.writerow([dataftouhi.collect()[i][0], dataftouhi.collect()[i][1].encode("utf-8"), dataftouhi.collect()[i][2].encode("utf-8"), dataftouhi.collect()[i][3].encode("utf-8"), dataftouhi.collect()[i][4].encode("utf-8"),  dataftouhi.collect()[i][5].encode("utf-8"),   dataftouhi.collect()[i][6].encode("utf-8"), dataftouhi.collect()[i][7].encode("utf-8"),  dataftouhi.collect()[i][8].encode("utf-8"), dataftouhi.collect()[i][9].encode("utf-8"), dataftouhi.collect()[i][10].encode("utf-8"), 
                     dataftouhi.collect()[i][11].encode("utf-8"), dataftouhi.collect()[i][12].encode("utf-8"), 
                     dataftouhi.collect()[i][13].encode("utf-8"), dataftouhi.collect()[i][14].encode("utf-8"), 
                     dataftouhi.collect()[i][15].encode("utf-8"),   dataftouhi.collect()[i][16].encode("utf-8"), 
                     dataftouhi.collect()[i][17].encode("utf-8"),  dataftouhi.collect()[i][18].encode("utf-8"),
                     dataftouhi.collect()[i][19].encode("utf-8"), dataftouhi.collect()[i][20].encode("utf-8"),
                      dataftouhi.collect()[i][21].encode("utf-8"), dataftouhi.collect()[i][22].encode("utf-8"),
                      dataftouhi.collect()[i][23].encode("utf-8"), dataftouhi.collect()[i][24].encode("utf-8")
                     ])


#print datanouri.collect()

#print cpt_ghanem


