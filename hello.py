# son = int(input("istalgan sonni kiriting "))
# kvadrat = son ** 2
# kubi = pow(son,3)
# print( str(son) + "  ning kvadrati  " + str(kvadrat) + "  ga teng \n" ,str(son) + "  ning kubi  " + str(kubi) + "  ga teng "  )

# yosh = int(input("yoshingiz nechchida"))
# yil = 2023 - yosh
# print("siz tug'ulgan yil " + str(yil) + "  ga teng ")

# ismlar = [ 'Abror', 'Otabek' , 'Alisher']
# print("Salom  " + ismlar[0] + " ," + " bugun choyxona bormi \n " + ismlar[1] + " , " + "choyxonaga borasizmi  \n" + ismlar[2] + "  tashkil qilmoqdaa" )

# sonlar = []
# sonlar.append("89")
# sonlar.append("78")
# sonlar.append( "5.6")
# sonlar.append(" -45")
# sonlar.insert(1,"763230918")
# del(sonlar[4])
# sonlar.remove("78")
# birinchisi = sonlar.pop()
# print(sonlar , " ,  ", birinchisi)

# davlatlar = [ 'uzbekistan' , 'pakistan' , 'korea' , 'hindiston' ]

# print(len(davlatlar))

# print(sort(davlatlar, reverse=True))
# davlatlar.sort(reverse=True)

# print(davlatlar)
# juft_sonlar = list(range(120,1200,2))
# print("juft sonlar : " , juft_sonlar)

# print(sum(juft_sonlar))
# print( min(juft_sonlar)-max(juft_sonlar))
# print(len(juft_sonlar))
# print(juft_sonlar[-20:])
# a = max(juft_sonlar)
# b = min(juft_sonlar)

# alfa = list((a-b)/2)
# c = alfa + 10
# print(list(juft_sonlar[alfa:c]))

# nonushta = []
# nonushta.append("asal")
# nonushta.append("chuchvara")
# nonushta.append("sho'rva ")
# nonushta.append("shakar choy")
# nonushta.append("non")
# print(nonushta)
# taomlar = nonushta[1:3]
# print(taomlar)

# taomlar.insert(1,"manti")
# taomlar.insert(2,"osh")

# print(taomlar)
# print(" taomlar = " + taomlar, "nonushta uchun = " + nonushta)
# print(nonushta)

# nonushta  = tuple(nonushta)
# taomlar = tuple(taomlar)
# print(  nonushta , taomlar)

# nonushta[0] = " qaymoq va non"

# print(nonushta)

# s=0
# ismlar = ("ali " , " vali " , " otabek " , " alisher " ," ogabek ")
# for ism ismlar :
#     s=s+1
#     print(f" salom {ism} " )
# print (s , ("marta takrorlandi"))

# sonlar = list(range (11,100,2))
# for son in sonlar:
#    print(f" { son } ning kubi {son**3} ga teng")


# cars = [ 'toyota' , 'mazda' , 'hyundai' , 'gm' , 'kia']
# for car in cars :
#     if car  == 'gm' :
#       print(car.upper())
#     else :
#        print(car.title())


# for avto in avtolar: # avtolar ichidadi har bir avto uchun ...
#     if avto == 'bmw':  # ... agar avto bmw ga teng bo'lsa ...
#         print(avto.upper()) # avto nomini hamma harflarini katta bilan yoz.
#     else: # aks holda ...
#         print(avto.title()) # a


# uydagilar = { 'otam':"o'ta aqilli" , 'onam':"uy bekasi" , "opam":"qattiqqo'l" }

# print(f" otam : { uydagilar['otam'].title()} - ishni ko'zini biladi , onam : {uydagilar['onam']} - mehribonim ")

# sevimli_taomlar = {'otam':'beshbarmoq', 'onam':"sho'rva" , 'akam': 'osh',"men":"chuchvara" }

# print(f" dadamning sevimli taomlari {sevimli_taomlar['otam'].title()}\
#       onamning sevimli taomlari { sevimli_taomlar['onam'].upper()}")

