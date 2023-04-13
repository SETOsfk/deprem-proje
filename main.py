


#program çalışmayı durdurduğunda
#bütün kayıtlı liste öğeleri siliniyor
#her kullanıcı tekrar üye olmak zorunda kalıyor
#nasıl çözeceğimi bulamadım


kullanici=[]
admin=[]
kullanici_sifre=[]
admin_sifre=[]
kullanici_adi=""
secim=0

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
            admin.append(kullanici_adi)
            sifre=input("Şifrenizi oluşturun\n")
            admin_sifre.append(sifre)
            
            
        elif(secim==2):
            kullanici_adi=input("Kullanıcı adınızı giriniz:\n")
            kullanici.append(kullanici_adi)
            sifre=input("Şifrenizi oluşturun:\n")
            kullanici_sifre.append(sifre)
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
              
              sifre=input("Şifre:")
              if admin.index(kullanici_adi)==admin_sifre.index(sifre):
                  print("Başarıyla giriş yaptınız...\n")
                  #admin menüsü özelllikleri
        else:
            kullanici_adi=input("Kullanıcı adınızı giriniz\n")
            if kullanici_adi not in kullanici:
              print("Böyle bir kullanıcı yok, tekrar deneyiniz\n")
              break

            else:
              print("Kullanıcı  adınızı yanlış girdiniz, lütfen tekrar deneyiniz\n")
              sifre=input("Şifre:")
              if kullanici[kullanici_adi]==sifre:
                  print("Başarıyla giriş yaptınız...\n")
                  #kullanıcı menüsü özelllikleri
            
     
         
              
    
                  
                
                  
                 
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
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
              

