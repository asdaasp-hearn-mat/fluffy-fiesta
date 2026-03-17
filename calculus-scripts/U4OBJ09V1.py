from manim import *

def crear_puntos_y_lineas(x_val, f, plane, color=ORANGE, nombre_funcion="f",nombre_punto="x"):
    f_x_val = f(x_val)
    punto = Dot(plane.c2p(x_val, f_x_val), color=color)
    etiqueta_x = MathTex(f"{nombre_punto}", font_size=30).next_to(Dot(plane.c2p(x_val, 0)), DOWN).set_color(color)
    etiqueta_fx = MathTex(f"{nombre_funcion}({nombre_punto})", font_size=30).next_to(Dot(plane.c2p(0, f_x_val)), RIGHT if x_val < 0 else LEFT, buff=0.05).set_color(color)
    lineas = plane.get_lines_to_point(plane.c2p(x_val, f_x_val))
    return VGroup(punto, etiqueta_x, etiqueta_fx, lineas)

def transform_texts(self, texts, position=ORIGIN, scale_factor=0.8, duration=1):
        if not texts:
            return None
        
        # Crear el texto inicial
        current_text = Tex(texts[0]).scale(scale_factor).move_to(position)
        self.play(Write(current_text))
        last_text = texts[0]  # Almacenar el último texto
        
        for next_text in texts[1:]:
            new_text = Tex(next_text).scale(scale_factor).move_to(position)
            self.play(Transform(current_text, new_text), run_time=duration)
            last_text = next_text
        return last_text  # Devolver el último texto para uso posterior




class E1(Scene):
    def construct(self):
        # Crear el plano cartesiano
        plane = NumberPlane(
            x_range=[-3.5, 3.5, 1],
            y_range=[-3.5, 3.5, 1],
            background_line_style={"stroke_opacity": 0.4}
        ).scale(0.70).move_to(ORIGIN)
        axes_labels = plane.get_axis_labels(x_label="x", y_label="y")
        
        # Título de la escena
        Titulo = Tex(r'"$f$ es creciente si la gráfica de $f$ sube"').to_edge(UP).scale(0.8)
        
        # Graficar la función f(x) = log(1 + exp(x)) en color azul
        f_graph = plane.plot(lambda x: np.log(1 + np.exp(x)), color=BLUE)
        
        # Etiqueta para la gráfica "f"
        f_label = MathTex("f").next_to(f_graph, buff=0.2).set_color(BLUE)
        
        # Flecha morada que aparece en la esquina superior izquierda
        arrow = Arrow(
            start=plane.c2p(-2, 1),
            end=plane.c2p(0, 2),
            color=PINK
        )
        
        # Animaciones iniciales
        self.play(Write(Titulo))  # Escribir el título
        self.wait(2)
        self.play(Create(plane), Write(axes_labels))  # Crear el plano
        self.wait(1)
        self.play(Create(f_graph), Write(f_label))  # Graficar la función y agregar la etiqueta
        self.wait(1)
        self.play(Create(arrow))  # Mostrar la flecha morada
        self.wait(1)
        self.play(FadeOut(arrow))  # Desaparecer la flecha después de 1 segundo
        
        plano = VGroup(plane, axes_labels, f_graph, f_label)
        enunciado = Tex(r"$f$ es creciente si: cuando\\ $x$ aumenta,  $f(x)$ también.", tex_environment="flushleft").to_edge(RIGHT).shift(1.5*UP+LEFT)
                # Cuadro amarillo alrededor del enunciado
        cuadro_titulo = SurroundingRectangle(enunciado, color=YELLOW, buff=0.3)
        # Mover el plano a la izquierda y transformar el título en el enunciado
        self.play(plano.animate.shift(LEFT * 4), ReplacementTransform(Titulo, enunciado), run_time=2)
        self.play(Create(cuadro_titulo))
                # Crear puntos y líneas para x_1 y x_2
        f = lambda x: np.log(1 + np.exp(x))
        punto_y_lineas_x1 = crear_puntos_y_lineas(-1.5, f, plane, color=ORANGE, 
                                                  nombre_funcion="f",nombre_punto="x_1")
        punto_y_lineas_x2 = crear_puntos_y_lineas(1.5, f, plane, color=ORANGE,
                                                   nombre_funcion="f",nombre_punto="x_2")
        
        # Graficar las etiquetas y los puntos
        self.play(GrowFromCenter(punto_y_lineas_x1))
        self.play(GrowFromCenter(punto_y_lineas_x2))
        self.wait(2)
        

        
        # Definición debajo del título, con un cuadro amarillo
        definicion = Tex(
            r"\textbf{Definición}. Se dice que $f$ es",r"creciente si y solo si",
              r"$f(x_1) \leq f(x_2)$ cuando $x_1 \leq x_2$",
                r"para todo $x_1,x_2 \in \mathrm{dom}(f)$",arg_separator=r"\\"
        ).scale(0.9).next_to(cuadro_titulo, DOWN, buff=0.9).align_to(enunciado, direction=ORIGIN)
        cuadro_definicion = SurroundingRectangle(definicion, color=YELLOW, buff=0.3).scale(1).align_to(cuadro_titulo, ORIGIN)
        self.play(Write(definicion), Create(cuadro_definicion),run_time=2)
        self.wait(2)

        

