#Soru1(GÜN-AY-YIL)
import sys
def fonksiyon():
    gunler = int(input("1-31 arasında gün sayısı giriniz."))
    if (gunler >= 1 and gunler <= 31):
        print("Aralık içinde gün girdiniz.")
    else:
        print("Araklık dışı bir gün girdiniz.")
        sys.exit()
    print(gunler)
    dict_aylar = {1: "Ocak", 2: "Şubat", 3: "Mart", 4: "Nisan", 5: "Mayıs", 6: "Haziran", 7: "Temmuz", 8: "Ağustos",
                  9: "Eylül", 10: "Ekim", 11: "Kasım", 12: "Aralık"}
    sayı = int(input("1-12 arasında bir sayı giriniz."))
    print(dict_aylar[sayı])
    yıl = int(input("Yıl giriniz:"))
    print(yıl)
    print(gunler, dict_aylar[sayı],yıl)
fonksiyon()

#Soru2(Fonksiyon)
# def f(x):
#  ret=0
#  if(x>=9 and x<16):
#    for i in range(0,2*x,2):
#      ret+=i
#  elif(x>=0 and x<9):
#    ret=1
#    for i in range(1,3*x,1):
#      ret*=i
#  return ret
# while(True):
#  sayı=int(input("x değerini giriniz: "))
#  if(sayı>=0 and sayı<16):
#    print(str(f(sayı)))
#  else:
#   print("Aralık dışında bir sayı girdiniz\n")


#Soru3(Matris)
# def sifre(matris1,matris2):
#  for l1 in matris1:
#   for l1_2 in l1:
#    for i in range(len(matris2)):
#     matris2[i]*l1_2
#  return matris2
# def sifrecoz(matris1,matris2):
#  for l1 in matris1:
#   for l1_2 in l1:
#    for i in range(len(matris2)):
#     matris2[i]/=l1_2
#  return matris2
# A=[[1,2,-1],[2,5,2],[-1,-2,2]]
# dict={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
#
# isim="leyladeligoz"
# kod=[[dict[isim[0]],dict[isim[1]],dict[isim[2]]],[dict[isim[3]],dict[isim[4]],dict[isim[5]]],
# [dict[isim[6]],dict[isim[7]],dict[isim[8]]],[dict[isim[9]],dict[isim[10]],dict[isim[11]]]]
# print("Sifresiz:")
# print(kod)
# for l1 in kod:
#  sifre(A,l1)
# print("Sifreli:")
# print(kod)
# print("Sifre çozuldu:")
# for l1 in kod:
#   sifrecoz(A,l1)
# print(kod)

#Soru4(Asal sayıları bulma)
# list = [2]
# def asalSayı():
#   for i in range(3,27):
#    bolundu = False
#    for y in range(2,i):
#     if i%y==0:
#      bolundu = True
#      break
#    if bolundu == False:
#     list.append(i)
# asalSayı()
# print(list)






















