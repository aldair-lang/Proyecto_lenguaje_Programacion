import subprocess
import shutil
import os

# CLASE PADRE (Superclase - Sesión 15)
class MotorExterno:
    def __init__(self, nombre: str, archivo: str):
        self.nombre = nombre
        self.__archivo = archivo  # Atributo privado (Encapsulamiento - Sesión 15)

    def obtener_archivo(self) -> str:
        return self.__archivo

    def ejecutar(self, datos: dict):  # Método polimórfico base
        raise NotImplementedError("Subclase debe implementar ejecutar()")

# CLASE HIJA 1 (Herencia y Polimorfismo - Sesión 15)
class MotorHaskell(MotorExterno):
    def __init__(self, archivo_hs: str, ejecutable: str):
        super().__init__("Haskell Funcional", archivo_hs)
        self.ejecutable = ejecutable

    def compilar(self):
        if not os.path.exists(self.ejecutable):
            subprocess.run(["ghc", "-O2", self.obtener_archivo(), "-o", "calculo"], check=True)

    def ejecutar(self, datos: dict) -> tuple:  # Devuelve una Tupla (Sesión 14)
        self.compilar()
        args = [
            self.ejecutable,
            datos["consumo"], datos["antiguo"], datos["estab"],
            datos["espacio"], datos["humedad"], datos["ausente"]
        ]
        res = subprocess.run(args, capture_output=True, text=True)
        partes = res.stdout.strip().split("|")
        return (partes[0], partes[1] if len(partes) > 1 else "Desconocido")

# CLASE HIJA 2 (Herencia y Polimorfismo - Sesión 15)
class MotorProlog(MotorExterno):
    def __init__(self, archivo_pl: str):
        super().__init__("Prolog Logico", archivo_pl)
        self.__ruta_swipl = shutil.which("swipl") or r"C:\Program Files\swipl\bin\swipl.exe"

    def ejecutar(self, datos: dict) -> str:
        consulta = (
            f"evaluar({datos['consumo']}, {datos['antiguo']}, {datos['estab']}, "
            f"{datos['espacio']}, {datos['humedad']}, {datos['ausente']})"
        )
        res = subprocess.run(
            [self.__ruta_swipl, "-q", "-s", self.obtener_archivo(), "-g", consulta, "-t", "halt"],
            capture_output=True, text=True
        )
        return res.stdout.strip()