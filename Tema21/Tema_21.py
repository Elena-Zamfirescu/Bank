# Hint built-in modules: datetime, time
# 1
# Sa se defineasca un decorator care:
# Printeaza ora la care a inceput executia functiei
# Printeaza ora la care functia s-a finalizat
# Printeaza cate secunde a rulat functia

# 2 Sa se defineasca un decorator care creaza un log file (un fisier txt cu 'jurnalul' de activitate) pentru fiecare functie decorata care sa contina:
# Ora la care a inceput/sfarsit
# Numele functiei
# In fisier sa avem cate 5 entries pentru fiecare apel de functie (sa avem cate 5 rulari separate in jurnal)

# Sa se aplice decoratoarele(pe rand, si dupa impreuna) pe urmatoarele functii:
# Functie care printeaza itereaza in 1 milion, si printeaza fiecare numar
# Functie care creaza 10 fisiere txt separate si scrie de la 1 la 1 milion(linii separate fiecare numar) in fiecare fisier
# Functie care printeaza 5 cuvinte, dar fiecare cuvant este printat odata la 5 secunde

# Sa incercam sa apelam fiecare functie separat, nu toate odata, considerand ca fiecare functie poate dura destul de mult.

from time import time, ctime, sleep

def detalii_functie(funct):
    def wrapper(*args):
        t1 = time()
        rezultat=funct(*args)
        t2 = time()
        print(f"Functia a inceput sa ruleze la {ctime(t1)} si s-a finalizat la {ctime(t2)}")
        timp_rulare=round((t2-t1),4)
        print(f"Timpul de rulare a fost de {timp_rulare} secunde")
        return rezultat
    return wrapper

def log_file(funct):
    def wrapper(*args):
        numar_linii = 0
        t1 = time()
        rezultat=funct(*args)
        t2 = time()
        name=funct.__name__
        file = open(f"fisier functie {name}.txt", "a")
        file.write(f"Functia {name} a inceput sa ruleze la {ctime(t1)} si s-a finalizat la {ctime(t2)}.\nTimpul de rulare a fost de {round((t2-t1),4)} secunde\n")
        file.close()
        try:
            file = open(f"fisier functie {name}.txt", "r")
            for line in file.readlines():
                numar_linii +=1
            file.close()
        except:
            numar_linii = 3
        file = open(f"fisier functie {name}.txt", "a")
        file.write(f"Final Executia {(numar_linii//4)+1}\n"+"*"*70+"\n")
        file.close()
        return rezultat
    return wrapper

# @detalii_functie
@log_file
def million():
    for i in range (1000001):
        print (i)
million()

# @detalii_functie
@log_file
def creare_fisiere():
    for i in range(10):
        file = open(f"fisier.{i+1}.txt","w")
        for i in range(1,1000001):
            file.write(f"{i}\n")
        file.close()
creare_fisiere()

# @detalii_functie
@log_file
def pause_function(*cuvinte):
    for i in cuvinte:
        sleep(5)
        print(i)
pause_function("Acesta","nu","este","un","melc")
