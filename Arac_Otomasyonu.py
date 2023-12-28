def Arac_Ekle():
    try:
        id = 1
        marka = input("Eklemek İstediğiniz Aracın Markası: ")
        model = input("Eklemek İstediğiniz Aracın Modeli: ")
        renk = input("Eklemek İstediğiniz Aracın Rengi: ")
        yil = input("Eklemek İstediğiniz Aracın Çıkış Yılı: ")
        fiyat = input("Eklemek İstediğiniz Aracın Fiyatı: ")

        with open("Araclar.txt", "r", encoding='utf-8') as file:
            araclar = file.readlines()
        if len(araclar) == 0:
            id = 1
        else:
            with open("Araclar.txt", "r", encoding='utf-8') as file:
                id = int(file.readlines()[-1].split("-")[0]) + 1

        with open("Araclar.txt", "a+", encoding='utf-8') as file:
            file.write(f"{id}-{marka},{model},{renk},{yil},{fiyat}\n")
            print('Başarıyla Kaydedilmiştir')
    except FileNotFoundError:
        print("Dosya bulunamadı.")
    except IOError:
        print("Dosya okuma veya yazma hatası.")
    except Exception as e:
        print("Bir hata oluştu:", str(e))

def Arac_Guncelle():
    try:
        with open("Araclar.txt", "r", encoding='utf-8') as file:
            araclar = file.readlines()

        secimid = int(input("Güncellemek istediğiniz aracın ID'sini giriniz: "))
        while secimid < 1 or secimid > len(araclar):
            secimid = int(input("1-{} arasında bir ID giriniz: ".format(len(araclar))))

        # Seçilen aracın bilgilerini ekrana yazdırma
        secilen_arac = araclar[secimid - 1].strip()
        bilgiler = secilen_arac.split(',')
        arac_markasi = []
        arac_markasi = bilgiler[0].split('-')
        print("Seçilen Araç Bilgileri:")
        print("Marka: ", arac_markasi[1])
        print("Model: ", bilgiler[1])
        print("Renk: ", bilgiler[2])
        print("Yıl: ", bilgiler[3])
        print("Fiyat: ", bilgiler[4])

        print("\nAracın hangi özelliğini güncellemek istiyorsunuz:")
        print("1. Tamamını")
        print("2. Modelini")
        print("3. Rengini")
        print("4. Yılını")
        print("5. Fiyatını")
        secim = int(input("Seçiminizi yapınız: "))

        if secim == 1:
            yeni_marka = input("Yeni Marka: ")
            yeni_model = input("Yeni Model: ")
            yeni_renk = input("Yeni Renk: ")
            yeni_yil = input("Yeni Yıl: ")
            yeni_fiyat = input("Yeni Fiyat: ")
            yeni_arac = f"{secimid}-{yeni_marka},{yeni_model},{yeni_renk},{yeni_yil},{yeni_fiyat}\n"
            araclar[secimid - 1] = yeni_arac
        elif secim == 2:
            yeni_model = input("Yeni Model: ")
            bilgiler[1] = yeni_model
            araclar[secimid - 1] = ','.join(bilgiler) + '\n'
        elif secim == 3:
            yeni_renk = input("Yeni Renk: ")
            bilgiler[2] = yeni_renk
            araclar[secimid - 1] = ','.join(bilgiler) + '\n'
        elif secim == 4:
            yeni_yil = input("Yeni Yıl: ")
            bilgiler[3] = yeni_yil
            araclar[secimid - 1] = ','.join(bilgiler) + '\n'
        elif secim == 5:
            yeni_fiyat = input("Yeni Fiyat: ")
            bilgiler[4] = yeni_fiyat
            araclar[secimid - 1] = ','.join(bilgiler) + '\n'
        else:
            print("Geçersiz seçim yapıldı.")

        with open("Araclar.txt", "w", encoding='utf-8') as file:
            file.writelines(araclar)

    except IOError:
        print("Dosya okuma veya yazma hatası.")
    except ValueError:
        print("Hatalı giriş.")
    except IndexError:
        print("Geçersiz ID veya araç kaydı bulunamadı.")


