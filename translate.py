import time as t
from selenium import webdriver
import sys

driver = webdriver.Chrome()
driver.minimize_window()

def eventCtrl(event):
    if(event.lower() == "q"):
        print("----------------------------------")
        while True:
            lang = str(input("Choose 'UI' Language(EN(English), TR(Türkçe), FR(Français), RU(Pусский), ES(Español), DE(Deutch)): "))
            #English
            if(lang.lower() == "en") or (lang.lower() == "english"):
                EN()
            #Türkçe
            elif(lang.lower() == "tr") or (lang.lower() == "türkçe"):
                TR()

            #Français
            elif(lang.lower() == "fr") or (lang.lower() == "français"):
                FR()

            #Pусский    
            elif(lang.lower() == "ru") or (lang.lower() == "русский"):
                RU()

            #Español
            elif(lang.lower() == "es") or (lang.lower() == "español"):
                ES()

            #Deutch
            elif(lang.lower() == "de") or (lang.lower() == "deutch"):
                DE()
            else:
                validLang()
                continue
    else:
        return False

def validLang():
    print("Please enter a valid language!")
    t.sleep(1)
    print("--------------------")

# ENGLISH - ENGLISH - ENGLISH - ENGLISH - ENGLISH - ENGLISH ! ! ! ! 
def EN():
    while True:
        fromLang = str(input("FROM LANGUAGE (EN(English), TR(Turkish), FR(French), RU(Russian), ES(Spanish), DE(German)): "))
        #English
        if(fromLang.lower() == "en") or (fromLang.lower() == "english"):
            fromLangSC = "en"
            fromLangName = "English"
            print("English language was chosen.")
        #Türkçe
        elif(fromLang.lower() == "tr") or (fromLang.lower() == "turkish"):
            fromLangSC = "tr"
            fromLangName = "Turkish"
            print("Turkish language was chosen.")
        #Français
        elif(fromLang.lower() == "fr") or (fromLang.lower() == "french"):
            fromLangSC = "fr"
            fromLangName = "French"
            print("French language was chosen.")

        #Pусский    
        elif(fromLang.lower() == "ru") or (fromLang.lower() == "russian"):
            fromLangSC = "ru"
            fromLangName = "Russian"
            print("Russian language was chosen.")

        #Español
        elif(fromLang.lower() == "es") or (fromLang.lower() == "spanish"):
            fromLangSC = "es"
            fromLangName = "Spanish"
            print("Spanish language was chosen.")

        #Deutch
        elif(fromLang.lower() == "de") or (fromLang.lower() == "german"):
            fromLangSC = "de"
            fromLangName = "German"
            print("German language was chosen.")
        else:
            validLang()
            continue

        toLang = str(input("TO LANGUAGE (EN(English), TR(Turkish), FR(French), RU(Russian), ES(Spanish), DE(German)): "))

        #English
        if(toLang.lower() == "en") or (toLang.lower() == "english"):
            toLangSC = "en"
            toLangName = "English"
            print("English language is chosen.")
        #Turkish
        elif(toLang.lower() == "tr") or (toLang.lower() == "turkish"):
            toLangSC = "tr"
            toLangName = "Turkish"
            print("Turkish language was chosen.")
        #French
        elif(toLang.lower() == "fr") or (toLang.lower() == "french"):
            toLangSC = "fr"
            toLangName = "French"
            print("French language was chosen.")

        #Russian    
        elif(toLang.lower() == "ru") or (toLang.lower() == "russian"):
            toLangSC = "ru"
            toLangName = "Russian"
            print("Russian language was chosen.")

        #Español
        elif(toLang.lower() == "es") or (toLang.lower() == "spanish"):
            toLangSC = "es"
            toLangName = "Spanish"
            print("Spanish language was chosen.")

        #Deutch
        elif(toLang.lower() == "de") or (toLang.lower() == "german"):
            toLangSC = "de"
            toLangName = "German"
            print("German language was chosen.")
        else:
            validLang()
            continue

        print("----------------------------------")
        print(f"FROM:{fromLangName} - TO:{toLangName}")

        while True:
            text = str(input("What do you want to translate: "))
            url = (f"https://translate.google.com/#view=home&op=translate&sl={fromLangSC}&tl={toLangSC}&text={text}")
            driver.get(url)
            t.sleep(2)
            result = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div/span[1]").text
            print(f"{fromLangName}: {text}")
            print(f"{toLangName}: {result}")
            t.sleep(1)
            event = input("Press ENTER to continue translating. Press 'Q' to change language: ")
            eventCtrl(event)

        
