def MRUListExSort(list1, value, successfull):
   
    successfull = True
    if value.name() == 'MRUListEx':
       
        hex_chars = map(int, map(ord, (value.value())))  # Read mrulistex
        i = 0
        for i, val in enumerate(hex_chars):  # remove '0' 
            if val == 255:
                break
            if i == 0 or i % 4 == 0:  # The numbers are index 0 and every fourth thereafter
                list1.append(int(val))
                i = i + 1
            else:
                i = i+1
        return list1