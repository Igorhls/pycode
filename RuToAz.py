def rumo_para_azimute(rumo):
    if rumo.endswith("N"):
        return int(rumo[:-2])
    elif rumo.endswith("S"):
        return int(rumo[:-2]) + 90
    elif rumo.endswith("O"):
        return int(rumo[:-2]) + 180
    elif rumo.endswith("L"):
        return int(rumo[:-2]) + 270
    else:
        return "Rumo inválido!"

azimute_str = input("Digite o valor do rumo: ")


print(rumo_para_azimute(azimute_str))
