# --------------------------------------------------EL GARMIT GAALOUL---------------------------------------------------

# ---------------------------------------------------- Décor du Jeu ----------------------------------------------------

from turtle import *


def Decor():
    tracer(50, 0)
    speed(0)
    hideturtle()
    bgcolor("#003366")

    def ombreville(x, y):
        pensize(5)
        speed(0)
        up()
        setposition(x, y)
        down()
        begin_fill()
        color("#24445C", "#24445C")
        right(160)
        circle(2900, -40)
        end_fill()
        up()
        setheading(0)

    def villes(x, y):
        speed(0)
        setposition(x, y)
        down()
        begin_fill()
        color("black", "black")
        up()
        setposition(x, y)
        down()
        n = 30
        i = 0
        while i < 5:
            for k in range(2):
                fd(n)
                left(90)
                fd(n * 2)
                left(90)

            fd(n)
            for k in range(2):
                fd(n * 1.5)
                left(90)
                fd(n * 1.5)
                left(90)
            fd(n * 1.5)
            for k in range(2):
                fd(n)
                left(90)
                fd(n * 3)
                left(90)
            fd(n)
            for k in range(2):
                fd(n * 2)
                left(90)
                fd(n)
                left(90)
            fd(n * 2)
            for k in range(2):
                fd(n * 1.5)
                left(90)
                fd(n * 2)
                left(90)
            fd(n * 1.5)
            for k in range(2):
                fd(n * 2)
                left(90)
                fd(n * 3)
                left(90)
            fd(n * 2)
            for k in range(2):
                fd(n * 1.5)
                left(90)
                fd(n * 1.5)
                left(90)
            fd(n * 1.5)
            for k in range(2):
                fd(n)
                left(90)
                fd(n * 4)
                left(90)
            fd(n)
            i = i + 1
        end_fill()

    def muretsol(x, y):
        speed(0)
        pensize(5)
        up()
        setposition(x, y)
        down()
        begin_fill()
        color("black", "#C8AD7F")
        for k in range(2):
            fd(2000)
            right(90)
            fd(200)
            right(90)
        end_fill()
        right(90)
        fd(200)
        left(90)
        begin_fill()
        color("black", "#606060")
        for k in range(2):
            fd(2000)
            right(90)
            fd(50)
            right(90)
        end_fill()
        right(90)
        fd(50)
        left(90)
        begin_fill()
        color("black", "#120D16")
        for k in range(2):
            fd(2000)
            right(90)
            fd(250)
            right(90)
        end_fill()
        i = 0
        begin_fill()
        color("black", "#606060")
        while i < 80:
            for k in range(2):
                fd(2000 / 100)
                right(90)
                fd(20)
                right(90)
            fd(20)
            i = i + 1
        end_fill()

    def etoile(x, y, t):
        pensize(1)
        up()
        setposition(x, y)
        down()
        begin_fill()
        color("white")
        for k in range(4):
            fd(t)
            bk(t)
            right(45)
            fd(t / 2)
            bk(t / 2)
            right(45)
        end_fill()

    def afficheLampadaire(x, y, Longeur, TailleAmpoule):
        setheading(0)
        pensize(4)
        up()
        setposition(x, y)
        down()
        begin_fill()
        color("black", "grey")
        for k in range(2):
            fd(Longeur)
            left(90)
            fd(TailleAmpoule)
            left(90)
        end_fill()
        up()
        setx(x + (3 / 4 * Longeur))
        sety(y + TailleAmpoule)
        down()
        setheading(90)
        color("black", "grey")
        begin_fill()
        for k in range(2):
            fd(Longeur * 2)
            left(90)
            fd(Longeur / 2)
            left(90)
        end_fill()
        up()
        sety(y + (TailleAmpoule + (Longeur * 2)))
        left(90)
        fd((Longeur / 2) / (7 / 2))
        right(90)
        down()
        color("black", "grey")
        begin_fill()
        for k in range(2):
            fd(Longeur * 4)
            left(90)
            fd((Longeur / 2) / 2.5)
            left(90)
        end_fill()
        fd(Longeur * 4)
        color("black", "grey")
        begin_fill()
        circle(Longeur, 135)
        left(90)
        fd((Longeur / 2) / 2.5)
        left(90)
        circle(-(Longeur - ((Longeur / 2) / (7 / 2)) * (3 / 2)), 135)
        end_fill()
        right(180)
        up()
        circle(Longeur * 2 / 3, 135)
        down()
        color("black", "grey")
        begin_fill()
        for k in range(2):
            fd((Longeur / 2) / 2.5)
            right(90)
            fd(3.5 * ((Longeur / 2) / 2.5))
            right(90)
        end_fill()
        up()
        right(90)
        fd((3.5 * ((Longeur / 2) / 2.5)) / 2)
        left(90)
        fd((Longeur / 2) / 2.5)
        left(90)
        down()
        color("black", "yellow")
        begin_fill()
        circle(-TailleAmpoule)
        end_fill()

    def afficheLampadaire2(x, y, Longeur, TailleAmpoule):
        setheading(0)
        pensize(4)
        up()
        setposition(x, y)
        down()
        begin_fill()
        color("black", "grey")
        for k in range(2):
            fd(Longeur)
            left(90)
            fd(TailleAmpoule)
            left(90)
        end_fill()
        up()
        setx(x + (3 / 4 * Longeur))
        sety(y + TailleAmpoule)
        down()
        setheading(90)
        color("black", "grey")
        begin_fill()
        for k in range(2):
            fd(Longeur * 2)
            left(90)
            fd(Longeur / 2)
            left(90)
        end_fill()
        up()
        sety(y + (TailleAmpoule + (Longeur * 2)))
        left(90)
        fd((Longeur / 2) / (7 / 2))
        right(90)
        down()
        color("black", "grey")
        begin_fill()
        for k in range(2):
            fd(Longeur * 4)
            left(90)
            fd((Longeur / 2) / 2.5)
            left(90)
        end_fill()
        fd(Longeur * 4)
        color("black", "grey")
        begin_fill()
        circle(-(Longeur - ((Longeur / 2) / (7 / 2)) * (3 / 2)), 135)
        left(90)
        fd((Longeur / 2) / 2.5)
        left(90)
        circle(Longeur, 135)
        end_fill()
        up()
        left(90)
        fd((Longeur / 2) / 2.5)
        left(90)
        circle(-(Longeur * 2 / 3), 135)
        down()
        color("black", "grey")
        begin_fill()
        for k in range(2):
            fd((Longeur / 2) / 2.5)
            right(90)
            fd(-(3.5 * ((Longeur / 2) / 2.5)))
            right(90)
        end_fill()
        up()
        right(90)
        fd((-(3.5 * ((Longeur / 2) / 2.5))) / 2)
        left(90)
        fd((Longeur / 2) / 2.5)
        left(90)
        down()
        color("black", "yellow")
        begin_fill()
        circle(-TailleAmpoule)
        end_fill()

    ombreville(-945, 50)
    villes(-800, 50)
    muretsol(-875, 50)
    etoile(-600, 330, 10)
    etoile(-460, 300, 10)
    etoile(-310, 270, 10)
    etoile(-160, 310, 10)
    etoile(-50, 330, 10)
    etoile(100, 250, 10)
    etoile(200, 325, 10)
    etoile(300, 275, 10)
    etoile(400, 330, 10)
    etoile(550, 300, 10)
    afficheLampadaire(580, -185, 50, 25)
    afficheLampadaire2(-500, -185, 50, 25)


