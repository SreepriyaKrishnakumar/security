import re

class Security:
    
    securities = []

    def __init__(self):
        self.name = input("Enter security Name: ")
        self.location = input("Enter security preferred Location: ")
        self.age = int(input("Enter Age: "))
        self.pancard = input("Enter pancard Number: ")

    def display(self):
        
        pan_no = self.pancard
 
        pattern = r'\b[A-Z]{5}[0-9]{4}[A-Z]{1}\b'

        match = re.findall(pattern, pan_no)

        if match:  
            
            Security.securities.append({
                'name': self.name,
                'location': self.location,
                'age': self.age,
                'pancard': self.pancard
            })

            conf = input("Do you want to add more security details (Y/N) : ")

            if conf.upper() == "Y":
                obj = Security()
                obj.display()  # Recursively handle adding more details
            else:
                print("Final list of securities:")
                for i, details in enumerate(Security.securities, 1):
                    print(f"Security {i}: {details}")
        else:
            print("Please recheck your pancard number")


class Client:

    clients = []

    def __init__(self):
        self.name = input("Enter security Name: ")  
        self.location = input("Enter security preferred Location: ")
        self.agepreference = int(input("Enter Age: ")) 

    
    



obj = Security()
obj.display()
