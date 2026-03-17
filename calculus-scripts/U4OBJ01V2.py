from manim import *
from lines_and_points import *
#comentario random
class E1(Scene):
    def construct(self):
        # Crear el texto y rodearlo con un cuadro amarillo
        texto = Tex(r"Si $f$ es una función diferenciable en $(a,b)$, entonces $f$ es continua en $(a,b)$",font_size=36)
        #cuadro = SurroundingRectangle(texto, color=YELLOW)
        
        # Posicionar el cuadro en el centro y luego reducir su tamaño y moverlo a la esquina superior izquierda
        self.play(Write(texto))
        self.wait(2)
        self.play(texto.animate.scale(0.5).to_corner(UL))
        self.wait(1)
        
        # Crear el plano cartesiano en el centro
        plano_1 = NumberPlane(x_range=[-2.5, 2.5, 1], y_range=[-2.5, 2.5, 1],             background_line_style={
                "stroke_color": GRAY,
                "stroke_width": 2,
                "stroke_opacity": 0.4
            })
        axes1=plano_1.get_axis_labels(x_label="x", y_label="y")
        # Graficar la función f(x) = abs(x)*x/2 en el centro
        grafica_f = plano_1.plot(lambda x: abs(x)*x/2, color=BLUE, x_range=[-2.45, 2.45])
        etiqueta_f = MathTex(r"f(x) = \frac{|x|x}{2}",color=BLUE).next_to(grafica_f,DOWN,buff=0.01).shift(2*UP)
        
        # Mostrar el plano y la función en el centro
        self.play(Create(plano_1), Create(grafica_f), Write(etiqueta_f),Write(axes1))
        self.wait(2)
        grupo1=VGroup(grafica_f,etiqueta_f,plano_1,axes1)
        # Mover la gráfica f(x) = abs(x)*x/2 hacia la izquierda
        self.play(grupo1.animate.to_edge(LEFT))
        self.wait(1)
        
        # Graficar la función f(x) = |x| en la parte derecha del plano
        plano_2 = NumberPlane(x_range=[-2.5, 2.5, 1], y_range=[-2.5, 2.5, 1],             background_line_style={
                "stroke_color": GRAY,
                "stroke_width": 2,
                "stroke_opacity": 0.4
            }).to_edge(RIGHT)
        axes2=plano_2.get_axis_labels(x_label="x", y_label="y")
        grafica_abs = plano_2.plot(lambda x: abs(x), color=RED)
        etiqueta_abs = MathTex(r"f'(x) = |x|",color=RED).next_to(grafica_abs,DOWN,buff=0.01).shift(2*DOWN)
        # Mostrar la función f(x) = |x| en el lado derecho
        self.play(Create(plano_2),Write(axes2),Create(grafica_abs), Write(etiqueta_abs))
        self.wait(2)