# TURKISH - TURKISH - TURKISH - TURKISH - TURKISH - TURKISH ! ! ! !       
def TR():
    while True:
        fromLang = str(input("BU DİLDEN (EN(İngilizce), TR(Türkçe), FR(Fransızca), RU(Rusça), ES(İspanyolca), DE(Almanca)): "))
        #English
        if(fromLang.lower() == "en") or (fromLang.lower() == "ingilizce"):
            fromLangSC = "en"
            fromLangName = "İngilizce"
            print("İngilizce dili seçildi.")
        #Türkçe
        elif(fromLang.lower() == "tr") or (fromLang.lower() == "türkçe"):
            fromLangSC = "tr"
            fromLangName = "Türkçe"
            print("Türkçe dili seçildi.")
        #Français
        elif(fromLang.lower() == "fr") or (fromLang.lower() == "fransızca"):
            fromLangSC = "fr"
            fromLangName = "Fransızca"
            print("Fransızca dili seçildi.")

        #Pусский    
        elif(fromLang.lower() == "ru") or (fromLang.lower() == "rusça"):
            fromLangSC = "ru"
            fromLangName = "Rusça"
            print("Rusça dili seçildi.")

        #Español
        elif(fromLang.lower() == "es") or (fromLang.lower() == "ispanyolca"):
            fromLangSC = "es"
            fromLangName = "İspanyolca"
            print("İspanyolca dili seçildi.")

        #Deutch
        elif(fromLang.lower() == "de") or (fromLang.lower() == "almanca"):
            fromLangSC = "de"
            fromLangName = "Almanca"
            print("Almanca dili seçildi.")
        else:
            validLang()
            continue

        toLang = str(input("BU DİLE (EN(İngilizce), TR(Türkçe), FR(Fransızca), RU(Rusça), ES(İspanyolca), DE(Almanca)): "))

        #English
        if(toLang.lower() == "en") or (toLang.lower() == "ingilizce"):
            toLangSC = "en"
            toLangName = "İngilizce"
            print("İngilizce dili seçildi.")
        #Türkçe
        elif(toLang.lower() == "tr") or (toLang.lower() == "türkçe"):
            toLangSC = "tr"
            toLangName = "Türkçe"
            print("Türkçe dili seçildi.")
        #Français
        elif(toLang.lower() == "fr") or (toLang.lower() == "fransızca"):
            toLangSC = "fr"
            toLangName = "Fransızca"
            print("Fransızca dili seçildi.")

        #Pусский    
        elif(toLang.lower() == "ru") or (toLang.lower() == "rusça"):
            toLangSC = "ru"
            toLangName = "Rusça"
            print("Rusça dili seçildi.")

        #Español
        elif(toLang.lower() == "es") or (toLang.lower() == "ispanyolca"):
            toLangSC = "es"
            toLangName = "İspanyolca"
            print("İspanyolca dili seçildi.")

        #Deutch
        elif(toLang.lower() == "de") or (toLang.lower() == "almanca"):
            toLangSC = "de"
            toLangName = "Almanca"
            print("Almanca dili seçildi.")
        else:
            validLang()
            continue

        print("----------------------------------")
        print(f"BU DİLDEN:{fromLangName} - BU DİLE:{toLangName}")

        while True:
            text = str(input("Neyi çevirmek istersiniz: "))
            url = (f"https://translate.google.com/#view=home&op=translate&sl={fromLangSC}&tl={toLangSC}&text={text}")
            driver.get(url)
            t.sleep(2)
            result = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div/span[1]").text
            print(f"{fromLangName}: {text}")
            print(f"{toLangName}: {result}")
            t.sleep(1)
            event = input("Çeviriye devam etmek için ENTER tuşuna basın. Dili değiştirmek için 'Q' tuşuna basın: ")
            eventCtrl(event)

