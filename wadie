import pyfiglet
print(pyfiglet.figlet_format("email creator"))
import rich
from rich import print
name = input("Enter your first name :")
nickname = input("Enter your nickname :")
birth_year = int(input("Enter your birth year :"))

birth_year = int(birth_year)

name = name.lower()
nickname = nickname.title()

email = name + "-" + nickname + "_" + str(birth_year) + "@gmail.com"
username = name + "." + nickname + "-" + str(birth_year)

email = "[bold red]"+ email
username = "[italic blue]"+ username

if birth_year > 2026:
    print("Invalid birth year.")
elif birth_year < 1912:
    print("Invali birth year.")    
else:
    print("")
    print("   ---Your account details---")
    print("Your email is : " +email)
    print("Your email username is :"+username)
