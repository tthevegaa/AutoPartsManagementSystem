
from colorama import Fore, Style, init
init(autoreset = True)

import pickle
import sys 
import os

def DetectHighestID():

    if not os.path.exists("storage.bin"):
        return 10300
    

    try:
        with open("storage.bin", "rb") as file:
            max = 10300
            while True:
                try:
                    data = pickle.load(file)
                    if data["ID"] > max:
                        max = data['ID']

                except EOFError:
                    break

        return max
    
    except FileNotFoundError:
        return 10300
    




def CreateProviders():
    prov = [
        {
            "PROVIDER": "AUTOTECH",
            "PRODUCTS": [
                {"NAME": "SPORT TIRE", "BRAND": "AUTOZONE", "TYPE": "TIRE", "ID": 20010, "PRICE": 87.90, "QUANTITY": 100, "DESCRIPTION": "HIGH QUALITY AND PERFORMANCE FOR LUXURY AND SPORTS VECHICLES"}, 
                {"NAME": "LED HEADLIGHTS", "BRAND": "Z MOTORS", "TYPE": "HEADLIGHT", "ID": 20011, "PRICE": 89.99, "QUANTITY": 100, "DESCRIPTION": "IDEAL FOR FOGGY DAYS, HIGH DURABILITY"}, 
                {"NAME": "SPECIAL RIM", "BRAND": "CAR X", "TYPE": "RIM", "ID": 20012, "PRICE": 104.99, "QUANTITY": 100, "DESCRIPTION": "STRONG RIM DESIGNED FOR PICK UP VEHICLES"}, 
                {"NAME": "NO-HAND SYSTEM", "BRAND": "VEGA INDUSTRIES", "TYPE": "SYSTEM", "ID": 20013, "PRICE": 978.66, "QUANTITY": 100, "DESCRIPTION": "AUTONUMOUS SOFTWARE DESIGNED FOR ADVANCED AUTOPILOT SYSTEM"}
            ]
        }, 

        { 
            "PROVIDER": "VW PUEBLA STORE",
            "PRODUCTS": [
                {"NAME": "REGULAR TIRE", "BRAND": "AUTOZONE", "TYPE": "TIRE", "ID": 63670, "PRICE": 65.42, "QUANTITY": 100, "DESCRIPTION": "ENSURED DURABILITY AND HIGH HIGH QUALITY FOR A LONGER LASTING USE"}, 
                {"NAME": "AIR FILTER", "BRAND": "ACME PUEBLA", "TYPE": "AIR CONDITIONING", "ID": 63671, "PRICE": 97.70, "QUANTITY": 100, "DESCRIPTION": "POWEFUL AIR CONDITIONING SYSTEM FOR SUPERIOR PURIFICATION"}, 
                {"NAME": "SPORT MOTOR", "BRAND": "XIOCCI", "TYPE": "MOTOR", "ID": 63672, "PRICE": 789.65, "QUANTITY": 100, "DESCRIPTION": "DESIGNED SPECIFICALLY FOR SPORTS CARS ENSURING A HIGHER PERFORMANCE AND REACHING 0-100 IN 4.5 SECONDS,"}, 
                {"NAME": "GPS SYSTEM", "BRAND": "VEGA INDUSTRIES", "TYPE": "SYSTEM", "ID": 63673, "PRICE": 349.90, "QUANTITY": 100, "DESCRIPTION": "THE MOST ADVANCED GPS SYSTEM DESIGNED IN MEXICO CONTROLLED BY VOICE AND ABLE TO GIVE ADVICE ABOUT TRAFIC UNEXPECTED EVENTS"}
            ]
        }, 

        {
            "PROVIDER": "CAR CASTLE SEATTLE",
            "PRODUCTS": [
                {"NAME": "SPORT STEERING WHEEL", "BRAND": "BENSON STORE STL", "TYPE": "STEERING WHEEL", "ID": 13012, "PRICE": 55.78, "QUANTITY": 100, "DESCRIPTION": "DURABILITY AND HIGH QUALITY OF MATERIALS. DESIGNED FOR SPORTS CARS"}, 
                {"NAME": "HEATED SEAT", "BRAND": "NO CARS NO LIFE", "TYPE": "SEAT", "ID": 13013, "PRICE": 287.90, "QUANTITY": 100, "DESCRIPTION": "HEADED PILOT SEAT MADE OF LEATHER"}, 
                {"NAME": "PLASTIC CAR MATS", "BRAND": "AUTOZONE", "TYPE": "MATS", "ID": 13014, "PRICE": 58.32, "QUANTITY": 100, "DESCRIPTION": "(NO DESCRIPTION FOUND)"},
                {"NAME": "LEATHER GEAR LEVER", "BRAND": "BENSON STORE STL", "TYPE": "GEAR SHIFT", "ID": 13015, "PRICE": 62.14, "QUANTITY": 100, "DESCRIPTION": "NICE LEATHER GEAR SHIFT"}

            ]
        }
    ]

    try:
        with open("providers.bin", "wb") as file:
            pickle.dump(prov, file)

        print(Fore.GREEN + "PROVIDERS SUCCESSFULLY STORED IN FILE" + Style.RESET_ALL)

    except FileNotFoundError:
        print(Fore.RED + "\nPROVIDERS COULD NOT BE SAVED IN FILE" + Style.RESET_ALL)