class E2(Scene):
    def construct(self):
        # Crear el plano cartesiano
        plane = NumberPlane(
            x_range=[-4.1, 4.1, 1],
            y_range=[-4.1, 4.1, 1],
            background_line_style={"stroke_opacity": 0.4}
        ).scale(0.70).to_edge(RIGHT)
        axes_labels = plane.get_axis_labels(x_label="x", y_label="y")
        # Gráfico inicial de g(x) = x^3
        g_graph = plane.plot(lambda x: x**3, x_range=[-1.6, 1.6], color=BLUE)
        g_label = MathTex("y=g(x)").set_color(BLUE).next_to(g_graph, UP,buff=0.5)

        # Usar la función `crear_puntos_y_lineas` para puntos y líneas iniciales
        punto_y_lineas_a = crear_puntos_y_lineas(-1.5, lambda x: x**3, plane, color=YELLOW, nombre_funcion="g", nombre_punto="a")
        punto_y_lineas_b = crear_puntos_y_lineas(1.5, lambda x: x**3, plane, color=YELLOW, nombre_funcion="g", nombre_punto="b")

 

        # Texto "a <= b" en la parte izquierda
        titulo_g= MathTex(r"g(x) = x^3").to_edge(LEFT, buff=1).shift(UP * 2)
        texto_inicial = MathTex(r"a \leq b").to_edge(LEFT, buff=1).shift(UP * 1)
        self.play(Write(titulo_g))
        # Animaciones iniciales
        self.play(Create(plane),Write(axes_labels), Create(g_graph), Write(g_label))
        self.play(GrowFromCenter(punto_y_lineas_a), GrowFromCenter(punto_y_lineas_b))
        self.wait(2)
        self.play(Write(texto_inicial))
        self.wait(1)

        # Texto "$a^3 \leq b^3$" debajo de "a <= b"
        texto_segundo = MathTex(r"a^3 \leq b^3").next_to(texto_inicial, DOWN, buff=0.5)
        self.play(Write(texto_segundo))
        self.wait(1)

        # Transformar "$a^3 \leq b^3$" en "$g(a) \leq g(b)$"
        texto_final = MathTex(r"g(a) \leq g(b)").move_to(texto_segundo)
        self.play(ReplacementTransform(texto_segundo, texto_final))
        self.wait(2)
        self.play(FadeOut(texto_final),FadeOut(texto_inicial))

        # Transformar g(x) en p(x)
        p_graph = plane.plot(lambda x: x**4, x_range=[-1.45, 1.45], color=GREEN)
        p_label = MathTex("y=p(x)").set_color(GREEN).next_to(p_graph, UP)
        titulo_p = MathTex(r"p(x) = x^4").to_edge(LEFT, buff=1).shift(UP * 2)
        # Nuevos valores y usar la función `crear_puntos_y_lineas` para la nueva gráfica
        nuevo_punto_y_lineas_a = crear_puntos_y_lineas(0.5, lambda x: x**4, plane, color=YELLOW, nombre_funcion="p", nombre_punto="a")
        nuevo_punto_y_lineas_b = crear_puntos_y_lineas(1, lambda x: x**4, plane, color=YELLOW, nombre_funcion="p", nombre_punto="b")
        
        # Ejecutar transformaciones simultáneamente
        self.play(ReplacementTransform(titulo_g,titulo_p),
                  ReplacementTransform(g_graph, p_graph),
                  ReplacementTransform(g_label, p_label),
                  ReplacementTransform(punto_y_lineas_a, nuevo_punto_y_lineas_a),
                  ReplacementTransform(punto_y_lineas_b, nuevo_punto_y_lineas_b))
        self.wait(2)

        # Título en la parte superior izquierda $p(x) = x^4$
        
        texto = Tex(r"No es necesariamente cierto que \\ $p(a) \leq p(b)$  siempre que $a \leq b$", color=YELLOW).next_to(titulo_p, DOWN, buff=0.7).shift(1.5*RIGHT)
        ejemplo_texto = Tex(r"si $a=\frac{1}{2}$ y $b=1$").next_to(texto, DOWN, buff=0.8)
        ejemplo = Tex(r"$$\frac{1}{16} < 1$$", color=YELLOW).next_to(ejemplo_texto,DOWN, buff=0.8)
        ejemplo_des = MathTex(r"\left(\frac{1}{2}\right)^4 < 1^4",color=YELLOW).move_to(ejemplo)
        fa_leq_fb= MathTex(r"p(a) < p(b)",color=YELLOW).move_to(ejemplo)
        self.wait(1)
        self.play(Write(texto)), self.play(Write(ejemplo_texto)), self.play(FadeIn(ejemplo))
        self.wait(1)
        self.wait(1)
        self.play(ReplacementTransform(ejemplo,ejemplo_des))
        self.play(ReplacementTransform(ejemplo_des,fa_leq_fb))
        self.wait(1)# Crear los nuevos puntos y líneas para el ejemplo
        nuevo_punto_y_lineas_a_2 = crear_puntos_y_lineas(-1, lambda x: x**4, plane, color=YELLOW, nombre_funcion="p", nombre_punto="a")
        nuevo_punto_y_lineas_b_2 = crear_puntos_y_lineas(0.5, lambda x: x**4, plane, color=YELLOW, nombre_funcion="p", nombre_punto="b")
        ejemplo_2 = Tex(r"$1 > \frac{1}{16}$", color=YELLOW).next_to(ejemplo_texto,DOWN, buff=0.8)
        ejemplo_2_texto = Tex(r"si $a=-1$ y $b=\frac{1}{2}$").next_to(texto, DOWN, buff=0.8)
        self.play(ReplacementTransform(nuevo_punto_y_lineas_a,nuevo_punto_y_lineas_a_2),
                  ReplacementTransform(nuevo_punto_y_lineas_b,nuevo_punto_y_lineas_b_2),
                  ReplacementTransform(ejemplo_texto,ejemplo_2_texto),
                  ReplacementTransform(fa_leq_fb,ejemplo_2)
                  )
        self.wait(1)
        variable=MathTex(r"(-1)^4>\left(\frac{1}{2} \right)^4",color=YELLOW).move_to(ejemplo_2)
        self.play(ReplacementTransform(ejemplo_2,variable))
        self.wait(1)
        variable2=MathTex(r"p(a)>p(b)",color=YELLOW).move_to(ejemplo_2)
        self.play(ReplacementTransform(variable,variable2))
        self.wait(1)
        self.play(FadeOut(VGroup(variable2,ejemplo_2_texto,nuevo_punto_y_lineas_a_2,nuevo_punto_y_lineas_b_2,texto)))
        self.wait(1)

        # Transformar p(x) en q(x)
        q_graph = plane.plot(lambda x: 0 if x <= 0 else x**(1/x),x_range=[-4,np.e], color=RED)
        q_label = MathTex("y=q(x)").set_color(RED).next_to(q_graph, UP)



        # Mostrar la regla de correspondencia de q(x) como una función definida por tramos
        regla_q = MathTex(
            r"q(x) = \begin{cases} 0 & \text{si } x \leq 0 \\ x^{\frac{1}{x}} & \text{si } e > x > 0 \end{cases}"
        ).to_edge(LEFT, buff=1).shift(UP * 2)
        self.play(ReplacementTransform(p_graph, q_graph),
                   ReplacementTransform(p_label, q_label),
                   ReplacementTransform(titulo_p,regla_q))
        self.wait(2)
        # Texto "q es creciente" en amarillo
        texto_creciente = Tex(r"$q$ es creciente", color=YELLOW).next_to(regla_q, DOWN, buff=0.5).shift(LEFT)
        self.play(Write(texto_creciente))
        self.wait(1)

        # Texto "pero tiene un tramo constante..."
        texto_constante = Tex(r"pero tiene un tramo constante...", color=WHITE).next_to(texto_creciente, DOWN, buff=0.5).align_to(texto_creciente,LEFT)
        self.play(Write(texto_constante))
        self.wait(2)

        # Borrar los textos
        self.play(FadeOut(regla_q), FadeOut(texto_creciente), FadeOut(texto_constante))
        self.wait(1)

        # Transformar q(x) en arctan(x)
        arctan_graph = plane.plot(lambda x: np.arctan(x), color=PURPLE)
        arctan_label = MathTex(r"y=\arctan(x)").set_color(PURPLE).next_to(arctan_graph, UP)

        self.play(ReplacementTransform(q_graph, arctan_graph), ReplacementTransform(q_label, arctan_label))
        self.wait(2)

        # Mostrar el texto final en la parte izquierda
        texto_final_1 = Tex(r"Si $f$ es creciente,").to_edge(LEFT, buff=1).shift(UP * 2)
        texto_final_2 = Tex(r"y además, $f$ es inyectiva,").next_to(texto_final_1, DOWN, aligned_edge=LEFT)
        texto_final_3 = Tex(r"diremos que $f$ es", color=YELLOW).next_to(texto_final_2, DOWN, aligned_edge=LEFT)
        texto_final_4 = Tex(r"estrictamente creciente.", color=YELLOW).next_to(texto_final_3, DOWN, aligned_edge=LEFT)

        self.play(Write(texto_final_1))
        self.play(Write(texto_final_2))
        self.play(Write(texto_final_3))
        self.play(Write(texto_final_4))
        self.wait(2)
        equivalencia_texto=Tex("Esto es equivalente a:").next_to(texto_final_4,DOWN)
        equivalencia=Tex(r"$f(a)<f(b)$ siempre que $a<b$ \\ para todo $a,b \in \mathrm{dom}(f)$ ",color=YELLOW).next_to(equivalencia_texto,DOWN)
        self.play(Write(equivalencia_texto))
        self.play(Write(equivalencia))