#FRENCH - FRENCH - FRENCH - FRENCH -FRENCH - FRENCH -FRENCH FRENCH- FRENCH FRENCH FRENCH FRENCH FRENCH !!!
def FR():
    while True:
        fromLang = str(input("FROM LANGUE (EN(Anglais), TR(Turc), FR(Français), RU(Russe), ES(Espagnol), DE(Allemand)):"))
        #English
        if(fromLang.lower() == "en") or (fromLang.lower() == "anglais"):
            fromLangSC = "en"
            fromLangName = "Anglais"
            print("La langue Anglaise a été choisie.")
        #Türkçe
        elif(fromLang.lower() == "tr") or (fromLang.lower() == "turc"):
            fromLangSC = "tr"
            fromLangName = "Turc"
            print("La langue Turc a été choisie.")
        #Français
        elif(fromLang.lower() == "fr") or (fromLang.lower() == "français"):
            fromLangSC = "fr"
            fromLangName = "Français"
            print("La langue Français a été choisie.")

        #Pусский    
        elif(fromLang.lower() == "ru") or (fromLang.lower() == "russe"):
            fromLangSC = "ru"
            fromLangName = "Russe"
            print("La langue Russe a été choisie.")

        #Español
        elif(fromLang.lower() == "es") or (fromLang.lower() == "espagnol"):
            fromLangSC = "es"
            fromLangName = "Espagnol"
            print("La langue Espagnol a été choisie.")

        #Deutch
        elif(fromLang.lower() == "de") or (fromLang.lower() == "allemand"):
            fromLangSC = "de"
            fromLangName = "Allemand"
            print("La langue Allemand a été choisie.")
        else:
            validLang()
            continue

        toLang = str(input("TO LANGUE (EN(Anglais), TR(Turc), FR(Français), RU(Russe), ES(Espagnol), DE(Allemand)):"))
        #English
        if(toLang.lower() == "en") or (toLang.lower() == "anglais"):
            toLangSC = "en"
            toLangName = "Anglais"
            print("La langue Anglaise a été choisie.")
        #Türkçe
        elif(toLang.lower() == "tr") or (toLang.lower() == "turc"):
            toLangSC = "tr"
            toLangName = "Turc"
            print("La langue Turc a été choisie.")
        #Français
        elif(toLang.lower() == "fr") or (toLang.lower() == "français"):
            toLangSC = "fr"
            toLangName = "Français"
            print("La langue Français a été choisie.")

        #Pусский    
        elif(toLang.lower() == "ru") or (toLang.lower() == "russe"):
            toLangSC = "ru"
            toLangName = "Russe"
            print("La langue Russe a été choisie.")

        #Español
        elif(toLang.lower() == "es") or (toLang.lower() == "espagnol"):
            toLangSC = "es"
            toLangName = "Espagnol"
            print("La langue Espagnol a été choisie.")

        #Deutch
        elif(toLang.lower() == "de") or (toLang.lower() == "allemand"):
            toLangSC = "de"
            toLangName = "Allemand"
            print("La langue Allemand a été choisie.")
        else:
            validLang()
            continue

        print("----------------------------------")
        print(f"FROM:{fromLangName} - TO:{toLangName}")

        while True:
            text = str(input("Que voulez-vous traduire: "))
            url = (f"https://translate.google.com/#view=home&op=translate&sl={fromLangSC}&tl={toLangSC}&text={text}")
            driver.get(url)
            t.sleep(2)
            result = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div/span[1]").text
            print(f"{fromLangName}: {text}")
            print(f"{toLangName}: {result}")
            t.sleep(1)
            event = input("Appuyez sur ENTER pour continuer la traduction. Appuyez sur 'Q' pour changer de langue: ")
            eventCtrl(event)