def Arac_Listele():
    try:
        with open("Araclar.txt", "r", encoding='utf-8') as file:
            araclar = file.readlines()

        if len(araclar) == 0:
            print("Kayıtlı araç bulunamadı.")
        else:
            for arac in araclar:
                arac = arac.strip()
                arac_bilgileri = arac.split(',')

                if len(arac_bilgileri) != 2:
                    print(arac)
                    continue

    except FileNotFoundError:
        print("Dosya bulunamadı.")
    except IOError:
        print("Dosya okuma hatası.")


def Arac_Ara():
    try:
        with open("Araclar.txt", "r", encoding='utf-8') as file:
            araclar = file.readlines()

        try:
            print("1- Aracın ID'sine göre")
            print("2- Aracın markasına göre")
            print("3- Aracın rengine göre")
            print("4- Aracın fiyat aralığına göre")
            secim_ara = int(input("Aramak istediğiniz aracın özelliğini seçin: "))
        except ValueError:
            print("Hatalı giriş. Bir tam sayı seçin.")
            return

        while secim_ara < 1 or secim_ara > 5:
            try:
                secim_ara = int(input("1-5 arasında bir sayı giriniz: "))
            except ValueError:
                print("Hatalı giriş. Bir tam sayı seçin.")
                return

        if secim_ara == 1:
            try:
                secimid = int(input("Aramak istediğiniz aracın ID'sini girin: "))
            except ValueError:
                print("Hatalı giriş. Bir tam sayı girin.")
                return

            if secimid < 1 or secimid > len(araclar):
                print("Böyle bir araç bulunamadı.")
                print("Tekrar denemek ister misiniz?")
                secim_tkrr = input("E/H: ").upper()
                if secim_tkrr == 'E':
                    try:
                        secimid = int(input("Aramak istediğiniz aracın ID'sini girin: "))
                    except ValueError:
                        print("Hatalı giriş. Bir tam sayı girin.")
                        return

                    if secimid < 1 or secimid > len(araclar):
                        print("Böyle bir araç bulunamadı.")
                    else:
                        arac = araclar.pop(secimid - 1)
                        print(arac)
            else:
                arac = araclar.pop(secimid - 1)
                print(arac)

        elif secim_ara == 2:
            secim_marka = input("Aramak istediğiniz aracın markasını girin: ")
            bulunan_arac = False

            for arac in araclar:
                if secim_marka in arac:
                    print(arac)
                    bulunan_arac = True

            if not bulunan_arac:
                print("Böyle bir araç bulunamadı.")
                print("Tekrar denemek ister misiniz?")
                secim_tkrr = input("E/H: ").upper()
                if secim_tkrr == 'E':
                    secim_marka = input("Aramak istediğiniz aracın markasını girin: ")
                    bulunan_arac = False

                    for arac in araclar:
                        if secim_marka in arac:
                            print(arac)
                            bulunan_arac = True

                    if not bulunan_arac:
                        print("Böyle bir araç bulunamadı.")

        elif secim_ara == 3:
            secim_renk = input("Aramak istediğiniz aracın rengini girin: ")
            bulunan_arac = False

            for arac in araclar:
                if secim_renk in arac:
                    print(arac)
                    bulunan_arac = True

            if not bulunan_arac:
                print("Böyle bir araç bulunamadı.")
                print("Tekrar denemek ister misiniz?")
                secim_tkrr = input("E/H: ").upper()
                if secim_tkrr == 'E':
                    secim_renk = input("Aramak istediğiniz aracın rengini girin: ")
                    bulunan_arac = False

                    for arac in araclar:
                        if secim_renk in arac:
                            print(arac)
                            bulunan_arac = True

                    if not bulunan_arac:
                        print("Böyle bir araç bulunamadı.")

        elif secim_ara == 4:
            try:
                secim_fiyat_min = float(input("Aramak istediğiniz aracın minimum fiyatını girin: "))
                secim_fiyat_max = float(input("Aramak istediğiniz aracın maksimum fiyatını girin: "))
            except ValueError:
                print("Hatalı giriş. Bir sayı girin.")
                return

            bulunan_arac = False

            for arac in araclar:
                fiyat = float(arac.split("-")[-1].split(",")[-1])
                if secim_fiyat_min <= fiyat <= secim_fiyat_max:
                    print(arac)
                    bulunan_arac = True

            if not bulunan_arac:
                print("Böyle bir araç bulunamadı.")

    except IOError:
        print("Dosya okuma hatası.")


