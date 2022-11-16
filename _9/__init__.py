import re


def getPrecio(transportType):
    if transportType == "b":
        return 1

    precioKm = float(input("Km: ")) * 0.25
    if transportType == "cmn":
        return precioKm + float(input("Toneladas: ")) * 0.15

    return precioKm


transportType = input("Tipo (b - bicicleta, m - moto, c - coche, cmn - camion): ")
print(getPrecio(transportType))
