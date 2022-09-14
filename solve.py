# Recurrencia
# -----------
#  t(n,w) = 0                                    : if n <= 0 or w = 0
#         = t(n-1,w)                             : if w(n) > w
#         = max (t(n-1,w), t(n-1,w-w(n)) + B(n))

def solve_memoization(items, capacity):
    mem={}
    taken = []

    # Utilizaremos esta función para generar la clave de acceso al
    # diccionario que utilizamos para guardar los resultados (mem).
    
    def getKey(n, w):
        Is = str(n) + "=>" + str(w) ;
        return Is # Retornamos la clave

    def t(n, w):
        # ...
        key = getKey(n, w)
        if n < 0 or w == 0:
            return 0
        if key in mem:
            return mem[key]
        if items[n].weight > w:
            mem[key] = t(n - 1, w)
            return mem[key]

        mem[key]=max(t(n-1,w), t(n-1,w-items[n].weight) + items[n].value)
        return mem[key]

    def fill_taken(n, w):
        # ...
        # ...
        taken_copy = [0]*len(items)
        max_value_copy = max_value;
        n_copy = n
        capacity= w

        while n_copy >= 0 and capacity > 0:
            if n_copy != 0:
                x = getKey(n_copy, capacity)
                y = getKey(n_copy - 1, capacity)
                if mem[x] != mem[y]:
                    taken_copy[n_copy] = items[n_copy].index
                    capacity -= items[n_copy].weight
                    max_value_copy -= items[n_copy].value
            else:
                z = getKey(n_copy, capacity)
                if mem[z] >= max_value_copy and items[n_copy].weight <= capacity:
                    taken_copy[n_copy] = items[n_copy].index
            n_copy -= 1;

        for i in reversed(taken_copy):
            if i!=0:
                taken.insert(0, i)

        return

    n=len(items)-1

    max_value = t(n,capacity)   # Calculo el valor maximo
    fill_taken(n,capacity)      # Genero la lista de items elegidos

    return max_value, taken
