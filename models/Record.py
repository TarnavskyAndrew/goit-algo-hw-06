from models.Phone import Phone
from models.Name import Name
# from colorama import Fore


# 4. Клас запису: описує один запис (контакт): ім'я + список телефонів
class Record: 
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        
    def add_phone(self, phone_str): #додає телефон 
        # new_phone = Phone(phone_str) # Створюється об'єкт класу Phone 
        # self.phones.append(new_phone) # Додаємо об'єкт Phone() до цього списку self.phones (class Record) 
        
        self.phones.append(Phone(phone_str))
        
        
    def remove_phone(self, phone_str): # видаляє телефон     
        # for i, phone in enumerate(self.phones):
        #     if phone.value == phone_str:
        #         removed = self.phones.pop(i)                
        #         print(f"{Fore.YELLOW}>>> DELETED phone = {phone} {Fore.RESET}")
        #         return
        # print(f"{Fore.RED}!!! Phone '{phone_str}' not found.{Fore.RESET}")
        # return None     

        phone = self.find_phone(phone_str)
        if phone:
            self.phones.remove(phone)
        else:
            print(f"Phone '{phone_str}' not found.")
            return None                
            
            
    def edit_phone(self, old, new): # замінює телефон, інакше `ValueError
        
        # for i, phone in enumerate(self.phones):
            # if phone.value == old:
                # self.phones[i] = Phone(new)
                # print(f"{Fore.YELLOW}>>> EDIT old_phone = {old} changed to {Phone(new)} {Fore.RESET}")
                # return
        # raise ValueError(f"{Fore.RED}!!! Phone number {old} not found.{Fore.RESET}")

        phone = self.find_phone(old)
        if phone:
            self.remove_phone(old)
            self.add_phone(new)
        else:
            raise ValueError(f"Phone number {old} not found.")
           
        
    def find_phone(self, phone_str): #повертає `Phone` або None
        
        for phone in self.phones:
            if phone.value == phone_str:
                return phone
        return None
    
    def __str__(self):
        phones = "; ".join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones}"