# -----------------------EL GARMIT GAALOUL-------------------------

from turtle import *


def ChoixOrdi(ChoixOrdi):
    tracer(50, 0)
    up()
    setposition(-685, -50)
    down()
    pencolor("black")
    write("L'ordinateur Joue : ", font=("Marker Felt", 14, "bold"))
    up()
    setheading(0)
    setposition(-636, -110)
    down()
    begin_fill()
    color("#C8AD7F", "#C8AD7F")
    for k in range(2):
        fd(110)
        left(90)
        fd(60)
        left(90)
    end_fill()
    pencolor("black")
    write(ChoixOrdi, font=("Marker Felt", 33, "bold"))


# --------------------------EL GARMIT GAALOUL------------------------------

from turtle import *


def NbTour(Nbtour):
    tracer(50, 0)
    up()
    setheading(0)
    setposition(-665, 0)
    down()
    begin_fill()
    color("#C8AD7F", "#C8AD7F")
    for k in range(2):
        fd(160)
        left(90)
        fd(40)
        left(90)
    end_fill()
    pencolor("black")
    write("Tour " + str(Nbtour), font=("Marker Felt", 33, "bold"))


# --------------------------------------------------EL GARMIT GAALOUL------------------------------------------------------------

# ------------------------------------------------------EXERCICE 1---------------------------------------------------------------
from turtle import *