#RUSSIAN - RUSSIAN - RUSSIAN -RUSSIAN -RUSSIAN -RUSSIAN -RUSSIAN -RUSSIAN -RUSSIAN -RUSSIAN -RUSSIAN !!!!
def RU():
    while True:
        fromLang = str(input("ИЗ ЭТОГО ЯЗЫКА (EN (английский), TR(турецкий), FR(французский), RU(Русский), ES(испанский), DE(немецкий)):"))
        #English
        if(fromLang.lower() == "en") or (fromLang.lower() == "английский"):
            fromLangSC = "en"
            fromLangName = "Английский"
            print("Английский язык был выбран.")
        #Türkçe
        elif(fromLang.lower() == "tr") or (fromLang.lower() == "турецкий"):
            fromLangSC = "tr"
            fromLangName = "Турецкий"
            print("Турецкий язык был выбран.")
        #Français
        elif(fromLang.lower() == "fr") or (fromLang.lower() == "французский"):
            fromLangSC = "fr"
            fromLangName = "Французский"
            print("Французский язык был выбран.")

        #Pусский    
        elif(fromLang.lower() == "ru") or (fromLang.lower() == "pусский"):
            fromLangSC = "ru"
            fromLangName = "Русский"
            print("Русский язык был выбран.")

        #Español
        elif(fromLang.lower() == "es") or (fromLang.lower() == "испанский"):
            fromLangSC = "es"
            fromLangName = "испанский"
            print("испанский язык был выбран.")

        #Deutch
        elif(fromLang.lower() == "de") or (fromLang.lower() == "немецкий"):
            fromLangSC = "de"
            fromLangName = "Немецкий"
            print("Немецкий язык был выбран.")
        else:
            validLang()
            continue

        toLang = str(input("НА ЯЗЫК (EN (английский), TR(турецкий), FR(французский), RU(Русский), ES(испанский), DE(немецкий)):"))
        #English
        if(toLang.lower() == "en") or (toLang.lower() == "английский"):
            toLangSC = "en"
            toLangName = "Английский"
            print("Английский язык был выбран.")
        #Türkçe
        elif(toLang.lower() == "tr") or (toLang.lower() == "турецкий"):
            toLangSC = "tr"
            toLangName = "Турецкий"
            print("Турецкий язык был выбран.")
        #Français
        elif(toLang.lower() == "fr") or (toLang.lower() == "французский"):
            toLangSC = "fr"
            toLangName = "Французский"
            print("Французский язык был выбран.")

        #Pусский    
        elif(toLang.lower() == "ru") or (toLang.lower() == "pусский"):
            toLangSC = "ru"
            toLangName = "Русский"
            print("Русский язык был выбран.")

        #Español
        elif(toLang.lower() == "es") or (toLang.lower() == "испанский"):
            toLangSC = "es"
            toLangName = "испанский"
            print("испанский язык был выбран.")

        #Deutch
        elif(toLang.lower() == "de") or (toLang.lower() == "немецкий"):
            toLangSC = "de"
            toLangName = "Немецкий"
            print("Немецкий язык был выбран.")
        else:
            validLang()
            continue

        print("----------------------------------")
        print(f"ИЗ:{fromLangName} - К:{toLangName}")

        while True:
            text = str(input("Что вы хотите перевести: "))
            url = (f"https://translate.google.com/#view=home&op=translate&sl={fromLangSC}&tl={toLangSC}&text={text}")
            driver.get(url)
            t.sleep(2)
            result = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div/span[1]").text
            print(f"{fromLangName}: {text}")
            print(f"{toLangName}: {result}")
            t.sleep(1)
            event = input("Нажмите «ENTER», чтобы продолжить перевод. Нажмите «Q», чтобы изменить язык:")
            eventCtrl(event)  

