import tkinter as tk
from tkinter import ttk, messagebox
import math

## logica de programacion ##

class FormaTridimensional: # Clase Padre (Base para las demás) 
    
    def __init__(self, titulo):
        self.nombre_forma = titulo

    def mostrar_info(self):
        return f"Figura seleccionada: {self.nombre_forma}"
    
    def calcular_volumen(self):
        raise NotImplementedError("Las clases hijas deben implementar 'calcular_volumen'")
    
    def calcular_superficie(self):
        raise NotImplementedError("Las clases hijas deben implementar 'calcular_superficie'")

class CilindroForma(FormaTridimensional): # clase hija
    
    def __init__(self, valor_radio, valor_altura):
        super().__init__("Cilindro")
        self.radio_dato = float(valor_radio)
        self.altura_dato = float(valor_altura)
        
    def calcular_volumen(self):
        volumen = math.pi * (self.radio_dato**2) * self.altura_dato
        return volumen
        
    def calcular_superficie(self):
        area_lateral = 2 * math.pi * self.radio_dato * self.altura_dato
        area_bases = 2 * math.pi * (self.radio_dato**2)
        superficie = area_lateral + area_bases
        return superficie
    
    def mostrar_info(self):
        info_base = super().mostrar_info()
        return (
            f"{info_base}\n"
            f"Radio (r): {self.radio_dato:.2f} cm\n"
            f"Altura (h): {self.altura_dato:.2f} cm"
        )

class EsferaForma(FormaTridimensional): # clase hija
    
    def __init__(self, valor_radio):
        super().__init__("Esfera")
        self.radio_dato = float(valor_radio)
        
    def calcular_volumen(self):
        volumen = (4/3) * math.pi * (self.radio_dato**3)
        return volumen

    def calcular_superficie(self):
        superficie = 4 * math.pi * (self.radio_dato**2)
        return superficie

    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base}\nRadio (r): {self.radio_dato:.2f} cm"

class PiramideForma(FormaTridimensional): # clase hija
    
    def __init__(self, valor_base, valor_altura, valor_apotema):
        super().__init__("Pirámide (Base Cuadrada)")
        self.base_dato = float(valor_base)
        self.altura_dato = float(valor_altura)
        self.apotema_dato = float(valor_apotema) 
        
    def area_base(self):
        return self.base_dato ** 2
    
    def perimetro_base(self):
        return 4 * self.base_dato

    def calcular_volumen(self):
        volumen = (1/3) * self.area_base() * self.altura_dato
        return volumen

    def calcular_superficie(self):
        area_base_calc = self.area_base()
        perimetro_base_calc = self.perimetro_base()
        
        area_lateral = (perimetro_base_calc * self.apotema_dato) / 2
        superficie = area_base_calc + area_lateral
        return superficie

    def mostrar_info(self):
        info_base = super().mostrar_info()
        return (
            f"{info_base}\n"
            f"Lado Base: {self.base_dato:.2f} cm\n"
            f"Altura (h): {self.altura_dato:.2f} cm\n"
            f"Apotema: {self.apotema_dato:.2f} cm"
        )


## interfaz grafica ##

