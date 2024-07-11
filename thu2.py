def fun(stri , n ):
    if len(stri) > 2:
        result = stri[:2] * n
    else:
        result = stri *n
    return result

print(fun("r" , 3))