#--------------------------------------------------------------------------------------
def ErrorMessage():
    print(Fore.RED + "\nSOMETHING WENT WRONG. TRY AGAIN LATER.\n" + Style.RESET_ALL)
#--------------------------------------------------------------------------------------



#takes item to search for.
def Searching_Type():

    print(Fore.YELLOW + "\n-----------------------------------------------------------------------------------------------------------------")
    print(Fore.YELLOW + "|                                                      NOTE                                                     |")
    print(Fore.YELLOW + "| IN ORDER TO FIND SYSTEMS SUCH AS GPS DEVICES OR ANY OTHER ITEM WHICH IS AUTOMATICALLY CONTROLLED BY A SOFWARE |")
    print(Fore.YELLOW + "| OR REQUIRES A NETWORK CONNECTION TO WORK, YOU CAN TRY TO WRITE 'SOFTWARE' OR 'SYSTEM' IN THE SEARCH BAR.      |")
    print(Fore.YELLOW + "-----------------------------------------------------------------------------------------------------------------\n" + Style.RESET_ALL)


    while True:

        search = input(Fore.BLUE + "\nENTER A TYPE OF ITEM TO SEARCH: " + Style.RESET_ALL).upper()

        if not search:
            print(Fore.RED + "\nENTER A VALID TYPE AND TRY AGAIN (NO SPECIAL CHARACTERS, NO NUMBERS).\n" + Style.RESET_ALL)
            continue

        if not all(x.isalpha() or x.isspace() for x in search):
            print(Fore.RED + "\nENTER A VALID TYPE AND TRY AGAIN (NO SPECIAL CHARACTERS, NO NUMBERS).\n" + Style.RESET_ALL)
            continue

        break

    return search



#loads all data in "providers.bin"
def LoadProviders():

    try:
        with open("providers.bin", "rb") as file:

            data = pickle.load(file)

    except FileNotFoundError:
        print(Fore.RED + "\nFILE COULD NOT BE OPEN. TRY AGAIN LATER. " + Style.RESET_ALL)
        return
    
    return data



