from manim import *
from scipy.optimize import fsolve
import numpy as np

def producto_cruzado(v1, v2):
    """Función para calcular el producto cruzado 2D"""

    return v1[0] * v2[1] - v1[1] * v2[0]

# Función para la espiral
espiral_function = lambda t: np.array([- 0.25*t * np.cos(t), 0.25*t * np.sin(t)])

# Derivada de la espiral (tangente)
def derivada_espiral(t):
    return np.array([- 0.25*(np.cos(t) - t * np.sin(t)), 0.25*(np.sin(t) + t * np.cos(t))])

# Función para encontrar w tal que la tangente sea paralela a la secante
def encontrar_w_value(t_value):
    p_0 = espiral_function(0)  # p(0)
    p_t = espiral_function(t_value)  # p(t_value)
    # Vectores
    secante = p_t - p_0  # p(t_value) - p(0)
    # Función para calcular el producto cruzado
    def ecuacion_paralelismo(w):
        tangente = derivada_espiral(w)
        return producto_cruzado(tangente, secante)
    # Adivinanza inicial para w
    guess = 0.9 * t_value  
    w_value = fsolve(ecuacion_paralelismo, guess, xtol=1e-6)[0]
    return w_value


    
class E1(Scene):
    def construct(self):
        # Paso 1: Mostrar el límite de la definición de la derivada en amarillo
        limite_derivada = MathTex(
            r"\lim_{x \to c} \frac{f(x) - f(c)}{x - c}",
            color=YELLOW
        ).scale(2)
        self.play(Write(limite_derivada))
        self.wait(2)
        
        # Paso 2: Transformación a 0/0
        indeterminada = MathTex(
            r"\frac{0}{0}",
            color=YELLOW
        ).scale(2)
        self.play(Transform(limite_derivada, indeterminada))
        self.wait(1)
        
        # Paso 3: Mostrar "Forma indeterminada" debajo
        forma_indeterminada = Text("Forma indeterminada", font_size=36)
        forma_indeterminada.next_to(indeterminada, DOWN)
        self.play(Write(forma_indeterminada))
        self.wait(2)
        
        # Paso 4: FadeOut de los objetos en pantalla
        self.play(FadeOut(limite_derivada), FadeOut(forma_indeterminada))
        self.wait(1)
        
        # Paso 5: Mostrar los nuevos límites
        limites_cero = MathTex(
            r"\lim_{x \to c} f(x) = \lim_{x \to c} g(x) = 0"
        ).scale(1.5).to_edge(UP).shift(DOWN)
        self.play(Write(limites_cero))
        self.wait(2)
        
        # Paso 6: Mostrar el límite del cociente en amarillo
        limite_cociente = MathTex(
            r"\text{?`}\lim_{x \to c} \frac{f(x)}{g(x)}\text{?}",
            color=YELLOW
        ).scale(1.5)
        limite_cociente.next_to(limites_cero, DOWN,buff=0.5)
        self.play(Write(limite_cociente))
        self.wait(2)
        
        # Paso 7: Mostrar "= ¿?" al lado del límite del cociente
        #pregunta = MathTex(r"= \text{?`?}").scale(1.5)
        #pregunta.next_to(limite_cociente, RIGHT)
        #self.play(Write(pregunta))
        self.wait(2)
        texto_final =Tex()





