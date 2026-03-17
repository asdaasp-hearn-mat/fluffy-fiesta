from scipy.optimize import fsolve
import numpy as np
def calcular_pendiente(p_a, p_b):
    x_a, y_a = p_a[0],p_a[1] 
    x_b, y_b = p_b[0],p_b[1]  
    pendiente = (y_b - y_a) / (x_b - x_a) if (x_b - x_a) != 0 else np.inf  # Evitar división por 0
    return pendiente

# Derivadas de la espiral 
def derivada_x(t):
    return -0.25 * (np.cos(t) - t * np.sin(t))

def derivada_y(t):
    return 0.25 * (np.sin(t) + t * np.cos(t))

# Pendiente de la tangente en t
def pendiente_tangente(t):
    dx_dt = derivada_x(t)
    dy_dt = derivada_y(t)
    return dy_dt / dx_dt if dx_dt != 0 else np.inf
# Función espiral de Arquímedes
def espiral_function(t):
    return np.array([-0.5 * t * np.cos(t), 0.5 * t * np.sin(t)])

# Función para encontrar los valores de t donde las pendientes son iguales
def ecuacion_pendiente(t, pendiente_recta):
    return pendiente_tangente(t) - pendiente_recta

# Puntos inicial y final (el final puede ser modificable con el t_value)
a=0
b=2*np.pi+np.pi/4 #este es el t_value
p_a = espiral_function(a)  # punto p(a)
p_b = espiral_function(b)  # punto p(b)

# Calcular la pendiente de la recta
pendiente_recta = calcular_pendiente(p_a, p_b)

# Encontrar los valores de t en [a, b] donde la pendiente de la tangente es igual a la de la recta
guesses= [a,0.8*a+0.2*b,(a + b) / 2,b]  
for guess in guesses:# Adivinanza inicial para w
    w_solucion = fsolve(ecuacion_pendiente, guess, args=(pendiente_recta))
    print(f"El valor de w donde la pendiente de la tangente es igual a la de la recta secante es: {w_solucion}")

