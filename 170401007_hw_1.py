#-*- coding: utf-8 -*-
kelimeler=[]
histogramListe=[]
arananlar=[]
maxKelimeler=[]
def myHistogram(histogramListe):
    myDic =dict()
    for i in histogramListe:
        if i in myDic:
            myDic[i] =+1
        else:
            myDic[i] = 1
    return myDic
            
def maxHistogram(myDic):
    max_Kelime ,key= 0,""
    for i in myDic:
        if myDic[i]>max_Kelime:
            key = i
            max_Kelime = myDic[i]
    return key

def readFile(kelimeler):
    dosya = open("1.txt","r")
    for i in dosya:
        for j in i.split():
            kelimeler.append(j.lower())
            
def writeInput():
    file = open("input.txt","w")
    while(1):
        inp = input("Aranacak İfadeyi Giriniz: ")
        if(inp == "-1"):
            break
        while len(inp.split())>5:
            print("5den fazla kelime giremezsiniz!")
            inp = input("Aranacak İfadeyi Giriniz: ")
        file.write(inp)
        file.write("\n")
    file.close()
            
def readInput():
    dosya = open("input.txt","r")
    for satir in dosya:
        arananlar.clear()
        for i in satir.split():
            arananlar.append(i)
        kelimeOnerme(arananlar)
  
def writeOutput(maxKelimeler):
    dosya = open("output.txt","w")
    uzunluk = len(maxKelimeler)
    i=0
    while i<uzunluk:
        dosya.write(maxKelimeler[i])
        dosya.write("\n")
        i=i+1
    dosya.close()

    
def replaceFonk(kelimeler):
    for k in range(0,len(kelimeler)):
        kelimeler[k] = kelimeler[k].replace(',','')
        kelimeler[k] = kelimeler[k].replace('.','')
        kelimeler[k] = kelimeler[k].replace(':','')
        kelimeler[k] = kelimeler[k].replace(';','')
        kelimeler[k] = kelimeler[k].replace('"','')
        kelimeler[k] = kelimeler[k].replace("'",'')
               
def kelimeOnerme(arananlar):
    uzunluk = len(arananlar)
    for i in range(len(kelimeler)):
        if kelimeler[i]==arananlar[0]: 
            c = 1
            for j in range(uzunluk):
                if kelimeler[i+j] == arananlar[j]:
                    c = c*1       
                else:
                    c = c*0
            if c == 1:
                histogramListe.append(kelimeler[i+uzunluk])

    myDic = myHistogram(histogramListe)
    maxKelime = maxHistogram(myDic)
    maxKelimeler.append(maxKelime)
    writeOutput(maxKelimeler)
    histogramListe.clear()
    
def main():
    readFile(kelimeler)
    replaceFonk(kelimeler)
    writeInput()
    readInput()

    
main() 

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    