class E2(Scene):
    def construct(self):
        # Crear el primer plano para la función f(x) = cuberoot(x)
        plano_f = NumberPlane(            background_line_style={
                "stroke_color": GRAY,
                "stroke_width": 2,
                "stroke_opacity": 0.4
            },
            x_range=[-3.5, 3.5, 1],
            y_range=[-3.5, 3.5, 1],
            axis_config={"include_numbers": False}, 

        ).scale(0.7)
        axis1=plano_f.get_axis_labels(x_label="x", y_label="y")
        # Gráfica de la función f(x) = cuberoot(x)
        grafica_f = plano_f.plot(lambda x: np.cbrt(x), color=BLUE,x_range=[-3.5, 3.5,0.01])
        
        # Etiqueta de f(x)
        etiqueta_f = MathTex(r"f(x) = \sqrt[3]{x}", color=BLUE).next_to(plano_f, UP).shift(0.2*UP)

        # Agrupar plano, gráfica y etiqueta
        group_f = VGroup(plano_f, grafica_f, etiqueta_f,axis1)

        # Crear el segundo plano para la derivada f'(x)
        plano_derivada = NumberPlane(
            background_line_style={
                "stroke_color": GRAY,
                "stroke_width": 2,
                "stroke_opacity": 0.4
            },
            x_range=[-3.5, 3.5, 1],
            y_range=[-3.5, 3.5, 1],
            axis_config={"include_numbers": False}
        ).scale(0.7).to_edge(RIGHT)
        axis2=plano_derivada.get_axis_labels(x_label="x", y_label="y")
        # Gráfica de la derivada f'(x) = 1/(3 * cuberoot(x^2)) en dos partes
        grafica_derivada_izq = plano_derivada.plot(
            lambda x: 1/(3 * np.cbrt(x**2)), x_range=[-3.5, -0.03,0.01], color=RED
        )
        grafica_derivada_der = plano_derivada.plot(
            lambda x: 1/(3 * np.cbrt(x**2)), x_range=[0.03, 3.5,0.01], color=RED
        )
        # Etiqueta de la derivada f'(x)
        etiqueta_derivada = MathTex(r"f'(x) = \frac{1}{3 \sqrt[3]{x^2}}", color=RED).next_to(plano_derivada, UP).shift(0.3*RIGHT)
        # Animaciones
        self.play(Create(plano_f), Create(grafica_f), Write(etiqueta_f),Write(axis1), run_time=2)
        self.play(group_f.animate.to_edge(LEFT))
        # Crear lentamente la derivada en dos partes
        self.play(Create(plano_derivada),Write(etiqueta_derivada),Write(axis2))
        self.play(Create(grafica_derivada_izq),run_time=2)
        self.play(Create(grafica_derivada_der), run_time=2)
        self.wait(2)



class E3(Scene):
    def construct(self):
        def f(x):
            if x != 0:
                return x**2 * np.sin(1/x)
            else:
                return 0

        # Crear el plano para f(x)
        plano_f = NumberPlane(
            background_line_style={
                "stroke_color": GRAY,
                "stroke_width": 2,
                "stroke_opacity": 0.4
            },
            x_range=[-3.5, 3.5, 1],
            y_range=[-3.5, 3.5, 1],
            axis_config={"include_numbers": False},
        ).scale(0.7)
        axes1=plano_f.get_axis_labels(x_label="x", y_label="y")
        
        # Gráfica de la función f(x)
        grafica_f = plano_f.plot(f, color=BLUE, x_range=[-3.5, 3.5, 0.01])

        # Etiqueta de f(x)
        etiqueta_f = MathTex(r"f(x) = x^2 \cdot \sin\left(\frac{1}{x}\right)", color=BLUE).next_to(plano_f, UP)
        centro_1=Dot(plano_f.c2p(0,0),color=YELLOW)
        # Agrupar plano, gráfica y etiqueta
        group_f = VGroup(plano_f, grafica_f, etiqueta_f,axes1,centro_1)

        self.play(Create(plano_f), Create(grafica_f),Create(centro_1), Write(etiqueta_f),Write(axes1), run_time=2)
        self.play(group_f.animate.to_edge(LEFT))

        # Crear el plano para la derivada
        plano_derivada = NumberPlane(
            background_line_style={
                "stroke_color": GRAY,
                "stroke_width": 2,
                "stroke_opacity": 0.4
            },
            x_range=[-3.5, 3.5, 1],
            y_range=[-3.5, 3.5, 1],
            axis_config={"include_numbers": False}
        ).scale(0.7).to_edge(RIGHT)
        axes2=plano_derivada.get_axis_labels(x_label="x", y_label="y")
        # Gráfica de la derivada f'(x)
        def derivada_f(x):
            if x != 0:
                return -np.cos(1/x) + 2 * x * np.sin(1/x)
            else:
                return 0

        grafica_derivada = plano_derivada.plot(
            derivada_f, x_range=[-3.5, 3.5, 0.01], color=RED
        )

        # Etiqueta de la derivada f'(x)
        etiqueta_derivada = MathTex(
            r"f'(x) = -\cos\left(\frac{1}{x}\right) + 2x \cdot \sin\left(\frac{1}{x}\right)",
            color=RED
        ).next_to(plano_derivada, UP).shift(0.50 * LEFT).scale(0.9)
        centro_2=Dot(plano_derivada.c2p(0,0),color=YELLOW)
        self.play(Create(plano_derivada), Write(etiqueta_derivada),Write(axes2),Create(centro_2))
        self.play(Create(grafica_derivada), run_time=3,rate_func=double_smooth)

        # Mostrar que el límite no existe
        no_existe = MathTex(
            r"\lim_{x \to 0} f'(x) \text{ no existe.}", color=YELLOW
        ).next_to(plano_derivada, DOWN, buff=0.1).scale(0.9)

        self.play(Write(no_existe))
        self.wait(2)