class E3(Scene):
    def construct(self):
        # Crear el plano cartesiano
        plane = NumberPlane(
            x_range=[-3.5, 3.5, 1],
            y_range=[-3.5, 3.5, 1],
            background_line_style={"stroke_opacity": 0.4}
        ).scale(0.70).move_to(ORIGIN)
        axes_labels = plane.get_axis_labels(x_label="x", y_label="y")
        
        # Título de la escena
        Titulo = Tex(r'"$f$ es decreciente si la gráfica de $f$ baja"').to_edge(UP).scale(0.8)
        
        # Definir función f
        def f(x):
            if -3.5 <= x <= -1:
                return -x
            elif -1 < x < 1:
                return 1
            elif 1 <= x <= 3.5:
                return -x + 2
        
        # Graficar la función f(x)
        f_graph = plane.plot(f, color=BLUE)
        f_label = MathTex("f").next_to(f_graph, buff=0.2).set_color(BLUE)
        
        # Flecha decorativa
        arrow = Arrow(
            start=plane.c2p(1, 3),
            end=plane.c2p(3, 2),
            color=PINK
        )

        # Animaciones iniciales
        self.play(Write(Titulo))
        self.wait(2)
        self.play(Create(plane), Write(axes_labels))
        self.wait(1)
        self.play(Create(f_graph), Write(f_label))
        self.wait(1)
        self.play(Create(arrow))
        self.wait(1)
        self.play(FadeOut(arrow))

        plano = VGroup(plane, axes_labels, f_graph, f_label)
        enunciado = Tex(r"$f$ es ", r"decreciente si:  $f(x)$ disminuye \\ a medida que $x$ aumenta.", 
                        tex_environment="flushleft").to_edge(RIGHT).scale(0.9).shift(1.5*UP)

        # Mover el plano a la izquierda y transformar el título en el enunciado
        self.play(plano.animate.shift(LEFT * 4), ReplacementTransform(Titulo, enunciado), run_time=2)
        # Usar la función `crear_puntos_y_lineas` para puntos y líneas en la función f(x)
        x1_val, x2_val = -1.5, 1.5
        punto_y_lineas_x1 = crear_puntos_y_lineas(x1_val, f, plane, color=ORANGE, nombre_funcion="f", nombre_punto="x_1")
        punto_y_lineas_x2 = crear_puntos_y_lineas(x2_val, f, plane, color=ORANGE, nombre_funcion="f", nombre_punto="x_2")

        # Graficar las etiquetas y los puntos
        self.play(GrowFromCenter(punto_y_lineas_x1))
        self.play(GrowFromCenter(punto_y_lineas_x2))
        self.wait(2)
        # Cuadro amarillo alrededor del enunciado
        cuadro_titulo = SurroundingRectangle(enunciado, color=YELLOW, buff=0.3)
        self.play(Create(cuadro_titulo))

        # Definición debajo del título, con cuadro amarillo
        definicion = Tex(
            r"\textbf{Definición}. Se dice que:  \\", r"$f$ es decreciente \\",
              r" si y solo si \\", r" $f(x_1) \geq f(x_2)$ cuando $x_1 \leq x_2$ \\",r"para todo $x_1,x_2 \in \mathrm{dom}(f)$",
              tex_environment="center"
        ).scale(0.9).next_to(cuadro_titulo, DOWN, buff=0.9).align_to(enunciado, direction=ORIGIN)
        cuadro_definicion = SurroundingRectangle(definicion, color=YELLOW, buff=0.3).align_to(cuadro_titulo, ORIGIN)
        self.play(Write(definicion), Create(cuadro_definicion))
        self.wait(2)



        # Transformar a definición de función estrictamente decreciente
        estrictamente = Tex(r"$f$ es estrictamente decreciente", color=YELLOW).move_to(definicion[1]).scale(0.9)
        condicion = Tex(r"$f(x_1) > f(x_2)$ cuando $x_1 < x_2$.", color=YELLOW).scale(0.9).move_to(definicion[3])
        self.play(ReplacementTransform(definicion[1], estrictamente),
                  ReplacementTransform(definicion[3], condicion))
        
        # Nueva función g(x)
        def g(x):
            return -x * abs(x) / 3

        g_graph = plane.plot(g, color=BLUE)

        # Actualizar las posiciones de los puntos y etiquetas con la nueva función g(x)
        nuevo_punto_y_lineas_x1 = crear_puntos_y_lineas(x1_val, g, plane, color=ORANGE, nombre_funcion="f", nombre_punto="x_1")
        nuevo_punto_y_lineas_x2 = crear_puntos_y_lineas(x2_val, g, plane, color=ORANGE, nombre_funcion="f", nombre_punto="x_2")

        # Reemplazar gráfica, puntos y etiquetas
        self.play(ReplacementTransform(f_graph, g_graph),
                  ReplacementTransform(punto_y_lineas_x1, nuevo_punto_y_lineas_x1),
                  ReplacementTransform(punto_y_lineas_x2, nuevo_punto_y_lineas_x2))
        self.wait(2)
