
def bin_to_decimal(bin):
    bin = str(bin)
    n=len(bin)
    decimal = 0
    for i in range(n):
        decimal += bin[i]*2**(index(n-1-i))
    return decimal
bin_to_decimal(100010)
                   
    
        








    
   

 