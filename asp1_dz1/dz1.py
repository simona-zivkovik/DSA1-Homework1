def define():
    global MODUL
    global MNOZILAC
    global INKREMENT
def pseudoslucajan_broj(seed):
        return (MNOZILAC * seed + INKREMENT) % MODUL
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def delete(self):
        if not self.head:
            data = None
        elif self.head == self.tail:
            data = self.head.data
            self.head = None
            self.tail = None
            self.length = 0
        else:
            data = self.head.data
            self.head = self.head.next
            self.length -= 1

        return data

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()

def init_csc(n):
    v = []
    r = []
    c = []

    for i in range(n+1):
        c.append(0)

    csc = [v, r, c]

    return csc

def add_to_csc(csc, data, i, j):
    g = csc[2][j]

    if (j<len(csc[2])-1 and csc[2][j] == csc[2][j+1]):
        csc[0].insert(csc[2][j], data)
        csc[1].insert(csc[2][j], i)
        for s in range(j+1, len(csc[2])):
            csc[2][s] += 1

        return csc

    if (csc[2][j] == csc[2][j-1]):
        csc[0].insert(csc[2][j], data)
        csc[1].insert(csc[2][j], i)
        for s in range(j+1, len(csc[2])):
            csc[2][s] += 1

        return csc

    for s in range(j+1, len(csc[2])):
        csc[2][s] += 1

    if(len(csc[0]) == 0):
        csc[0].append(data)
        csc[1].append(i)
        return csc

    for s in range(g, len(csc[0])):
        if(csc[1][s] > i):
            csc[0].insert(s,data)
            csc[1].insert(s, i)
            return csc

    csc[0].insert(csc[0], data)
    csc[1].insert(csc[1], i)

    return csc

def remove_from_csc(csc, data, i, j):
    br = 0

    for s in range(len(csc[0])):
        if(csc[0][s] == data and csc[1][s] == i):
            csc[0].pop(s)
            csc[1].pop(s)
            break
        br+=1

    for s in range(len(csc[2])):
        if(csc[2][s] > br):
            csc[2][s] -=1

    return csc

def print_csc(csc):
    print()
    print("V: ", end='')
    print(csc[0])
    print("R: ", end='')
    print(csc[1])
    print("C: ", end='')
    print(csc[2])
    print()

def print_talon(csc):
    mat = []

    for i in range(len(csc[2])-1):
        mat.append([])
        for j in range(len(csc[2])-1):
            mat[i].append(0)

    for i in range(len(csc[2])-1):
        for j in range(csc[2][i+1] - csc[2][i]):
            mat[csc[1][csc[2][i] + j]][i] = csc[0][csc[2][i] + j]

    print("-------------------------")
    for i in range(len(mat)):
        for j in mat[i]:
            print(j, end="  ")
        print()

### main ###
MODUL = 4294967296 #2^32
MNOZILAC = 1664525
INKREMENT = 1013904223

print("Dobrodosli u Ne ljuti se covece!")

while True:
    n = int(input("Unesite neparan broj za velicinu talona! \n"))
    if n%2==0:
        print("Pokusajte ponovo!")
    elif n<5:
        print("Pokusajte ponovo!")
    else:
        talon = init_csc(n)
        print_talon(talon)
        break

print("\nKoliko igraca igraju?")

while True:
    broj_igraca = int(input())
    if broj_igraca<2 or broj_igraca>4:
        print("Broj igraca sme da je izmedju 2 i 4! Pokusaj ponovo.")
    else:
        break

igrac1_talon = LinkedList()
for i in range(4):
    igrac1_talon.append("C1")

igrac2_talon = LinkedList()
for i in range(4):
    igrac2_talon.append("C2")

if broj_igraca==3:
    igrac3_talon = LinkedList()
    for i in range(4):
        igrac3_talon.append("C3")

elif broj_igraca==4:
    igrac4_talon = LinkedList()
    for i in range(4):
        igrac4_talon.append("C4")

