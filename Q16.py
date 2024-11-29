def inverter_string(texto):
    if not texto:
        return ""
    else:
        return texto[-1] + inverter_string(texto[:-1])
    
texto = "recursao"
print(inverter_string(texto))