def Arac_Sil():
    try:
        with open("Araclar.txt", "r", encoding='utf-8') as file:
            araclar = file.readlines()

        try:
            secim = int(input("Silmek istediğiniz aracın id'sini giriniz: "))
        except ValueError:
            print("Hatalı giriş. Bir tam sayı girin.")
            return

        while secim < 1 or secim > len(araclar):
            try:
                secim = int(input("1-{} arasında bir sayı giriniz: ".format(len(araclar))))
            except ValueError:
                print("Hatalı giriş. Bir tam sayı girin.")
                return

        araclar.pop(secim - 1)

        sayac = 1
        kalanaraclar = []

        for arac in araclar:
            kalanaraclar.append(str(sayac) + "-" + arac.split("-")[1])
            sayac += 1

        with open("Araclar.txt", "w", encoding='utf-8') as file:
            file.writelines(kalanaraclar)

    except IOError:
        print("Dosya okuma hatası.")


def Kazanc_Hesapla():
    try:
        aracBilgi = []
        aracFiyati = []

        with open("Satilanlar.txt", "r", encoding='utf-8') as file:
            for satir in file:
                satir = satir.strip()
                liste = satir.split(',')
                if len(liste) > 1:
                    aracBilgi.append(liste[0])
                    aracFiyati.append(int(liste[4]))

        hizmetBilgi = []
        hizmetFiyati = []

        with open("Alinan_Hizmetler.txt", "r", encoding='utf-8') as file:
            for satir in file:
                satir = satir.strip()
                liste2 = satir.split(':')
                if len(liste2) > 1:
                    hizmetBilgi.append(liste2[0])
                    hizmetFiyati.append(int(liste2[1]))

        toplam1 = sum(aracFiyati)
        toplam2 = sum(hizmetFiyati)

        toplam3 = toplam1 + toplam2

        print('Kazancınız:', toplam3)

    except FileNotFoundError:
        print("Dosya bulunamadı.")
    except IOError:
        print("Dosya okuma hatası.")
    except IndexError:
        print("Geçersiz dosya formatı. İndeks hatası.")
    except ValueError:
        print("Geçersiz değer bulundu. Kazanç hesaplanamadı.")

