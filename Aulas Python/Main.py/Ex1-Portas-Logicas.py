# NOT
p = False

resultado = not p #Resultado será True
print("NOT:", resultado)

#and
p = True
q = False

resultado  = p and q #Resultado será False
print("AND:", resultado)

#OR
p = True
q = False

resultado = p or q #Resultado será True
print("OR:", resultado)

#XOR
p = True
q = False

resultado = p != q #Resultado será True
print("XOR:", resultado)

#Implicação
p = True
q = False

resultado = not p or q #Resultado será False
print("Implicação:", resultado)

#Bicondicional
p = True
q = True

resultado = p == q #Resultado será True
print("Bicondicional:", resultado)