def afficheQuilles(q, n):
    NbLignes = len(q)
    i = 0
    SchemaFinale = ""

    # Cas où il n'y a pas de quilles debout, donc pas de liste,
    if NbLignes == 0:
        SchemaFinale = SchemaFinale + "." * n

    # Cas où il y au moins une quille debout
    else:

        # Cette première boucle while va nous permettre d'étudier toutes les quilles une à une et
        # elle va surtout nous permettre de délimiter le nombre de quilles à afficher pour ne pas
        # qu'il y en ait plus que prévu au final.
        while i < n:
            x = 0

            # Cette deuxième boucle va nous permettre d'étudier toutes les listes de quilles debout
            while x < NbLignes:

                # Ce if nous permet de savoir si la quille etudiée (i) est bien la première quille debout d'une liste,
                # n'importe laquelle
                if i == q[x][0]:

                    # Cas où i (la quille etudiée) est la premiere quille debout de la première liste
                    if x == 0:

                        # Cette variable permet de calculer le nombre d'éléments (donc de quilles parterre),
                        # de 0 jusqu'à la première liste ainsi que le nombre d'éléments dans la première liste (donc de
                        # quilles debout), bien sûr si ces quilles existent, et de les multiplier par leur symbole, "|"
                        # pour debout et "." pour parterre.
                        QuillesJusquaPrmListe = ((q[x][0] - 1) + 1) * "." + (q[x][1] - (q[x][0] - 1)) * "|"

                        # Ici l'ordi retient cet enchaînement de caractère, dans le bon sens pour pouvoir l'afficher
                        # à la fin de la procédure, dans ce cas là (if).
                        SchemaFinale = SchemaFinale + QuillesJusquaPrmListe

                    # Cas où la quille etudiée (i) n'est pas la première quille debout de la première liste
                    else:

                        # Cette variable fait la même chose que la précédente sauf que l'on part plus de zéro mais de
                        # la fin de la liste précédente jusqu'à la fin de la liste suivante.
                        QuillesEntrePrmDrnListe = (q[x][0] - (q[x - 1][1] - 1) - 2) * "." + (
                                    q[x][1] - (q[x][0] - 1)) * "|"

                        # Ici l'ordi retient encore cet enchaînement de caractère, pour pouvoir l'afficher
                        # à la fin de la procédure, mais dans ce cas là (else).
                        SchemaFinale = SchemaFinale + QuillesEntrePrmDrnListe
                x = x + 1
            i = i + 1

        # Cette dernière variable permet de calculer le nombre de quilles parterre, donc d'élément, entre la dernière
        # liste et la dernière quille, si il y en a biensûr.
        DernierresQuilles = (n - 1) - q[len(q) - 1][1]

        # Ici l'ordi ajoute à l'enchaînement de caractère sortie de la boucle while la dernière ligne de quilles
        # parterre si elle existe.
        SchemaFinale = SchemaFinale + "." * DernierresQuilles

    # Enfin la fonction renvoie l'enchaînement final de quilles (de caractère).
    return SchemaFinale


# ------------------------------------------------------EXERCICE 2---------------------------------------------------------------

def ordiJoue(q):
    NbLignes = len(q)

    # Premièrement on fait choisir la ligne et la position à l'ordinateur grâce aux fonction randint et choice.
    from random import choice
    from random import randint
    ChoixLigne = randint(1, NbLignes)
    ChoixPosition = choice(["G", "M", "D"])

    # La fonction définie retient le numéro de ligne rentré par l'ordinateur et la position
    # sous la forme demandée et en str.

    ChoixOrdi(str(ChoixLigne) + ":" + ChoixPosition)
    return str(ChoixLigne) + ":" + ChoixPosition


# ------------------------------------------------------EXERCICE 3---------------------------------------------------------------

def joueurJoue(q):
    NbLignes = len(q)

    # Premierèment on fait choisir la ligne au joueur.
    ChoixLigne = textinput("À vous de jouer", "Veuillez entrer une ligne de flamme à viser: (nombre attendue)")

    # Si la ligne n'est pas valide on lui redemande de choisir une ligne avec une précision sur le nombre
    # de lignes possibles, pour l'aider et ceci tant que la ligne rentrée n'est pas valide (boucle while).
    while ChoixLigne not in str(range(1, NbLignes)) or ChoixLigne in ["", " ", ","]:
        ChoixLigne = textinput("À vous de jouer",
                               "Veuillez rerentrer un numero de ligne valide entre 1 et " + str(NbLignes) + " :")

    # Deuxièmement on fait choisir la position au joueur
    ChoixPosition = textinput("À vous de jouer",
                              "Veuillez entrer une position parmi M (milieu) , G (gauche) et D (droite) :")

    # Si la position n'est pas valide on lui redemande de choisir une position et ceci tant que
    # la position rentrée n'est pas valide (boucle while).
    while ChoixPosition not in ["M", "G", "D"]:
        ChoixPosition = textinput("À vous de jouer",
                                  "Veuillez rerentrer une position valide parmi M (milieu) , G (gauche) et D (droite) :")

    # Finalement la fonction retient le numéro de ligne rentré par le joueur et la position
    # sous la forme demandé et en str.
    return str(ChoixLigne) + ":" + ChoixPosition


