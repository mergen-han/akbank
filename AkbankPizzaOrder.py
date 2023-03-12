# -*- coding: utf-8 -*-
"""AkbankPizzaOrder.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E6mg5Wgi-EQhTwZcyASTlnos-ULxbwtn
"""

#Kullanılacak Kütüphanelerin Dahil Edilmesi
import csv
from datetime import datetime 


#pizza sinıfı
class Pizza:    

    def __init__(self, description, cost): 
        self.description = description     
        self.cost = cost 

    def get_description(self):
        return self.description 

    def get_cost(self):
        return self.cost 

#alt pizza sınıfları
class KlasikPizza(Pizza):

    def __init__(self):
        super().__init__("Klasik Pizza", 119.90)

class MargheritaPizza(Pizza):

    def __init__(self):
        super().__init__("Margherita Pizza", 106.90)

class KopernikPizza(Pizza):
    
    def __init__(self):
        super().__init__("Kopernik Pizza", 149.90)

class BolBolPizza(Pizza):
    
    def __init__(self):
        super().__init__("Bol Bol Pizza", 99.90)

#dekoratör sınıfı
class Decorator(Pizza):

    def __init__(self, component, description, cost):
        self.component = component
        self.description = description
        self.cost = cost

    def get_description(self):
        return self.component.get_description() + " ve " + self.description

    def get_cost(self):
        return self.component.get_cost() + self.cost

    def get_soscost(self):
        return self.cost
    
    def get_sosdescription(self):
        return self.description

#dekor için alt pizza sınıfları
class Sosistemiyorum(Decorator):
    
    def __init__(self, component):
        super().__init__(component, "Sos İstemiyorum", 0.00)

class Mantar(Decorator):

    def __init__(self, component):
        super().__init__(component, "Mantar", 4.90)

class Peynir(Decorator):
        
    def __init__(self, component):
        super().__init__(component, "Peynir", 12.90)

class Zeytin(Decorator):

    def __init__(self, component):
        super().__init__(component, "Zeytin", 14.90)

class Sogan(Decorator):
        
    def __init__(self, component):
        super().__init__(component, "Soğan", 4.90)    

class Misir(Decorator):

    def __init__(self, component):
        super().__init__(component, "Mısır", 4.90)


def isValidID(id_number):
    id_number = str(id_number) #converting the id number to string

    if not len(id_number) == 11: #checking if the id number is 11 digits 
        return False
    
    if not id_number.isdigit(): #checking if the id number containing only digits
        return False

    if int(id_number[0]) == 0: #checking if the id number starts with 0
        return False
    
    digits = [int(x) for x in id_number] #converting the id number to a list of digits	

    if not sum(digits[:10]) % 10 == digits[10]: #checking if the 
        return False
    
    if not (((7 * sum(digits[:9][-1::-2])) - sum(digits[:9][-2::-2])) % 10) == digits[9]: #
        return False

    return True
#TC kontrol
def CheckTC(tc):
    tc_str = str(tc)
    
    if len(tc_str) != 11 or not tc_str.isdigit() or tc_str[0] == '0':
        return False
        
    tc_list = [int(i) for i in tc_str]
    
    if sum(tc_list[:10]) % 10 != tc_list[10]:
        return False
        
    if (sum(tc_list[:9:2]) * 7 - sum(tc_list[1:9:2])) % 10 != tc_list[9]:
        return False
        
    return True

#kredi kart numara kontrol Luhn Algoritması
def CheckKrediKart(kredi_kart_numara):
  kredi_kart_numara = kredi_kart_numara.replace(" ", "")
  if not kredi_kart_numara.isdigit():
    return False
        
  digits = list(map(int, kredi_kart_numara)) 
  for i in range(len(digits) - 2, -1, -2):
    digits[i] *= 2
    if digits[i] > 9:
      digits[i] -= 9
  return sum(digits) % 10 == 0