class E2(Scene):
    def construct(self):

        # Crear plano y ejes
        plano_graficado = NumberPlane(
            background_line_style={
                "stroke_color": GRAY,
                "stroke_width": 2,
                "stroke_opacity": 0.4
            }
        ).shift(LEFT + DOWN).scale(2)
        axes_labels = plano_graficado.get_axis_labels(x_label="x", y_label="y")

        # Mostrar el plano graficado
        self.play(Create(plano_graficado), Write(axes_labels))

        # Función paramétrica que representa la espiral
        espiral_function = lambda t: plano_graficado.c2p(- 0.25*t * np.cos(t), 0.25*t * np.sin(t))
        a = -1
        b = 2*np.pi+np.pi/4

        # Crear espiral
        espiral = ParametricFunction(
            espiral_function,
            t_range=[a, b],
            color=BLUE
        )
        self.play(Create(espiral))

        # ValueTracker para t_value
        t_tracker = ValueTracker(b)

        # Crear punto y secante
        punto = always_redraw(
            lambda: Dot(espiral_function(t_tracker.get_value()), color=YELLOW)
        )
        punto_inicial=Dot(plano_graficado.c2p(0,0),color=YELLOW)
        punto_label = always_redraw(
            lambda: MathTex(r"(g(t), f(t))", color=YELLOW).next_to(punto, RIGHT)
        )
        secante = always_redraw(
            lambda: Line(espiral_function(0), espiral_function(t_tracker.get_value()), color=ORANGE)
        )

        self.play(Create(secante), Create(punto), Write(punto_label),Create(punto_inicial))
        # Añadir textos y cajas en la parte derecha
        texto_1 = MathTex(r"f(c) = g(c) = 0", color=YELLOW)
        texto_2 = MathTex(r"f \text{ y } g \text{ suaves}", r"\text{ excepto quizás en el valor } c", color=WHITE).scale(0.8)
        texto_3 = MathTex(
            r"\frac{f(t)}{g(t)} = \frac{f(t) - f(c)}{g(t) - g(c)}", color=YELLOW
        )
        texto_4 = Tex("pendiente de la secante", color=PURPLE)

        # Posicionar los textos
        texto_1.to_corner(UR)
        texto_2.next_to(texto_1, DOWN, aligned_edge=RIGHT)
        texto_3.next_to(texto_2, DOWN, aligned_edge=RIGHT)
        texto_4.next_to(texto_3, DOWN, aligned_edge=RIGHT)

        # Crear recuadros alrededor de los textos
        box_1 = SurroundingRectangle(texto_1, color=YELLOW)
        box_2 = SurroundingRectangle(texto_2, color=YELLOW)
        box_3 = SurroundingRectangle(texto_3, color=PURPLE)

        # Mostrar los textos con sus recuadros
        self.play(Write(texto_1), Create(box_1))
        self.play(Write(texto_2), Create(box_2))
        self.play(Write(texto_3), Write(texto_4), Create(box_3))
        self.wait(2)
        self.play(FadeOut(VGroup(texto_1,texto_2,texto_3,texto_4,box_1,box_2,box_3)))
        self.wait(2)
        # Tangente
        def tangente_parametrica(w, k_range=(-1, 1)):
            # La función de la tangente es p(w) + k * p'(w)
            return ParametricFunction(
                lambda k: plano_graficado.c2p(
            - 0.25*w * np.cos(w) + k * derivada_espiral(w)[0],  # Componente x
            0.25*w * np.sin(w) + k * derivada_espiral(w)[1]   # Componente y
        ),
        t_range=k_range,
        color=GREEN
    )  
        tangente = always_redraw(
            lambda: tangente_parametrica(encontrar_w_value(t_tracker.get_value()))
        )

        self.play(Create(tangente))
        self.wait(2)
        punto_w = always_redraw(
            lambda: Dot(espiral_function(encontrar_w_value(t_tracker.get_value())), color=YELLOW)
        )   
        w_label=always_redraw(
            lambda: MathTex(r"(g(w), f(w))", color=YELLOW).next_to(punto_w, DOWN)
        )
        #punto_w_coords = tangente.get_function[0]
        #punto_w = always_redraw(lambda: Dot(punto_w_coords, color=YELLOW))
        self.play(Create(punto_w),Create(w_label))
        limite_inicial = MathTex(r"\lim_{t \to c} \frac{f(t)}{g(t)}").to_corner(UP + RIGHT)
        condicion = Tex(r"Por el teorema de Cauchy").next_to(limite_inicial, DOWN,buff=0.7).align_to(limite_inicial,RIGHT)
        intermedio = MathTex(r"\frac{f(t)}{g(t)} = \frac{g'(w)}{g'(w)}").next_to(condicion, DOWN).align_to(limite_inicial,RIGHT)
        # Mostrar en pantalla
        #self.play(Create(limite_inicial))
        self.play(Create(condicion))
        self.play(Create(intermedio))
        # Desaparecer la condición y transformar el intermedio
        self.play(FadeOut(condicion))
        intermedio.generate_target()
        intermedio.target = MathTex(r"\lim_{t \to c} \frac{f(t)}{g(t)} = \lim_{w \to c} \frac{g'(w)}{g'(w)}").move_to(intermedio).align_to(limite_inicial,RIGHT)
        self.wait()
        self.play(t_tracker.animate.set_value(0), run_time=5, rate_func=linear)
        self.play(MoveToTarget(intermedio))
        self.wait(2)