#searches for matches and ask for wanted item's ID.
def FindMatchesProv(lines, search):
        matches = []

        print(f"\nFOUND MATCHES FOR THE SEARCH '{search}': ")

        out = []

        for provider in lines:
            for item in provider['PRODUCTS']:
            
                if item["TYPE"] == search:
                    print("-------------------------------------------------------------------------------------------------------------------")
                    print(f"NAME: {item['NAME']}  |  BRAND: {item['BRAND']}  |  TYPE: {item['TYPE']}  |  ID: {item['ID']}")
                    print(f"PRICE: {item['PRICE']}  |  AVAILABLE QUANTITY: {item['QUANTITY']}")
                    print(f"DESCRIPTION: {item['DESCRIPTION']}")
                    print("-------------------------------------------------------------------------------------------------------------------\n")
                     
                    matches.append(item)
                    if item['QUANTITY'] <= 0:
                        out.append(item['ID'])
    
    
        if len(matches) <= 0:
            print(Fore.RED + "\n--------------NO FOUND MATCHES-------------\n" + Style.RESET_ALL)
            
            while True:
                print("TRY AGAIN -> 1")
                print("QUIT -> 2")

                try:
                    a = int(input("ENTER THE OPTION: "))

                    if a not in [1, 2]:
                        print(Fore.RED + "\nINVALID OPTION. TRY AGAIN: \n" + Style.RESET_ALL)
                        continue

                    break

                except ValueError:
                    print(Fore.RED + "\nINVALID OPTION. TRY AGAIN: \n" + Style.RESET_ALL)

            return a
        
    
        IDs = [x['ID'] for x in matches]
    
        while True:
            try:
    
                id = int(input("ENTER THE ID OF THE ITEM YOU'D LIKE TO CHOOSE: "))
    
                if id not in IDs:
                    print(Fore.RED + "\nENTER A VALID ID AND TRY AGAIN.\n" + Style.RESET_ALL)
                    continue
    
                if id in out:
                    print(Fore.RED + "\nTHIS PRODUCT IS CURRENTLY OUT OF STOCK\n" + Style.RESET_ALL)
                    continue
    
                break
    
            except ValueError:
                print(Fore.RED + "\nENTER A VALID ID AND TRY AGAIN.\n" + Style.RESET_ALL)
    
        return id




#searches for the entered item and saved it in the variable "chosen_product". At the mean time, takes the quantity of pieces to buy (hm).
def LocateProduct(data, id):

    chosen_product = None

    for provider in data:
        for item in provider["PRODUCTS"]:
            if item["ID"] == id:

                chosen_product = item
                break
        
    while True:
        try:

            hm = int(input("ENTER QUANTITY OF ITEMS YOU'D LIKE TO BUY: "))

            if hm <= 0:
                print(Fore.RED + "\nENTER A VALID QUANTITY: \n" + Style.RESET_ALL)
                continue

            if hm > chosen_product["QUANTITY"]:
                print(Fore.RED + f"\nONLY {item['QUANTITY']} AVAILABLE PIECES." + Style.RESET_ALL)
                continue

            break

        except ValueError:
            print(Fore.RED + "\nENTER A VALID VALUE.\n" + Style.RESET_ALL)

    
    print("\nPURCHASE SUMMARY: ")
    print("-------------------------------------------------------------------------------------------------------------------")
    print(f"NAME: {chosen_product['NAME']}  |  BRAND: {chosen_product['BRAND']}  |  TYPE: {chosen_product['TYPE']}  |  ID: {chosen_product['ID']}")
    print(f"PRICE (EACH): {chosen_product['PRICE']}  |  WANTED PIECES: {hm}  |  TOTAL: {chosen_product['PRICE'] * hm}")
    print(f"DESCRIPTION: {chosen_product['DESCRIPTION']}")
    print("-------------------------------------------------------------------------------------------------------------------")

    

    chosen_product["QUANTITY"] -= hm
    return chosen_product, hm




#Updates file "providers.bin". 
def RewriteProv(data):
    try:
        with open("providers.bin", "wb") as archive:

            pickle.dump(data, archive)

    except FileNotFoundError:
            print(Fore.RED + "ACTION COULD NOT BE EXECUTED. TRY AGAIN LATER.\n" + Style.RESET_ALL)
            return False  
    
    print(Fore.LIGHTGREEN_EX + "\nPROVIDERS FILE WAS SUCCESFULLY EDITED.\n" + Style.RESET_ALL)
    return True




#creates a dictionary in order to store it in "storage.bin" as a new product. 
def CreatePurchase(chosen_product, hm):
    global ID_NOW

    porcentage = chosen_product["PRICE"] * 0.20
    new_price = chosen_product["PRICE"] + porcentage

    final = chosen_product["PRICE"] * hm


    bought_item = {

        "NAME": chosen_product["NAME"], 
        "BRAND": chosen_product["BRAND"],
        "TYPE": chosen_product["TYPE"],
        "ID": ID_NOW,
        "PRICE": new_price,
        "QUANTITY": hm,
        "DESCRIPTION": chosen_product["DESCRIPTION"],
        "ORIGINAL_PRICE": chosen_product["PRICE"],
        "TOTAL": final
    } 
       

    try:
        with open("storage.bin", "ab") as document:

            pickle.dump(bought_item, document)
            
    except FileNotFoundError:
        print(Fore.RED + "\nITEM COULD NOT BE SAVED IN STORAGE. TRY AGAIN LATER.\n" + Style.RESET_ALL)
        return False
    

    print(Fore.LIGHTGREEN_EX + f"\nITEM WAS SUCCESFULLY BOUGHT AND SAVED IN STORAGE.\n" + Style.RESET_ALL)

    ID_NOW += 1
    return True




