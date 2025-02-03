

def decorator(original_funcion):

    def wrapper(Vk,Vn,t):
        original_funcion(Vk,Vn,t)
        S= (((Vk-Vn)/t)*(t*t))/2
        print('после',S)
    return wrapper

def alone_function(Vk,Vn,t):
    a =(Vk-Vn)/t
    print('во время',a)


try:
    Vk=float(input())
    Vn=float(input())
    t=float(input())



    alone_function=decorator(alone_function)
    alone_function(Vk,Vn,t)
except ValueError:
    print("Вы что-то попутали с вводом")
except ZeroDivisionError:
    print("Деление на ноль")