#main fonksiyonu
def main():
    #menu.txt
    file = open("menu.txt", "w") 

    pizza_menu = """
  -----------------------------------------------
  |                 PIZZA MENU                  |
  |                                             |                       
  |         Lütfen Bir Pizza Tabanı Seçin:      |
  |          ------------------------           |
  |          1. Klasik Pizza 119.90 ₺           |
  |          2. Margherita Pizza 106.90 ₺       |
  |          3. Kopernik Pizza 149.90 ₺         |
  |          4. Bol Bol Pizza 99.90 ₺           |
  |                                             |
  |                                             |
  |         Lütfen Bir Sos Tercihi Yapın:       |
  |           ------------------------          |
  |            11. Sos İstemiyorum 0.0 ₺        |
  |            12. Mantar +4.90 ₺               |    
  |            13. Peynir +12.90 ₺              |
  |            14. Zeytin +14.90 ₺              |
  |            15. Soğan +4.90 ₺                |
  |            16. Mısır +4.90 ₺                |
  |                                             |
  |              * Teşekkürler!                 |
  -----------------------------------------------
  """



    file.write(pizza_menu) 
    file.close()
     
    #Menüyü ekrana bas
    print(pizza_menu)

    
    #pizza tabanı bilgisinin alınması
    while(True):
        pizza_taban = input("Lütfen Seçtiğiniz Pizza Tabanı Numarasını Girin: ") 
        if pizza_taban == "1":
            pizza = KlasikPizza() 
            break
        elif pizza_taban == "2":
            pizza = MargheritaPizza()
            break
        elif pizza_taban == "3":
            pizza = KopernikPizza()
            break
        elif pizza_taban == "4":
            pizza = BolBolPizza()
            break
        else:
            print("Geçersiz seçim yaptınız!\nLütfen Sadece Seçmek İstediğiniz Pizza Tabanı Numarasını Tuşlayın")
    #seçilen pizzanın tutulması
    secilenpizza = pizza 	

    #pizza sosu bilgisinin alınması
    while(True):
        sauce_type = input("Lütfen seçtiğiniz sos numarasını girin: ")
        if sauce_type == "11":
            pizza = Sosistemiyorum(pizza)
            break
        elif sauce_type == "12":
            pizza = Mantar(pizza)
            break
        elif sauce_type == "13":
            pizza = Peynir(pizza)
            break
        elif sauce_type == "14":
            pizza = Zeytin(pizza)
            break
        elif sauce_type == "15":
            pizza = Sogan(pizza)
            break
        elif sauce_type == "16":
            pizza = Misir(pizza)
            break
        else:
            print("Geçersiz seçim yaptınız!")
    
    #isim bilgisinin alınması
    isim = input("İsminizi Giriniz: ") 
    
    #kimlik numarası bilgisinin alınması
    tc = input("Kimlik Numaranızı Giriniz: ")
    
    #geçerli bir kimlik numarası girildiğinin kontrolü
    while(True):
        if CheckTC(tc): 
            break
        else:
            print("Geçersiz Kimlik Numarası Girdiniz!")
            tc = input("Lütfen Kimlik Numaranızı Girin: ")
    
    #kullanıcıya sipariş özeti bilgisinin verilmesi
    print("\nSipariş Özetiniz:") 
    print(secilenpizza.get_description() + " " + f"{secilenpizza.get_cost():.2f} ₺") 
    print(pizza.get_sosdescription() + " " + f"{pizza.get_soscost():.2f} ₺") 
    print("----------------------------------")
    print("Toplam Tutar: " + f"{pizza.get_cost():.2f} ₺") 

    #Ödeme Ekranı
    print("\n              ÖDEME EKRANI")

    #kredi kart numarası bilgisinin alınması
    kredi_kart_numara = input("\nSiparişinizi Tamamlamak İçin Kredi Kartı Numaranızı Giriniz: ") 
    
    #kredi kart numarası geçerlilik kontrol edilmesi
    while(True):
        if CheckKrediKart(kredi_kart_numara): 
            break
        else:
            print("Geçersiz Kredi Kartı Bilgisi Girdiniz!")
            kredi_kart_numara = input("Lütfen Kredi Kartı Numaranızı Girin: ")

    #kredi kart şifre bilgisinin alınması
    kredi_kart_sifre = input("Kredi Kartı Şifresini Giriniz: ") 
    
    #açıklama için bilgiler
    description = pizza.get_description()
    cost = pizza.get_cost()
    
    #saat ve tarih bilgisi alınması
    gettarih = datetime.now() 
    tarih = gettarih.strftime("%d/%m/%Y, %H:%M:%S") 

    #alınan bilgilerin Orders_Database.csv dosyasında tutlması
    with open("Orders_Database.csv", "a") as csvfile: 
        writer = csv.writer(csvfile) 
        writer.writerow([isim, tc, kredi_kart_numara, description, cost, tarih, kredi_kart_sifre]) 
    
    #Kullanıcıya bilgilendirmenin yapılması
    print("\nŞiparişiniz İçin Teşekkürler!")
    print("\nŞipariş Detaylarınız:")
    print("İsim: " + isim)
    print("Kimlik Numarası: " + tc)
    print("Sipariş: " + description)
    print(f"Tutar: {cost:.2f} ₺")
    print("Tarih: " + tarih)
    print("Şiparişiniz Veri Tabanına Kaydedildilmiştir!")



        

if __name__ == "__main__":
    main()