def Confirming():
    print(Fore.YELLOW + "\nARE YOU CONFIRMING TO CARRY OUT THIS ACTION?" + Style.RESET_ALL)
    while True:

        print("CONFIRM -> 1")
        print("CANCEL -> 2")

        try:
            f = int(input("ENTER THE OPTION: "))

            if f not in [1, 2]:
                print(Fore.RED + "\nINVALID OPTION. TRY AGAIN: \n" + Style.RESET_ALL)
                continue

            break

        except ValueError:
            print(Fore.RED + "\nINVALID OPTION. TRY AGAIN: \n" + Style.RESET_ALL)

        
    if f == 2:
        print(Fore.YELLOW + "\nACTION CANCELLED\n" + Style.RESET_ALL)
        return False
    
    print("\nSUCCESS!!!")
    return True



#Function searches for a item in providers' storage and then addes it to our own storage.
def OrderAsCustumer():

    data = LoadProviders()
    if data is None:
        return


    while True:
        search = Searching_Type()
        if search is None:
            ErrorMessage()
            return
    

        id = FindMatchesProv(data, search)
        if id is None:
            ErrorMessage()
            return
        
        if id == 1:
            continue
        elif id == 2:
            return
        
        break
    
    

    chosen_product, hm = LocateProduct(data, id)
    if chosen_product is None:
        return
    

    if not Confirming():
        return
    

    if not RewriteProv(data):
        return
    

    if not CreatePurchase(chosen_product, hm):
        return



        
#Function shows all the stored information in own storage file.
def Displaying():

    try:
        if os.path.getsize("storage.bin") == 0:
            
            print(Fore.YELLOW + "\nSTORAGE IS CURRENTLY EMPTY.\n" + Style.RESET_ALL)
            return

    except FileNotFoundError:
        print(Fore.RED + "\nFILE COULD NOT BE OPENED. TRY AGAIN LATER.\n" + Style.RESET_ALL)
        return
    


    try:
        with open("storage.bin", "rb") as file:

            print("\n------------------------------------------------------STORAGE------------------------------------------------------\n")

            while True:
                try:
                    data = pickle.load(file)

                    print("-------------------------------------------------------------------------------------------------------------------")
                    print(f"NAME: {data['NAME']}  |  BRAND: {data['BRAND']}  |  TYPE: {data['TYPE']}  |  ID: {data['ID']}")
                    print(f"PRICE: {data['PRICE']}  |  AVAILABLE QUANTITY: {data['QUANTITY']}")
                    print(f"DESCRIPTION: {data['DESCRIPTION']}")
                    print("-------------------------------------------------------------------------------------------------------------------\n")

                except EOFError:
                    break

    except FileNotFoundError:
        print(Fore.RED + "\nSTORAGE COULD NOT BE OPENED. TRY AGAIN LATER. \n" + Style.RESET_ALL)





#stores an element in sales history.
def SaveSalesHistory(chosen_item, status, hm, finalp):

    dictionary = {
        
        "STATUS": status,
        "NAME": chosen_item["NAME"],
        "BRAND": chosen_item["BRAND"],
        "TYPE": chosen_item["TYPE"],
        "ID": chosen_item["ID"],
        "PRICE": chosen_item["PRICE"],
        "FINAL_PRICE": finalp,
        "QUANTITY": hm,

    }


    try:
        with open("history.bin", "ab") as filee:
            pickle.dump(dictionary, filee)

            print("\nACTION REGISTERED IN SALES HISTORY.")
            return True

    except FileNotFoundError:
        print(Fore.RED + "\nACTION COULD NOT BE REGISTERED IN SALES HISTORY.\n" + Style.RESET_ALL)
        return False