class E3B(Scene):
    def construct(self):
        # Texto central que ocupa el ancho de la pantalla
        tex = r"""¿Cómo podemos determinar analíticamente \\  si una función 
        es creciente o decreciente?"""
        texto = Tex(tex, font_size=48).scale(0.9)
        texto.move_to(ORIGIN)
        self.play(FadeIn(texto))
        self.wait(3)


class E4(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-10, 15],
            x_length = 17,
            y_range=[-5, 25],
            y_length = 10,
           
            axis_config={"include_numbers": False, "include_tip": False},
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")

        recta = axes.plot(
            lambda x: -(3/2)*(x-6), color = BLUE
        )
        recta1 = axes.plot(
            lambda x: x+2, color = BLUE
        )
        recta_label = MathTex(r"f", r"(x)", r"=" , r"m", r"x", r"+", r"b", tex_to_color_map= {r"f": BLUE, r"m": RED}).move_to(3*RIGHT+3*UP)
        eme = MathTex(r"m", r"<", r"0", tex_to_color_map = {r"m": RED}).next_to(recta_label, DOWN)
        derecha = Tex(r"$f$ decrece").next_to(eme, DOWN)
        emedos = MathTex(r"m", r">", r"0", tex_to_color_map = {r"m": RED}).next_to(derecha, DOWN)
        izquierda = Tex(r"$f$ crece.").next_to(emedos, DOWN)
        d = Dot(axes.c2p(0,9), color = RED)
        flechinha = Arrow(start = ORIGIN, end = RIGHT).move_to(axes.c2p(2,2))
        
        self.add(axes, axes_labels)
        self.play(Create(recta))
        self.wait()
        self.play(Write(recta_label))
        self.wait()
        self.play(ReplacementTransform(recta_label[3].copy(), eme[0]))
        self.play(Write(eme[1:]))
        self.wait()
        self.play( Write(derecha))
        self.play(MoveAlongPath(d, Line(start = axes.c2p(0,9), end = axes.c2p(6,0))), rate_func = there_and_back, run_time = 4)
        self.wait(2)
        self.play(ReplacementTransform(recta, recta1), d.animate.move_to(axes.c2p(0,2)))
        self.wait()
        self.play(ReplacementTransform(recta_label[3].copy(), emedos[0]))
        self.play(Write(emedos[1:]))
        self.wait()
        self.play( ReplacementTransform(derecha.copy(), izquierda))
        self.play(MoveAlongPath(d, Line(start = axes.c2p(0,2), end = axes.c2p(3,5))), rate_func = there_and_back, run_time = 4)
        self.wait()