class AplicacionSolido:
    def __init__(self, ventana_principal):
        self.ventana = ventana_principal
        ventana_principal.title("Calculadora de Sólidos (Cilindro, Esfera, Pirámide)")
        ventana_principal.resizable(False, False)
        
        self.figura_instancia = None 
        self.tipo_seleccionado = tk.StringVar(value="Cilindro")
        self.campos_texto = {}
        self.etiquetas_campos = {}
        
        frame_principal = ttk.Frame(ventana_principal, padding="15")
        frame_principal.pack(padx=10, pady=10)

        ttk.Label(frame_principal, text="1. Seleccione la Figura Sólida:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        
        lista_opciones = ["Cilindro", "Esfera", "Pirámide"]
        self.menu_desplegable = ttk.Combobox(frame_principal, textvariable=self.tipo_seleccionado, values=lista_opciones, state="readonly", width=18)
        self.menu_desplegable.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.menu_desplegable.bind("<<ComboboxSelected>>", self.actualizar_campos_visibles)

        frame_parametros = ttk.LabelFrame(frame_principal, text="2. Ingrese Parámetros", padding="10")
        frame_parametros.grid(row=1, column=0, columnspan=2, padx=5, pady=10, sticky="ew")

        campos_def = [("dato1", "Radio/Lado Base:"), ("dato2", "Altura:"), ("dato3", "Apotema:")]
        valores_iniciales = ["5.0", "10.0", "12.0"]

        for i, (clave, texto) in enumerate(campos_def):
            etiqueta = ttk.Label(frame_parametros, text=texto)
            etiqueta.grid(row=i, column=0, padx=5, pady=5, sticky="w")
            self.etiquetas_campos[clave] = etiqueta
            
            entrada = ttk.Entry(frame_parametros, width=15)
            entrada.grid(row=i, column=1, padx=5, pady=5)
            entrada.insert(0, valores_iniciales[i])
            self.campos_texto[clave] = entrada
        
        self.actualizar_campos_visibles() 

        ttk.Button(frame_principal, text="Calcular Volumen y Superficie", command=self.calcular).grid(row=4, column=0, columnspan=2, pady=10)

        frame_resultados = ttk.LabelFrame(frame_principal, text="3. Resultados", padding="10")
        frame_resultados.grid(row=5, column=0, columnspan=2, padx=5, pady=10, sticky="ew")

        self.texto_figura = ttk.Label(frame_resultados, text="Figura: ")
        self.texto_figura.pack(anchor='w', pady=2)
        self.texto_volumen = ttk.Label(frame_resultados, text="Volumen (V): ")
        self.texto_volumen.pack(anchor='w', pady=2)
        self.texto_superficie = ttk.Label(frame_resultados, text="Superficie Total (A): ")
        self.texto_superficie.pack(anchor='w', pady=2)
        self.texto_detalles = ttk.Label(frame_resultados, text="Detalles: ")
        self.texto_detalles.pack(anchor='w', pady=2)

    def actualizar_campos_visibles(self, evento=None):
        figura = self.tipo_seleccionado.get()
        
        for etiqueta in self.etiquetas_campos.values():
            etiqueta.grid_remove()
        for entrada in self.campos_texto.values():
            entrada.grid_remove()

        if figura == "Cilindro":
            self.etiquetas_campos["dato1"].config(text="Radio (r):")
            self.etiquetas_campos["dato1"].grid(row=0, column=0, sticky="w")
            self.campos_texto["dato1"].grid(row=0, column=1)
            
            self.etiquetas_campos["dato2"].config(text="Altura (h):")
            self.etiquetas_campos["dato2"].grid(row=1, column=0, sticky="w")
            self.campos_texto["dato2"].grid(row=1, column=1)
        
        elif figura == "Esfera":
            self.etiquetas_campos["dato1"].config(text="Radio (r):")
            self.etiquetas_campos["dato1"].grid(row=0, column=0, sticky="w")
            self.campos_texto["dato1"].grid(row=0, column=1)
        
        elif figura == "Pirámide":
            self.etiquetas_campos["dato1"].config(text="Lado Base:")
            self.etiquetas_campos["dato1"].grid(row=0, column=0, sticky="w")
            self.campos_texto["dato1"].grid(row=0, column=1)
            
            self.etiquetas_campos["dato2"].config(text="Altura (h):")
            self.etiquetas_campos["dato2"].grid(row=1, column=0, sticky="w")
            self.campos_texto["dato2"].grid(row=1, column=1)
            
            self.etiquetas_campos["dato3"].config(text="Apotema (a):")
            self.etiquetas_campos["dato3"].grid(row=2, column=0, sticky="w")
            self.campos_texto["dato3"].grid(row=2, column=1)

    def calcular(self):
        
        tipo_actual = self.tipo_seleccionado.get()
        
        try:
            v1 = self.campos_texto["dato1"].get().replace(',', '.').strip()
            v2 = self.campos_texto["dato2"].get().replace(',', '.').strip()
            v3 = self.campos_texto["dato3"].get().replace(',', '.').strip()
            
            figura_nueva = None

            if tipo_actual == "Cilindro":
                if not v1 or not v2:
                    raise ValueError("Debe ingresar Radio y Altura.")
                figura_nueva = CilindroForma(v1, v2)
            
            elif tipo_actual == "Esfera":
                if not v1:
                    raise ValueError("Debe ingresar el Radio.")
                figura_nueva = EsferaForma(v1)
            
            elif tipo_actual == "Pirámide":
                if not v1 or not v2 or not v3:
                    raise ValueError("Debe ingresar Lado Base, Altura y Apotema.")
                figura_nueva = PiramideForma(v1, v2, v3)

            if figura_nueva:
                volumen = figura_nueva.calcular_volumen()
                superficie = figura_nueva.calcular_superficie()
                
                self.texto_figura.config(text=f"Figura: {figura_nueva.nombre_forma}")
                self.texto_volumen.config(text=f"Volumen (V): {volumen:.2f} cm³")
                self.texto_superficie.config(text=f"Superficie Total (A): {superficie:.2f} cm²")
                
                detalles = figura_nueva.mostrar_info().split('\n')[1:]
                self.texto_detalles.config(text="Detalles: " + " | ".join(detalles))
                
        except ValueError as e:
            messagebox.showerror("Error de Entrada", f"Valor inválido o faltante. {e}. Asegúrese de usar números positivos.")
        except Exception as e:
            messagebox.showerror("Error del Sistema", f"Ocurrió un error inesperado. Mensaje: {e}")


if __name__ == "__main__":
    raiz = tk.Tk()
    app = AplicacionSolido(raiz)
    raiz.mainloop()