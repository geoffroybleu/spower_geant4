import matplotlib.pyplot as plt

# recupere les données de l'ancienne version

energie_old = []
spower_old = []
incertitudes_old = []

with open("spowerold.txt", "r") as f:
    for line in f:
        a, b, c = line.split()
        energie_old.append(float(a))
        spower_old.append(float(b))
        incertitudes_old.append(float(c))

# recupere les données de la nouvelle version

energie_new = []
spower_new = []
incertitudes_new = []

with open("spowernew.txt", "r") as f:
    for line in f:
        a, b, c = line.split()
        energie_new.append(float(a))
        spower_new.append(float(b))
        incertitudes_new.append(float(c))

#permet d'avoir l'incertitudes négative pour faire les courbes d'incertitudes
incertitudes_moins_old = [-x for x in incertitudes_old]
incertitudes_moins_new = [-x for x in incertitudes_new]

# permet d'avoir une ligne y = 0 pour le graphe de la différence entre les deux courbes
lignenul = []
for i in range(len(energie_new)):
    lignenul.append(0)

#donne le spower plus ou moins l'incertitude pour faire les courbes d'incertitudes

def spower_plus(spower, incertitude):
    temp = []
    for i in range (len(spower)):
        temp.append(spower[i] + incertitude[i])
    return temp

def spower_moins(spower, incertitude):
    temp = []
    for i in range (len(spower)):
        temp.append(spower[i] - incertitude[i])
    return temp

# fait une difference en pourcent des deux courbes

def difference_en_pourcent(spower1, spower2):
    temp = []
    for i in range(len(spower1)):
        temp1 = (spower2[i] / spower1[i]) - 1
        temp.append(temp1 * 100)
    return temp

#fait une difference simple entre les deux courbes

def difference(spower1, spower2):
    temp = []
    for i in range(len(spower1)):
        temp1 = (spower2[i] - spower1[i])
        temp.append(temp1)
    return temp

plt.subplot(2, 1, 1)
plt.plot(energie_old, spower_old, 'blue', label = 'simulations geant4 old')
plt.xscale('log')
plt.yscale('log')
plt.ylabel("spower")
plt.plot(energie_new, spower_new, 'red', label = 'simulations geant4 new')

"""
si on veut tracer autour des courbes de spower l'incertitude lié à la nouvelle et l'ancienne version


plt.plot(energie_new, spower_plus(spower_old, incertitudes_old), 'green', linestyle = ':', label = 'incertitudes')
plt.plot(energie_new, spower_moins(spower_old, incertitudes_old), 'green', linestyle = ':')

plt.plot(energie_new, spower_plus(spower_new, incertitudes_new), 'black', linestyle = ':', label = 'incertitudes')
plt.plot(energie_new, spower_moins(spower_new, incertitudes_new), 'black', linestyle = ':')

"""
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(energie_old, difference_en_pourcent(spower_old, spower_new))
plt.xscale('log')
plt.ylabel("difference entre les deux courbes")
plt.xlabel("energie en echelle logarithmique")
plt.plot(energie_new, lignenul, 'red', label = 'y = 0')

"""

de même que pour spower on peut encadrer la courbe de la difference entre les deux courbes avec les incertitudes

plt.plot(energie_new, incertitudes_old, 'green', linestyle = ':', label = 'incertitudes')
plt.plot(energie_new, incertitudes_moins_old, 'green', linestyle = ':')

plt.plot(energie_new, incertitudes_new, 'green', linestyle = ':', label = 'incertitudes')
plt.plot(energie_new, incertitudes_moins_new, 'green', linestyle = ':')

"""

plt.show()