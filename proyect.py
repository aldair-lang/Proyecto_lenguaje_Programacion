import os
from motores import MotorHaskell, MotorProlog  # Modularidad (Sesión 14)

def preguntar_opcion(texto: str, opciones: list) -> str:
    while True:  # Estructura repetitiva (Sesión 13)
        resp = input(f"{texto} ({'/'.join(opciones)}): ").strip().lower()
        if resp in opciones:  # Condicional y pertenencia en lista (Sesiones 12 y 13)
            return resp
        print(f"  [!] Opcion invalida. Elija: {', '.join(opciones)}")

def main():
    print("==========================================================")
    print("  ASISTENTE PREVENTIVO DE RIESGOS (Python + Prolog + Haskell)")
    print("==========================================================\n")

    # Diccionario para estructurar los datos (Sesión 14)
    respuestas = {
        "consumo": preguntar_opcion("1. Nivel de consumo electrico simultaneo", ["bajo", "medio", "alto"]),
        "antiguo": preguntar_opcion("2. El cableado tiene mas de 10 anos?", ["si", "no"]),
        "estab":   preguntar_opcion("3. Cuenta con estabilizador o supresor?", ["si", "no"]),
        "espacio": preguntar_opcion("4. Tipo de ventilacion del ambiente", ["ventilado", "cerrado"]),
        "humedad": preguntar_opcion("5. Se detecta humedad o filtraciones?", ["si", "no"]),
        "ausente": preguntar_opcion("6. Quedan equipos encendidos cuando sales?", ["si", "no"])
    }

    print("\n--- Procesando inferencia logica y calculo funcional ---\n")

    # Instanciación de objetos (Sesión 15)
    exe_hs = "calculo.exe" if os.name == "nt" else "./calculo"
    motor_hs = MotorHaskell("calculo.hs", exe_hs)
    motor_pl = MotorProlog("razonador.pl")

    puntaje, nivel = motor_hs.ejecutar(respuestas)  # Desempaquetado de Tupla (Sesión 14)
    deducciones = motor_pl.ejecutar(respuestas)

    print(f"DIAGNOSTICO GENERAL : {nivel}")
    print(f"INDICE DE RIESGO    : {puntaje} / 100 puntos\n")
    print("ANALISIS DEDUCTIVO (Prolog):")
    if deducciones:
        print(deducciones)
    else:
        print("-> No se detectaron combinaciones de riesgo critico.")

if __name__ == "__main__":
    main()