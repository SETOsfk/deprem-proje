#DİLEK KUTUSU
#Sertan ŞAFAK 201003029
#Algoritma ve Programlama II Dönem Ödevi



import pandas as pd

kullanici={}
admin={}
kullanici_adi=""
secim=0
istekler={}

istek={}
urunler_df=pd.read_csv('Urunler.csv',sep=";")

while(True):

    print("""
          1-Sisteme Üye Ol

          2-Sisteme Giriş Yap

          3-Şifremi Unuttum
          
          4-Çıkış yap\n""")
    secim=int(input("Lütfen seçim yapınız...\n"))
    
    
    if(secim==1):
        print(""" 
              1-Admin üyeliği
              2-Kullanıcı üyeliği
              """
              )
        secim=int(input("Lütfen seçim yapınız\n"))
        if(secim==1):
            kullanici_adi=input("Kullanıcı adınızı giriniz:\n")
            
            sifre=input("Şifrenizi oluşturun\n")
            admin.setdefault(kullanici_adi,sifre)
            
            
        elif(secim==2):
            kullanici_adi=input("Kullanıcı adınızı giriniz:\n")
            
            sifre=input("Şifrenizi oluşturun:\n")
            kullanici.setdefault(kullanici_adi,sifre)
        else:
            print("Yanlış tuşlama yaptınız.\n")
            break
            
            
    
    
    elif(secim==2):
        print("""
              1-Admin girişi
              2-Kullanıcı girişi
              """)
        secim=int(input("Lütfen seçim yapınız...\n"))
        if secim==1:
            kullanici_adi=input("Kullanıcı adınızı giriniz\n")
            if kullanici_adi not in admin:
              print("Böyle bir kullanıcı yok, tekrar deneyiniz\n")
              break
             
          
          
          
          
          
            else:
              #ADMİN MENÜSÜ BURADADIR
              sifre=input("Şifre:")
              if admin[kullanici_adi]==sifre:
                  print("Başarıyla giriş yaptınız...\n")
                  print("""
                        1-İstekleri kontrol et
                        2-Ürünleri kontrol et
                        3-Ürün girişi yap
                        4-Çıkış yap
                        """)
                  secim_admin=int(input("Lütfen seçim yapınız....\n"))
                  if (secim_admin==4):
                      break
                  elif(secim_admin==1):
                      istekler.keys()
                      secim_istek=input("İsteğini kontrol etmek istediğiniz kullanıcı adını giriniz\n")
                      print("{} isimli kullanıcı {} kategorisinden {} istemiştir".format(secim_istek,istekler[secim_istek],istekler.values()))
                      urun_onay=input("Gönderimi onaylıyor musunuz?\n evet/hayır")
                      if(urun_onay=="evet"):
                      
                    #ADMİN MENÜSÜNDEN İSTEĞE BAĞLI ÜRÜN İHTİYACI GÖNDERİP, STOK GÜNCELLEME
                          print("""
                                1-Temel Gıda
                                2-Tekstil
                                3-Sağlık
                                4-Ekstra 
                                """)
                          kategori=int(input("Lütfen kategorinizi belirtin\n"))
                          adet=int(input("Ürün adetini belirtiniz"))
                          if(kategori==1):
                              urunler_df.loc[0,'adet']+=-adet
                              print("Ürün stoğu başarıyla güncellenmiştir.")
                              print(urunler_df)
                          elif(kategori==2):
                              urunler_df.loc[1,'adet']+=-adet
                              print("Ürün stoğu başarıyla güncellenmiştir.")
                              print(urunler_df)
                          elif(kategori==2):
                              urunler_df.loc[2,'adet']+=-adet
                              print("Ürün stoğu başarıyla güncellenmiştir.")
                              print(urunler_df)
                          elif(kategori==2):
                              urunler_df.loc[3,'adet']+=-adet
                              print("Ürün stoğu başarıyla güncellenmiştir.")
                              print(urunler_df)
                      elif(urun_onay=="hayır"):
                            print("Ürün gönderilemiyor...")
                            continue
                          

                            
                  elif(secim_admin==2):
                    
                    print(urunler_df)
                    continue
                  elif(secim_admin==3):
                     
                    #ADMİN MENÜSÜNDEN ÜRÜN STOĞU GÜNCELLEME
                     print("""
                           1-Temel Gıda
                           2-Tekstil
                           3-Sağlık
                           4-Ekstra
                           """)
                     kategori=int(input("Lütfen kategorinizi belirtin\n"))
                     adet=int(input("Ürün adetini belirtiniz"))
                     if(kategori==1):
                         urunler_df.loc[0,'adet']+=adet
                         print("Ürün stoğu başarıyla güncellenmiştir.")
                         print(urunler_df)
                     elif(kategori==2):
                         urunler_df.loc[1,'adet']+=adet
                         print("Ürün stoğu başarıyla güncellenmiştir.")
                         print(urunler_df)
                     elif(kategori==2):
                         urunler_df.loc[2,'adet']+=adet
                         print("Ürün stoğu başarıyla güncellenmiştir.")
                         print(urunler_df)
                     elif(kategori==2):
                         urunler_df.loc[3,'adet']+=adet
                         print("Ürün stoğu başarıyla güncellenmiştir.")
                         print(urunler_df)
   
                  
                  
        else:
            kullanici_adi=input("Kullanıcı adınızı giriniz\n")
            if kullanici_adi not in kullanici:
              print("Böyle bir kullanıcı yok, tekrar deneyiniz\n")
              break

            else:
              #KULLANICI MENÜSÜ BURADADIR
              sifre=input("Şifre:")
              if kullanici[kullanici_adi]==sifre:
                  print("Başarıyla giriş yaptınız...\n")
                  print("""
                        1-İstek oluştur
                        2-Çıkış yap
                        """)
                  secim=int(input("Lütfen seçim yapınız\n"))
                  if secim==2:
                      print("Çıkış yapılıyor...")
                      break
                  elif(secim==1):
                      print("""
                            1-Temel Gıda
                            2-Tekstil
                            3-Sağlık
                            4-Ekstra
                            """)
                      kategori=input("Lütfen kategorinizi belirtin\n")
                      #Ekstra kategorisi yukarıdaki kategorilerde olmayan şeyler için vardır.
                      #Örneğin; bilgisayarı hasar görmüş öğrenci bilgisayar ihtiyacını buradan giderebilir vb.

                      istek_cevap=input("Lütfen isteğinizi giriniz...\n")
                      istek.setdefault(kategori,istek_cevap)
                      istekler.setdefault(kullanici_adi,istek)
                      print("İstediğiniz başarılıyla oluşturulmuştur.\n")
                      cevap=input("Başka bir işlem yapmak ister misiniz?(evet/hayır)").lower()
                      if cevap=="hayır":
                          break
                      elif cevap=="evet":
                          continue
  
    elif(secim==3):
        kullanici_adi=input("Lütfen kullanıcı adınızı giriniz...\n")
        if kullanici_adi in kullanici:
            yeni_sifre=input("Yeni şifrenizi giriniz:")
            kullanici[kullanici_adi]=yeni_sifre
            print("Şifreniz sıfırlandı...")
        else:
            print("Kullanıcı adınızı yanlış girdiniz, lütefen kayıt olun.")
            break
            
            
        
    elif(secim==4):
        print("Çıkış yapılıyor...")
        break
              

