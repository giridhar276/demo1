

x = "Hi"
def read_x():
    print(x)    
read_x()






def read_y():
    y = "Hello"
    print(y)
read_y()



# If a name is bound inside a function, it is by default accessible only within the function
def test():
    a = 5
    print(a)    #5
print(a)



#### Normally an assignment inside a scope will shadow any outer variables of same name
x = "Hi"
def change_local_x():
    x = "Bye"
    print(x)   # Bye

change_local_x()
print(x)       #Hi


# declaring a name global means that, for the rest of the scope, any assignments to the name
# will happen at the module's top level
x = "Hi"
def change_global_x():
    global x
    x = "Bye"
    print(x)

change_global_x()
print(x)




