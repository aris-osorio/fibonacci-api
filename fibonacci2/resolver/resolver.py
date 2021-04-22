class Resolver():
    def fibonacci(num):
        res = 0
        lis = [0,1]
        rev = []

        if num == 0:
            return([0])
        elif num > 1:
            while(num > res):
                res = lis[len(lis)-1] + lis[len(lis)-2]
                if num < res:
                    break
                lis.append(res)

        rev = lis.copy()
        rev.pop(len(rev)-1)
        rev.reverse() 
        return(lis + rev)