class E5(Scene):
    def construct(self):
        axes = NumberPlane()
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        func = lambda t: 2*np.cos(t)
        f = axes.plot(func, color = RED)
        t = ValueTracker(0.1)
        
        tang = always_redraw(
               lambda : VGroup(Dot(axes.c2p(t.get_value(), func(t.get_value()))), Line(start = axes.c2p(t.get_value(), func(t.get_value())), end =axes.c2p(t.get_value()+0.01, func(t.get_value()+0.01)), color = YELLOW).set_length(15))
               )
        p_label = always_redraw(
               lambda: MathTex(r"f'(a)", color = YELLOW).next_to(tang[0], UP)
        )       
        texto = Tex(r"Si", r"$f'(a)$", r"$<$", r"$0$", r", " , "$f$", r" decrece").to_edge(UL)
        texto1 = Tex(r"Si", r"$f'(a)$", r"$>$", r"$0$", r", " , "$f$", r" crece").to_edge(DL).shift(0.5*UP)
        
        self.add(axes, axes_labels)
        self.play(Create(f))
        self.wait()
        self.play(Create(tang), FadeIn(p_label))
        self.wait(2)
        self.play(Create(BackgroundRectangle(texto)))
        self.play(Write(texto))
        self.play(t.animate.set_value(PI-0.1), run_time = 3)
        self.wait()
        self.play(t.animate.set_value(PI+0.1))
        self.wait()
        self.play(Create(BackgroundRectangle(texto1)))
        self.play(Write(texto1))
        self.play(t.animate.set_value(2*PI-0.1), run_time = 3)
        self.wait()



