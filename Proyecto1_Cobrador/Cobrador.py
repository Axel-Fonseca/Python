#Global Variables
stock = [] #Lista para los articulos del inventario
stock_price = [] #Lista para precio de articulos inventario
Id = [] #Lista para ID de stock
Id_cart = [] #Lista ID carrito
cart = [] #Lista para carrito
cart_bill = [] #Lista para cuenta del carrito

#def Functions

#Funcion añadir producto, precio y cantidad al stock
def Add_Stock(product,amount,price):
    stock.extend(amount*[product])
    stock_price.extend(amount*[price])
    #Creacion lista de ID
    if bool(Id):
        Id.extend(range(Id[-1]+1,len(stock)))
    else:
        Id.extend(range(len(stock)))

#Funcion remover producto, id y precio
def Remove_Stock(Id_erase):
    stock.remove(stock[Id.index(Id_erase)])
    stock_price.remove(stock_price[(Id.index(Id_erase))])
    Id.remove(Id_erase)

#Funcion añadir producto del stock al carrito con ID
def Add_Cart(Id_add_cart):
    cart.append(stock[Id.index(Id_add_cart)])
    cart_bill.append(stock_price[Id.index(Id_add_cart)])
    Id_cart.append(Id_add_cart)

#Funcion remover producto del stock al carrito con ID
def Remove_Cart(Id_remove_cart):
    cart.remove(cart[Id_cart.index(Id_remove_cart)])
    cart_bill.remove(cart_bill[Id_cart.index(Id_remove_cart)])
    Id_cart.remove(Id_remove_cart)

#Funcion cobrar carrito
def Charge(cart_bill):
    return sum(cart_bill)


#Menú
while True:
    print("""\n             BIENVENIDO
    Por favor seleccione una opción del Menú:
    *Agregar producto nuevo: 1
    *Remover producto: 2
    *Agregar producto al carrito: 3
    *Remover producto del carrito: 4
    *Cobrar: 5
    *Salir: 6\n""")

    option = int(input("Seleccione un número del Menú: "))

    if option == 1: #Agregar Stock
        print("ID       Producto        Precio")
        for (i,j,k) in zip (range(len(Id)),range(len(stock)),range(len(stock_price))): #Triple "for" simultaneo para imprimir ID y Stock
            print(Id[i],"       ",stock[j],"            $",stock_price[k])

        product = input("\nEscriba el nombre del producto: ")
        amount = int(input("Escriba la cantidad: "))
        price = int(input("Escriba el precio: "))

        Add_Stock(product,amount,price)
        print("\nProducto agregado al Stock....\n")

    elif option == 2: #Remover Stock
        print("ID       Producto        Precio")
        for (i,j,k) in zip (range(len(Id)),range(len(stock)),range(len(stock_price))): #Triple "for" simultaneo para imprimir ID y Stock
            print(Id[i],"       ",stock[j],"            $",stock_price[k])
            
        Id_erase = int(input("\nSeleccione el ID correspondiente para borrar: "))
        Remove_Stock(Id_erase)

        print("\nProducto removido del Stock....\n")
    
    elif option == 3: #Agregar carrito
        print("ID       Producto        Precio")
        for (i,j,k) in zip (range(len(Id)),range(len(stock)),range(len(stock_price))): #Triple "for" simultaneo para imprimir ID y Stock
            print(Id[i],"       ",stock[j],"            $",stock_price[k])

        Id_add_cart = int(input("\nSeleccione el ID correspondiente para agregar al carrito: "))
        Add_Cart(Id_add_cart)
        
        print("\nProducto agregado al carrito....\n")

    elif option == 4: #Remover carrito
        print("ID       Carrito        Cuenta")
        for (i,j,k) in zip (range(len(Id_cart)),range(len(cart)),range(len(cart_bill))):
            print(Id_cart[i],"       ",cart[j],"           $",cart_bill[k])

        Id_remove_cart = int(input("\nSeleccione el ID correspondiente para remover del carrito: "))
        Remove_Cart(Id_remove_cart)

        print("\nProducto removido al carrito....\n")

    elif option == 5: #Cuenta
        print("\nLa cuenta total del carrito es: $",Charge(cart_bill),"\n")
    
    elif option == 6: #Salir
        print("GRACIAS VUELVA PRONTO....")
        break

    elif option > 7 or option == 0:
        print("\nOpción no valida...\n")