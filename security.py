
import re
import hashlib
import sys

print(" ")
print("SECURITY MANAGEMENT SYSTEM")
print("--------------------------")
print(" ")

# chatgpt
# Client Emojis 🤵🏻 📞 💼 

class User:
    
    def __init__(self, username, password, role):
        self.username = username
        self.password = self.hash_password(password)
        self.role = role

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
 
    def verify_password(self, password):
        return self.password == hashlib.sha256(password.encode()).hexdigest()


class Auth:
         
    def __init__(self):
        self.users = {}

    def Register(self, username, password, role="admin" ):
        
        if username in self.users: 
            print(f"User '{username}' already exists! ⛔")
        
        else:
            new_user = User(username, password, role)
            self.users[username] = new_user
            print(f"User '{username}' registered successfully! ✔️")


    def login(self, username, password):
        
        user = self.users.get(username)
        
        if user and user.verify_password(password):

            print(f"User '{username}' logged in successfully! 🎉")
            self.post_login_menu()   
            return user 
        
        else:
            print(f"Invalid credentials for user '{username}'")
            return None
 
    def post_login_menu(self):
        
        while True:
            print(" ")
            print("1. Add Security 👮")
            print("2. Add Client 🤵")
            print("3. Allocate Security 👨🏻‍💻")
            print("4. Logout 🔒")
            print(" ")

            menu = input("Select an option: ")

            if menu == "1":
                obj = SecurityManagementSystem()
                obj.display()

            elif menu == "2":
                obj = ClientManagementSystem()
                obj.client_details()

            elif menu == "3":
                obj = AssigneeManagementSystem()
                obj.assign()

            elif menu == "4":
                print("Logging out...")  
                print(f"User logged out successfully. 👋")
                sys.exit(0)
                 
            else:
                print("Invalid choice. Please try again.")


class ClientManagementSystem:

    clients_details = []

    def __init__(self):
        self.name = input("Enter Company Name: ")  
        self.location = input("Enter Client preferred Location: ")
        self.agepreference = input("Enter Age preference: ")


    def client_details(self):
        
        ClientManagementSystem.clients_details.append({
                'c_name': self.name,
                'c_location': self.location.lower(),
                'c_age': self.agepreference
            })
        
        print(" ")
        conf_c = input("Do you want to add more security details (Y/N) : ")
        print(" ")

        if conf_c.upper() == "Y":
            obj2 = ClientManagementSystem()
            obj2.client_details()
        else:
            print("Final list of Clients")
            print("---------------------")
            for i, details in enumerate(ClientManagementSystem.clients_details, 1):
                print(f"Security {i}: {details}")


class SecurityManagementSystem:
    
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
            
            SecurityManagementSystem.securities.append({
                'name': self.name,
                'location': self.location.lower(),
                'age': self.age,
                'pancard': self.pancard
            })

            print(" ")
            conf = input("Do you want to add more security details (Y/N) : ")
            print(" ")

            if conf.upper() == "Y":
                obj = SecurityManagementSystem()
                obj.display()   
            else:
                print("Final list of securities")
                print("------------------------")
                for i, details in enumerate(SecurityManagementSystem.securities, 1):
                    print(f"Security {i}: {details}")
        else:
            print("Please recheck your pancard number")


class AssigneeManagementSystem:
    
    assigned_securities = []

    def assign(self):
        
        print(" ")
        print("Client Details")
        for k, cl_details in enumerate(ClientManagementSystem.clients_details, 1):
            print(f"Client {k}: {cl_details}")


        print(" ")
        print("Security Details")
        for i, details in enumerate(SecurityManagementSystem.securities, 1):
            print(f"Security {i}: {details}")

        print(" ")
        client = int(input("Select a Client to assign(Client number): "))
        security = int(input("Select a Security to assign(Security number): "))
        
        assigned_client = ClientManagementSystem.clients_details[client - 1]
        assigned_security = SecurityManagementSystem.securities[security - 1]

        # print(assigned_client['c_name'])
        # print(assigned_security)

        AssigneeManagementSystem.assigned_securities.append({
                'security': assigned_security['name'],
                'client': assigned_client['c_name'],
                'assigned_location':assigned_client['c_location']
            })
 
        print(f"\nSecurity '{assigned_security['name']}' has been assigned to client '{assigned_client['c_name']}'.")

        print(" ")
        ass_conf = input("Do you want to add more security details (Y/N) : ")
        print(" ")

        if ass_conf.upper() == "Y":
            obj3 = AssigneeManagementSystem()
            obj3.assign()   
        else:
            print("Assigned Employee Details")
            print("-------------------------")
            for j, assignd_details in enumerate(AssigneeManagementSystem.assigned_securities, 1):
                print(f"Assignee {j}: {assignd_details}")


def main():
    
    system = Auth()
    logged_in_user = 1
    
    while True:

        if logged_in_user == 1: 
            
            print("1.📑  Register")
            print("2.🔓  Login")
            print("3.🔚  Exit")
            choice = input("Enter choice: ")

            if choice == "1":
                username = input("👨🏻‍💼 Enter username: ")
                password = input("🔑 Enter password: ")
                role = "admin"
                system.Register(username, password, role)

            elif choice == "2":
                logged_in_user = 2
                username = input("Enter username: ")
                password = input("Enter password: ")
                system.login(username, password)
                
            elif choice == "3":
                print("Exiting system...") 
                print("Thank you for your Valuable Time...") 
                sys.exit(0)

            else:
                print("Invalid choice. Please try again.")

        elif logged_in_user == 2:  
            system.post_login_menu()
             

if __name__ == "__main__":
    main()
