from models.AddressBook import AddressBook
from models.Record import Record
from colorama import Fore



def main():
    
    print(f"{Fore.GREEN}>>>{Fore.RESET}"*30) 
     
    book = AddressBook()
    rec = Record("Anatoliy")
       
    # Додамо телефони 
    rec.add_phone("1234567890")
    rec.add_phone("0987654321")
    rec.add_phone("1112223331")
 
    # Додамо запис до книги 
    book.add_record(rec)

    # Знайти запис 
    print(f"{Fore.GREEN}>>>{Fore.RESET} FIND RECORD:", book.find("Anatoliy"))
    
    # Знайти номер 
    phone = rec.find_phone("1234567890")
    print(f"{Fore.GREEN}>>>{Fore.RESET} FOUND PHONE:", phone)

    # Редагувати номер 
    rec.edit_phone("1234567890", "0502577755")

    # Видалити номер 
    rec.remove_phone("0987654321")

    # Вивід книги
    print(f"\n{Fore.GREEN}>>>{Fore.RESET} FULL ADDRESSBOOK:\n", book)
    
    print(f"{Fore.GREEN}>>>{Fore.RESET} LIST OF ALL NAMES:", list(book.keys()))

    # Видалити запис 
    book.delete("Anatoliy")  
    print(f"{Fore.GREEN}>>>{Fore.RESET} AFTER DELETE:\n", book.find("Anatoliy"))
    book.delete("Anatoliy")
    
    
if __name__ == "__main__":
    main()
    
    

   