# ------------------------------------------------------EXERCICE 4---------------------------------------------------------------
# Première Partie : procédures jouerCote et jouerMilieu -------------------------------------------------------------------

# Cette procédure correspond au cas où le joueur joue sur un côté, gauche ou droite.
def jouerCote(c, q):
    nbElementListe = q[int(c[0]) - 1][1] - ((q[int(c[0]) - 1][0]) - 1)
    if c[2] == "D" or c[2] == "G":

        # Cas ou le joueur choisit une liste à un élément
        if nbElementListe == 1:

            # Dans ce cas là liste est supprimée tout simplement car droite ou gauche c'est pareil
            # la quille va tomber dans tout les cas
            q.remove(q[int(c[0]) - 1])

        # Cas où le joueur choisit de jouer à droite
        elif c[2] == "D":

            # On enlève une quille à droite de la liste choisie, en soustrayant 1 à l'index de la dernière quille
            # debout de la liste
            FinLimiteListeModifier = (q[int(c[0]) - 1][1]) - 1
            q[int(c[0]) - 1].remove(q[int(c[0]) - 1][1])
            q[int(c[0]) - 1].append(FinLimiteListeModifier)

        # Cas où le joueur choisit de jouer à gauche
        elif c[2] == "G":

            # On enlève une quille à gauche de la liste choise en ajoutant 1 à l'index de la première quille
            # debout de la liste
            DbtLimiteListeModifier = (q[int(c[0]) - 1][0]) + 1
            q[int(c[0]) - 1].remove(q[int(c[0]) - 1][0])
            q[int(c[0]) - 1].insert(0, DbtLimiteListeModifier)


# Cette procédure correspond au cas où le joueur joue au milieu.
def jouerMilieu(c, q):
    nbElementListe = q[int(c[0]) - 1][1] - ((q[int(c[0]) - 1][0]) - 1)
    if c[2] == "M":

        # Cas où le joueur choisit une liste à un élément
        if nbElementListe == 1:

            # Dans ce cas là liste est supprimée tout simplement
            q.remove(q[int(c[0]) - 1])

        # Cas où le joueur choisit une liste à deux éléments
        elif nbElementListe == 2:

            # Dans ce cas là la liste aussi est supprimée car lorsque l'on choisit de jouer au milieu
            # deux quilles tombent
            q.remove(q[int(c[0]) - 1])

        # Cas où le joueur choisit une liste à trois éléments
        elif nbElementListe == 3:

            # Cette variable permet de calculer la nouvelle quille de départ de
            # la liste de quille debout
            FinLimiteListeModifier = (q[int(c[0]) - 1][1]) - 2

            # Ici on change simplement l'ancienne quille de depart de la liste de
            # quille debout par la nouvelle
            q[int(c[0]) - 1].remove(q[int(c[0]) - 1][1])
            q[int(c[0]) - 1].append(FinLimiteListeModifier)

        # Cas où le joueur choisit une liste à plus de 3 éléments
        elif nbElementListe > 3:

            # Dans ce cas là la liste est divisée en deux il faut donc modifier la liste existante et
            # en créer une autre

            # Cette variable permet de calculer l'index de la dernière quille debout de la liste créée
            FinLimitePremiereListe = (int(nbElementListe / 2) - 1) - 1

            # Cette variable permet de calculer l'index de la première quille debout de la liste de base
            DbtLimiteDeuxiemeListe = (int(nbElementListe / 2) - 1) + 2
            DbtListeModifier = q[int(c[0]) - 1][0]

            # Donc ici on change la première quille debout de la liste de base par la nouvelle
            q[int(c[0]) - 1].remove(q[int(c[0]) - 1][0])
            q[int(c[0]) - 1].insert(0, DbtLimiteDeuxiemeListe)

            # Et ici on crée la nouvelle liste avec comme première quille debout celle de la liste
            # de base et on met en dernière quille debout la variable que l'on a calculé précédemment.
            # On place cette nouvelle liste à la place de l'ancienne pour que tout soit dans l'ordre
            q.insert((int(c[0]) - 1), [DbtListeModifier, FinLimitePremiereListe])