# python_izlug = { 'len': "uzunlikni o'lchaydi", 
#                 'upper':'hammasi katta harflar bilan chiqaradi',
#                 'lower': 'hammsini kichik harflarda chiqaradi',
#                 "if_else":"agar yoki"}
 # print(python_izlug['lower'])

# birortasidaa =input("kiritasan plastik kartenni  kodi bilan   ")

# tarjimon =python_izlug.get(birortasidaa)

# if tarjimon == None:
    
#      print ("bunday so'z mavjud emas")

# else :
#     print( f"{birortasidaa.lower()} so'zi {tarjimon} - degan ma'noni anglatadi ")

# python_izlug = { 'len': "uzunlikni o'lchaydi", 
#                 'upper':'hammasi katta harflar bilan chiqaradi',
#                 'lower': 'hammsini kichik harflarda chiqaradi',
#                 "if_else":"agar yoki",
#                 'print':'chiqarish aperatori',
#                 'insert':'listlarga element qoshsa boladi ',
#                 'remove':"xohlagan elementni o'chirish",
#                 'title':"so'zlarni bosh harf bialn yozib beradi",
#                 "del":"o'chiradi",
#                 "typle":"o'zgarmas ro'yxatga aylantiradi"
#                 }
# print(python_izlug.items())
# for key , value in sorted(python_izlug.items()) :
#     print(f"Kalit : {key}")
# for key , value in sorted(python_izlug.items()) :
#     print(f"qiymat : {value}")

# print('faqat 3ta sozni sorat olasiz')

# buyurtmalar=[]
# for n in range(3):
#     buyurtmalar.append(input(f" {n+1}-so'z: ").lower())

# for buyurtma in buyurtmalar :
#     if buyurtma in python_izlug :
#         print(f" {buyurtma.title()}, so'znining manosi - {python_izlug[buyurtma]}")
#     else :
#         print(f"Kechirasiz bizda bunday {buyurtma} so'z mavjud emas")

#Bismillah

# alisher_navoiy = {
#     "ism":"Alisher Navoiy",
#     "asari":["xamsa,qush tili",]
    
#     }
# amir_temur = {
#     "ism":"Amir Tmur",
#     "asari":["temur tuzuklari,jang",]
#     }
# ibn_sino = {
#     "ism":"Ibn Sino",
#      "asari":["tib qonunlari,tabobat",]
#     }
# buxoriy = {
#     "ism":"Imom Buxoriy",
#     "asari":["hadisi sha'rif,hadislar"]
#     }
# mashhurs = [alisher_navoiy,amir_temur,ibn_sino,buxoriy]
# for mashhur in mashhurs :
#     kitobi = mashhur['asari']
#     ismi = mashhur['ism']
#     print(f"\n {ismi}ning  quyidagi asarlari mavjud",)
#     for  kitob in kitobi :
#         print(kitob)

# films = {
#     "ali":["terminator, supermen , tor"],
#     "vali":["halk,temir odam","spyder"],
#     "salim":["mahalla, abdullajon, simba"],
#     }
# for ism,kinosi in films.items() :
#     print(f"\n {ism.title()}ning sevimli kinolari")
    
#     for kino in kinosi :
#         print(kino)
    
#!!!!!!!!!!qaytaddan bajar
# davlatlar = {
#         "uzbekistan" : { "poytaxti":"toshkent",
#                         "tili":"o'zbek",
#                         "puli birligi":"so'm"
#                         },
#         "rossiya" : {"poytaxti":"maskva",
#                     "tili":"rus",
#                     "puli birligi":"rubl"
#                     },
#         "aqsh" : {"poytaxti":"vashington",
#                   "tili":"ingliz",
#                   "puli birligi":"dollor"
#                   }
#         } 

# for mamlakat,malumoti in davlatlar.items():
# #     print(f" \n {mamlakat.title()} haqida ba'zi ma'lumotlar")
    
# #     for asos,qiymat in malumoti.items():
# #         print(f"{asos} : " )
# #         print( qiymat)

#       if mamlakat.lower()=='aqsh'
           
      
#       mamlakat = mamlakat.capitalize():
#           print(f" \n {mamlakat.title()} haqida ba'zi ma'lumotlar",
#     !!!!!!!!            f)

