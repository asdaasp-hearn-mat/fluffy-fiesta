from manim import *
from lines_and_points import *
import numpy as np
from scipy.special import legendre

class E1(Scene):
    def construct(self):
        # Pantalla en negro durante 2 segundos
        self.wait(2)
        
        # Crear el plano 
        plano = NumberPlane(

        ).scale(2)
        plano_graficado = NumberPlane(
               background_line_style={
                "stroke_color": GRAY,
                "stroke_width": 2,
                "stroke_opacity": 0.4
            }         
        ).scale(2).shift(LEFT)

        axes_labels = plano_graficado.get_axis_labels(x_label="x", y_label="y")
        
        self.play(Create(plano_graficado), Write(axes_labels))
        self.wait(2)
        
        # Definir la función constante f(x) = 1
        f_const = lambda x: 1
        
        # Definir los valores de a y b
        a = -3
        b = 3
        

        
        # Graficar los puntos en la frontera
        punto_a = crear_puntos_y_lineas(a, f_const, plano, color=RED, nombre_punto="a", mostrar_linea_horizontal=False)
        punto_b = crear_puntos_y_lineas(b, f_const, plano, color=RED, nombre_punto="b", mostrar_linea_horizontal=False)
        self.play(Create(punto_a), Create(punto_b))
        self.wait(2)
        # Graficar la recta f(x) = 1 entre a y b
        linea_const = plano.plot(lambda x: f_const(x), x_range=[a, b], color=BLUE)
        self.play(Create(linea_const))
     # Definir polinomios de Legendre ajustados al intervalo [-3, 3]
        def polinomio_legendre(n):
            Pn = legendre(n)
            return lambda x: Pn(x / 3)  
        
        legendre_pares = [
            (polinomio_legendre(2), GREEN),
            (polinomio_legendre(4), RED_D),
            (polinomio_legendre(6), PURPLE),
            (polinomio_legendre(0), BLUE_B)
            # Agregar más polinomios si es necesario
        ]
        
        for f, color in legendre_pares:
            linea_funcion = plano.plot(lambda x: f(x), x_range=[a, b], color=color)
            self.play(ReplacementTransform(linea_const,linea_funcion))
            self.wait(1)
            linea_const=linea_funcion
        
        # Agregar la función -cos(x)
        f_cos_neg = lambda x: -np.cos(x)
        linea_cos_neg = plano.plot(lambda x: f_cos_neg(x), x_range=[a, b], color=YELLOW)
        self.play(FadeIn(linea_cos_neg))
        
        # Valor de c
        c = 0
        f_c = f_cos_neg(c)
        
        # Graficar el punto (c, f(c)) en azul solo con la componente vertical
        punto_c = crear_puntos_y_lineas(c, f_cos_neg, plano, color=DARK_BLUE, nombre_punto="c", mostrar_linea_horizontal=False)
        self.play(Create(punto_c))
        
        # Calcular la pendiente de la recta tangente en (c, f(c))
        derivada_f = lambda x: np.sin(x)  # Derivada de -cos(x) es sin(x)
        pendiente_tangente = derivada_f(c)
        
        # Definir la ecuación de la recta tangente
        def recta_tangente(x):
            return pendiente_tangente * (x - c) + f_c
        
        # Graficar la recta tangente alrededor del punto (c, f(c)) limitada al dominio [a, b]
        recta_tangente_grafica = plano.plot(lambda x: recta_tangente(x), x_range=[a, b], color=DARK_BLUE)
        self.play(Create(recta_tangente_grafica))
        
        self.wait(2)

