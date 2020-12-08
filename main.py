from models.Nodo import Nodo
import csv
import operator

def leer_csv():
    lista_csv = []

    with open('data.csv', newline='') as File:
        reader = csv.reader(File)
        lista_csv = [row for row in reader]

    lista_csv.pop(0)    # Elimina cabecera
    return lista_csv

# Añade los objetos Nodo a una lista
def lista_nodos(lista_row):
    lista = []

    for row in lista_row:
        lista.append(Nodo(row[0], row[1], row[2]))
    
    return lista


# Ordena la lista primero por el campo parent y luego por el id
def ordenar_arbol(lista):
    return sorted(lista, key=operator.itemgetter(2, 1))


# Obtiene un objeto Nodo de una lista según su ID
def get_node_by_id(lista, id):
    for nodo in lista:
        if nodo.id == str(id):
            return nodo
    return None


# Obtiene el primer hijo Nodo del padre con el ID introducido
def get_node_by_parent(lista, id):
    for nodo in lista:
        if nodo.parent == str(id):
            return nodo
    return None


# Borra un objeto Nodo de una lista por su ID
def remove_node_by_id(lista, id):
    borrado = False
    i = 0
    while (not borrado and i < len(lista)):
        if lista[i].id == str(id):
            del lista[i]
            borrado = True
        i += 1
        

# Ordena la estructura arbol post orden    
def ordenar():
    nodo = lista[0]

    # Bucle hasta que haya utilizado todos los registro de la lista
    while len(lista_aux) > 0:

        if nodo != None:
            nodo_hijo = get_node_by_parent(lista_aux, nodo.id)  # Obtiene el nodo hijo
            
            if nodo_hijo != None:   #Tiene hijo
                # En caso de que no esté en la lista nueva lo añade
                if get_node_by_id(lista_new, nodo_hijo.id) == None:
                    lista_new.append(nodo_hijo)
                nodo = nodo_hijo    # Recoje el nodo hijo
            else:   # Si no tiene nodo hijo, obtiene el padre
                id_nodo = nodo.id
                nodo = get_node_by_id(lista_aux, nodo.parent)
                
                # Borra el nodo hijo de la lista auxiliar porque ya no va a hacer mas falta
                # Se borra en caso de que ya no tenga más hijos
                remove_node_by_id(lista_aux, id_nodo)
                

lista = ordenar_arbol(lista_nodos(leer_csv()))

# OUTPUT lista
# Nodo = { versn: fbkxn, id: 1, parent: 0}
# Nodo = { versn: ez511, id: 2, parent: 1}
# Nodo = { versn: idc0s, id: 4, parent: 1}
# Nodo = { versn: 07r7w, id: 3, parent: 2}
# Nodo = { versn: 7tcvs, id: 5, parent: 4}
# Nodo = { versn: jg8jm, id: 6, parent: 4}
# Nodo = { versn: 0cb9t, id: 7, parent: 5}
# Nodo = { versn: 58k4x, id: 8, parent: 5}
# Nodo = { versn: djpm4, id: 9, parent: 5}
# Nodo = { versn: olv9i, id: 10, parent: 6}

lista_new = []
lista_aux = lista

ordenar()

for x in lista_new:
    print(x)

# OUTPUT lista_new
# Nodo = { versn: ez511, id: 2, parent: 1}
# Nodo = { versn: 07r7w, id: 3, parent: 2}
# Nodo = { versn: idc0s, id: 4, parent: 1}
# Nodo = { versn: 7tcvs, id: 5, parent: 4}
# Nodo = { versn: 0cb9t, id: 7, parent: 5}
# Nodo = { versn: 58k4x, id: 8, parent: 5}
# Nodo = { versn: djpm4, id: 9, parent: 5}
# Nodo = { versn: jg8jm, id: 6, parent: 4}
# Nodo = { versn: olv9i, id: 10, parent: 6}