# Deuxieme Partie (FINAL): Procedure jouer -----------------------------------------------------------------------------


# Pour cette procédure nous avons juste additioné les procédures précédentes
# le premier if correspond à la procédure jouerCote et le deuxiéme if correspond
# à la procédure jouerMilieu
def jouer(c, q):
    nbElementListe = q[int(c[0]) - 1][1] - ((q[int(c[0]) - 1][0]) - 1)
    if c[2] == "D" or c[2] == "G":
        if nbElementListe == 1:
            q.remove(q[int(c[0]) - 1])
        elif c[2] == "D":
            FinLimiteListeModifier = (q[int(c[0]) - 1][1]) - 1
            q[int(c[0]) - 1].remove(q[int(c[0]) - 1][1])
            q[int(c[0]) - 1].append(FinLimiteListeModifier)
        elif c[2] == "G":
            DbtLimiteListeModifier = (q[int(c[0]) - 1][0]) + 1
            q[int(c[0]) - 1].remove(q[int(c[0]) - 1][0])
            q[int(c[0]) - 1].insert(0, DbtLimiteListeModifier)
    if c[2] == "M":
        if nbElementListe == 1:
            q.remove(q[int(c[0]) - 1])
        elif nbElementListe == 2:
            q.remove(q[int(c[0]) - 1])
        elif nbElementListe == 3:
            FinLimiteListeModifier = (q[int(c[0]) - 1][1]) - 2
            q[int(c[0]) - 1].remove(q[int(c[0]) - 1][1])
            q[int(c[0]) - 1].append(FinLimiteListeModifier)
        elif nbElementListe > 3:
            FinLimitePremiereListe = int((q[int(c[0]) - 1][0] + q[int(c[0]) - 1][1]) / 2) - 1
            DbtLimiteDeuxiemeListe = int((q[int(c[0]) - 1][0] + q[int(c[0]) - 1][1]) / 2) + 2
            DbtListeModifier = q[int(c[0]) - 1][0]
            q[int(c[0]) - 1].remove(q[int(c[0]) - 1][0])
            q[int(c[0]) - 1].insert(0, DbtLimiteDeuxiemeListe)
            q.insert((int(c[0]) - 1), [DbtListeModifier, FinLimitePremiereListe])


# -----------------------------------------------EL GARMIT GAALOUL----------------------------------------------------------

# ----------------------------------------------- Quilles Debout ---------------------------------------------------------

from turtle import *
from math import *


def QuillesDebout(x, y, n):
    tracer(50, 0)

    def Lesflammes(x, y, n):
        def Laflamme(x, y, n, c):
            setheading(0)
            up()
            setposition(x, y)
            down()
            pensize(2)
            begin_fill()
            color("black", c)
            left(60)
            fd(n)
            right(180 - 60)
            fd(n / 3)
            left(180 - 60)
            fd(n)
            right(180 - 60)
            fd(n)
            left(120)
            fd(n / 3)
            right(120)
            fd(n)
            setheading(0)
            left(120)
            circle(4 / 3 * n, -240)
            end_fill()

        Laflamme(x, y, n, "orange")
        Laflamme(x + n / 1.7, y - n / 3, n / 2, "yellow")

    Lesflammes(x, y, n)
    Lesflammes(x + 4 / 3 * n * 2, y, n)
    Lesflammes(x + (4 / 3 * n * 2) / 2, y - n * 1.5, n)

    def tuyau(x, y, t):
        setheading(0)
        speed(0)
        pensize(5)
        up()
        setposition(x, y)
        down()
        begin_fill()
        color("black", "red")
        for k in range(2):
            fd(t)
            left(90)
            fd(t * 1.5)
            left(90)
        end_fill()
        up()
        setposition(x, y + (1.5 * t))
        down()
        begin_fill()
        color("black", "grey")
        for k in range(2):
            fd(t)
            left(90)
            fd(t / 1.5)
            left(90)
        end_fill()
        pensize(3)
        up()
        setposition(x - (t / 3), y + (t * 1.5) + (t / 1.5))
        down()
        begin_fill()
        color("black", "grey")
        for k in range(2):
            fd((t / 3) * 2 + t)
            left(90)
            fd(t / 6)
            left(90)
        end_fill()
        begin_fill()
        color("black", "grey")
        for k in range(2):
            fd(t / 6)
            left(90)
            fd(t / 1.5)
            left(90)
        end_fill()
        fd((t / 3) * 2 + t - (t / 6))
        begin_fill()
        color("black", "grey")
        for k in range(2):
            fd(t / 6)
            left(90)
            fd(t / 1.5)
            left(90)
        end_fill()
        up()
        setposition(x, y + (1.5 * t) + t / 1.5 + (t / 6))
        down()
        begin_fill()
        color("black", "#318CE7")
        left(90)
        fd(t / 1.5)
        right(90)
        goto(x - (t / 3), y + (10 / 3) * t)
        for k in range(4):
            circle(t / 2, -180)
            left(120)
        goto(x + t, y + 3 * t)
        goto(x + t, y + (1.5 * t) + t / 1.5 + (t / 6))
        end_fill()
        L = 90
        up()
        setposition(1300 / 2, -800 / 2)
        setheading(0)
        left(90)
        down()
        begin_fill()
        color("black", "red")
        circle(-(L - ((L / 2) / (7 / 2)) * (3 / 2)), 90)
        left(90)
        fd((L / (5 / 2)))
        left(90)
        circle(L * 1.2, 90)
        end_fill()

    tuyau(40, -820 / 2, 55)