class E4(Scene):
    def construct(self):
        # Paso 1: Escribir el teorema en partes con una correcta estructuración.
        teorema_text = Tex(
            r"\textbf{Teorema} (Regla de L'Hôpital). Sean $f:(a,b) \to \mathbb{R}$ y $g:(a,b) \to \mathbb{R}$, ",
            r"funciones diferenciables, excepto tal vez en $c$, tales que:", 
            tex_environment="flushleft", font_size=36
        )
        
        # Limites iniciales
        lim_f_g = MathTex(r"\lim_{x \to c^{ }} f(x) = 0, \quad \lim_{x \to c^{ }} g(x) = 0", font_size=36)
        lim_L = MathTex(r"L = \lim_{x \to c^{ }} \frac{f'(x)}{g'(x)}", font_size=36)
        entonces_text = Tex(r"Entonces:", font_size=36)
        lim_final = MathTex(r"\lim_{x \to", r"c^{ }", r"} \frac{f(x)}{g(x)} = L.", color=YELLOW, font_size=36) 
        # Agrupación del teorema
        teorema_completo = VGroup(teorema_text, lim_f_g, lim_L, lim_final).arrange(DOWN)
        entonces_text.move_to(lim_final).shift(4*LEFT).align_to(teorema_text,LEFT)
        # Paso 2: Mostrar el teorema en pantalla
        self.play(Write(teorema_text))
        self.play(Write(lim_f_g), Write(lim_L))
        self.play(Write(entonces_text))
        self.play(Write(lim_final))

        # Paso 3: Rodear el teorema con un cuadro amarillo
        cuadro = SurroundingRectangle(teorema_completo, color=YELLOW)
        self.play(Create(cuadro))
        self.wait(2)

        # Crear expresiones con "c^{-}" y mantener las posiciones
        lim_f_g_c_neg = MathTex(r"\lim_{x \to c^{-}} f(x) = 0, \quad \lim_{x \to c^{-}} g(x) = 0", font_size=36).move_to(lim_f_g)
        lim_L_c_neg = MathTex(r"L = \lim_{x \to c^{-}} \frac{f'(x)}{g'(x)}", font_size=36).move_to(lim_L)
        lim_final_c_neg = MathTex(
            r"\lim_{x \to", r"c^{-}", r"} \frac{f(x)}{g(x)} = L.", 
            color=YELLOW, font_size=36
        ).move_to(lim_final)

        # Transformaciones con "c^{-}" usando TransformMatchingTex
        self.play(Transform(lim_f_g, lim_f_g_c_neg),
                  Transform(lim_L, lim_L_c_neg),
                  Transform(lim_final, lim_final_c_neg))
        self.wait(2)

        # Crear expresiones con "c^{+}" y mantener las posiciones
        lim_f_g_c_pos = MathTex(r"\lim_{x \to c^{+}} f(x) = 0, \quad \lim_{x \to c^{+}} g(x) = 0", font_size=36).move_to(lim_f_g)
        lim_L_c_pos = MathTex(r"L = \lim_{x \to c^{+}} \frac{f'(x)}{g'(x)}", font_size=36).move_to(lim_L)
        lim_final_c_pos = MathTex(
            r"\lim_{x \to", r"c^{+}", r"} \frac{f(x)}{g(x)} = L.", 
            color=YELLOW, font_size=36
        ).move_to(lim_final)

        # Transformaciones con "c^{+}" usando TransformMatchingTex
        self.play(TransformMatchingTex(lim_f_g_c_neg, lim_f_g_c_pos),
                  TransformMatchingTex(lim_L_c_neg, lim_L_c_pos),
                  TransformMatchingTex(lim_final_c_neg, lim_final_c_pos))
        self.wait(2)