while True:
    for i in range(1, (broj_igraca+1)):
        print("\nKoji poteg zelite da napravite?")
        print("Meni: \n 1) Baci kocku \n 2) Pomeri figuru \n 3) Ubaci figuru na talonu \n")

        izbor = int(input())
        izbor2 = 0

        if izbor == 1:
            print("Unesite pozitivan random broj da bi ste bacili kocku!")
            seed = int(input())
            seed = pseudoslucajan_broj(seed)
            rezultat = (seed % 6) + 1
            print("Dobili ste: ", rezultat)
            if rezultat == 6:
                izbor2 = int(input("Da li hocete da \n  1) Ubacite figuru na talonu \n  2) Pomeriti figuru\n"))
                if izbor2 == 1:
                    izbor = 3
                elif izbor2 == 2:
                    izbor = 2
            """else:
                izbor = 2"""


        if izbor == 2:
            pass

        if izbor == 3:

            if i == 1:
                print("Igrac 1")
                print("Trenutne figure na raspolaganju: ")
                igrac1_talon.print_list()

                if izbor2 !=1:
                    print("Da bi ubacili figuru, treba da dobijete 6 na bacanje kocku. Unesite pozitivan random broj da bi ste bacili kocku!")
                    seed = int(input())

                igraci = igrac1_talon.length

                if igraci == 0:
                    print("Nemate figuri da bi izbacili!")

                if izbor2 != 1:
                    for j in range(3):
                        seed = pseudoslucajan_broj(seed)
                        rezultat = (seed % 6) + 1
                        print("Dobili ste: ", rezultat)

                        if rezultat == 6:
                            print("Ubacili ste na talonu!")
                            igrac1_talon.delete()
                            igrac1_talon.print_list()
                            talon = add_to_csc(talon, "C1", (n - 1), 0)
                            print_talon(talon)
                            break

                        if igraci != 4:
                            break

                if izbor2 == 1:
                    for j in range(2):
                        seed = pseudoslucajan_broj(seed)
                        rezultat = (seed % 6) + 1
                        print("Dobili ste: ", rezultat)

                        if rezultat == 6:
                            print("Ubacili ste na talonu!")
                            igrac1_talon.delete()
                            igrac1_talon.print_list()
                            talon = add_to_csc(talon, "C1", (n - 1), 0)
                            print_talon(talon)
                            break

                        if igraci != 4:
                            break


            if i == 2:
                print("Igrac 2")
                print("Trenutne figure na raspolaganju: ")
                igrac2_talon.print_list()

                if izbor2 !=1:
                    print("Da bi ubacili figuru, treba da dobijete 6 na bacanje kocku. Unesite pozitivan random broj da bi ste bacili kocku!")
                    seed = int(input())

                igraci = igrac2_talon.length

                if igraci == 0:
                    print("Nemate figuri da bi izbacili!")

                if izbor2 != 1:
                    for j in range(3):
                        seed = pseudoslucajan_broj(seed)
                        rezultat = (seed % 6) + 1
                        print("Dobili ste: ", rezultat)

                        if rezultat == 6:
                            print("Ubacili ste na talonu!")
                            igrac2_talon.delete()
                            igrac2_talon.print_list()
                            talon = add_to_csc(talon, "C2", 0, 0)
                            print_talon(talon)
                            break

                        if igraci != 4:
                            break

                if izbor2 == 1:
                    for j in range(2):
                        seed = pseudoslucajan_broj(seed)
                        rezultat = (seed % 6) + 1
                        print("Dobili ste: ", rezultat)

                        if rezultat == 6:
                            print("Ubacili ste na talonu!")
                            igrac2_talon.delete()
                            igrac2_talon.print_list()
                            talon = add_to_csc(talon, "C2", 0, 0)
                            print_talon(talon)
                            break

                        if igraci != 4:
                            break


            if i == 3:
                print("Igrac 3")
                print("Trenutne figure na raspolaganju: ")
                igrac3_talon.print_list()

                if izbor2 !=1:
                    print("Da bi ubacili figuru, treba da dobijete 6 na bacanje kocku. Unesite pozitivan random broj da bi ste bacili kocku!")
                    seed = int(input())

                igraci = igrac3_talon.length

                if igraci == 0:
                    print("Nemate figuri da bi izbacili!")

                if izbor2 != 1:
                    for j in range(3):
                        seed = pseudoslucajan_broj(seed)
                        rezultat = (seed % 6) + 1
                        print("Dobili ste: ", rezultat)

                        if rezultat == 6:
                            print("Ubacili ste na talonu!")
                            igrac3_talon.delete()
                            igrac3_talon.print_list()
                            talon = add_to_csc(talon, "C3", 0, (n-1))
                            print_talon(talon)
                            break

                        if igraci != 4:
                            break

                if izbor2 == 1:
                    for j in range(2):
                        seed = pseudoslucajan_broj(seed)
                        rezultat = (seed % 6) + 1
                        print("Dobili ste: ", rezultat)

                        if rezultat == 6:
                            print("Ubacili ste na talonu!")
                            igrac3_talon.delete()
                            igrac3_talon.print_list()
                            talon = add_to_csc(talon, "C3", 0, (n-1))
                            print_talon(talon)
                            break

                        if igraci != 4:
                            break

            if i == 4:
                print("Igrac 4")
                print("Trenutne figure na raspolaganju: ")
                igrac4_talon.print_list()

                if izbor2 !=1:
                    print("Da bi ubacili figuru, treba da dobijete 6 na bacanje kocku. Unesite pozitivan random broj da bi ste bacili kocku!")
                    seed = int(input())

                igraci = igrac4_talon.length

                if igraci == 0:
                    print("Nemate figuri da bi izbacili!")

                if izbor2 != 1:
                    for j in range(3):
                        seed = pseudoslucajan_broj(seed)
                        rezultat = (seed % 6) + 1
                        print("Dobili ste: ", rezultat)

                        if rezultat == 6:
                            print("Ubacili ste na talonu!")
                            igrac4_talon.delete()
                            igrac4_talon.print_list()
                            talon = add_to_csc(talon, "C4", (n-1), (n-1))
                            print_talon(talon)
                            break

                        if igraci != 4:
                            break

                if izbor2 == 1:
                    for j in range(2):
                        seed = pseudoslucajan_broj(seed)
                        rezultat = (seed % 6) + 1
                        print("Dobili ste: ", rezultat)

                        if rezultat == 6:
                            print("Ubacili ste na talonu!")
                            igrac4_talon.delete()
                            igrac4_talon.print_list()
                            talon = add_to_csc(talon, "C4", (n-1), (n-1))
                            print_talon(talon)
                            break

                        if igraci != 4:
                            break

            continue

        else:
            print("Molim Vas ukucajte validan broj!")