class E6(Scene):
    def construct(self):
        # Texto inicial del teorema
        teo = Tex(r"\textbf{Teorema} (\textit{criterio de monotonía.}) Sea $f$ una función diferenciable en $(a,b)$:", font_size=40).shift(1.5*UP)
        
        # Lista con viñetas para los casos de f'(x) > 0 y f'(x) < 0
        lista = BulletedList(
            r"Si $f'(x) > 0$ para todo $x \in (a,b)$, entonces $f$ es creciente en $(a,b)$.",
            r"Si $f'(x) < 0$ para todo $x \in (a,b)$, entonces $f$ es decreciente en $(a,b)$.",
            font_size=40
        )
        lista.next_to(teo, DOWN, aligned_edge=LEFT,buff=0.5)
        self.play(Write(teo))
        self.play(Write(lista))
        
        # Opcional: Añadir un recuadro alrededor de ambos
        self.play(Create(SurroundingRectangle(VGroup(teo, lista))))
        self.wait(2)



class E7(Scene):
    def construct(self):

        k = ValueTracker(-3)  # Tracking the end values of stuff to show

        # Adding Mobjects for the first plane
        plane1 = NumberPlane(x_range=[-3, 4, 1], x_length=5, y_range=[-8, 9, 2], y_length=5).shift(LEFT * 3.5)
        axes_labels1 = plane1.get_axis_labels(x_label="x", y_label="y").scale(0.75)
        axes_labels1[0].shift(1*DOWN*plane1.get_y_unit_size())
        axes_labels1[1].shift(1*LEFT*plane1.get_x_unit_size())
        func1 = plane1.plot(
            lambda x:  x ** 2, x_range=[-3, 3], color=RED_C
        )
        func1_lab = (
            MathTex(r"f(x)=\frac{1}{2}x^2")
            .set(width=2.5)
            .next_to(plane1, UP, buff=0.2)
            .set_color(RED_C)
        )

        moving_slope = always_redraw(
            lambda: plane1.get_secant_slope_group(
                x=k.get_value(),
                graph=func1,
                dx=0.05,
                secant_line_length=4,
                secant_line_color=YELLOW,
            )
        )

        dot = always_redraw(
            lambda: Dot().move_to(
                plane1.c2p(k.get_value(), func1.underlying_function(k.get_value()))
            )
        )

        # Adding Mobjects for the second plane
        plane2 = NumberPlane(x_range=[-3, 4, 1], x_length=5, y_range=[-8, 9, 2], y_length=5).shift(RIGHT * 3.5)
        
        axes_labels2 = plane2.get_axis_labels(x_label="x", y_label="y").scale(0.75)
        axes_labels2[0].shift(1*DOWN*plane2.get_y_unit_size())
        axes_labels2[1].shift(1*LEFT*plane2.get_x_unit_size())

        func2 = always_redraw(
            lambda: plane2.plot(
                lambda x: 2*x, x_range=[-3, k.get_value()], color=GREEN
            )
        )
        func2_lab = (
            MathTex("f'(x)=x")
            .set(width=2.5)
            .next_to(plane2, UP, buff=0.2)
            .set_color(GREEN)
        )

        moving_h_line = always_redraw(
    lambda: crear_puntos_y_lineas(
        x_val=k.get_value(),
        f=lambda x: 2 * x,  # Derivada de f(x) = x^2
        plane=plane2,
        color=YELLOW,
        nombre_funcion="f'",
        nombre_punto="x"
    )
)

        # Adding the slope value stuff
        slope_value_text = (
            Tex("Slope value: ")
            .next_to(plane1, DOWN, buff=0.1)
            .set_color(YELLOW)
            .add_background_rectangle()
        )

        slope_value = always_redraw(
            lambda: DecimalNumber(num_decimal_places=1)
            .set_value(func2.underlying_function(k.get_value()))
            .next_to(slope_value_text, RIGHT, buff=0.1)
            .set_color(YELLOW)
        ).add_background_rectangle()
        # Playing the animation
        self.play(
            LaggedStart(
                DrawBorderThenFill(plane1),
                Write(axes_labels1),
                DrawBorderThenFill(plane2),
                Write(axes_labels2),
                Create(func1),
                Write(func1_lab),
                Write(func2_lab),
                run_time=5,
                lag_ratio=0.5,
            )
        )
        self.add(moving_slope, moving_h_line, func2,dot)
        self.play(k.animate.set_value(3), run_time=15, rate_func=linear)
        self.wait()
        self.wait()