# ----------------------------------------------------EL GARMIT GAALOUL--------------------------------------------------

# --------------------------------------------------- Quilles Parterre -------------------------------------------------

from turtle import *
from math import *


def QuilleParterre(x, y, n):
    tracer(50, 0)

    def flammefinale(x, y, n):
        def Lesflammes(x, y, n):
            def Laflamme(x, y, n, c):
                setheading(0)
                up()
                setposition(x, y)
                down()
                pensize(4)
                begin_fill()
                color("#C8AD7F", c)
                left(60)
                fd(n)
                right(180 - 60)
                fd(n / 3)
                left(180 - 60)
                fd(n)
                right(180 - 60)
                fd(n)
                left(120)
                fd(n / 3)
                right(120)
                fd(n)
                setheading(0)
                left(120)
                circle(4 / 3 * n, -240)
                end_fill()

            Laflamme(x, y, n, "#C8AD7F")
            Laflamme(x + n / 1.7, y - n / 3, n / 2, "#C8AD7F")

        Lesflammes(x, y, n)
        Lesflammes(x + 4 / 3 * n * 2, y, n)
        Lesflammes(x + (4 / 3 * n * 2) / 2, y - n * 1.5, n)

    flammefinale(x, y, n)
    longeurcote = n / 2

    def brule(x, y, longeurcote):
        setheading(0)
        tracer(50)
        pensize(2)
        up()
        setposition(x, y)
        down()
        begin_fill()
        color("black", "grey")
        i = 0
        while i < 3:
            if i > 0:
                bk(longeurcote * 2)
            for k in range(2):
                fd(longeurcote * 2)
                left(90)
                fd(longeurcote)
                left(90)
            i = i + 1
        end_fill()
        begin_fill()
        sety(y + longeurcote)
        fd((longeurcote * 2 * 3) - (longeurcote))
        for k in range(2):
            fd(longeurcote)
            left(90)
            fd(longeurcote)
            left(90)
        i = 0
        while i < 3 - 1:
            bk(longeurcote * 2)
            for k in range(2):
                fd(longeurcote * 2)
                left(90)
                fd(longeurcote)
                left(90)
            i = i + 1
        bk(longeurcote)
        for k in range(2):
            fd(longeurcote)
            left(90)
            fd(longeurcote)
            left(90)
        end_fill()
        sety(y + (longeurcote * 2))
        fd((longeurcote * 2) * 3)
        i = 0
        while i < 3:
            begin_fill()
            bk(longeurcote * 2)
            for k in range(2):
                fd(longeurcote * 2)
                left(90)
                fd(longeurcote)
                left(90)
            end_fill()
            i = i + 1
        up()
        setposition(x + longeurcote, y)
        right(90)
        down()
        begin_fill()
        color("black", "black")
        circle(longeurcote, 270)
        end_fill()
        up()
        setposition(x - (longeurcote * 3.2), y)
        left(90)
        down()
        begin_fill()
        color("black", "black")
        circle(longeurcote, 180)
        end_fill()
        up()
        setposition(x - (longeurcote * 4), y + (longeurcote))
        right(90)
        down()
        begin_fill()
        color("black", "black")
        circle(longeurcote, -180)
        end_fill()
        up()
        setposition(x, y + (longeurcote * 3))
        right(90)
        down()
        begin_fill()
        color("black", "black")
        circle(longeurcote * 1.5, 180)
        end_fill()
        up()
        setposition(x - (longeurcote * 3), y + longeurcote * 3)
        left(90)
        down()
        begin_fill()
        color("black", "white")
        pensize(0.5)
        for k in range(5):
            circle(longeurcote, 180)
            right(108)
        end_fill()
        up()
        setposition(x + (longeurcote * 4.5), y + longeurcote * 2.5)
        down()
        begin_fill()
        color("black", "white")
        for k in range(7):
            circle(longeurcote, 180)
            right(128.5)
        end_fill()
        up()
        setposition(x + (longeurcote * 2), y - (longeurcote * 3))
        down()
        begin_fill()
        color("black", "white")
        for k in range(6):
            circle(longeurcote, 180)
            right(120)
        end_fill()
        up()
        setposition(x - (longeurcote * 3.5), y - (longeurcote * 1.5))
        down()
        begin_fill()
        color("black", "white")
        for k in range(4):
            circle(longeurcote, 180)
            right(90)
        end_fill()

    brule(x + 3 * n, y - n * 2, longeurcote)

    def tuyau(x, y, t):
        setheading(0)
        speed(0)
        pensize(5)
        up()
        setposition(x, y)
        down()
        begin_fill()
        color("black", "red")
        for k in range(2):
            fd(t)
            left(90)
            fd(t * 1.5)
            left(90)
        end_fill()
        up()
        setposition(x, y + (1.5 * t))
        down()
        begin_fill()
        color("black", "grey")
        for k in range(2):
            fd(t)
            left(90)
            fd(t / 1.5)
            left(90)
        end_fill()
        pensize(3)
        up()
        setposition(x - (t / 3), y + (t * 1.5) + (t / 1.5))
        down()
        begin_fill()
        color("black", "grey")
        for k in range(2):
            fd((t / 3) * 2 + t)
            left(90)
            fd(t / 6)
            left(90)
        end_fill()
        begin_fill()
        color("black", "grey")
        for k in range(2):
            fd(t / 6)
            left(90)
            fd(t / 1.5)
            left(90)
        end_fill()
        fd((t / 3) * 2 + t - (t / 6))
        begin_fill()
        color("black", "grey")
        for k in range(2):
            fd(t / 6)
            left(90)
            fd(t / 1.5)
            left(90)
        end_fill()
        up()
        setposition(x, y + (1.5 * t) + t / 1.5 + (t / 6))
        down()
        begin_fill()
        color("black", "#318CE7")
        left(90)
        fd(t / 1.5)
        right(90)
        goto(x - (t / 3), y + (10 / 3) * t)
        for k in range(4):
            circle(t / 2, -180)
            left(120)
        goto(x + t, y + 3 * t)
        goto(x + t, y + (1.5 * t) + t / 1.5 + (t / 6))
        end_fill()
        L = 90
        up()
        setposition(1300 / 2, -800 / 2)
        setheading(0)
        left(90)
        down()
        begin_fill()
        color("black", "red")
        circle(-(L - ((L / 2) / (7 / 2)) * (3 / 2)), 90)
        left(90)
        fd((L / (5 / 2)))
        left(90)
        circle(L * 1.2, 90)
        end_fill()

    tuyau(40, -820 / 2, 55)