#rewrites file "storage.bin".
def ReWriteStorage(lines):
    try:
        with open("storage.bin", "wb") as archive:
            for z in lines:
                pickle.dump(z, archive)

            return True

    except FileNotFoundError:
        print(Fore.RED + "\nFILE COULD NOT BE SAVED. TRY AGAIN LATER.\n" + Style.RESET_ALL)
        return False
    


#loads all data from file "storage.bin".
def Load_FromStorage():

    lines = []

    try:
        with open("storage.bin", "rb") as file:
            while True:
                try:

                    lines.append(pickle.load(file))

                except EOFError:
                    break
        
    except FileNotFoundError:
        print(Fore.RED + "\nFILE COULD NOT BE FOUND. TRY AGAIN LATER.\n" + Style.RESET_ALL)
        return False
    
    return lines



#checks that file is not empty
def File_IsEmpty():
    try:
        if os.path.getsize("storage.bin") == 0:
            print(Fore.BLUE + "\n---------------STORAGE IS EMPTY.---------------\n" + Style.RESET_ALL)
            return True

    except FileNotFoundError:
        print(Fore.RED + "\nFILE COULD NOT BE FOUND. TRY AGAIN LATER.\n" + Style.RESET_ALL)
        return True
    
    return False




#searches for matches and ask for wanted item's ID.
def FindMatches(lines, search):
    matches = []

    print(f"\nFOUND MATCHES FOR THE SEARCH '{search}': ")

    out = []

    for item in lines:
        if item["TYPE"] == search:
            print("-------------------------------------------------------------------------------------------------------------------")
            print(f"NAME: {item['NAME']}  |  BRAND: {item['BRAND']}  |  TYPE: {item['TYPE']}  |  ID: {item['ID']}")
            print(f"PRICE: {item['PRICE']}  |  AVAILABLE QUANTITY: {item['QUANTITY']}")
            print(f"DESCRIPTION: {item['DESCRIPTION']}")
            print("-------------------------------------------------------------------------------------------------------------------\n")

            matches.append(item)
            if item['QUANTITY'] <= 0:
                out.append(item['ID'])


    if len(matches) <= 0:
        print(Fore.RED + "\n--------------NO FOUND MATCHES-------------\n" + Style.RESET_ALL)

        while True:
            print("TRY AGAIN -> 1")
            print("QUIT -> 2")

            try:
                x = int(input("ENTER THE OPTION: "))

                if x not in [1, 2]:
                    print(Fore.RED + "\nINVALID OPTION. TRY AGAIN: \n" + Style.RESET_ALL)
                    continue

                break

            except ValueError:
                print(Fore.RED + "\nINVALID OPTION. TRY AGAIN: \n" + Style.RESET_ALL)

        return x
        


    IDs = [x['ID'] for x in matches]

    while True:
        try:

            id = int(input("ENTER THE ID OF THE ITEM YOU'D LIKE TO CHOOSE: "))

            if id not in IDs:
                print(Fore.RED + "\nENTER A VALID ID AND TRY AGAIN.\n" + Style.RESET_ALL)
                continue

            if id in out:
                print(Fore.RED + "\nTHIS PRODUCT IS CURRENTLY OUT OF STOCK\n" + Style.RESET_ALL)
                continue

            break

        except ValueError:
            print(Fore.RED + "\nENTER A VALID ID AND TRY AGAIN.\n" + Style.RESET_ALL)

    return id



#Shows a short resume of the summary in a little chart.
def Purchase_Summary(lines, id):

    chosen_item = None

    for i in lines:
        if i['ID'] == id:
            chosen_item = i
            break


    while True:
        try:
            hm = int(input("ENTER QUANTITY TO SELL: "))

            if hm > chosen_item['QUANTITY']:
                print(Fore.YELLOW + f"ONLY {chosen_item['QUANTITY']} AVAILABLE ITEMS TO SELL." + Style.RESET_ALL)
                continue

            break

        except ValueError:
            print(Fore.RED + "\nENTER A VALID VALUE AND TRY AGAIN: \n" + Style.RESET_ALL)


    chosen_item['QUANTITY'] -= hm 

    finalp = chosen_item['PRICE'] * hm

    print("\nPURCHASE SUMMARY: ")
    print("-------------------------------------------------------------------------------------------------------------------")
    print(f"NAME: {chosen_item['NAME']}  |  BRAND: {chosen_item['BRAND']}  |  TYPE: {chosen_item['TYPE']}  |  ID: {chosen_item['ID']}")
    print(f"PRICE (EACH): {chosen_item['PRICE']}  |  BOUGHT ITEMS: {hm}  |  FINAL PRICE: {finalp}")  
    print("-------------------------------------------------------------------------------------------------------------------")


    
    return chosen_item, hm, finalp




