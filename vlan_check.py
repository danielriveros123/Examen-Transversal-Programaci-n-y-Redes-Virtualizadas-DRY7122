# vlan_check.py

def check_vlan(vlan_id):
    if 1 <= vlan_id <= 99:
        return "VLAN de rango normal"
    elif vlan_id > 99:
        return "VLAN de rango extendido"
    else:
        return "VLAN fuera de rango"

def main():
    try:
        vlan_id = int(input("Ingrese el número de VLAN: "))
        result = check_vlan(vlan_id)
        print(result)
    except ValueError:
        print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()
