# ism = "kumushoy"
# familiya = "raximberdiyeva"
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif.upper())
# print(ism_sharif.lower())
# print(ism_sharif.title())
# print(ism_sharif.capitalize())
# print('zafarovna'.title())

# name = input("Ismingiz nima?\n>>>")
# print("Assalomu alaykum, " + name + "!")

# kocha = "Bog'bon"
# mahalla = "Sog'bon"
# tuman = "Bodomzor"
# viloyat = "Samarqand"

# print("Iltimos, quyidagi ma'lumotlarni kiriting: \n")
# kocha = input("Ko'changiz: \n>>>")
# mahalla = input("Mahallangiz: \n>>>")
# tuman = input("Tumaningiz: \n>>>")
# viloyat = input("Viloyatingiz: \n>>>")
# print(kocha + " ko'chasi, " + mahalla + " mahallasi, " +
#       tuman + " tumani, " + viloyat + " viloyati")
# print(kocha + " ko'chasi,\n" + mahalla + " mahallasi,\n" +
#       tuman + " tumani,\n" + viloyat + " viloyati")
# manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
# print(manzil)

# aholi_soni = 8_000_000_000
# print("Yer yuzida", aholi_soni, " ga yaqin odam yashaydi")

# ism = "Jobir"
# yosh = 36
# xabar = ism + ' ' + str(yosh) + ' yoshda'
# print(xabar)
# print(type(yosh))
# str()— int yoki float turidagi sonlarni matnga o'zgartiradi.
# int()— matn yoki float ko'rinishidagi qiymatlarni butun songa o'zgartiradi. Bunda matn butun son ko'rinishida bo'lishi kerak.
# float()— matn yoki int ko'rinishidagi qiymatlarni o'nlik songa o'zgartiradi.

# 1 Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur____________________________________________

# son = int(input("Istalgan sonni kiriting: \n>>>"))
# kvadrat = son**2
# kub = son**3
# print(son, ' ning kvadrati ', kvadrat, ' ga teng')
# print(son, ' ning kubi ', kub, ' ga teng')

# 2 Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, konsolga chiqaruvchi dastur_______________________

# yosh = int(input("Yoshingiz nechida? \n>>>"))
# t_yili = 2025 - yosh
# print('Siz ', t_yili, " da tug'ilgansiz")

# 3 Foydalanuvchidan ikki son kiritshni so'rab, kiritilgan sonlarning yig'indisi, ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur____________________________________________

# a = int(input('Birinchi sonni kiriting: >>> '))
# b = int(input('Ikkinchi sonni kiriting: >>> '))
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

# ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting

# ismlar = ['Malika', 'Mubina', 'Nastarin']
# # print('Salom', ismlar[0] + ',', 'bugun choyxonaga boramizmi?')
# # print('Salom', ismlar[1] + ',', 'bugun choyxonga boramizmi?')
# # print('Salom', ismlar[2] + ',', 'choyxonaga boramizmi?')

# print("Salom " + ismlar[0] + " ishlaring yaxshimi?")
# print(f"{ismlar[0]} va {ismlar[1]} egizaklar")
# print(ismlar[-1] + " sani yaxshi ko'raman)")

# sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).

# sonlar = [22, -58.2, 34.0, 67, 1983, 123_456_678_000, 112.4]
# Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring.
# sonlar[0] = sonlar[0] + sonlar[-1]
# sonlar[1] = 65.2
# sonlar[4] = sonlar[4] + 14
# del sonlar[5]
# print(sonlar)

# t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.

# t_shaxslar = ['Navoiy', 'Amir Temur', 'Mirzo Ulugbek']
# z_shaxslar = ['Otam', 'Onam', 'Bill Gates']
# print(
#     f"\n Men tarixiy shaxslardan {t_shaxslar.pop(1)} bilan, zamonaviy shaxslardan esa {z_shaxslar.pop(2)} bilan suhbatlashishni istar edim.")
# print(t_shaxslar)

# friends = []
# friends.append('Nastarin')
# friends.append('Muhammad')
# friends.append('Asadbek')
# friends.append('Malika')
# friends.append('Mubina')
# friends.remove('Mubina')
# friends.remove('Malika')
# friends.append('Begzod')
# friends.insert(0, 'Abdulloh')
# friends.insert(3, 'Muhammadnabi')


# mehmonlar = []
# mehmonlar.append(friends.pop(0))
# mehmonlar.append(friends.pop(-1))
# mehmonlar.append(friends.pop(1))
# mehmonlar.append(friends.pop(2))

# print(mehmonlar)
# cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# cars.sort(reverse=True)
# print(cars)
# mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
# mehmonlar.reverse()
# print(mehmonlar)
# sonlar = list(range(1, 10, 2))
# print(sonlar)

# davlatlar = ['Korea', 'Arabiston', 'Fransiya', 'Rossiya',
#              'Amerika', 'Buyuk Britaniya', 'Italiya', 'Germaniya', 'Hindiston']

# # davlatlar.sort(reverse=True)
# print(davlatlar)
# sonlar = list(range(120, 1201, 2))
# # print(sonlar[:20])
# # print(sonlar[-20:])
# print(sonlar[530:550])