# WHILE BOSHLADIKMIIII



# savol = "dasturni to'xtatmoqchi bo'lsangiz 'stop' so'zni qoldiring        "
# savol =savol + "(yaxshi ko'rgan kitoblaringizni kiriting \n )"

# while True :
#     kitob = input(savol)
#     if kitob ==  'stop':
#        break
# print("rahmat")

# savol = "yoshingizni kiriting"

# royxatimiz = []

# # savol = savol + "(tugatmoqchi bo'lsangiz 'stop' so'zini qoldiring \n)"
# n=1

# while True:
    
#     savol = "buyurtmangizni kiriting \n"
   
#     royxat = input(savol.title())
    
#     royxatimiz.append(royxat)
    
#     javob = input("yana buyurtma bermoqchimisiz? (ha\yo'q)")
    
#     if javob == "ha":
#         n+=1
#         print(n)
#         continue
#     else:
#         break


# bozorimiz = {}

# n=1

# while True:
    
#     mahsulot =input ("mahsulotingizni nomini kiriting \n")
#     narxi = input("narxini kiriting \n")
    
#     bozorimiz[mahsulot] = int(narxi)
    
#     javob = input("yana mahsulot qo'shmoqchimisiz ? (ha\yo'q) \n")
    
#     if javob == "ha":
#         n+=1
#         print(n)
#         continue
#     else:
#         break
    
#     for mahsulot,narxi in bozorimiz :
#         print(f" {mahsulot}ning narxi {narxi}ga teng")
 

       
# mahsulot = [ 'olma ', 'anjir','uzum','qovun']
# bozorimiz = {
#     'olma':'2000',
#     "anjir":"3000",
#     "uzum":"3400",
#     "qovun":"4500"
#     }   
# while mahsulot :
#     buyurtma = mahsulot.pop()
#     if buyurtma in bozorimiz.keys() :
#         narx = bozorimiz[buyurtma]
#         print(f" {buyurtma.title() } - {narx }  so'm")
#     else :
#         print(f"bizda {buyurtma} yo'q")


###   Funksiya

# def ism_ayt(ism):
#     """ ismni qabul qilib chiqarib beruvchi funksiya"""
#     print(f"Xush kelibsiz hurmatli {ism.title()}")
# ism_ayt("ergashjon")



# def toliq_ism(ism, familiya):
#     """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")
 
# toliq_ism('olim', 'hakimov')

# Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.
    
# def ism_yosh_chiqar(ism,yosh):
#     """ Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya ! """
#     print(f"Foydalanuvchi ismi:{ism.title()}\n"
#           f"Janob {ism.title()} {2023-yosh} - yilda tug'ulgan ekanlar")
# ism_yosh_chiqar('ergashjon', 20)
    
    
#Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.

# def son_hisobla(son):
#     """ Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya !"""
#     print(f"{son}-ning kvadrati {son**2}-ga teng \n"
#           f"{son}-ning kubi {son**3}-ga teng ")

# son_hisobla(4)


# Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.

# def juft_toq_aniqla(son):
#     """ Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya !"""
#     if son%2 ==0:
#         print(f"{son} juft son")
#     else:
#         print(f"{son} toq son")
    
# juft_toq_aniqla(9)

# Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.

# def max_min_chiqar(son1,son2):
#     """ 2 sonni taqqoslovchi funksiya"""
#     if son1>son2 :
#         print(f"birinchi {son1} soni ikkinchi {son2} sonidan katta")
#     elif son1==son2 :
#         print("sonlar teng")
#     else:
#         print(f"birinchi {son1} soni ikkinchi {son2} sonidan kichik")
        
# max_min_chiqar(67, 67)

# Foydalanuvchidan x va y sonlarini olib, ni konsolga chiqaruvchi funksiya yozing.

# def daraja_chiqar(x,y=2):
#     """ Foydalanuvchidan x va y sonlarini olib, ni konsolga chiqaruvchi funksiya !"""
#     print(f"{x} - ning , {y} - darajasi {x**y}-ga teng")
    

# Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring.