#--------------------------------------------------EL GARMIT GAALOUL-----------------------------------------------------------

#------------------------------------------------------JEU FINAL---------------------------------------------------------------
from turtle import*
import time
import sys

try:
    setworldcoordinates(-0.9 * getscreen().window_height(), -0.5 * getscreen().window_height(),
                            0.9 * getscreen().window_width(), 0.6 * getscreen().window_width())
    setup(width=800, height=700)
    Screen().cv._rootwindow.resizable(False, False)

    rejouer = "OUI"
    
    # Première Boucle permettant de rejouer tant de fois que le joueur le souhaite
    # et le décor du jeu se redessine en début de boucle
    while rejouer=="OUI":

        Decor()
    # Utilisation de la base du projet textuel pour relier le textuel au graphique
        from random import randint
        NbQuilles = randint(6,8)
        ListeQuillesDbt = [[0,NbQuilles - 1]]

        # On fait retenir à l'ordi le schéma des quilles (afficheQuilles) du début pour pouvoir l'utiliser
        # par la suite car il va changer lorsque le joueur ou l'ordi vont jouer
        SchemaQuillesDebut = afficheQuilles(ListeQuillesDbt, NbQuilles)

    #Première boucle qui va dessiner les quilles debout par rapport au nombre de quilles choisi aléatoirement par l'ordi

        for k in range(len(SchemaQuillesDebut)):
            if SchemaQuillesDebut[k]=="|":
                
                # La taille des quilles et leur distance les unes par rapport aux autres sont dessinés
                # par rapport au nombre de quilles au total, tout simplement en changeant les variables
                # position et taille dans la définition des quilles debout (QuillesDebout)
                QuillesDebout(-430+k*(990/len(SchemaQuillesDebut)), -22+((-1)**k)*30, 28-((len(SchemaQuillesDebut)*(7/10))))

        Regle = textinput("Vite la ville brûle","Vous devez éteindre le feu !! Celui qui éteint la dernière flamme a gagné.\nÀ vous de jouer... (Cliquez sur un des boutons pour commencer)")

    # Boucle du projet textuel qui fait jouer à tour de rôle le joueur puis l'ordi jusqu'à ce qu'il n'y ait
    # plus de quilles debout
        i=1
        while not(len(ListeQuillesDbt) == 0):


            # Cette fonction permet de savoir le numéro du tour auquel on est donc on l'appelle en début de boucle pour qu'elle
            # se répète
            NbTour(i)

            # Pour le premier tour uniquement, en assimile le schéma des quilles du début au schéma des quilles apres que
            # l'ordi ait joué pour lancer la boucle
            if i == 1:

                SchemaQuillesOrdi = SchemaQuillesDebut
                
            time.sleep(1)
            jouer(joueurJoue(ListeQuillesDbt),ListeQuillesDbt)

            # Apres que le joueur ait joué, le schéma des quilles change, donc on appelle la variable SchemaQuillesJoueur
            # le schéma des quilles après que le joueur ait joué

            SchemaQuillesJoueur = afficheQuilles(ListeQuillesDbt, NbQuilles)

            # Cette boucle permet de comparer les schémas des quilles après que le joueur ait joué et après que l'ordinateur
            # ait joué, et si le schéma est différent cela veut dire qu'une quille ou plusieurs quilles sont tombées donc on appelle
            # la fonction Quilleparterre qui va faire disparaître la quille debout et dessiner la quille parterre au même
            # endroit car la fonction quille parterre a été realisé à partir de la fonction quilles debout. Donc la quille
            # debout se redessine mais de la même couleur que le mur pour la faire disparaître et c'est alors que se dessine
            # la quille parterre.
            for k in range(len(SchemaQuillesJoueur)):

                if SchemaQuillesJoueur[k] != SchemaQuillesOrdi[k] :
                    QuilleParterre(-430 + k * (990 / len(SchemaQuillesJoueur)), -22 + ((-1) ** k) * 30, 28 - ((len(SchemaQuillesJoueur) * (7 / 10))))


            # Si apres que le joueur ait joué il n'y a plus de quilles alors il a gagné, on le lui fait savoir et on lui
            # demande si il veut rejouer, si oui il rejoue sinon le jeu s'arrête
            if len(ListeQuillesDbt) == 0:

                rejouer = textinput("FIN","Félicitations, vous avez gagné !!! Voulez-vous rejouer ? (OUI ou NON) ")

            else:
                time.sleep(1)
                jouer(ordiJoue(ListeQuillesDbt),ListeQuillesDbt)


                # Il s'agit de la même boucle que la précédente sauf que maintenant on compare les schémas des quilles apres
                # que l'ordinateur ait joué et apres que le joueur ait joué.
                SchemaQuillesOrdi = afficheQuilles(ListeQuillesDbt, NbQuilles)
                for k in range(len(SchemaQuillesOrdi)):
                    if SchemaQuillesOrdi[k]  != SchemaQuillesJoueur[k] :
                        QuilleParterre(-430 + k * (990 / len(SchemaQuillesOrdi)), -22 + ((-1) ** k) * 30, 28 - ((len(SchemaQuillesOrdi) * (7 / 10))))

                # Si après que l'ordinateur ait joué il n'y a plus de quilles alors le joueur a perdu, on le lui fait
                # savoir et on lui demande si il veut rejouer, si oui il rejoue sinon le jeu se ferme
                if len(ListeQuillesDbt) == 0:
                    rejouer = textinput("FIN","Quel dommage... vous avez perdu ! Voulez-vous retenter votre chance ? (OUI ou NON)")

            i=i+1

        # Pour rejouer ou arrêter il faut que le joueur écrive bien OUI ou NON en majuscule sinon le programme lui
        # redemande si il veut rejouer et ceci tant que ce n'est pas bien fait
        while rejouer not in ["OUI","NON"]:
            rejouer = textinput("FIN","Non n'avons pas très bien compris, voulez vous rejouer tapez OUI ou NON (en majuscules)")

except:
    sys.exit()