class E2(Scene):
    def construct(self):
        axes = NumberPlane(
                                    background_line_style={
                "stroke_color": GRAY,
                "stroke_width": 2,
                "stroke_opacity": 0.4}
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        p1 = Dot(axes.c2p(-2,0))
        p1_label = MathTex(r"a").next_to(p1, DOWN)
        p2 = Dot(axes.c2p(2,0))
        p2_label = MathTex(r"b").next_to(p2, DOWN)
        t= ValueTracker(0)
        s= ValueTracker(0)
        f = always_redraw (
                lambda: axes.plot(lambda x: -(x**2-4)*(1-t.get_value()), color = RED, x_range = [-2,2])
                )
        dibujo = VMobject()
        d = always_redraw(
            lambda: Dot().move_to(f.point_from_proportion(   s.get_value()  ))
        )
        texto1 = Tex(r"$f$ es continua en $[a,b]$ \\ y diferenciable en $(a,b)$", font_size = 28).to_edge(UL)
        texto2 = Tex(r"$f$ tiene un máximo y mínimo en $[a,b]$", font_size = 28).next_to(texto1, DOWN).align_to(texto1, LEFT)
        caso1 = Tex(r"Caso 1", font_size = 28).next_to(texto2, DOWN).align_to(texto1, LEFT)
        caso11 = Tex(r"$f$ tiene un máximo en $c \in (a,b)$", font_size = 28).next_to(caso1, DOWN).align_to(texto1, LEFT)
        fp = MathTex(r"f'(c)=0").next_to(caso11, DOWN).align_to(texto1, LEFT)
        c = Dot(ORIGIN, color = YELLOW)
        t1 = always_redraw(
                lambda: TangentLine(f, alpha =0.5, color = YELLOW).set_length(5)
                )
        g = axes.plot(lambda x: 0.5*(x**2-4)*(1-t.get_value()), color = RED, x_range = [-2,2])
        t2 = TangentLine(g, alpha =0.5, color = YELLOW).set_length(5)  
        c_label = MathTex(r"c", color = YELLOW).next_to(c, DOWN)
        caso2 = Tex(r"Caso 2", font_size = 28).next_to(fp, DOWN).align_to(texto1, LEFT)
        caso22 = Tex(r"$f$ tiene un mínimo en $c \in (a,b)$", font_size = 28).next_to(caso2, DOWN).align_to(texto1, LEFT)
        fp1 = fp.copy().next_to(caso22, DOWN).align_to(texto1, LEFT)
        caso3 = Tex(r"Caso 3", font_size = 28).next_to(fp1, DOWN).align_to(texto1, LEFT)
        caso33 = Tex(r"$f$ tiene un máximo y mínimo en $a$ o en $b$", font_size = 28).next_to(caso3, DOWN).align_to(texto1, LEFT)       
        l = Line(p1.get_center(), p2.get_center(), color = RED)
        fp2 = fp.copy().next_to(caso33, DOWN).align_to(texto1, LEFT)
        
        
        self.add(axes, axes_labels)
        self.wait(1.5)
        self.play(FadeIn(VGroup(p1, p1_label, p2, p2_label)))
        self.add(dibujo, d)
        self.wait()
        dibujo.add_updater(lambda x: x.become(f.get_subcurve(0, s.get_value()) ))
        self.play(s.animate.set_value(1), run_time = 4)
        self.add(f)
        self.remove(dibujo, d)
        self.wait(2)
        self.play(t.animate.set_value(1), run_time = 4)
        self.wait(2)
        self.play(t.animate.set_value(0.5))
        self.wait()
        self.play(Create(BackgroundRectangle(texto1)))
        self.play(Write(texto1))
        self.wait()
        self.play(Create(BackgroundRectangle(texto2)))
        self.play(Write(texto2))
        self.wait()
        self.play(Create(BackgroundRectangle(caso1)))
        self.play(Write(caso1))
        self.wait()
        self.play(Create(BackgroundRectangle(caso11)))
        self.play(Write(caso11))
        self.wait()
        self.play(FadeIn(VGroup(c, c_label)))
        self.wait()
        self.play(Create(t1))
        self.wait()
        self.play(Create(BackgroundRectangle(fp)))
        self.play(Write(fp))
        self.wait()
        self.play(Create(BackgroundRectangle(caso2)))
        self.play(Write(caso2))
        self.wait()
        self.play(Create(BackgroundRectangle(caso22)))
        self.play(Write(caso22))
        self.play(ReplacementTransform(f, g), ReplacementTransform(t1, t2))
        self.wait()
        self.play(Create(BackgroundRectangle(fp1)))
        self.play(Write(fp1))
        self.wait()
        self.play(Create(BackgroundRectangle(caso3)))
        self.play(Write(caso3))
        self.wait()
        self.play(Create(BackgroundRectangle(caso33)))
        self.play(Write(caso33))
        self.play(ReplacementTransform(g, l), FadeOut(t2))
        self.wait()
        self.play(Create(BackgroundRectangle(fp2)))
        self.play(Write(fp2))
        self.wait()
        self.play(*[Create(SurroundingRectangle(_)) for _ in VGroup(fp, fp1, fp2)])
        self.wait()
        


class E3(Scene):
    def construct(self):
        # Teorema de Rolle
        teo = Tex(r"\textbf{Teorema}. (\textit{Rolle}). Sea $f$ una función continua en $[a,b]$ y "
                  r"diferenciable en $(a,b)$ y $f(a)=f(b)$. Entonces existe $c \in (a,b)$ tal que $f'(c)=0$.", 
                  font_size=36, tex_environment="flushleft")
        rec1 = SurroundingRectangle(teo, color=YELLOW,buff=0.3)
        
        # Animación del teorema de Rolle
        self.play(Create(rec1))
        self.play(Write(teo), run_time=3)
        self.wait(3)
        teorema= VGroup(teo,rec1)
        # Mover el teorema hacia arriba
        self.play(teorema.animate.to_edge(UP).shift(DOWN))
        
        # Proposición 1
        prop1 = Tex(r"\textbf{Proposición}. Si $f'(x) \neq 0$ para todo $x \in (a,b)$, entonces $f(a) \neq f(b)$", 
                    font_size=36)
        rec2 = SurroundingRectangle(prop1, color=YELLOW)
        
        # Proposición 2
        prop2 = Tex(r"\textbf{Proposición}. Si $f'(x) \neq 0$ en un intervalo, $f$ es inyectiva en dicho intervalo.", 
                    font_size=36).next_to(prop1,DOWN,buff=1)
        rec3 = SurroundingRectangle(prop2, color=YELLOW)
        
        # Animaciones para las proposiciones
        self.play(Write(prop1), Create(rec2))
        self.wait(1)

        self.play(Write(prop2), Create(rec3))
        self.wait(2)


class E4(Scene):
    def construct(self):
        # Pantalla en negro durante 2 segundos
        self.wait(2)
        
        # Crear el plano con etiquetas en los ejes x e y
        plano = NumberPlane().scale(2)
        plano_graficado = NumberPlane(
            background_line_style={
                "stroke_color": GRAY,
                "stroke_width": 2,
                "stroke_opacity": 0.4
            }
        ).scale(2).shift(LEFT)

        axes_labels = plano_graficado.get_axis_labels(x_label="x", y_label="y")
        
        # Mostrar el plano en pantalla completa
        self.play(Create(plano_graficado), Write(axes_labels))
        self.wait(2)
        
        # Definir los valores de a y b
        a = -3
        b = 3
        # Graficar la recta y = (1/3)*x entre a y b
        f_linea = lambda x: (1/3) * x
        linea_const = plano.plot(lambda x: f_linea(x), x_range=[a, b], color=BLUE)        

        
        # Graficar los puntos en la frontera con etiquetas
        punto_a = crear_puntos_y_lineas(a, f_linea, plano, color=RED, nombre_punto="a", mostrar_linea_horizontal=False)
        punto_b = crear_puntos_y_lineas(b, f_linea, plano, color=RED, nombre_punto="b", mostrar_linea_horizontal=False)
        self.play(Create(punto_a), Create(punto_b))
        self.wait(2)
        self.play(Create(linea_const))
        self.wait(2)
        # Definir polinomios de Legendre ajustados al intervalo [-3, 3]
        def polinomio_legendre(n):
            Pn = legendre(n)
            return lambda x: Pn(x / 3)  # Ajustar el dominio para que sea en el intervalo [-3, 3]
        
        legendre_impares = [
            (polinomio_legendre(3), RED_D),
            (polinomio_legendre(5), PURPLE),
            (polinomio_legendre(7), BLUE_B),
            (polinomio_legendre(1), GREEN),
        ]
        
        # Transformar la recta en los polinomios de Legendre de grado impar
        for f, color in legendre_impares:
            linea_funcion = plano.plot(lambda x: f(x), x_range=[a, b], color=color)
            self.play(ReplacementTransform(linea_const, linea_funcion))
            self.wait(1)
            linea_const = linea_funcion
        
        # Transformar la última función en 2*ln(x+3)/ln(7) - 1
        f_log = lambda x: 2 * np.log(x + 4) / np.log(7) - 1
        linea_log = plano.plot(lambda x: f_log(x), x_range=[a, b], color=YELLOW)
        self.play(FadeIn(linea_log))
        self.wait(2)
        
        # Valor de c
        c = 6 / np.log(7) - 4
        f_c = f_log(c)
        
        # Graficar el punto (c, f(c)) en azul solo con la componente vertical
        punto_c = crear_puntos_y_lineas(c, f_log, plano, color=DARK_BLUE, nombre_punto="c", mostrar_linea_horizontal=False)
        self.play(Create(punto_c))
        
        # Calcular la pendiente de la recta tangente en (c, f(c))
        derivada_f = lambda x: 2 / (np.log(7) * (x + 4))  # Derivada de 2*ln(x+3)/ln(7) - 1
        pendiente_tangente = derivada_f(c)
        
        # Definir la ecuación de la recta tangente
        def recta_tangente(x):
            return pendiente_tangente * (x - c) + f_c
        
        # Graficar la recta tangente alrededor del punto (c, f(c)) limitada al dominio [a, b]
        recta_tangente_grafica = plano.plot(lambda x: recta_tangente(x), x_range=[a, b], color=DARK_BLUE)
        self.play(Create(recta_tangente_grafica))
        self.wait(2)



class E5(Scene):
    def construct(self):    
        axes = Axes(x_range=(-1,10,1),
                    y_range=(-1,20,1),
                    axis_config={"include_numbers": False, "include_tip": False}).shift(0.5*LEFT)
        axes_labels = axes.get_axis_labels()

        p1 = axes.c2p(1,5)
        p2 = axes.c2p(8, 15)
        

        f=lambda x: (-5/168)*(-64+x*(-103+(-2+x)*x))
        g=lambda x:5+10*(x-1)/7
        bezier = axes.plot(f,x_range=[1,8],color=BLUE)
        #tange = VGroup(*[TangentLine(bezier, 0.1+i*0.1, color = YELLOW).set_length(8) for i in range(9)]) #Esto fue para muestrear al ojo
        tval = TangentLine(bezier, 0.59, color = YELLOW).set_length(12)
        line = axes.plot(g,x_range=[1,8],color=RED)
        p1d=crear_puntos_y_lineas(x_val=1,f=f,plane=axes,color=WHITE,nombre_funcion="f",nombre_punto="a")
        p2d=crear_puntos_y_lineas(x_val=8,f=f,plane=axes,color=WHITE,nombre_funcion="f",nombre_punto="b")
        #p1d = Dot(p1)
        #l1 = axes.get_lines_to_point(p1)
        #l2 = axes.get_lines_to_point(p2)
        #p1d_label = MathTex(r"a").next_to(axes.c2p(1, 0), DOWN).shift(0.25*RIGHT)
        #p2d = Dot(p2)
        #p2d_label = MathTex(r"b").next_to(p2d, DOWN).next_to(axes.c2p(1, 0), DOWN).shift(0.25*RIGHT)
        f_label = MathTex(r"f(x)", color = BLUE, font_size=24).next_to(bezier, UP).shift(0.5*UP)
        l_eq = MathTex(r"g(x) = \frac{f(b)-f(a)}{b-a}(x-a)+f(a)", color = RED, font_size = 24).next_to(line, DOWN).shift(1*UP)
        distances = VGroup(*[Line(axes.c2p(i+1,g(i+1)),axes.c2p(i+1,f(i+1)) , color = ORANGE) for i in range(8)])
        d_eq = MathTex(r"d(x)= f(x)-g(x)", font_size = 24, color = ORANGE).to_edge(UR)
        d_a = MathTex(r"d(a)= f(a)-g(a)", r"=0", font_size = 24).next_to(d_eq, DOWN).align_to(d_eq, LEFT)
        d_b = MathTex(r"d(b)= f(b)-g(b)", r"=0", font_size = 24).next_to(d_a, DOWN).align_to(d_eq, LEFT) 
        rolle = Tex(r"Del teorema de Rolle", font_size = 24, color = YELLOW).next_to(d_b, DOWN)
        rolle2 = Tex(r"existe $c \in (a,b):$", font_size = 24).next_to(rolle, DOWN)
        rolle3 = MathTex(r"d'(c)=0", font_size = 24).next_to(rolle2, DOWN).align_to(d_eq, LEFT)
        sectan = MathTex(r"f'(c)", r"-", r"g'(c)", r"=", r"0", font_size = 24).next_to(rolle3, DOWN).align_to(d_eq, LEFT)
        sectan1 = MathTex(r"f'(c)", r"=", r"g'(c)", font_size = 24).next_to(rolle3, DOWN).align_to(d_eq, LEFT)
        sPrima = MathTex(r"g'(x) = \frac{f(b)-f(a)}{b-a}", font_size = 24, color = RED).next_to(l_eq, DOWN).align_to(l_eq, LEFT)
        sectan2 = MathTex(r"f'(c)", r"=", r"\frac{f(b)-f(a)}{b-a}", font_size = 24).next_to(sectan1, DOWN).align_to(d_eq, LEFT)
        ces = axes.get_lines_to_point(bezier.point_from_proportion(0.59), color = YELLOW)
        c = MathTex(r"c", color = YELLOW).move_to((bezier.point_from_proportion(0.59)[0],axes.c2p(0,0)[1],0)).shift(0.4*DOWN)
              
        self.add(axes, axes_labels)
        self.wait()
        self.play(Create(bezier),Write(f_label))    
        self.wait()
        self.play(FadeIn(p1d, p2d)) 
        self.wait(2)    

        self.play(Create(line), Write(l_eq)) 
        self.wait()    
        #self.play(AnimationGroup([Create(t) for t in tange], lag_ratio =1   ))
        #self.play(Create(tval))
        self.wait(2)
        # Crear una copia de la recta secante extendida a todo el plano
        recta_secante_extendida = axes.plot(lambda x:g(x),x_range=[-10,20],color=YELLOW)

        # Añadir la recta extendida a la escena
        self.add(recta_secante_extendida)
        self.play(MoveAlongPath(recta_secante_extendida,Line(axes.c2p(5,g(5)),axes.c2p(6,g(5)+3))),
                  rate_func=there_and_back,
                  run_time=4)
        # Eliminar la recta después de que regrese a su posición original
        self.play(FadeOut(recta_secante_extendida))
        self.wait(1)
        #Resto de la animación, que pereza comentar esto NOem
        self.play(AnimationGroup([Create(l) for l in distances], lag_ratio = 0.5))
        self.play(Uncreate(distances))
        self.wait(2)
        self.play(Write(d_eq))
        self.wait()
        self.play(Write(d_a[0]))
        self.wait()
        self.play(Write(d_a[1]))
        self.wait()
        self.play(Write(d_b[0]))
        self.wait()
        self.play(Write(d_b[1]))
        self.wait()
        self.play(AnimationGroup([Write(t) for t in VGroup(rolle, rolle2, rolle3)], lag_ratio = 1))
        self.wait()
        self.play(Write(sectan))
        self.wait()
        self.play(TransformMatchingTex(sectan, sectan1))
        self.wait()
        self.play(Write(sPrima))
        self.wait()
        self.play(Write(sectan2))
        self.wait()
        self.play(Create(SurroundingRectangle(sectan2)))
        self.wait()
        self.play(Create(VGroup(ces, c)))
        self.play(Create(tval))
        self.wait(2)


class E6(Scene):
    def construct(self):
        # Definir el texto del teorema
        teorema_texto = Tex(
            r"\textbf{Teorema} (Valor Medio de Lagrange) Sea $f:[a,b] \to \mathbb{R}$ una función \\ continua  y derivable en $(a,b)$. Entonces existe un $c \in (a,b)$ tal que:",
            r"$$f'(c) = \frac{f(b) - f(a)}{b - a}$$", tex_environment="flushleft",
            font_size=40
        ).scale(1)

        # Crear un rectángulo de fondo amarillo
        fondo_rectangulo = SurroundingRectangle(teorema_texto, color=YELLOW, buff=0.4)

        # Posicionar el texto y el rectángulo en el centro de la pantalla
        teorema_texto.move_to(ORIGIN)
        fondo_rectangulo.move_to(ORIGIN)

        # Mostrar el fondo amarillo y el texto
        self.play(Create(fondo_rectangulo), Write(teorema_texto))
        self.wait(5)

class E7(Scene):
    def construct(self):
        # Pantalla en negro durante 2 segundos
        self.wait(2)

        # Crear el plano base y el plano graficado
        plano = NumberPlane()
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
        self.wait(2)
        # Marcar los puntos inicial y final
        espiral_function = lambda t: plano.c2p(-0.5 * t * np.cos(t), 0.5 * t * np.sin(t))
        a = 0
        b = 2 * np.pi + np.pi / 4

        espiral = ParametricFunction(
            espiral_function,
            t_range=[a, b],
            color=BLUE
        )
        punto_inicial = Dot(espiral_function(a), color=RED)
        punto_final = Dot(espiral_function(b), color=RED)
        self.play(Create(punto_inicial), Create(punto_final))
        self.wait(1)
        # Crear el texto en el lado izquierdo de la pantalla
        texto_derecha = MathTex(
            r"x = g(t)", r"y = f(t)", r"a \leq t \leq b",
            font_size=40
        ).arrange(DOWN).to_corner(UR).shift(LEFT)
        
        corchetes = Brace(texto_derecha, direction=LEFT)
        
        # Mostrar el texto con corchetes
        self.play(Create(corchetes), Write(texto_derecha))
        self.wait(2)

        # Definir la espiral de Arquímedes en coordenadas paramétricas




        # Crear la espiral
        self.play(Create(espiral))
        self.wait(1)

        # Agregar el texto de la fracción en amarillo después de la secante
        fraccion_secante = MathTex(
            r"\frac{f(b) - f(a)}{g(b) - g(a)}", 
            font_size=40, color=YELLOW
        ).next_to(texto_derecha, DOWN, aligned_edge=LEFT)

        # Definir la recta secante entre p(a) y p(b)
        recta_function = lambda t: espiral_function(a) + t * (espiral_function(b) - espiral_function(a))

        recta_secante = ParametricFunction(
            recta_function,
            t_range=[0, 1],
            color=YELLOW
        )
        
        # Graficar la recta secante y mostrar el texto
        self.play(Create(recta_secante))
        self.play(Write(fraccion_secante))
        self.wait(2)
        # Crear una copia de la recta secante extendida a todo el plano
        recta_secante_extendida=ParametricFunction(
            recta_function,
            t_range=[-10, 10],
            color=YELLOW
        ) # Extendiendo la recta

        # Crear un ValueTracker para mover la recta hacia abajo y luego hacia arriba
        desplazamiento_tracker = ValueTracker(0)

        # Función de movimiento de la recta
        recta_secante_extendida.add_updater(
            lambda m: m.set_y(desplazamiento_tracker.get_value())
        )

        # Añadir la recta extendida a la escena
        self.add(recta_secante_extendida)

        # Mover la recta hacia abajo y luego hacia arriba usando there_and_back
        self.play(
            desplazamiento_tracker.animate.set_value(-4),
            rate_func=there_and_back,   
            run_time=4
        )
        self.play(
            desplazamiento_tracker.animate.set_value(1.8),
            rate_func=there_and_back,
            run_time=4
        )
        # Eliminar la recta después de que regrese a su posición original
        self.play(FadeOut(recta_secante_extendida))
        self.wait(1)
        # Valores de t donde las pendientes de la tangente son iguales a la secante
        c_vals = [5.67228968, 2.70973013, 0.40262817]

        # Funciones para calcular la derivada de la espiral (r'(t))
        def derivada_x(t):
            return -0.5 * (np.cos(t) - t * np.sin(t))

        def derivada_y(t):
            return 0.5 * (np.sin(t) + t * np.cos(t))

        def vector_tangente(t):
            dx_dt = derivada_x(t)
            dy_dt = derivada_y(t)
            return np.array([dx_dt, dy_dt, 0])

        # Crear y graficar las rectas tangentes en cada c_i
        for i, c_i in enumerate(c_vals):
            r_c_i = espiral_function(c_i)
            r_prime_c_i = vector_tangente(c_i)

            tangente_function = lambda t: r_c_i + t * r_prime_c_i

            tangente = ParametricFunction(
                tangente_function,
                t_range=[-1, 1],
                color=GREEN
            )

            # Mostrar la tangente y etiquetar el punto con c_i
            etiqueta_c_i = MathTex(f"c_{i+1}", font_size=30).next_to(Dot(r_c_i), UP)
            if i==2:
                etiqueta_c_i.shift(DOWN)
                
            self.play(Create(Dot(r_c_i, color=GREEN)), Write(etiqueta_c_i))
            self.play(Create(tangente))
            self.wait(1)

        # Cambiar la fracción para mostrar el teorema de Cauchy
        teorema_cauchy = MathTex(
            r"\frac{f(b) - f(a)}{g(b) - g(a)} = \frac{f'(c)}{g'(c)}",
            font_size=40, color=YELLOW
        ).move_to(fraccion_secante)
        self.play(Transform(fraccion_secante, teorema_cauchy))
        self.wait(2)


class E8(Scene):
    def construct(self):
        # Definir el texto del teorema
        teorema_texto = Tex(
            r"\textbf{Teorema} (Valor Medio de Cauchy). Sean $f:[a,b] \to \mathbb{R}$ y $g:[a,b] \to \mathbb{R}$ funciones continuas y derivables en $(a,b)$. ",
            r"Con $g'(x) \neq 0$ para todo $x \in (a,b)$. Existe entonces un $c \in (a,b)$ tal que:",
            r"$$\frac{f'(c)}{g'(c)} = \frac{f(b) - f(a)}{g(b) - g(a)}$$",
            font_size=40, tex_environment="flushleft"
        ).scale(1)  # Ajustar el tamaño del texto si es necesario

        # Crear un rectángulo de fondo amarillo
        fondo_rectangulo = SurroundingRectangle(teorema_texto, color=YELLOW, buff=0.1)

        # Posicionar el texto y el rectángulo en el centro de la pantalla
        teorema_texto.move_to(ORIGIN)
        fondo_rectangulo.move_to(ORIGIN)

        # Mostrar el fondo amarillo y el texto
        self.play(Create(fondo_rectangulo), Write(teorema_texto))
        self.wait(5)