#----------------------------
#This funtion searches for an item to sell and edits the storage
def OrderAsSeller():

    if File_IsEmpty():
        return
    

    lines = Load_FromStorage()
    if not lines:
        ErrorMessage()
        return
    

    while True:
        search = Searching_Type()
        if search is None:
            ErrorMessage()
            return

        id = FindMatches(lines, search)
        if id is None:
            ErrorMessage()
            return
        
        if id == 1:
            continue
        elif id == 2:
            return
        
        break


    chosen_item, hm, finalp = Purchase_Summary(lines, id)

    if chosen_item is None:
        return
    

    if not Confirming():
        return
    

    if chosen_item['QUANTITY'] <= 0:
        Delete_All(lines, id)
        return


    if not ReWriteStorage(lines):
        return
    

    if not SaveSalesHistory(chosen_item, "SOLD", hm, finalp):
        return




#deletes some pieces of a item
def DeletePartially(lines, id):
    
    chosen_item = None

    for x in lines:
        if id == x["ID"]:
            chosen_item = x
            break
      
    while True:
        try:
            hm = int(input("ENTER NUMBER OF PIECES TO DELETE: "))

            if hm > chosen_item['QUANTITY']:
                print(Fore.YELLOW + f"\nONLY {chosen_item['QUANTITY']} PIECES OF THIS ITEM. TRY AGAIN: \n" + Style.RESET_ALL)
                continue

            if hm <= 0:
                print(Fore.RED + "\nENTER A VALID QUANTITY AND TRY AGAIN: \n" + Style.RESET_ALL)
                continue

            break

        except ValueError:
            print(Fore.RED + "\nINVALID VALUE.\n" + Style.RESET_ALL)


   
    chosen_item['QUANTITY'] -= hm
    finalp = chosen_item["PRICE"] * hm

    return chosen_item, hm, finalp





#removes an entire item.
def Delete_All(lines, id):


    new_lines = []

    for x in lines:
        if x["ID"] == id:
            continue

        else:
            new_lines.append(x)


    try:
        with open("storage.bin", "wb") as archive:
            for z in new_lines:
                pickle.dump(z, archive)

            print(Fore.GREEN + "\nITEM WAS SUCCESFULLY DELETED FROM STORAGE.\n" + Style.RESET_ALL)
            return True

    except FileNotFoundError:
        print(Fore.RED + "\nFILE COULD NOT BE SAVED. TRY AGAIN LATER.\n" + Style.RESET_ALL)
        return False




#takes type of item, searches for it in file and deletes complete or partially.
def Deleting():

    if File_IsEmpty():
        return
    

    lines = Load_FromStorage()
    if not lines:
        return
        

    while True:
        search = Searching_Type()
        if search is None:
            ErrorMessage()
            return  

        id = FindMatches(lines, search)
        if id is None:
            return
        
        if id == 1:
            continue
        elif id == 2:
            return
        
        break
    

    while True:

        print(Fore.BLUE + "\nYOU'D LIKE TO... " + Style.RESET_ALL)
        print("DELETE ENTIRE ITEM -> 1")
        print("DELETE ONLY SOME PIECES OF THIS ITEM -> 2")
        print("CANCEL -> 7")
        print("------------------------------------------")

        try: 
            opt = int(input("ENTER THE OPTION: "))

            if opt not in [1, 2, 7]:
                print(Fore.RED + "\nINVALID OPTION. TRY AGAIN: \n" + Style.RESET_ALL)
                continue

            break

        except ValueError:
            print(Fore.RED + "\nINVALID VALUE.\n" + Style.RESET_ALL)


    match opt:

        case 1:

            if not Confirming():
                return


            if not Delete_All(lines, id):
                return
            

        case 2:
            chosen_item, hm, finalp = DeletePartially(lines, id)

            if chosen_item is None:
                return
            
            if not Confirming():
                return
            
            
            if chosen_item['QUANTITY'] <= 0:
                if not Delete_All(lines, id):
                    return
                return
            

            if not ReWriteStorage(lines):
                return
            
            print(Fore.GREEN + "PIECES SUCCESFULLY DELETED" + Style.RESET_ALL)

            if not SaveSalesHistory(chosen_item, "DELETED", hm, finalp):
                return


        case 7:
            print(Fore.YELLOW + "\nACTION CANCELLED" + Style.RESET_ALL)
            return 
        


