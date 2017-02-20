def pow_mod(x, y, z):
    number=[[1,1],[1,0]]
    while y:
        if y & 1:
            number = matrixMultiplication(number,x,z)
        y /=2
        x = matrixMultiplication(x,x,z)
    return number
def matrixMultiplication(a,b,m):
    return [[(a[0][0]*b[0][0]+a[0][1]*b[1][0])%m,(a[0][0]*b[0][1]+a[0][1]*b[1][1])%m],[(a[1][0]*b[0][0]+a[1][1]*b[1][0])%m,(a[1][0]*b[0][1]+a[1][1]*b[1][1])%m]]
a = [[1,1],[1,0]]
mod=10**9+7
for i in range((input())):
    print (pow_mod(a,input()+2,mod)[1][1])
