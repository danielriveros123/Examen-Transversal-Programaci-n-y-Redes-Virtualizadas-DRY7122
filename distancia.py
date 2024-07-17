import requests
import sys

def obtener_coordenadas(ciudad):
    api_key = 'd5aa4db70bbd4df7b94775e07d9ae4cd'
    url = f'https://api.opencagedata.com/geocode/v1/json?q={ciudad}&key={api_key}&language=es'
    response = requests.get(url).json()
    if response['results']:
        coordenadas = response['results'][0]['geometry']
        return coordenadas['lat'], coordenadas['lng']
    else:
        print(f"No se encontraron coordenadas para la ciudad {ciudad}.")
        return None, None

def obtener_distancia(origen, destino, transporte):
    coords_origen = obtener_coordenadas(origen)
    coords_destino = obtener_coordenadas(destino)
    if not coords_origen or not coords_destino:
        return None, None, None
   
    url = f'https://graphhopper.com/api/1/route?point={coords_origen[0]},{coords_origen[1]}&point={coords_destino[0]},{coords_destino[1]}&vehicle={transporte}&locale=es&calc_points=true&key=64ce46ac-1149-4e9a-9dd4-5f708a87e6b0'
    response = requests.get(url).json()
   
    if 'paths' in response and response['paths']:
        distancia_km = response['paths'][0]['distance'] / 1000
        distancia_millas = distancia_km * 0.621371
        tiempo_seg = response['paths'][0]['time'] / 1000
        return distancia_km, distancia_millas, tiempo_seg
    else:
        print("No se pudo calcular la distancia.")
        return None, None, None

def mostrar_narrativa(origen, destino, distancia_km, distancia_millas, tiempo_horas, tiempo_minutos):
    print(f"\nNarrativa del viaje desde {origen} hasta {destino}:")
    print(f"La distancia entre {origen} y {destino} es de {distancia_km:.2f} km ({distancia_millas:.2f} millas).")
    print(f"El tiempo estimado de viaje es de {tiempo_horas:.0f} horas y {tiempo_minutos:.0f} minutos.\n")

def main():
    while True:
        print("\n----- Medición de distancia entre ciudades -----")
        origen = input("Ciudad de Origen (o 's' para salir): ").strip().lower()
        if origen == 's':
            print("Saliendo del programa.")
            sys.exit()
       
        destino = input("Ciudad de Destino (o 's' para salir): ").strip().lower()
        if destino == 's':
            print("Saliendo del programa.")
            sys.exit()

        print("Elige el medio de transporte (car, bike, foot) (o 's' para salir): ")
        transporte = input("Transporte: ").strip().lower()
        if transporte == 's':
            print("Saliendo del programa.")
            sys.exit()

        if transporte not in ['car', 'bike', 'foot']:
            print("Medio de transporte no válido. Usa 'car', 'bike' o 'foot'.")
            continue

        distancia_km, distancia_millas, tiempo_seg = obtener_distancia(origen, destino, transporte)

        if distancia_km and distancia_millas and tiempo_seg:
            tiempo_horas = tiempo_seg // 3600
            tiempo_minutos = (tiempo_seg % 3600) // 60
            mostrar_narrativa(origen, destino, distancia_km, distancia_millas, tiempo_horas, tiempo_minutos)
        else:
            print("No se pudo calcular la distancia. Verifica los nombres de las ciudades y el medio de transporte.")

if __name__ == "__main__":
    main()
