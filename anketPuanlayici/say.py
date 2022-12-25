from os import name, write
import pandas as pd

# Variables Starting

formFile = "Test.csv" #Anket bilgileri
nameQuest = "İsminiz:" #Anketteki isim bilgisini çeker
mailQuest = "Mail adresiniz:" #Anketteki mail bilgisini çeker
answersFile = "Answers.txt" #Anketin doğru cevapları, her satıra sırayla doğru cevaplar yazılacak.
rankFile = "Ranking.txt" #Her soru 1 puan değerinde olacak şekilde puanı hesaplayıp çıktıyı bu isimle kaydedecek.

# Variables Ending

anketList = pd.read_csv(formFile, sep=",", encoding="utf-8")

persons = anketList[nameQuest].values.tolist()
mails = anketList[mailQuest].values.tolist()
f_cevaplar = open(answersFile, "r", encoding="utf-8")
txt_cevap = f_cevaplar.read().split("\n")

f_siralama = open(rankFile, "w", encoding="utf-8")

Soru1 = anketList["Soru 1"].values.tolist() #Soru "anketList'in içerisine" yazılacak.
Soru2 = anketList["Soru 2"].values.tolist()
# Soru3 = anketList["Soru 3"].values.tolist()
# Soru4 = anketList["Soru 4"].values.tolist()
# Soru5 = anketList["Soru 5"].values.tolist()
# Soru6 = anketList["Soru 6"].values.tolist()
# Soru7 = anketList["Soru 7"].values.tolist()
# Soru8 = anketList["Soru 8"].values.tolist()
# Soru9 = anketList["Soru 9"].values.tolist()
# Soru10 = anketList["Soru 10"].values.tolist()
# Soru11 = anketList["Soru 11"].values.tolist()
# Soru12 = anketList["Soru 12"].values.tolist()
# Soru13 = anketList["Soru 13"].values.tolist()
# Soru14 = anketList["Soru 14"].values.tolist()
# Soru15 = anketList["Soru 15"].values.tolist()

points = []
for i in range(len(mails)):
    personalPoint = 0
    if str(Soru1[i]) == txt_cevap[0]:
        personalPoint += 1
    if str(Soru2[i]) == txt_cevap[1]:
        personalPoint += 1
    # if str(Soru3[i]) == "1":
    #     personalPoint += 1
    # if str(Soru4[i]) == "1":
    #     personalPoint += 1
    # if str(Soru5[i]) == "1":
    #     personalPoint += 1
    # if str(Soru6[i]) == "1":
    #     personalPoint += 1
    # if str(Soru7[i]) == "1":
    #     personalPoint += 1
    # if str(Soru8[i]) == "1":
    #     personalPoint += 1
    # if str(Soru9[i]) == "1":
    #     personalPoint += 1
    # if str(Soru10[i]) == "1":
    #     personalPoint += 1
    # if str(Soru11[i]) == "1":
    #     personalPoint += 1
    # if str(Soru12[i]) == "1":
    #     personalPoint += 1
    # if str(Soru13[i]) == "1":
    #     personalPoint += 1
    # if str(Soru14[i]) == "1":
    #     personalPoint += 1
    # if str(Soru15[i]) == "1":
    #     personalPoint += 1
    

    points.append(str(personalPoint) + " puan: " + mails[i])

points.sort(reverse=True)
for rank in points:
    f_siralama.write(rank + "\n")