class E4(Scene):
    def construct(self):
        # Texto que se va a mostrar
        texto = Tex(
            r"\textbf{Teorema.} \textit{Valor intermedio para derivadas (Darboux)}.  Sea $f$ una función definida en un intervalo $I$.  Si $a,b \in I$ tales que ",
            r"$f'(a)<z<f'(b)$, entonces existe un $c \in (a,b)$ tal que:",
            tex_environment="flushleft",font_size = 36
        )      
        # Ecuación debajo del texto
        ecuacion = MathTex(
            r"f'(c) = z",font_size = 36
        ).next_to(texto, DOWN,buff=0.5)

        # Agrupar texto y ecuación
        group = VGroup(texto, ecuacion)
        
        # Rectángulo amarillo que rodea el grupo
        rectangulo = SurroundingRectangle(group, color=YELLOW, buff=0.2)
        
        # Animar la creación del texto y el rectángulo
        self.play(Write(texto))
        self.play(Write(ecuacion))
        self.play(Create(rectangulo))
        self.wait(2)

class E5(Scene):
    def construct(self):
        # Definir el plano
        plano = NumberPlane(
            background_line_style={
                "stroke_color": GRAY,
                "stroke_width": 2,
                "stroke_opacity": 0.4
            },
            axis_config={"include_numbers": False}
        )
        axes_labels = plano.get_axis_labels(x_label="x", y_label="y")
        # Definir la función sgn(x) (sqrt(abs(x)) + 1)
        def f(x):
            return np.sign(x) * (np.sqrt(abs(x)) + 1)
        
        # Graficar la función en morado
        grafica_f_izquierda = plano.plot(f, color=BLUE,x_range=[-7,-0.01])
        grafica_f_derecha = plano.plot(f, color=BLUE,x_range=[0.01,7])
        # Colocar un punto morado en el origen
        punto_origen = Dot(point=plano.c2p(0, 0), color=BLUE)
        # Colocar puntos en (0,-1) y (0,1) con borde morado y relleno negro
        punto_neg1 = Dot(point=plano.c2p(0, -1), color=BLACK, stroke_color=BLUE, stroke_width=3)
        punto_pos1 = Dot(point=plano.c2p(0, 1), color=BLACK, stroke_color=BLUE, stroke_width=3)

        # Etiqueta de f' encima de la gráfica
        #etiqueta_f_derivada = MathTex(r"f'", color=BLUE).next_to(grafica_f_izquierda, UP, buff=0.5)

        # Texto "por ejemplo," en la esquina con fondo negro
        texto_por_ejemplo = Tex(r"¿La siguiente gráfica corresponde a \\ la derivada de alguna función?", font_size=36, color=WHITE)
        rectangulo_ejemplo = BackgroundRectangle(texto_por_ejemplo, color=BLACK, fill_opacity=0.5)
        grupo_ejemplo = VGroup(rectangulo_ejemplo, texto_por_ejemplo).to_corner(UL, buff=0.5)
        # Texto "ninguna función podría tener así su derivada." en la otra esquina

        texto_ninguna_funcion = Tex(r"Ninguna función podría  tener así \\ la gráfica de su derivada.", font_size=36, color=WHITE)
        rectangulo_ninguna = BackgroundRectangle(texto_ninguna_funcion, color=BLACK, fill_opacity=0.5)
        grupo_ninguna = VGroup(rectangulo_ninguna, texto_ninguna_funcion).to_corner(DR, buff=0.5).shift(UP)

        # Animaciones
        self.play(Create(plano),Write(axes_labels))
        self.play(Create(grafica_f_izquierda),FadeIn(punto_neg1))
        self.play(Create(grafica_f_derecha),FadeIn(punto_pos1))
        self.play(FadeIn(punto_origen))
        #self.play(Write(etiqueta_f_derivada))
        self.play(FadeIn(grupo_ejemplo))
        self.wait(2)
        recta_secante_extendida=plano.plot(
            lambda x:0*x-1,
            x_range=[-10, 10],
            color=YELLOW
        ) # Extendiendo la recta


        self.add(recta_secante_extendida)

        # Mover la recta hacia abajo y luego hacia arriba usando there_and_back
        self.play(MoveAlongPath(recta_secante_extendida,Line(plano.c2p(0,-1),plano.c2p(0,1))),
                  rate_func=there_and_back,
                  run_time=4)
        self.play(FadeIn(grupo_ninguna))