def Arac_Sat():
    try:
        with open("Araclar.txt", "r", encoding='utf-8') as file:
            araclar = file.readlines()

        secim = int(input("Satmak istediğiniz aracın ID'sini giriniz: "))
        while secim < 1 or secim > len(araclar):
            secim = int(input("1-{} arasında bir sayı giriniz: ".format(len(araclar))))

        arac = araclar[secim - 1]
        fiyat = float(arac.split(",")[4])

        taksit_secimi = input("Aracı tek çekim mi yoksa taksitle mi satmak istersiniz? (T/Tek Çekim, K/Taksit): ")
        while taksit_secimi not in ['T', 'K']:
            taksit_secimi = input("Geçerli bir seçenek giriniz (T/Tek Çekim, K/Taksit): ")

        if taksit_secimi == 'T':
            satilan_arac = araclar.pop(secim - 1)
            sayac = 1
            kalan_araclar = []

            for arac in araclar:
                kalan_araclar.append(str(sayac) + "-" + arac.split("-")[1])
                sayac += 1

            with open("Araclar.txt", "w", encoding='utf-8') as file:
                file.writelines(kalan_araclar)

            with open("Satilanlar.txt", "a+", encoding='utf-8') as file:
                file.write(satilan_arac.split("-")[1])

            print("Aracı tek çekim ile satın aldınız.")

        elif taksit_secimi == 'K':
            def Odeme_Plani(fiyat):
                aracFiyatlari = {
                    '0-100000': {
                        '12 Ay Taksit': '1639',
                        '24 Ay Taksit': '2263',
                        '36 Ay Taksit': '4170'
                    },
                    '100001-200000': {
                        '12 Ay Taksit': '3278',
                        '24 Ay Taksit': '4526',
                        '36 Ay Taksit': '8341'
                    },
                    '200001-300000': {
                        '12 Ay Taksit': '4918',
                        '24 Ay Taksit': '6789',
                        '36 Ay Taksit': '12511'
                    },
                    '300001-400000': {
                        '12 Ay Taksit': '6557',
                        '24 Ay Taksit': '9052',
                        '36 Ay Taksit': '16682'
                    },
                    '240001-500000': {
                        '12 Ay Taksit': '8195',
                        '24 Ay Taksit': '11315',
                        '36 Ay Taksit': '20852'
                    },
                    '500001-600000': {
                        '12 Ay Taksit': '9834',
                        '24 Ay Taksit': '13579',
                        '36 Ay Taksit': '25023'
                    },
                    '600001-700000': {
                        '12 Ay Taksit': '11473',
                        '24 Ay Taksit': '15843',
                        '36 Ay Taksit': '29193'
                    }
                }

                for aralik, taksitler in aracFiyatlari.items():
                    aralik_baslangic, aralik_son = map(int, aralik.split('-'))
                    if aralik_baslangic <= fiyat <= aralik_son:
                        print(f"Taksit Seçenekleri (Fiyat Aralığı: {aralik})")
                        for taksit, taksit_miktari in taksitler.items():
                            print(f"{taksit}: {taksit_miktari}")

                        taksit_secimi = input(
                            "Ödeme yapmak istediğiniz taksit seçeneğini giriniz (Örneğin '12 Ay Taksit'): ")
                        while taksit_secimi not in taksitler.keys():
                            taksit_secimi = input("Geçerli bir taksit seçeneği giriniz: ")

                        taksit_tutari = int(taksitler[taksit_secimi].split(' ')[0])
                        toplam_tutar = fiyat + taksit_tutari

                        satilan_arac = araclar.pop(secim - 1)

                        satilan_arac_id_markasi = []
                        satilan_arac_markasi = []
                        satilan_arac_modeli = []
                        satilan_arac_rengi = []
                        satilan_arac_yili = []
                        satilan_arac_fiyati = []

                        liste = satilan_arac.split(',')
                        if len(liste) > 1:
                            satilan_arac_id_markasi = liste[0]
                            satilan_arac_modeli = liste[1]
                            satilan_arac_rengi = liste[2]
                            satilan_arac_yili = liste[3]
                            satilan_arac_fiyati.append(int(liste[4]))

                        satilan_arac_markasi = satilan_arac_id_markasi.split('-')

                        satilan_arac_fiyati = int(toplam_tutar)

                        sayac = 1
                        kalan_araclar = []

                        satilan_arac = str(satilan_arac_markasi[1]) + ',' + str(satilan_arac_modeli) + ',' + str(
                            satilan_arac_rengi) + ',' + str(satilan_arac_yili) + ',' + str(satilan_arac_fiyati)

                        for arac in araclar:
                            kalan_araclar.append(str(sayac) + "-" + arac.split("-")[1])
                            sayac += 1

                        with open("Araclar.txt", "w", encoding='utf-8') as file:
                            file.writelines(kalan_araclar)

                        with open("Satilanlar.txt", "a+", encoding='utf-8') as file:
                            file.write(satilan_arac + "\n")

                        print(f"Aracı {taksit_secimi} seçeneğiyle taksitle satın aldınız.")
                        print(f"Toplam Tutar: {toplam_tutar} TL")
                        break
                else:
                    print("Taksit seçenekleri bulunamadı.")

            Odeme_Plani(fiyat)


    except IOError:
        print("Dosya okuma veya yazma hatası.")
    except ValueError:
        print("Geçersiz değer bulundu. Satış gerçekleştirilemedi.")
    except Exception as e:
        print("Beklenmeyen bir hata oluştu:", str(e))