# def bolishni_tek(son):
#     """ Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya"""
#     for alo in range(2,11):
#         if son%alo == 0:
#             print(f"{son} soni qoldiqsiz bo'linuvchi sonlar {alo}")
#             continue
#         else:
#             print(alo)
# bolishni_tek(20)


#  qiymat qaytaruvchi funksiya

# Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)



# def mijoz_info(ism, familiya, tyil, tjoy, email="", tel=None):
#     """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     mijoz = {
#         "ism": ism,
#         "familiya": familiya,
#         "tyil": tyil,
#         "yoshi": 2020 - tyil,
#         "tjoy": tjoy,
#         "email": email,
#         "telefon": tel,
#     }
#     return mijoz

# while True:
#     ism = input("Ismi: ")
#     familiya = input("Familiyasi: ")

# print("Mijoz haqida ma'lumotlarni kiriting.")
# mijozlar = []
#     tyil = int(input("Tug'ilgan yili: "))
#     tjoy = input("Tug'ilgan joyi: ")
#     email = input("Email: ")
#     telefon = input("Telefon raqami: ")
#     mijozlar.append(mijoz_info(ism, familiya, tyil, tjoy, email, telefon))
#     javob = input("Davom etasizmi? (ha/yo'q)")
#     if javob != "ha":
#         break

# print("Mijozlar:")
# for mijoz in mijozlar:
#     print(
#         f"{mijoz['ism'].title()} {mijoz['familiya'].title()},"
#         f"{mijoz['yoshi']} yoshda, telefoni: {mijoz['telefon']}"
#     )

# def max_chiqar(son1,son2,son3):
#     if max(son1, son2, son3):
#         a = max(son1, son2, son3)
#         print(f"sonlarning eng kattasi {a}")
#         return a

    
# max_chiqar(12, -56, 0)

# def kattasi(x, y, z):
#     max = x
#     if y >= max:
#         max = y
#     if z >= max:
#         max = z
#     return max

# kattasi(1,  0, -3)


# def aylana_info (radius):
#     PI= 3.14
#     parametrlar = {
#         "radius ":radius,
#         # "diametri":2*radius,
#         # "yuzasi":PI*radius**2
#         }
#     print(f"aylana radiusi {radius} ,\n"
#           f"aylana diametri {2*radius}, \n"
#           f"aylana yuzi {PI*radius**2}")
#     return parametrlar

# aylana_info(3)


# # a = 123456%10
# # b = 123456//10%10
# # c = 123456//100%10
# # d =%,//
# # d= 123456// 1000%100%10
# # e = 123456%100000//10000
# # print(e)
# #for son in list(range(:6)



# sonlar = list(range(1,11))
# for son in sonlar:
# biror_son = list(range(2,10))
# for soncha in biror_son:
#     sonlar = list(range(1,11))
#     for son in sonlar:
#         a = soncha *son
#         print(f"{soncha} * {son} = {a}")
#     print()


# susu = daraja_chiqar(2*4)
# kuku = mijoz_info('aa','aaa',1999,'ddd','ssaadas')

# print(kuku)
# print()


# def oraliq(min,max,qadam = ""):
#     sonlar = []
#     if qadam:
#         while min < max:
#             sonlar.append(min)
#             min = min + qadam 
#         return sonlar
#     else:
#         while min < max:
#             sonlar.append(min)
#             min = min + 1 
#         return sonlar
        
# print(oraliq(1,10))
# print(oraliq(10,20,2))



# def oraliq(min,max):
#     sonlar = [] # bo'sh ro'yxat
#     while min<max:
#         sonlar.append(min)
#         min += 1
#     return sonlar

# print(oraliq(1,10))
# print(oraliq(10,20))

# Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili 
# va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya yozing.
# Lug'atda foydalanuvchu yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni ixtiyoriy 
# qiling (masalan, tel.raqam, el.manzil)

# def Foydalanuvchidan_mal(ismi,familyasi,t_yil,t_joy,email,tel ,yosh):
#     mal = {
#         'ismi' : ismi,
#         'familyasi':familyasi,
#         "t_yil":t_yil,
#         't_joy':t_joy,
#         "email":email,
#         "tel":tel,
#         "yosh":2023-t_yil
#         }
#     return mal
    