class E6(Scene):
    def construct(self):
        # Enunciado en la parte superior
        enunciado = Tex(r"$f'(c)$ no puede existir si $$\lim_{x \to c} f'(x) = \infty$$", font_size=36).to_edge(UP)
        
        # Plano con ejes visibles
        plano = NumberPlane(
            background_line_style={
                "stroke_color": GRAY,
                "stroke_width": 2,
                "stroke_opacity": 0.4
            },
        )
        
        axes_labels = plano.get_axis_labels(x_label="x", y_label="y")

        # Definir la función
        f = lambda x: 1 / (x - 1)**2

        # Crear un ValueTracker para t
        t_tracker = ValueTracker(7)
        # Funciones para actualizar las gráficas
        def update_grafica_izquierda(grafica):
            a = 1 - t_tracker.get_value()  # a = 1 - t
            grafica.become(plano.plot(f, x_range=[a, 0.99, 0.01], color=PURPLE_E))
        
        def update_grafica_derecha(grafica):
            b = 1 + t_tracker.get_value()  # b = 1 + t
            grafica.become(plano.plot(f, x_range=[1.01, b, 0.01], color=PURPLE_E))

        # Crear gráficas iniciales
        grafica_f_izquierda = plano.plot(f, x_range=[-8, 0.99, 0.01], color=PURPLE_E)
        grafica_f_derecha = plano.plot(f, x_range=[1.01, 8, 0.01], color=PURPLE_E)

        # Puntos que representan el infinito en x = 1
        punto_infinito = Dot(plano.c2p(1, 2), color=PURPLE_E)

        # Funciones para actualizar los puntos (a, f(a)) y (b, f(b))
        def update_punto_a(puntos):
            a = 1 - t_tracker.get_value()
            puntos.become(crear_puntos_y_lineas(a, f, plano, color=YELLOW, nombre_punto="a",mostrar_linea_horizontal=False))

        def update_punto_b(puntos):
            b = 1 + t_tracker.get_value()
            puntos.become(crear_puntos_y_lineas(b, f, plano, color=YELLOW, nombre_punto="b",mostrar_linea_horizontal=False))

        # Crear puntos iniciales (a, f(a)) y (b, f(b))
        punto_a = crear_puntos_y_lineas(-8, f, plano, color=YELLOW, nombre_punto="a",mostrar_linea_horizontal=False)
        punto_b = crear_puntos_y_lineas(8, f, plano, color=YELLOW, nombre_punto="b",mostrar_linea_horizontal=False)

        # Añadir las gráficas y los elementos al escenario
        self.play(Write(enunciado))
        self.play(enunciado.animate.to_corner(UL))
        self.play(Create(plano), Write(axes_labels))
        self.play(Create(grafica_f_izquierda), Create(grafica_f_derecha), FadeIn(punto_infinito))
        self.wait()
        self.play(FadeIn(punto_a), FadeIn(punto_b))

        # Conectar los actualizadores a las gráficas y los puntos
        grafica_f_izquierda.add_updater(update_grafica_izquierda)
        grafica_f_derecha.add_updater(update_grafica_derecha)
        punto_a.add_updater(update_punto_a)
        punto_b.add_updater(update_punto_b)

        # Animar el valor de t de 1 a 0.6 (haciendo que a y b se acerquen a 1)
        self.play(t_tracker.animate.set_value(0.6), run_time=4,rate_func=exponential_decay)
        self.wait(2)
        # Remover actualizadores después de la animación
        grafica_f_izquierda.remove_updater(update_grafica_izquierda)
        grafica_f_derecha.remove_updater(update_grafica_derecha)
        punto_a.remove_updater(update_punto_a)
        punto_b.remove_updater(update_punto_b)

        # Linea recta que se va moviendo 
        recta=plano.plot(
            lambda x:0*x+2,
            x_range=[-10, 10],
            color=RED
        )
        self.play(FadeIn(recta))
        self.play(MoveAlongPath(recta,Line(plano.c2p(0,2),plano.c2p(0,2.5))),
                  rate_func=there_and_back,
                  run_time=4)  
        self.play(FadeOut(recta))      