#SPANISH - SPANISH - SPANISH - SPANISH - SPANISH - SPANISH - SPANISH - SPANISH !!!
def ES():
    while True:
        fromLang = str(input("DEL IDIOMA (EN(Inglés), TR(Turco), FR(Francés), RU(Ruso), ES(Español), DE(Alemán)):"))
        #English
        if(fromLang.lower() == "en") or (fromLang.lower() == "inglés"):
            fromLangSC = "en"
            fromLangName = "Inglés"
            print("Se eligió el idioma Inglés.")
        #Türkçe
        elif(fromLang.lower() == "tr") or (fromLang.lower() == "turco"):
            fromLangSC = "tr"
            fromLangName = "Turco"
            print("Se eligió el idioma Turco.")
        #Français
        elif(fromLang.lower() == "fr") or (fromLang.lower() == "francés"):
            fromLangSC = "fr"
            fromLangName = "Francés"
            print("Se eligió el idioma Francés.")

        #Pусский    
        elif(fromLang.lower() == "ru") or (fromLang.lower() == "ruso"):
            fromLangSC = "ru"
            fromLangName = "Ruso"
            print("Se eligió el idioma Ruso.")

        #Español
        elif(fromLang.lower() == "es") or (fromLang.lower() == "español"):
            fromLangSC = "es"
            fromLangName = "Español"
            print("Se eligió el idioma Español.")

        #Deutch
        elif(fromLang.lower() == "de") or (fromLang.lower() == "alemán"):
            fromLangSC = "de"
            fromLangName = "Alemán"
            print("Se eligió el idioma Alemán.")
        else:
            validLang()
            continue

        toLang = str(input("A LENGUA (EN(Inglés), TR(Turco), FR(Francés), RU(Ruso), ES(Español), DE(Alemán)):"))
        #English
        if(toLang.lower() == "en") or (toLang.lower() == "inglés"):
            toLangSC = "en"
            toLangName = "Inglés"
            print("Se eligió el idioma Inglés.")
        #Türkçe
        elif(toLang.lower() == "tr") or (toLang.lower() == "turco"):
            toLangSC = "tr"
            toLangName = "Turco"
            print("Se eligió el idioma Turco.")
        #Français
        elif(toLang.lower() == "fr") or (toLang.lower() == "francés"):
            toLangSC = "fr"
            toLangName = "Francés"
            print("Se eligió el idioma Francés.")

        #Pусский    
        elif(toLang.lower() == "ru") or (toLang.lower() == "ruso"):
            toLangSC = "ru"
            toLangName = "Ruso"
            print("Se eligió el idioma Ruso.")

        #Español
        elif(toLang.lower() == "es") or (toLang.lower() == "español"):
            toLangSC = "es"
            toLangName = "Español"
            print("Se eligió el idioma Español.")

        #Deutch
        elif(toLang.lower() == "de") or (toLang.lower() == "alemán"):
            toLangSC = "de"
            toLangName = "Alemán"
            print("Se eligió el idioma Alemán.")
        else:
            validLang()
            continue

        print("----------------------------------")
        print(f"DE:{fromLangName} - A:{toLangName}")

        while True:
            text = str(input("¿Qué quieres traducir: "))
            url = (f"https://translate.google.com/#view=home&op=translate&sl={fromLangSC}&tl={toLangSC}&text={text}")
            driver.get(url)
            t.sleep(2)
            result = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div/span[1]").text
            print(f"{fromLangName}: {text}")
            print(f"{toLangName}: {result}")
            t.sleep(1)
            event = input("Presione 'ENTER' para continuar traduciendo. Presione 'Q' para cambiar el idioma:")
            eventCtrl(event) 
