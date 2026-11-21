import tkinter as tk
from tkinter import ttk, messagebox

def evaluar_riesgos():
    puntos_riesgo = 0
    alertas = []
    recomendaciones = []

    # 1. Análisis Eléctrico
    equipos = combo_equipos.get()
    proteccion = var_estabilizador.get()
    cableado_antiguo = var_antiguo.get()

    if equipos == "Alta (PC Gamer, Estufa, Microondas)" and cableado_antiguo:
        puntos_riesgo += 40
        alertas.append("• Sobrecarga severa inminente: alta demanda en cableado con desgaste.")
        recomendaciones.append("Distribuir las cargas en circuitos independientes y revisar térmicas.")
    elif equipos == "Alta (PC Gamer, Estufa, Microondas)" and not proteccion:
        puntos_riesgo += 25
        alertas.append("• Equipos de alto consumo sin supresor ni estabilizador.")
        recomendaciones.append("Conectar regulador de voltaje para evitar daños por picos.")

    # 2. Análisis Ambiental / Ventilación
    espacio = combo_espacio.get()
    humedad = var_humedad.get()

    if espacio == "Cerrado / Sin ventanas" and humedad:
        puntos_riesgo += 30
        alertas.append("• Ambiente propenso a condensación y fallas por sulfatación.")
        recomendaciones.append("Instalar extractor o deshumidificador para proteger conexiones y salud.")
    elif espacio == "Cerrado / Sin ventanas":
        puntos_riesgo += 15
        recomendaciones.append("Ventilar periódicamente para evitar concentración térmica.")

    # 3. Análisis de Accesos y Descuido
    ausente = var_ausente.get()
    sin_supervision = var_ninos_mascotas.get()

    if ausente and equipos != "Baja (Cargadores, Lámparas)":
        puntos_riesgo += 20
        alertas.append("• Cargas activas sin presencia de personas en el predio.")
        recomendaciones.append("Desconectar periféricos y cargas térmicas al salir.")

    if sin_supervision:
        puntos_riesgo += 15
        recomendaciones.append("Proteger tomacorrientes a nivel de suelo con tapas de seguridad.")

    # Razonamiento Global
    txt_resultado.config(state="normal")
    txt_resultado.delete("1.0", tk.END)

    if puntos_riesgo >= 50:
        nivel = "CRÍTICO (Acción Inmediata)"
        color = "#b30000"
    elif puntos_riesgo >= 25:
        nivel = "MODERADO (Atención Preventiva)"
        color = "#d97706"
    else:
        nivel = "SEGURO (Bajo Control)"
        color = "#15803d"

    informe = f"DIAGNÓSTICO: {nivel}\nNivel de Vulnerabilidad: {puntos_riesgo}/100\n\n"
    
    if alertas:
        informe += "FACTORES DE RIESGO DETECTADOS:\n" + "\n".join(alertas) + "\n\n"
    else:
        informe += "No se identificaron factores críticos de riesgo inmediato.\n\n"

    if recomendaciones:
        informe += "ACCIONES PREVENTIVAS SUGERIDAS:\n" + "\n".join(f"→ {r}" for r in recomendaciones)
    else:
        informe += "→ Mantener los hábitos actuales de inspección."

    txt_resultado.insert(tk.END, informe)
    lbl_estado.config(text=f"Estado: {nivel}", fg=color)
    txt_resultado.config(state="disabled")

# Configuración de Ventana
root = tk.Tk()
root.title("Monitor Preventivo de Seguridad y Cargas")
root.geometry("620x680")
root.resizable(False, False)

frame = ttk.Frame(root, padding="15")
frame.pack(fill="both", expand=True)

ttk.Label(frame, text="Evaluador Preventivo de Entorno", font=("Segoe UI", 14, "bold")).pack(anchor="w", pady=(0, 10))

# Sección Eléctrica
lf_elec = ttk.LabelFrame(frame, text=" 1. Estado de Instalación Eléctrica ", padding="10")
lf_elec.pack(fill="x", pady=5)

ttk.Label(lf_elec, text="Nivel de consumo simultáneo:").grid(row=0, column=0, sticky="w", pady=2)
combo_equipos = ttk.Combobox(lf_elec, values=["Baja (Cargadores, Lámparas)", "Media (Laptop, TV, Ventilador)", "Alta (PC Gamer, Estufa, Microondas)"], state="readonly", width=35)
combo_equipos.current(1)
combo_equipos.grid(row=0, column=1, pady=2, padx=5)

var_estabilizador = tk.BooleanVar()
chk_estab = ttk.Checkbutton(lf_elec, text="Cuenta con estabilizador / regulador", variable=var_estabilizador)
chk_estab.grid(row=1, column=0, columnspan=2, sticky="w", pady=2)

var_antiguo = tk.BooleanVar()
chk_ant = ttk.Checkbutton(lf_elec, text="Cableado o infraestructura con más de 10 años", variable=var_antiguo)
chk_ant.grid(row=2, column=0, columnspan=2, sticky="w", pady=2)

# Sección Entorno
lf_entorno = ttk.LabelFrame(frame, text=" 2. Entorno y Hábitos ", padding="10")
lf_entorno.pack(fill="x", pady=5)

ttk.Label(lf_entorno, text="Tipo de habitación:").grid(row=0, column=0, sticky="w", pady=2)
combo_espacio = ttk.Combobox(lf_entorno, values=["Ventilación cruzada / Ventanas amplias", "Cerrado / Sin ventanas"], state="readonly", width=35)
combo_espacio.current(0)
combo_espacio.grid(row=0, column=1, pady=2, padx=5)

var_humedad = tk.BooleanVar()
ttk.Checkbutton(lf_entorno, text="Presencia notoria de humedad o filtraciones", variable=var_humedad).grid(row=1, column=0, columnspan=2, sticky="w", pady=2)

var_ausente = tk.BooleanVar()
ttk.Checkbutton(lf_entorno, text="Equipos operando mientras el lugar queda vacío", variable=var_ausente).grid(row=2, column=0, columnspan=2, sticky="w", pady=2)

var_ninos_mascotas = tk.BooleanVar()
ttk.Checkbutton(lf_entorno, text="Cables accesibles a ras de piso con tránsito frecuente", variable=var_ninos_mascotas).grid(row=3, column=0, columnspan=2, sticky="w", pady=2)

# Botón Acción
btn_evaluar = tk.Button(frame, text="Analizar y Razonar Prevención", font=("Segoe UI", 10, "bold"), bg="#0284c7", fg="white", relief="flat", command=evaluar_riesgos, pady=6)
btn_evaluar.pack(fill="x", pady=12)

# Resultados
lbl_estado = tk.Label(frame, text="Estado: Pendiente de análisis", font=("Segoe UI", 10, "bold"), fg="#4b5563")
lbl_estado.pack(anchor="w")

txt_resultado = tk.Text(frame, height=11, font=("Consolas", 9), wrap="word", padx=8, pady=8)
txt_resultado.pack(fill="both", expand=True, pady=5)
txt_resultado.config(state="disabled")

root.mainloop()