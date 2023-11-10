def azimute_para_rumo(azimute):
    if azimute >= 0 and azimute < 90:
        return str(azimute) + "°N"
    elif azimute >= 90 and azimute < 180:
        return str(azimute - 90) + "°Leste"
    elif azimute >= 180 and azimute < 270:
        return str(azimute - 180) + "°S"
    elif azimute >= 270 and azimute < 360:
        return str(azimute - 270) + "°Oeste"
    else:
        return "Azimute inválido!"
    
azimute = int(input('Digite o azimute: '))

print(azimute_para_rumo(azimute))