class E3(Scene):
    def construct(self):
        # Texto superior en amarillo
        enunciado = Tex("Calcule de existir el siguiente límite", color=YELLOW)
        enunciado.to_edge(UP)     
        # Límite original
        limite_original = MathTex(r"\lim_{x \to 1^+} \frac{\sin(x-1)}{\sqrt{x-1}}")
        limite_original.next_to(enunciado, DOWN, buff=1)
        # Añade el enunciado y el límite
        self.play(Write(enunciado), Write(limite_original))
        # Primera parte de las evaluaciones
        eval1 = MathTex(r"\lim_{x \to 1^+} \sin(x-1) = \lim_{x \to 1^+} \sqrt{x-1} = 0")
        eval1.next_to(limite_original, DOWN, buff=0.8)

        # Diferenciabilidad de las funciones
        diferenciabilidad = MathTex(r"f(x) = \sin(x-1) \quad \text{y} \quad g(x) = \sqrt{x-1} \quad \text{son diferenciables para} \quad x > 1")
        diferenciabilidad.next_to(eval1, DOWN, buff=0.8)

        # Definición del límite L
        limite_L = MathTex(r"L = \lim_{x \to 1^+} \frac{f'(x)}{g'(x)}")
        limite_L.next_to(diferenciabilidad, DOWN, buff=0.8)

        # Agregar "=L" al límite original
        igual_L = MathTex(r"= L")
        igual_L.next_to(limite_original, RIGHT, buff=0.2)
        self.play(Write(eval1))
        self.play(Write(diferenciabilidad))
        self.play(Write(limite_L))
        self.play(Write(igual_L))
        # Mantener la escena visible un momento
        self.wait(2)
        self.play(FadeOut(VGroup(eval1,diferenciabilidad,limite_L,igual_L)))
        # Escribir derivadas
        derivadas = MathTex(
            r"\frac{\frac{d}{dx} \sin(x-1)}{\frac{d}{dx} \sqrt{x-1}}",r"= \frac{\cos(x-1)}{\frac{1}{2\sqrt{x-1}}}"
        ).next_to(limite_original, DOWN)

        self.play(Write(derivadas))

        # Simplificar la fracción
        simplificado = MathTex(r"= 2 \sqrt{x-1} \cos(x-1)").move_to(derivadas[1]).align_to(derivadas[1],LEFT)

        self.play(Transform(derivadas[1], simplificado))

        # Aplicar el límite
        limite_aplicado = MathTex(
            r"\lim_{x \to 1^+} \frac{\frac{d}{dx} \sin(x-1)}{\frac{d}{dx} \sqrt{x-1}} = \lim_{x \to 1^+} 2 \sqrt{x-1} \cos(x-1)" 
            , r"= 2 \cdot 0 \cdot 1"
        ).next_to(limite_original, DOWN)
        resultado=limite_aplicado
        self.play(Transform(derivadas, limite_aplicado[0]))
        self.play(Write(limite_aplicado[1]))
        cero=MathTex("= 0").move_to(limite_aplicado[1]).align_to(limite_aplicado[1],LEFT)
        self.play(ReplacementTransform(limite_aplicado[1],cero))
        # Explicación de L'Hôpital
        explicacion = Tex("por el Teorema de L'Hôpital").next_to(resultado, DOWN)
        self.play(Write(explicacion))
        # Actualizar límite original
        limite_final = MathTex(r"\lim_{x \to 1^+} \frac{\sin(x-1)}{\sqrt{x-1}} = 0").move_to(limite_original)
        self.play(Transform(limite_original, limite_final))
        self.wait(2)


