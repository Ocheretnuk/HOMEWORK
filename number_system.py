NUM = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]


def convert1(nomer, sis):
    list = []
    while nomer > 0:
        x = nomer % sis
        nomer /= sis
        list.insert(0, str(NUM[x]))
        
        nomer = int(nomer)
        
    return "".join(list)
    
    
def convert2(nomer, sis):
    lim = len(nomer)
    result = 0
    for k, v in enumerate(range(lim, 0, -1)):
        num = NUM.index(nomer[k].upper())
        result += int(num) * sis**(v-1)
        
    return result




def dec2bin(nomer):
    return convert1(nomer, 2)


def dec2oct(nomer):
    return convert1(nomer, 8)
    
   
def dec2hex(nomer):
    return convert1(nomer, 16)
   
  
def bin2dec(nomer):
    return convert2(nomer, 2)


def oct2dec(nomer):
    return convert2(nomer, 8)

    
def hex2dec(nomer):
    return convert2(nomer, 16)
    
    
