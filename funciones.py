print("============================================")
A = {1,2,3,4,5}
B = {6,7,8,9,0}

F = {(1,6),(2,9),(4,7),(3,8),(5,0)}

print ("A =", A)
print ("B =", B)
print ("F =", F)

# Conocer si F es una función
esFuncion = True
dominio = set ()

for (x,y) in F:
    if x in dominio:
        esFuncion = False
    dominio.add(x)

print("F es funcion"if esFuncion else "F no es función") 

esInyectiva = True
rango = set()

for (x,y) in F:
    if y in rango:
            esInyectiva = False
    rango.add(y)

print("F es inyectiva"if esInyectiva else "F si es inyectiva") 

esSobreyectiva = False
if rango == B:
     esSobreyectiva = True
print("F es sobreyectiva"if esSobreyectiva else "F si es sobreyectiva") 

esBiyectiva = esInyectiva and esSobreyectiva

print("F es Biyectiva"if esBiyectiva else "F si es Biyectiva") 

esTotal = False

if dominio == A:
    esTotal = True

print("F es Total"if esTotal else "F si es Total") 