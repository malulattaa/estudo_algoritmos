def inverter(string):
    if len(string) <= 1:
        return string
    return string[-1] + inverter(string[:-1])

palavra = input("Palavra que deseja inverter: ")
print(inverter(palavra))