#DEUTSCH - DEUTSCH - DEUTSCH -DEUTSCH -DEUTSCH -DEUTSCH -DEUTSCH -DEUTSCH -DEUTSCH -DEUTSCH-DEUTSCH !!!
def DE():
    while True:
        fromLang = str(input("AUS DER SPRACHE (EN(Englisch), TR(Türkisch), FR(Französisch), RU(Russisch), ES(Spanisch), DE(Deutsch)):"))
        #English
        if(fromLang.lower() == "en") or (fromLang.lower() == "englisch"):
            fromLangSC = "en"
            fromLangName = "Englisch"
            print("Die Englische Sprache wurde gewählt.")
        #Türkçe
        elif(fromLang.lower() == "tr") or (fromLang.lower() == "türkisch"):
            fromLangSC = "tr"
            fromLangName = "Türkisch"
            print("Die Türkische Sprache wurde gewählt.")
        #Français
        elif(fromLang.lower() == "fr") or (fromLang.lower() == "französisch"):
            fromLangSC = "fr"
            fromLangName = "Französisch"
            print("Die Französische Sprache wurde gewählt.")

        #Pусский    
        elif(fromLang.lower() == "ru") or (fromLang.lower() == "russisch"):
            fromLangSC = "ru"
            fromLangName = "Russisch"
            print("Die Russische Sprache wurde gewählt.")

        #Español
        elif(fromLang.lower() == "es") or (fromLang.lower() == "spanisch"):
            fromLangSC = "es"
            fromLangName = "Spanisch"
            print("Die Spanische Sprache wurde gewählt.")

        #Deutch
        elif(fromLang.lower() == "de") or (fromLang.lower() == "deutsch"):
            fromLangSC = "de"
            fromLangName = "Deutsch"
            print("Die Deutsche Sprache wurde gewählt.")
        else:
            validLang()
            continue

        toLang = str(input("ZU SPRACHE (EN(Englisch), TR(Türkisch), FR(Französisch), RU(Russisch), ES(Spanisch), DE(Deutsch)):"))
        #English
        if(toLang.lower() == "en") or (toLang.lower() == "englisch"):
            toLangSC = "en"
            toLangName = "Englisch"
            print("Die Englische Sprache wurde gewählt.")
        #Türkçe
        elif(toLang.lower() == "tr") or (toLang.lower() == "türkisch"):
            toLangSC = "tr"
            toLangName = "Türkisch"
            print("Die Türkische Sprache wurde gewählt.")
        #Français
        elif(toLang.lower() == "fr") or (toLang.lower() == "französisch"):
            toLangSC = "fr"
            toLangName = "Französisch"
            print("Die Französische Sprache wurde gewählt.")

        #Pусский    
        elif(toLang.lower() == "ru") or (toLang.lower() == "russisch"):
            toLangSC = "ru"
            toLangName = "Russisch"
            print("Die Russische Sprache wurde gewählt.")

        #Español
        elif(toLang.lower() == "es") or (toLang.lower() == "spanisch"):
            toLangSC = "es"
            toLangName = "Spanisch"
            print("Die Spanische Sprache wurde gewählt.")

        #Deutch
        elif(toLang.lower() == "de") or (toLang.lower() == "deutsch"):
            toLangSC = "de"
            toLangName = "Deutsch"
            print("Die Deutsche Sprache wurde gewählt.")
        else:
            validLang()
            continue

        print("----------------------------------")
        print(f"FROM:{fromLangName} - TO:{toLangName}")

        while True:
            text = str(input("Was möchten Sie übersetzen: "))
            url = (f"https://translate.google.com/#view=home&op=translate&sl={fromLangSC}&tl={toLangSC}&text={text}")
            driver.get(url)
            t.sleep(2)
            result = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div/span[1]").text
            print(f"{fromLangName}: {text}")
            print(f"{toLangName}: {result}")
            t.sleep(1)
            event = input("Drücken Sie die EINGABETASTE, um die Übersetzung fortzusetzen. Drücken Sie 'Q', um die Sprache zu ändern: ")
            eventCtrl(event)



while True:
    lang = str(input("Choose 'UI' Language(EN(English), TR(Türkçe), FR(Français), RU(Pусский), ES(Español), DE(Deutch)): "))
    #English
    if(lang.lower() == "en") or (lang.lower() == "english"):
        url = "https://translate.google.com/?hl=en"
        print("English language was chosen.")
        EN()

    #Türkçe
    elif(lang.lower() == "tr") or (lang.lower() == "türkçe"):
        url = "https://translate.google.com/?hl=tr"
        print("Türkçe dili seçildi.")
        TR()

    #Français
    elif(lang.lower() == "fr") or (lang.lower() == "français"):
        print("La langue française a été choisie.")
        FR()

    #Pусский    
    elif(lang.lower() == "ru") or (lang.lower() == "русский"):
        print("Русский язык был выбран.")
        RU()

    #Español
    elif(lang.lower() == "es") or (lang.lower() == "español"):
        print("Se eligió el idioma inglés.")
        ES()

    #Deutch
    elif(lang.lower() == "de") or (lang.lower() == "deutch"):
        print("Die deutsche Sprache wurde gewählt.")
        DE()

    else:
        validLang()
        continue