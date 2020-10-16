def decoder(encodedValues):
    totalBits = 32
    lengthEachBit = 8
    original_string = ""
    for value in encodedValues:
        ascii_arr = [0 for j in range(totalBits)]
        binValue = bin(int(value))[2:].zfill(totalBits)
        j = 0
        for i in range(len(binValue)):
            k = i
            if j >= totalBits:
                break
            while k < totalBits:
                ascii_arr[j] = binValue[k] 
                j+=1
                k+=4
        ascii_value = ""
        for bit in ascii_arr:
            ascii_value += bit
        
        temp_str = ""
        for i in range (0,len(ascii_value),8):
            temp_str+=chr(int(ascii_value[i:i+8],2))
        original_string += temp_str[::-1]
    return original_string

           