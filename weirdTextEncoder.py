def weirdTextEncoder(textNum):
    
    totalBits = 32
    lengthEachBit = 8
    
    ascii_arr = []

    ## Conversion of the string into ASCII array
    for s in textNum:
        len_bit = len(bin(ord(s)).replace("0b",""))
        if len_bit < lengthEachBit:
            binValue = '0'*(lengthEachBit-len_bit)+bin(ord(s)).replace("0b","")
        else:
            binValue = bin(ord(s)).replace("0b","")
        ascii_arr.extend([bit for bit in reversed(binValue)])
    
    if len(ascii_arr) < totalBits:
        k = (totalBits-len(ascii_arr))
        while k > 0:
            ascii_arr += ["0"]
            k -=1

    ## Reversing the array to get it into correct format.
    ascii_arr = ascii_arr[::-1] 
    
    ## Designing the Encoded array from the ascii array.
    encoded_arr = []
    for i in range (lengthEachBit):
        j = i
        while j < totalBits:
            encoded_arr.append(ascii_arr[j])
            j+=8

    ## Calculating the Decimal Output (Final Result)        
    encoded_output = 0
    for x in range(len(encoded_arr)):
        encoded_output+= (2**(31-x))*int(encoded_arr[x])
    
    return encoded_output
