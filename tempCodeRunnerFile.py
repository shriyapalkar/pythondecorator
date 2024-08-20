def hello_decorator(func):
    #inner1 is a wrapper function in
    #which the argument is called
    #inner function can access the outer local
    #function like in thus case "func"
    
    def inner1():
        print('Hello,this is before function execution')
        #calling the actual function now
        #inside the wrapper function
        func()
        print('This is after function execution')
        
    return inner1

def function_to_be_used():
    print('This is inside the function!')
    
#passing 'function_to_be_used' inside the
#decorator to control its behaviour

function_to_be_used = hello_decorator(function_to_be_used)

#calling the function
function_to_be_used()

