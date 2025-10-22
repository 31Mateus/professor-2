clientes = ["Larica", "Gabriel", "Anna", "Ze",]
clientes.append("Teteu")
print(clientes)

clientes.remove("Teteu")
print(clientes)

clientes.pop(0)
print(clientes)

clientes[1] = "novo"
for i in clientes:
    print(i)