# taomlar = ['osh', 'manti', 'dimlama', 'kabob', 'somsa']
# nonushta = taomlar[:]
# nonushta.remove('osh')
# nonushta.remove('dimlama')
# nonushta.remove('manti')
# nonushta.remove('kabob')
# nonushta.remove('somsa')
# nonushta.append('quymoq')
# nonushta.append('tuxum')
# nonushta.append('tvorog')
# nonushta = tuple(nonushta)

# nonushta = list(nonushta)
# nonushta[0] = 'qaymoq va non'
# nonushta = tuple(nonushta)
# print(type(nonushta))
# print(nonushta)
# print(taomlar)

# ismlar = ['Kumush', 'Muhammad', 'Nastarin', 'Asadbek']
# n = 0
# for ism in ismlar:
#     print('Salom ' + ism)
#     n += 1
# print(f"Kod {n} marta takrorlandi")
# print(f"Kod {len(ismlar)} marta takrorlandi")

# toq_sonlar = list(range(11, 101, 2))

# sonlar_kubi = []
# for son in toq_sonlar:
#     sonlar_kubi.append(son**3)

# print(toq_sonlar)
# print(sonlar_kubi)

# kinolar = []
# print("5 ta yoqtirgan kinofilmingiz qaysilar? ")
# for kino in range(5):
#     kinolar.append(input(f"{kino+1} kinoyingizni kiriting >>>>> "))
# print(kinolar)

# odamlar = int(input("Bugun nechta odam bilan suhbatlashdingiz? "))
# ismlar = []
# for ism in range(odamlar):
#     ismlar.append(input(f"{ism+1} - suhbat qilgan insoningiz kim edi? "))
# print(ismlar)
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car != 'gm':
#         print(car.title())
#     else:
#         print(car.upper())

# login = input("Hurmatli mijoz, ismingizni kiriting: ")
# if login.lower() == 'admin':
#     print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz, {login} ")

# print("Hurmatli mijoz, 2ta son kiriting: ")
# son1 = int(input('1 - son >>>> '))
# son2 = int(input('2 - son >>>> '))
# if son1 == son2:
#     print("Sonlar teng ekan")
# else:
#     print("Rahmat")

# son = int(input('Istalgan sonni kiriting: '))
# if son > 0:
#     print("Musbat son")
# else:
#     print("Manfiy son")

# son = int(input('Son kiriting: '))
# if son > 0:
#     ildiz = pow(son, 0.5)
#     print(ildiz)
# if son < 0:
#     print('Musbat son kiriting!')

# Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.

# son = int(input("Hurmatli mijoz, juft son kiriting >>>  "))
# if son % 2 == 0:
#     print("Rahmat!")
# else:
#     print("Bu juft son emas")

# Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
# Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
# Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
# Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
# yosh = int(input('Yoshingiz nechida? >>> '))
# if yosh <= 4 or yosh >= 60:
#     narx = 0
# elif yosh <= 18:
#     narx = 10000
# elif yosh > 18:
#     narx = 20000
# print(f"Siz uchun muzeyga kirish uchun chipta narxi {narx} so'm")


# Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring
# son1 = float(input('Birinchi sonni kiriting: >>> '))
# son2 = float(input('Ikkinchi sonni kiriting: >>>'))
# if son1 > son2:
#     print(f"{son1} > {son2}")
# elif son1 < son2:
#     print(f"{son2} < {son1}")
# else:
#     print(f"{son1} = {son2}")


# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
# mahsulotlar = ['olma', 'banan', 'yogurt', 'malako', 'gilos',
#                'pichina', 'moxito', 'qand', 'chupa-chups', 'non']
# savat = []
# for mahsulot in range(5):
#     savat.append(input(f"Savatga {mahsulot+1} - mahsulotni qo'shing: "))
# print(savat)

# for buyurtma in savat:
#     if buyurtma in mahsulotlar:
#         print(f"Do'konimizda {buyurtma} bor")
#     else:
#         print(f"Do'konimizda {buyurtma} yo'q")


# Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.  Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.

# mahsulotlar = ['olma', 'banan', 'yogurt', 'malako', 'gilos',
#                'pichina', 'moxito', 'qand', 'chupa-chups', 'non']
# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1} - mahsulotni qo'shing: "))
# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#     print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

# foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.
# foydalanuvchilar = ['Kumush', 'Kumushoy',
#                     'KUMUSH', 'Kumushoy0705, K_zafarovna']
# yangi_login = input('Yangi login tanlang: >>> ')
# if yangi_login in foydalanuvchilar:
#     print('Login band, yangi login tanlang!')
# else:
#     print("Xush kelibsiz, foydalanuvchi!")

# Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.

# son = int(input('Biror butun son kiriting: >>> '))
# for n in range(2, 11):
#     if not son % n:
#         print(f"Son {n} ga qoldiqsiz bo'linadi")
# kunlik_vaqt = int(input("Kuniga necha daqiqa o‘qiysiz? >>> "))
# umumiy_vaqt = 7 * 800
# kunlar_soni = umumiy_vaqt / kunlik_vaqt
# print(f"Siz barcha bo‘limni {kunlar_soni:.1f} kunda tugatasiz.")
# daqiqalar = int(input("Daqiqani kiriting: >>> "))

# soat = daqiqalar // 60         # Butun soatlarni hisoblaydi
# qolgan_daqiqa = daqiqalar % 60  # Qolgan daqiqani hisoblaydi

# print(f"{daqiqalar} daqiqa = {soat} soat {qolgan_daqiqa} daqiqa")