def locating_item(lines, id):

    chosen_item = None

    for x in lines:
        if id == x['ID']:
            chosen_item = x
            break

    if chosen_item is None:
        return
    
    print("-------------------------------------------------------------------------------------------------------------------")
    print(f"NAME: {chosen_item['NAME']}  |  BRAND: {chosen_item['BRAND']}  |  TYPE: {chosen_item['TYPE']}  |  ID: {chosen_item['ID']}")
    print(f"PRICE (EACH): {chosen_item['PRICE']}  |")  
    print("-------------------------------------------------------------------------------------------------------------------\n")

    return chosen_item




#shows a menu in order to take what to edit.
def Choicex():

    while True:
        print(Fore.BLUE + "\nYOU WANNA EDIT..." + Style.RESET_ALL)
        print("NAME -> 1")
        print("BRAND -> 2")
        print("TYPE -> 3")
        print("PRICE -> 4")
        print("CANCEL -> 0")
        print("------------------")
        
        try:
            opt = int(input("ENTER THE OPTION: "))

            if opt < 0 or opt > 4:
                print(Fore.RED + "\nINVALID OPTION. TRY AGAIN: \n" + Style.RESET_ALL)
                continue

            break

        except ValueError:
            print(Fore.RED + "\nINVALID VALUE. TRY AGAIN: \n" + Style.RESET_ALL)

    return opt




#Takes the new price, name or type and updates the list.
def GetNew(y):

    while True:
        if y == "PRICE":
            try:
                
                new = float(input("ENTER THE NEW PRICE: "))

                if new <= 0:
                    print(Fore.RED + "\nENTER A VALID PRICE AND TRY AGAIN.\n" + Style.RESET_ALL)
                    continue

                break

            except ValueError:
                print(Fore.RED + "\nINVALID VALUE. TRY AGAIN: \n" + Style.RESET_ALL)

        else:
            new = input(f"ENTER THE NEW {y}: ").strip()

            if new == "":
                print(Fore.RED + f"\nINVALID {y}. PLEASE, TRY AGAIN: \n" + Style.RESET_ALL)
                continue

            break

    return new

    


#take type as parameter and searches for it in file, then, edits and rewrites file.
def Editing():

    if File_IsEmpty():
        return
    
    lines = Load_FromStorage()
    if lines == False or lines is None:
        return
    
    

    while True:
        search = Searching_Type()
        if search == None:
            
            ErrorMessage()
            return
    
    
        id = FindMatches(lines, search)
        if id is None:
            ErrorMessage()
            return
        
        if id == 1:
            continue
        elif id == 2:
            return
        
        break
    

    chosen_item = locating_item(lines, id)
    if chosen_item is None:
        ErrorMessage()
        return
        

    opt = Choicex()
    if opt is None:
        ErrorMessage()
        return
    

    match opt:

        case 0:
            print("LEAVING...")
            return
        
        
        case 1:
            y = "NAME"
            new = GetNew(y)
            if new is None:
                ErrorMessage()
                return
            
            chosen_item['NAME'] = new


        case 2:

            y = "BRAND"
            new = GetNew(y)
            if new is None:
                ErrorMessage()
                return
            
            chosen_item['BRAND'] = new


        case 3:
            y = "TYPE"
            new = GetNew(y)
            if new is None:
                ErrorMessage()
                return
            
            chosen_item['TYPE'] = new


        case 4:
            y = "PRICE"
            new = GetNew(y)
            if new is None:
                ErrorMessage()
                return
            
            chosen_item['PRICE'] = new


    if not Confirming():
        return

    if not ReWriteStorage(lines):
                return

    