# while True:
#         print("foydalanuvchi ma'lumotlarini kiriting")
#         malumotlar = []
#         ismi = input("Ismi : ")
#         familyasi = input("Familyasi : ")
#         t_yil = int(input("Tug'ulgan yili : "))
#         t_joy = input("Tug'ulgan joyi : ")
#         email = input(" email adress : ")
#         tel  = input("tefon raqami")
#         yosh = 2023 - t_yil
        
#         malumotlar.append(Foydalanuvchidan_mal(ismi, familyasi, t_yil, t_joy, email, tel, yosh))
        
#         javob = input("yana qo'shishni xohlaysizmi , 'yes'/ 'no' \n ")
#         if javob == 'no':
#             break
         
# for malumot in malumotlar:
#     # print(f" {malumotlar[0]['ismi']}") """ bu ham to'gri chiqarish usulidan biri"""
#     print(f" {malumot['ismi']}")

# Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini,
#  perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing


# def aylana_mal(radiusi,diametri,perimetri,yuzi):
#     mal = {
#         'radiusi' : radiusi,
#         'diametri':diametri,
#         "perimetri":perimetri,
#         'yuzi':yuzi,
#         }
#     return mal
    
# while True:
#         pi = 3.14
#         print("aylana radiusini kiriting")
#         malumotlar = []
#         radiusi = float(input("Radiusi : "))
#         diametri = 2*radiusi
#         perimetri =pi*diametri
#         yuzi = pi*radiusi**2

        
#         malumotlar.append(aylana_mal(radiusi,diametri,perimetri,yuzi))
        
#         javob = input("yana qo'shishni xohlaysizmi , 'yes'/ 'no' \n ")
#         if javob == 'no':
#             break
         
# for malumot in malumotlar:
#     # print(f" {malumotlar[0]['ismi']}") """ bu ham to'gri chiqarish usulidan biri"""
#     print(f" {malumot}")



# min = int(input("kichik sonni kiriting \n"))
# max = int(input("katta sonni kiriting \n"))

# def tub_sonlar_top(min, max):
#     tub_sonlar = []
#     for n in range(min, max + 1):
#         tub = True
#         if n == 1:
#             tub = False
#         elif n == 2:
#             tub = True
#         else:
#             for x in range(2, n):
#                 if n % x == 0:
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)

#     return tub_sonlar

# a=tub_sonlar_top(min, max)
# print(a)

# n=int(input("sonni kiriting \n"))
# def fibonachi (n):
#     sonlar = []
#     for x in range(n):
#         if x == 0 or x==1 :
#             sonlar.append(x)
#         else:
#             sonlar.append(sonlar[x-1]+sonlar[x-2])
#     return sonlar

# a=fibonachi(n)
# print(a)


# def katta_harf_yoz(ismlar):
#     yangisi = []
#     while ismlar:
#         ism = ismlar.pop()
#         yangisi.append(f"{ism.title()}")
#     return yangisi

# maydasi = ['ali', 'vali', 'hasan', 'husan']
# yangisi = katta_harf_yoz(maydasi[:])
# eskisi = yangisi.reverse()
# #print(yangisi)
# #print(maydasi)

# def bahola(ismlar):
#     ismlar = ismlar[:]
#     baholar = {}
#     for ism in ismlar:
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting : \n")
#         baholar[ism.title()] = int(baho)
#     return baholar


# ismlar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(ismlar)

# print(baholar)
# print(yangisi)


# def kopaytir(*sonlar):
#     kopaytma = 1 
#     for son in sonlar:
#         kopaytma *=son
#     return kopaytma
# a=kopaytir(4,5,56,7,8)

# print(a)


# def talab_mal(ismi,familyasi,**boshqalar):
#     boshqalar["ismi"] = ismi
#     boshqalar["familyasi"] = familyasi
#     return boshqalar
    
# talaba1 = talab_mal("Ergash", "Baqoyev", yoshi=20,t_joy="Nurota")

# print(talaba1)













