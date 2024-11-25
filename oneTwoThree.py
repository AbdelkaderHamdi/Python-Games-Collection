
c = 0
while c < 21:
    n = int(input("Joueur A Donner un entier (1, 2 ou 3) : "))
    while n > 3 or n < 1:
        n = int(input("Donner un entier (1, 2 ou 3) : "))
    c = c + n
    print("Le compteur = ", c)
    if c > 20:
        print("Le joueur B (ordinateur) a gagné 🙂")
        break
    else:
        # Stratégie pour que le joueur B (ordinateur) gagne
        if (c % 4) == 0 or (c%4)==1:
            m = 3
        elif (c % 4) == 2:
            m = 2
        else:
            m = 1
        
        print("Joueur B (ordinateur) propose un entier: ", m)
        c = c + m
        print("Le compteur = ", c)
        if c > 20:
            print("Le joueur A a gagné 🙂")
            break
