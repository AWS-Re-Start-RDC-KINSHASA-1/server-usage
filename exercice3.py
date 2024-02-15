import os
import subprocess


def add_user_to_group():
    username = input("Indiquez le nom de l'utilisateur à ajouter à ungroupe: ")
    output = subprocess.Popen('groups', stdout=subprocess.PIPE).communicate()[0]
    print("Entrez une liste de groupes auxquels ajouter l'utilisateur")
    print("La liste doit être séparée par des espaces, par exemple:\r\n group1 group2 groupe3")
    print("Les groupes disponibles sont :\r\n " + output)
    chosenGroups = str(input("Groups: "))

    output = output.split(" ")
    chosenGroups = chosenGroups.split(" ")
    print("Ajouter à:")
    found = True
    groupString = ""
    for grp in chosenGroups:
        for existingGrp in output:
            if grp == existingGrp:
                found = True
                print("-Groupe existant : " + grp)
                groupString = groupString + grp + ","
        if found == False:
            print("-Nouveau groupe : " + grp)
            groupString = groupString + grp + ","
        else:
            found = False
            groupString = groupString[:-1] + " "
            confirm = " "
            while confirm != "Y" and confirm != "N" :
                print("Ajouter un utilisateur '" + username + "' à ces groupes? (Y/N)")
                confirm = input().upper()
            if confirm == "N":
                print("Utilisateur '" + username + "' non ajouté")
            elif confirm == "Y":
                os.system("sudo usermod -aG " + groupString + username)
                print("Utilisateur'" + username + "' ajouté")



