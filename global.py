x = 'global'

def outer():
    x = 'outer'
    
    def inner_outer():
        print('this should print outer:')
        print(x)

    def inner_global():
        global x
        print('this should print global:')
        print(x)

    def inner_inner():
        x = 'inner'
        print('this should print inner:')
        print(x)

    inner_outer()
    inner_global()
    inner_inner()
    
outer()
