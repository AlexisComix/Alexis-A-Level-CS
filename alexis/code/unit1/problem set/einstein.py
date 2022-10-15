def emc2():
    C = 300_000_000
    str_mass = ""
    numeric = False
    while not numeric:
        str_mass = input("Input mass in kg: ")
        numeric = str_mass.isnumeric()
        if not numeric or str_mass == "":
            print("Invalid input.")
    return float(str_mass) * C**2

if __name__ == "__main__":
    energy = emc2()
    print(f"{energy}J")