class E7(Scene):
    def construct(self):
        # Texto de la definición con parte en amarillo
        definicion_c1 = Tex(
            r"\textbf{Definición}. Una función $f$ es ",
            r"continuamente diferenciable ",
            r"en $(a,b)$ si ",
            r"$f':(a,b)\to\mathbb{R}$ ",
            r"es continua.",
            font_size=36
        )
        
        # Resaltar en amarillo las partes solicitadas
        definicion_c1[1].set_color(YELLOW)  # "continuamente diferenciable"
        definicion_c1[3].set_color(YELLOW)  # "f':(a,b)->R"

        # Posicionar el texto en el centro
        definicion_c1.move_to(ORIGIN)

        # Rectángulo amarillo alrededor del texto
        rectangulo = SurroundingRectangle(definicion_c1, color=YELLOW, buff=0.2)

        # Texto adicional debajo del rectángulo
        texto_adicional = Tex(
            r"También se dice que $f$ es $C^1$ en $(a,b)$ o $f \in C^1(a,b)$.",
            font_size=36
        ).next_to(rectangulo, DOWN, buff=0.3)

        # Animaciones
        self.play(Write(definicion_c1))
        self.play(Create(rectangulo))
        self.wait(1)
        self.play(Write(texto_adicional))
        self.wait(2)

from manim import *

class E8(Scene):
    def construct(self):
        # Enunciado inicial
        enunciado = Tex(r"Determine $f'(x)$ para la función definida por:",color=YELLOW).to_edge(UP)
        self.play(Write(enunciado))
        funcion = MathTex(r"f(x) = \sqrt{x}-\sqrt[3]{x}").next_to(enunciado, DOWN, buff=0.3)
        self.play(Write(funcion))

        # Texto para x > 0
        x_greater = Tex(r"Cuando $x > 0$:",color=YELLOW).to_edge(LEFT).shift(UP)
        self.play(Write(x_greater))
        # Derivada inicial
        derivada_inicial = MathTex(r"f'(x) = \frac{1}{2\sqrt{x}} - \frac{1}{3\sqrt[3]{x^2}}").next_to(x_greater, DOWN, buff=0.5).align_to(x_greater,LEFT)
        x_to =Tex(r"Cuando $x \to 0^+$:",color=YELLOW).to_edge(RIGHT).shift(UP)
        derivada_inicial_2=derivada_inicial.copy().next_to(x_to,DOWN, buff=0.5).align_to(x_to,RIGHT)
        self.play(Write(derivada_inicial))
        self.play(Write(x_to))
        self.play(Write(derivada_inicial_2))
        # Transformación de la derivada
        derivada_transformada = MathTex(
            r"f'(x) = \frac{1}{2\sqrt{x}} \left( 1 - \frac{1}{6\sqrt[6]{x}} \right)"
        ).move_to(derivada_inicial_2)
        self.play(Transform(derivada_inicial_2, derivada_transformada))

        # Límite cuando x tiende a 0 desde la derecha
        limite = MathTex(
            r"\lim_{x \to 0^+} f'(x) =",  r"\infty ( -\infty)"
        ).next_to(derivada_transformada, DOWN, buff=0.5)
        self.play(Write(limite))
        Minus_infinity=MathTex(r"-\infty").move_to(limite[1]).align_to(limite[1],LEFT)
        self.play(ReplacementTransform(limite[1],Minus_infinity))
        self.wait(2)