#checks if sales history is empty, if so, it shows a mesagge to the user and returns true to "ShowHistory".
def HistoryIsEmpty():

    try:
        if os.path.getsize("history.bin") == 0:
            print(Fore.YELLOW + "\n-----------------HISTORY IS CURRENTLY EMPTY-----------------\n" + Style.RESET_ALL)
            return True

    except FileNotFoundError:
        print(Fore.RED + "\nHISTORY COULD NOT BE OPEN. TRY AGAIN LATER.\n" + Style.RESET_ALL)
        return True
    
    return False



#Loads the data in history and saves it in the variable "data"
def LoadHistory():

    data = []

    try:
        with open("history.bin", "rb") as file:
            while True:
                try:

                    data.append(pickle.load(file))
                
                except EOFError:
                    break

    except FileNotFoundError:
        print(Fore.RED + "\nHISTORY COULD NOT BE OPEN. TRY AGAIN LATER.\n" + Style.RESET_ALL)
        return
    
    return data




#Displays all content in sales history
def ShowHistory():

    if HistoryIsEmpty():
        return
    

    data = LoadHistory()
    if data is None:
        return
    
    print("\n*****************************************************SALES HISTORY*****************************************************\n")
    
    print(f"{'NAME':^20} | {'STATUS':^10} | {'ID':^10} | {'PIECES':^7} | {'TYPE':^17} | {'BRAND':^25} | {'PRICE (EACH)':^10} | {'TOTAL':^10}\n")
    
    for item in data:
        print(" ")
        print("-" * 130)
        print(f"\n{item['NAME']:^20} | {item['STATUS']:^10} | {item['ID']:^10} | {item['QUANTITY']:^7} | {item['TYPE']:^17} | {item['BRAND']:^25} | {item['PRICE']:^10} | {item['FINAL_PRICE']:^10}\n")
        print("-" * 130)
        print()

    



#this little function allows the user to either exit or return to main menu after using any function.
def AfterFunct():

    print(Fore.LIGHTBLUE_EX + "\nNOW WHAT?" + Style.RESET_ALL)

    while True:
        print("RETURN TO MAIN MENU -> 1")
        print("EXIT PROGRAM -> 2")
        print("------------------------")

        try:
            opt = int(input("ENTER THE OPTION: "))

            if opt not in [1, 2]:
                print(Fore.RED + "\nINVALID OPTION. TRY AGAIN: \n" + Style.RESET_ALL)
                continue
                
            break

        except ValueError:
            print(Fore.RED + "\nINVALID VALUE. TRY AGAIN: \n" + Style.RESET_ALL)


    if opt == 2:
        print("\nLEAVING...")
        sys.exit(0)

    



ID_NOW = DetectHighestID() + 1
#****************main code****************

print("---------------------------------WELCOME---------------------------------")


if not os.path.exists("providers.bin"):
    CreateProviders()



while True:
    print(Fore.BLUE + "\n     MAIN MENU    " + Style.RESET_ALL)

    print("************************")
    print("BUY AS CUSTOMER -> A")
    print("BUY AS SELLER -> B")
    print("DISPLAY STORED ITEMS -> C")
    print("DELETE ITEM FROM STORAGE -> D")
    print("EDIT ITEM IN STORAGE -> E")
    print("VIEW SALE HISTORY -> F")
    print("EXIT -> Z")
    print("************************")
    opt = input("ENTER AN OPTION: ").upper()


    if not opt.isalpha() or opt not in ['A', 'B', 'C', 'D', 'E', 'F', 'Z']:
        print(Fore.RED + "\nINVALID OPTION. TRY AGAIN: \n" + Style.RESET_ALL)
        continue


    match opt:

        case 'A':
            OrderAsCustumer()
            AfterFunct()


        case 'B':
            OrderAsSeller()
            AfterFunct()


        case 'C':
            Displaying()
            AfterFunct()


        case 'D':
            Deleting()
            AfterFunct()


        case 'E':
            Editing()
            AfterFunct()


        case 'F':
            ShowHistory()
            AfterFunct()


        case 'Z':
            print(Fore.YELLOW + "\nLEAVING..." + Style.RESET_ALL)
            
            sys.exit(0)



