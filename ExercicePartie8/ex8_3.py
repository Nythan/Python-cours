def saisirOption(min:int,max:int) -> int:
    ok = False
    print("Saisir un entier compris entre ", min, " et ", max, end=" : ")
    while not ok:
        try:
            saisi = int(input())
            if min<=saisi<=max:
                ok = True
            else:
                print("Vous n'avez pas saisi un entier compris entre ",min," et ",max, "recommencé : ", end="")

        except ValueError:
            print("Vous n'avez pas saisi un entier recommencé écrivez un entier compris entre : ",min," et ",max, end=" : ")
    return saisi


def menu(listeOptions:list):
    for i in range(len(listeOptions)):
        print(i,listeOptions[i])
    option = saisirOption(0,len(listeOptions)-1)
    print("l'option que vous avez choisi est l'option n°",option, " qui correspond à : ", listeOptions[option])



optionList = ["youh ouh", "test", "yolo"]

menu(optionList)