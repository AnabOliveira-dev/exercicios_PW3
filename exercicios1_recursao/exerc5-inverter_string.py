def inverter_string(palavra):
    # caso base
    if palavra == "":
        return ""
    
    # caso recursivo
    return inverter_string(palavra[1:]) + palavra[0]

print(inverter_string("python"))  # "nohtyp"