class E5(Scene):
    def construct(self):
        # Título de la escena
        titulo = Tex(r"Determine si la función $f:(0,\infty) \to \mathbb{R}$ es diferenciable en $x=1$", color=YELLOW).scale(0.7).to_edge(UP)
        self.play(Write(titulo))
        self.wait(1)
        
        # Definición de la función
        funcion = MathTex(
            r"f(x) = \begin{cases} \frac{x\ln x - x + 1}{\ln x} & x \neq 1 \\ 0 & x = 1 \end{cases}"
        ).next_to(titulo, DOWN, buff=0.5)
        
        # Cálculo de la derivada en x=1
        derivada = MathTex(
            r"\lim_{x \to 1} \frac{f(x) - f(1)}{x - 1} = ","\lim_{x \to 1} \frac{1}{(x-1)} \cdot \frac{x\ln x - x + 1}{\ln x}"
        ).next_to(funcion, DOWN, buff=1)
        
        # Mostrar texto inicial en pantalla.
        self.play(Write(funcion))
        self.wait(2)
        self.play(Write(derivada))
        self.wait(2)   
        # Tendencia a cero
        to_zero = MathTex(r" \to \frac{0}{0}").next_to(derivada, RIGHT, buff=0.4).align_to(derivada, ORIGIN)
        self.play(Write(to_zero))
        self.wait(1)
        self.play(FadeOut(VGroup(derivada, to_zero)))
        
        # Añadir la nueva expresión derivada
        nueva_expresion = MathTex(
            r"\frac{\frac{d}{dx} \left( x \ln x - x + 1 \right)}{\frac{d}{dx} \left( (x - 1)\ln x \right)} = ","\frac{x \cdot \frac{1}{x} + \ln x - 1}{(x - 1) \frac{1}{x} + \ln x}"
        ).next_to(funcion, DOWN, buff=1)
        simplificado_expresion=MathTex(r"\frac{x \cdot \frac{1}{x} + \ln x - 1}{(x - 1) \frac{1}{x} + \ln x}")
        # Mostrar la derivada de nuevo
        self.play(Write(nueva_expresion))
        self.wait(2)

        # Nueva indeterminación
        indeterminacion = MathTex(r" \to \frac{0}{0}").next_to(nueva_expresion, RIGHT, buff=0.4).align_to(nueva_expresion, ORIGIN)
        self.play(Write(indeterminacion))
        self.wait(1)
        self.play(FadeOut(indeterminacion),FadeOut(nueva_expresion))

        # Derivada de nuevo (segunda vez)
        nueva_derivada = MathTex(
            r"\frac{\frac{d}{dx} \left( x \ln x - x + 1 \right)}{\frac{d}{dx} \left( (x - 1)\ln x \right)} = \frac{1 + \ln x}{\frac{1}{x} + \ln x + 1}"
        ).next_to(funcion, DOWN, buff=1)
        self.play(Write(nueva_derivada))
        self.wait(2)
 
        # Evaluar en el límite x -> 1
        evaluacion_limite = MathTex(
            r"\lim_{x \to 1} \frac{1 + \ln x}{\frac{1}{x} + \ln x + 1} = \frac{1 + 0}{1 + 0 + 1} = \frac{1}{2}"
        ).next_to(nueva_derivada, DOWN, buff=1)
        self.play(Write(evaluacion_limite))
        self.wait(2)


class E6(Scene):
    def construct(self):
        # Paso 1: Mostrar la proposición con un rectángulo amarillo
        proposicion = Tex(
            r"\textbf{Proposición.} Si $f$ es una función definida en un intervalo que contiene a $c$ y $\lim_{x \to c} f'(x)$ existe, entonces $f$ es diferenciable en $c$ y además:"
,
            font_size=36
        ).to_edge(UP).set_tex_environment("flushleft").shift(DOWN)

        ecuacion = MathTex(r"f'(c) = \lim_{x \to c} f'(x)", font_size=36).next_to(proposicion, DOWN, buff=0.5)

        # Crear un rectángulo amarillo alrededor de la proposición y la ecuación
        grupo = VGroup(proposicion, ecuacion)
        cuadro = SurroundingRectangle(grupo, color=YELLOW)

        # Mostrar la proposición y la ecuación
        self.play(Write(proposicion))
        self.play(Write(ecuacion))
        self.play(Create(cuadro))
        self.wait(2)
        # Paso 2: Demostración - primer límite
        limite1 = MathTex(r"\lim_{x \to c} f(x) - f(c) = \lim_{x \to c} (x - c) = 0", font_size=36).next_to(ecuacion, DOWN,buff=0.5)
        self.play(Write(limite1))
        self.wait(2)

        # Borrar el primer límite
        self.play(FadeOut(limite1))

        # Paso 3: Mostrar el segundo límite
        limite2 = MathTex(r"\lim_{x \to c} \frac{f(x) - f(c)}{x - c}", font_size=36).next_to(ecuacion, DOWN,buff=0.7).shift(LEFT)
        self.play(Write(limite2))
        self.wait(2)

        # Paso 4: Mostrar la derivada en la parte derecha
        derivada = MathTex(r"= \lim_{x \to c} \frac{\frac{d}{dx} (f(x) - f(c))}{\frac{d}{dx} (x - c)}"
        , font_size=36).next_to(limite2, RIGHT)
        self.play(Write(derivada))
        self.wait(2)

        # Paso 5: Transformar la derivada
        limite3 = MathTex(r"= \lim_{x \to c} \frac{f'(x)}{1}", font_size=36).next_to(limite2, RIGHT)
        self.play(ReplacementTransform(derivada, limite3))
        self.wait(2)

        # Paso 6: Transformar a f'(x)
        limite4 = MathTex(r"= \lim_{x \to c} f'(x)", font_size=36).next_to(limite2, RIGHT)
        self.play(ReplacementTransform(limite3, limite4))
        self.wait(2)

