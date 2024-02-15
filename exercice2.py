import os


def remove_user():
    confirm = "N"
    while confirm != "Y":
        username = input("Indiquez le nom de l'utilisateur à supprimer: ")
        print("Supprimer l'utilisateur : '" + username + "'? (Y/N)")
        confirm = input().upper()
    os.system("sudo userdel -r " + username) 
