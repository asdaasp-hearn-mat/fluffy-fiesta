from manim import *

class E1(Scene):
    def construct(self):
        # Presentación inicial del problema
        problema = Tex(r"La ecuación de la demanda de una camisa es $2px + 65p - 4950 = 0$, donde $x$ es la demanda en cientos de camisas por semana y $p$ es el precio en dólares.", color=YELLOW, font_size=30).to_edge(UP)
        condiciones = Tex(r"Si esta semana el precio de una camisa es 30 dólares y el precio aumenta a razón de 0.20 dólares por semana, calcule la tasa de cambio de la demanda.", color=YELLOW, font_size=30).next_to(problema, DOWN).align_to(problema, LEFT)

        # Mostrar línea central "El precio de una camisa es 30 dólares"
        precio_linea = Tex(r"El precio de una camisa es 30 dólares", color=WHITE, font_size=36).move_to(UP*1)
        precio_ecuacion = MathTex(r"p=30", color=WHITE, font_size=48).move_to(precio_linea.get_center())

        # Mostrar la línea "El precio aumenta a razón de 0.20 dólares por semana"
        tasa_precio_linea = Tex(r"El precio aumenta a razón de 0.20 dólares por semana", color=WHITE, font_size=36).next_to(precio_linea, DOWN, buff=0.5)
        tasa_precio_ecuacion = MathTex(r"\frac{dp}{dt} = 0.20", color=WHITE, font_size=48).move_to(tasa_precio_linea.get_center())

        # Mostrar la línea "La tasa de cambio de la demanda"
        tasa_demanda_linea = Tex(r"La tasa de cambio de la demanda", color=WHITE, font_size=36).next_to(tasa_precio_linea, DOWN, buff=0.5)
        tasa_demanda_ecuacion = MathTex(r"  \frac{dx}{dt} ", color=YELLOW, font_size=48).move_to(tasa_demanda_linea.get_center())

        # Animaciones
        self.play(Write(problema))
        self.wait(2)
        self.play(Write(condiciones))
        self.wait(2)
        self.play(Write(precio_linea))
        self.wait()
        self.play(Transform(precio_linea, precio_ecuacion))
        self.wait()
        self.play(Write(tasa_precio_linea))
        self.wait()
        self.play(Transform(tasa_precio_linea, tasa_precio_ecuacion))
        self.wait()
        self.play(Write(tasa_demanda_linea))
        self.wait()
        self.play(Transform(tasa_demanda_linea, tasa_demanda_ecuacion))
        self.wait()



class E2(Scene):
    def construct(self):
        # Visualización de la ecuación inicial
        eq_inicial = MathTex(r"2px + 65p - 4950 = 0", color=WHITE).to_edge(UP)
        # Diferenciación con respecto al tiempo
        dif_t = MathTex(r"\frac{d}{dt}\left(2px + 65p - 4950\right) = 0", color=WHITE).next_to(eq_inicial, DOWN, buff=0.75).align_to(eq_inicial, LEFT)
        dif_eq = MathTex(r"2 \left( \frac{dp}{dt} \cdot x + p \cdot \frac{dx}{dt} \right) + 65 \frac{dp}{dt} = 0", color=WHITE).next_to(dif_t, DOWN, buff=0.75).align_to(dif_t, LEFT)
        
        # Sustitución y simplificación
        sustitucion = MathTex(r"2 \left( 0.20 \cdot x + 30 \cdot \frac{dx}{dt} \right) + 65 \cdot 0.20 = 0", color=WHITE).next_to(dif_eq, DOWN, buff=0.75).align_to(dif_eq, LEFT)
        simplificacion = MathTex(r"0.4x + 60 \cdot \frac{dx}{dt} + 13 = 0", color=WHITE).move_to(sustitucion.get_center())
        solucion = MathTex(r"60 \cdot \frac{dx}{dt} = -0.4x - 13", color=WHITE).move_to(simplificacion.get_center())
        dx_dt = MathTex(r"\frac{dx}{dt} = -\frac{0.4x + 13}{60}", color=WHITE).move_to(solucion.get_center())
        
        # Determinación de x cuando p=30
        eq_x = MathTex(r"60x + 1950 = 4950", color=WHITE).to_edge(LEFT).shift(UP)
        solucion_x = MathTex(r"x = 50", color=WHITE).next_to(eq_x, DOWN).align_to(eq_x, LEFT)
        
        # Sustitución de x en dx/dt
        sustitucion_x = MathTex(r"\frac{dx}{dt} = -\frac{0.4(50) + 13}{60}", color=WHITE).move_to(dx_dt.get_center())
        
        # Animaciones
        self.play(Write(eq_inicial))
        self.wait()
        self.play(Write(dif_t))
        self.wait()
        self.play(Write(dif_eq))
        self.wait()
        self.play(Write(sustitucion))
        self.wait()
        self.play(ReplacementTransform(sustitucion, simplificacion))
        self.wait()
        self.play(ReplacementTransform(simplificacion, solucion))
        self.wait()
        self.play(ReplacementTransform(solucion, dx_dt))
        self.wait()
        self.play(FadeOut(VGroup(eq_inicial, dif_t, dif_eq)))
        self.wait()
        self.play(Write(eq_x))
        self.wait()
        self.play(Write(solucion_x))
        self.wait()
        self.play(ReplacementTransform(solucion_x, dx_dt[0][8:10]))
        self.play(ReplacementTransform(dx_dt, sustitucion_x))
        self.play(Create(SurroundingRectangle(sustitucion_x[-1])))
        self.wait()

