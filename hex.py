t = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A' , 'B', 'C', 'D', 'E', 'F']

def decTohex(n):
    if(n<=0):
        return ''
    p = n%16
    return  decTohex(n//16)+t[p]
        
decimal = int(input("nombre: "))
print("Hexadecimal: ",decTohex(decimal))