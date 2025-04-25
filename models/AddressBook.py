from collections import UserDict
from colorama import Fore

#  5. Адресна книга: зберігає всі записи
class AddressBook(UserDict): 
           
    def add_record(self, record): # додає телефон 
        self.data[record.name.value] = record
        
    def find(self, name): # повертає на ім'я 
        return self.data.get(name) 
    
    def delete(self, name): # видаляє на ім'я 
        
        if name in self.data:
            removed = self.data[name]
            del self.data[name]
            print(f"{Fore.YELLOW}>>> DELETED {removed}{Fore.RESET}")
        else:                
            print(f"{Fore.RED}!!! Contact name: '{name}' not found.{Fore.RESET}")
            return None  
    
    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())