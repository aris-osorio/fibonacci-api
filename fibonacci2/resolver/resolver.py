def operacion(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return operacion(n-1) + operacion(n-2)

class Resolver():
    
    def fibonacci(num):
        res = 0
        con = 0
        lis = []
        rev = []

        if num == 0:
            return [0]

        while(num > res):
            res = operacion(con)

            if num < res:
                break

            lis.append(res)
            con += 1

        rev = lis.copy()
        rev.pop(len(rev)-1)
        rev.reverse() 
        return lis + rev

