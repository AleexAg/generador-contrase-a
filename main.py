import random


def g_contrasena():
    may = ['A', 'B', 'C', '', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    min = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'e', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    sim = ['&', '#', '$', '%']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    caracteres = may + min + sim + nums
    contrasena = []

    for i in range(15):
        car_random = random.choice(caracteres)
        contrasena.append(car_random)
    contrasenas = "".join(contrasena)

    return contrasenas


def principal():
    contrasena = g_contrasena()
    print("Su nueva contraseña es:", contrasena)


if __name__ == '__main__':
    principal()