def Hizmetlerden_Faydalan():
    #Bu sene ekledim
    try:
        with open("Hizmetler.txt", "r", encoding='utf-8') as file:
            hizmetler = file.readlines()

        print("Faydalanmak istediğiniz hizmetin ID numarasını tuşlayınız lütfen!")
        print("1-Araç içi temizlik kiti: 500 TL")
        print("2-Yedek lastik: 1000 TL")
        print("3-1 yıllık araç bakım: 5000 TL")
        print("4-İlk 3 ay iç dış temizlik hizmeti: 500 TL")
        print("5-Far temizleme hizmeti: 300 TL")
        print("6-Koltuk koruma hizmeti: 800 TL")
        print("7-Boya koruma hizmeti: 1500 TL")
        print("8-Cam filmi uygulaması: 1200 TL")
        print("9-Lastik koruma hizmeti: 600 TL")
        print("10-Kaput koruma hizmeti: 2000 TL")

        secim_hizmet = int(input("Seçiminiz: "))
        while secim_hizmet < 1 or secim_hizmet > len(hizmetler):
            secim_hizmet = int(input("1-{} arasında bir sayı giriniz: ".format(len(hizmetler))))

        satin_alinan_hizmet = hizmetler[secim_hizmet - 1]

        with open("Alinan_Hizmetler.txt", "a+", encoding='utf-8') as file:
            file.write(satin_alinan_hizmet.split("-")[1])

        devam_et = input("Başka bir hizmetten yararlanmak ister misiniz? (Evet/Hayır): ")
        while devam_et.lower() != "evet" and devam_et.lower() != "hayır":
            devam_et = input("Geçerli bir yanıt giriniz (Evet/Hayır): ")

        if devam_et.lower() == "evet":
            Hizmetlerden_Faydalan()

    except IOError:
        print("Dosya okuma veya yazma hatası oluştu.")
    except ValueError:
        print("Geçersiz bir seçim yapıldı. Lütfen doğru bir sayı giriniz.")

def menu():
    while True:
        try:
            print("\n<----- Galerimize Hoşgeldiniz ----->")
            print("1- Araç Ekle")
            print("2- Araç Listele")
            print("3- Araç Güncelle")
            print("4- Araç Ara")
            print("5- Araç Sil")
            print("6- Araç Sat")
            print("7- Hizmetlerden Faydalan")
            print("8- Kazanç Hesapla")
            print("9- Ana Menü")
            print("10- Çıkış")

            secim = int(input("Seçiminiz: "))
            while secim < 1 or secim > 10:
                secim = int(input("1-10 arasında bir sayı giriniz: "))

            if secim == 1:
                Arac_Ekle()
            elif secim == 2:
                Arac_Listele()
            elif secim == 3:
                Arac_Guncelle()
            elif secim == 4:
                Arac_Ara()
            elif secim == 5:
                Arac_Sil()
            elif secim == 6:
                Arac_Sat()
            elif secim == 7:
                Hizmetlerden_Faydalan()
            elif secim == 8:
                Kazanc_Hesapla()
            elif secim == 9:
                continue  # Ana menüye dön
            elif secim == 10:
                print("Çıkış Yapılmıştır!")
                break
            else:
                print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")

        except ValueError:
            print("Geçersiz bir değer girdiniz. Lütfen bir sayı girin.")
        except Exception as e:
            print("Beklenmeyen bir hata oluştu:", str(e))

menu()
