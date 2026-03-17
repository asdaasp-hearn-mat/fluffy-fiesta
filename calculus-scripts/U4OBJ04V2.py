from manim import *
import numpy as np
import math

class E1(Scene):
    def construct(self):
        # Plano
        plane = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-1, 6, 1],
            background_line_style={"stroke_opacity": 0.4},
            axis_config={"color": BLUE},
        ).scale(0.9).to_edge(LEFT)
        self.play(Create(plane))

        # f(x) = e^x
        exp_graph = plane.plot(lambda x: np.exp(x), color=YELLOW, x_range=[-2, 2])
        self.play(Create(exp_graph))
        f_label = MathTex("f(x)=e^x").to_edge(RIGHT).shift(2.5*UP)
        self.play(Write(f_label))
        self.wait(0.5)
        # Textos iniciales a la derecha
        eq1 = MathTex("y=f(x_0)+f'(x_0)(x-x_0)")
        eq2 = MathTex("x_0=0")
        eq3 = MathTex("y=1+x")
        equations = VGroup(eq1, eq2, eq3).arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT)
        self.play(Write(equations))

        # Recta tangente y = 1 + x
        tangent = plane.plot(lambda x: 1 + x, color=RED, x_range=[-2, 2])
        self.play(Create(tangent))
        self.wait(1)

        # Borrar las dos primeras ecuaciones
        self.play(FadeOut(eq1), FadeOut(eq2))
        self.wait(0.5)

        # Transformar "y=1+x" en "y=1+x+ax^2"
        parabola_eq = MathTex("y=1+x+ax^2").move_to(eq3)
        self.play(ReplacementTransform(eq3, parabola_eq))
        self.wait(0.5)

        # Valores de a
        a_values = [1/4, 2/3, 3/4, 1/2]
        a_texts = [
            MathTex(r"y=1+x+\frac{1}{4}x^2"),
            MathTex(r"y=1+x+\frac{2}{3}x^2"),
            MathTex(r"y=1+x+\frac{3}{4}x^2"),
            MathTex(r"y=1+x+?x^2"),
        ]

        current_graph = tangent
        for a_val, a_tex in zip(a_values, a_texts):
            a_tex.move_to(parabola_eq)
            parabola = plane.plot(lambda x, a=a_val: 1 + x + a * x**2, color=PURPLE, x_range=[-2, 2])
            self.play(ReplacementTransform(current_graph, parabola), ReplacementTransform(parabola_eq, a_tex), run_time=1.5)
            current_graph = parabola
            parabola_eq = a_tex
            self.wait(1)

        self.wait(1.5)

        # 🔄 Borrar todo excepto: gráfica f(x), parábola final, y texto f(x)=e^x
        self.play(
            FadeOut(parabola_eq)
        )


        # Mostrar debajo las líneas:
        # p_1(x)=1+x
        # f(0)=1; p_1(0)=1
        # f'(0)=1; p_1'(0)=1
        p1 = MathTex("p_1(x) = 1 + x").next_to(f_label, DOWN, buff=0.5,aligned_edge=RIGHT)
        cond1 = MathTex("f(0) = 1;", "p_1(0) = 1").next_to(p1, DOWN, aligned_edge=RIGHT)
        cond2 = MathTex("f'(0) = 1;", "p_1'(0) = 1").next_to(cond1, DOWN, aligned_edge=RIGHT)
        group1 = VGroup(p1, cond1, cond2)
        self.play(Write(group1))
        self.wait(1)

        # Efecto: resaltar y temblar
        for obj in group1:
            self.play(Indicate(obj, color=RED), run_time=0.7)

        # Borrarlos
        self.play(FadeOut(group1))

        # Mostrar p_2(x) y sus derivadas
        p2 = MathTex("p_2(x) = 1 + x + ax^2").next_to(f_label, DOWN, buff=0.5,aligned_edge=RIGHT)
        p2p = MathTex("p_2'(x) = 1 + 2ax").next_to(p2, DOWN, aligned_edge=RIGHT)
        p2pp = MathTex("p_2''(x) = 2a").next_to(p2p, DOWN, aligned_edge=RIGHT)

        self.play(Write(p2), Write(p2p), Write(p2pp))
        self.wait(0.5)

        # p_2''(0)=2a
        p2pp_0 = MathTex("p_2''(0) = 2a").move_to(p2pp)
        self.play(ReplacementTransform(p2pp, p2pp_0))
        self.wait(0.5)

        # f''(0)=1
        f2 = MathTex("f''(0) = 1").next_to(p2pp_0, DOWN, aligned_edge=RIGHT)
        self.play(Write(f2))
        self.wait(0.5)

        # a = 1/2
        sol = MathTex("a = \\frac{1}{2}").next_to(f2, DOWN, aligned_edge=RIGHT)
        self.play(Write(sol))
        self.wait(1)

        # Reemplazar en p_2(x)
        final_p2 = MathTex(r"p_2(x) = 1 + x + \frac{1}{2}x^2").move_to(p2)
        self.play(ReplacementTransform(p2, final_p2),FadeOut(p2p,p2pp,p2pp_0,f2))
        self.wait(2)


class E2(Scene):
    def construct(self):
        # Crear las ecuaciones con MathTex
        ecuaciones = [
            MathTex(r"\text{Dada } f \text{ y } x_0 \in \mathrm{dom}(f)"),
            MathTex(r"p_1(x) = f(x_0) + f'(x_0)(x - x_0)"),
            MathTex(r"p_2(x) = f(x_0) + f'(x_0)(x - x_0) + \frac{f''(x_0)}{2}(x - x_0)^2"),
            MathTex(r"\text{son los}"),
            MathTex(r"\text{Polinomios de Taylor}"),
            MathTex(r"\text{de primer y segundo orden de } f"),
        ]

        # Colorear "Polinomios de Taylor"
        ecuaciones[4].set_color(BLUE)

        # Agrupar y centrar
        grupo = VGroup(*ecuaciones).arrange(DOWN, aligned_edge=ORIGIN, buff=0.5).move_to(ORIGIN)

        # Animar con Write uno por uno
        for eq in ecuaciones:
            self.play(Write(eq))
            self.wait(0.3)

        self.wait(2)




class E3(Scene):
    def construct(self):
        # === ETAPA 1 ===
        # Lado izquierdo
        left_eqs = [
            MathTex(r"f(x) = \ln(x)"),
            MathTex(r"f'(x) = \frac{1}{x}"),
            MathTex(r"f''(x) = -\frac{1}{x^2}"),
            MathTex(r"p_1(x) = 0 + (x - 1)"),
            MathTex(r"p_2(x) = (x - 1) - \frac{1}{2}(x - 1)^2"),
        ]

        # Lado derecho
        right_eqs = [
            MathTex(r"f(1) = 0"),
            MathTex(r"f'(1) = 1"),
            MathTex(r"f''(1) = -1"),
        ]

        # Posicionamiento
        left_group = VGroup(*left_eqs).arrange(DOWN, aligned_edge=LEFT, buff=0.6).to_edge(LEFT, buff=0.5)
        right_group = VGroup(*right_eqs).arrange(DOWN, aligned_edge=LEFT, buff=0.6).to_edge(RIGHT, buff=1)

        # Alinear por línea
        for i in range(3):
            right_group[i].move_to(left_group[i], aligned_edge=DOWN).to_edge(RIGHT)

        # Animaciones: líneas 1 a 3
        for i in range(3):
            self.play(Write(left_eqs[i]))
            self.play(Write(right_eqs[i]))
            self.wait(0.3)

        # Línea 4 (p_1 antes de simplificar)
        self.play(Write(left_eqs[3]))
        self.wait(0.3)

        # Simplificar p_1: ReplacementTransform
        p1_simple = MathTex(r"p_1(x) = x - 1").move_to(left_eqs[3], aligned_edge=LEFT)
        self.play(ReplacementTransform(left_eqs[3], p1_simple))
        left_eqs[3] = p1_simple
        self.wait(0.3)

        # Línea 5 (p_2)
        self.play(Write(left_eqs[4]))
        self.wait(1)

        # === ETAPA 2 ===
        # Eliminar las ecuaciones intermedias
        self.play(*[FadeOut(mob) for mob in [
            left_eqs[1], left_eqs[2],
            right_group[0], right_group[1], right_group[2]
        ]])
        self.wait(0.3)

        # Reacomodar p_1 y p_2
        self.play(
            left_eqs[3].animate.move_to(left_eqs[1], aligned_edge=LEFT),
            left_eqs[4].animate.move_to(left_eqs[2], aligned_edge=LEFT),
        )

        self.wait(2)
        # === ETAPA 3: Gráfico ===
        self.wait(1)
        plane = NumberPlane(
            x_range=[0, 3, 1],
            y_range=[-2, 2, 1],
            x_length=7,
            y_length=4,
            background_line_style={"stroke_opacity": 0.2}
        ).to_edge(RIGHT, buff=0.5)

        self.play(Create(plane))
        axes_labels = plane.get_axis_labels(x_label="x", y_label="y")  
        self.play(Write(axes_labels))
        self.wait(0.5)        

        # Definir funciones
        graph_fx = plane.plot(lambda x: np.log(x), x_range=[0.2, 3], color=BLUE)
        graph_p1 = plane.plot(lambda x: x - 1, x_range=[0.2, 3], color=GREEN)
        graph_p2 = plane.plot(lambda x: (x - 1) - 0.5 * (x - 1) ** 2, x_range=[0.2, 3], color=PURPLE)

        # Pintar renglones correspondientes
        self.play(Create(graph_fx), left_eqs[0].animate.set_color(BLUE))
        self.wait(0.5)

        self.play(Create(graph_p1), left_eqs[3].animate.set_color(GREEN))
        self.wait(0.5)

        self.play(Create(graph_p2), left_eqs[4].animate.set_color(PURPLE))
        self.wait(2)
        label_fx = MathTex("f").set_color(BLUE).scale(0.7).move_to(plane.c2p(2.8, np.log(2.8)) + LEFT * 0.3)
        label_p1 = MathTex("p_1").set_color(GREEN).scale(0.7).move_to(plane.c2p(2.8, 2.8 - 1) + UP * 0.3)
        label_p2 = MathTex("p_2").set_color(PURPLE).scale(0.7).move_to(plane.c2p(2.8, (2.8 - 1) - 0.5 * (2.8 - 1) ** 2) + UP * 0.3)

        self.play(Write(label_fx), Write(label_p1), Write(label_p2))
        x1_dot = Dot(plane.c2p(1, 0), color=WHITE)
        x1_line = DashedLine(plane.c2p(1, -2), plane.c2p(1, 2), color=WHITE, stroke_opacity=0.3)
        x1_label = MathTex("x = 1").scale(0.6).next_to(x1_line, DOWN)

        self.play(Create(x1_line), FadeIn(x1_dot), Write(x1_label))
        self.wait()


class E4(Scene):
    def construct(self):
        # === ETAPA 1 ===
        # Lado izquierdo: función y derivadas de sin(x)
        left_eqs = [
            MathTex(r"f(x) = \sin(x)"),
            MathTex(r"f'(x) = \cos(x)"),
            MathTex(r"f''(x) = -\sin(x)"),
            MathTex(r"p_1(x) = 0 + (x - 0)"),  # punto de expansión en 0
            MathTex(r"p_2(x) = (x - 0) - \frac{0}{2}(x - 0)^2"),  # porque f''(0) = 0, se repite p_1
        ]

        # Lado derecho: valores evaluados en 0
        right_eqs = [
            MathTex(r"f(0) = 0"),
            MathTex(r"f'(0) = 1"),
            MathTex(r"f''(0) = 0"),
        ]

        # Posicionamiento
        left_group = VGroup(*left_eqs).arrange(DOWN, aligned_edge=LEFT, buff=0.6).to_edge(LEFT, buff=0.5)
        right_group = VGroup(*right_eqs).arrange(DOWN, aligned_edge=LEFT, buff=0.6).to_edge(RIGHT, buff=1)

        # Alinear por línea (las 3 primeras)
        for i in range(3):
            right_group[i].move_to(left_group[i], aligned_edge=DOWN).to_edge(RIGHT)

        # Animaciones: líneas 1 a 3
        for i in range(3):
            self.play(Write(left_eqs[i]))
            self.play(Write(right_eqs[i]))
            self.wait(0.3)

        # Línea 4 (p_1 antes de simplificar)
        self.play(Write(left_eqs[3]))
        self.wait(0.3)

        # Simplificar p_1: ReplacementTransform
        p1_simple = MathTex(r"p_1(x) = x").move_to(left_eqs[3], aligned_edge=LEFT)
        self.play(ReplacementTransform(left_eqs[3], p1_simple))
        left_eqs[3] = p1_simple
        self.wait(0.3)

        # Línea 5 (p_2)
        self.play(Write(left_eqs[4]))
        self.wait(1)

        # === ETAPA 2 ===
        # Eliminar ecuaciones intermedias
        self.play(*[FadeOut(mob) for mob in [
            left_eqs[1], left_eqs[2],
            right_group[0], right_group[1], right_group[2]
        ]])
        self.wait(0.3)

        # Reacomodar p_1 y p_2
        self.play(
            left_eqs[3].animate.move_to(left_eqs[1], aligned_edge=LEFT),
            left_eqs[4].animate.move_to(left_eqs[2], aligned_edge=LEFT),
        )

        self.wait(2)

        # === ETAPA 3: Gráfico ===
        self.wait(1)
        plane = NumberPlane(
            x_range=[-2, 4, 1],
            y_range=[-2, 2, 1],
            x_length=7,
            y_length=4,
            background_line_style={"stroke_opacity": 0.2}
        ).to_edge(RIGHT, buff=0.5)

        self.play(Create(plane))
        axes_labels = plane.get_axis_labels(x_label="x", y_label="y")
        self.play(Write(axes_labels))
        self.wait(0.5)


        # Colores para p1 y p2 ahora rojo y amarillo
        color_p1 = RED
        color_p2 = YELLOW

        graph_fx = plane.plot(lambda x: np.sin(x), x_range=[-1.5, 3], color=BLUE)
        graph_p1 = plane.plot(lambda x: x, x_range=[-1.5, 3], color=color_p1)
        graph_p2 = plane.plot(lambda x: x, x_range=[-1.5, 3], color=color_p2)

        self.play(Create(graph_fx), left_eqs[0].animate.set_color(BLUE))
        self.wait(0.5)

        # Dibujamos p1 y p2 con sus colores respectivos
        self.play(Create(graph_p1), left_eqs[3].animate.set_color(color_p1))
        self.wait(0.5)
        self.play(Create(graph_p2), left_eqs[4].animate.set_color(color_p2))
        self.wait(1)

        # Ahora crear un solo gráfico para p1=p2 con degradado rojo a amarillo
        # Para eso, re-creamos la curva usando LineGradient (Manim Community tiene LinearGradient)

        # Para hacerlo “manual”, usamos VMobject y coloreamos los segmentos


        # Aplicamos el degradado (rojo->amarillo)
        self.play(graph_p2.animate.set_color_by_gradient(RED, YELLOW))

        # Animación de transición: hacer desaparecer p1 y p2, aparecer la curva degradada
        #self.play(FadeOut(graph_p1), FadeOut(graph_p2))
        #self.play(Create(gradient_p))

        # Cambiar color del texto "p_1 = p_2" a degradado también
        label_p1 = MathTex(r"p_1 = p_2").move_to(plane.c2p(3, 3) + UP * 0.3).scale(0.7)
        label_p1.set_color_by_gradient(RED, YELLOW)

        # Ya escribimos antes label_fx, volvemos a mostrar
        label_fx = MathTex("f").set_color(BLUE).scale(0.7).move_to(plane.c2p(3, np.sin(3)) + LEFT * 0.3)

        self.play(Write(label_fx), Write(label_p1))

        # Punto y línea vertical en x=0 (punto de expansión)
        x0_dot = Dot(plane.c2p(0, 0), color=WHITE)
        x0_line = DashedLine(plane.c2p(0, -2), plane.c2p(0, 2), color=WHITE, stroke_opacity=0.3)
        x0_label = MathTex("x = 0").scale(0.6).next_to(x0_line, DOWN)

        self.play(Create(x0_line), FadeIn(x0_dot), Write(x0_label))
        self.wait()


class E5(Scene):
    def construct(self):
        # Fórmula polinomio de Taylor de orden 2 (p2)
        p2 = MathTex(
            r"p_2(x) = f(x_0) + f'(x_0)(x - x_0) + \frac{f''(x_0)}{2}(x - x_0)^2"
        ).scale(0.6).to_edge(LEFT)

        # Fórmula p3 añadiendo término cúbico
        p3 = MathTex(
            r"p_3(x) = f(x_0) + f'(x_0)(x - x_0) + \frac{f''(x_0)}{2}(x - x_0)^2 +",
            r"\frac{f^{(3)}(x_0)}{3!}(x - x_0)^3"
        ).scale(0.6).to_edge(LEFT)

        # Fórmula p4 añadiendo término cuarto
        p4 = MathTex(
            r"p_4(x) = f(x_0) + f'(x_0)(x - x_0) + \frac{f''(x_0)}{2}(x - x_0)^2 +",
            r"\frac{f^{(3)}(x_0)}{3!}(x - x_0)^3 +",
            r"\frac{f^{(4)}(x_0)}{4!}(x - x_0)^4"
        ).scale(0.6).to_edge(LEFT)

         # Fórmula general sin sigma, con puntos suspensivos
        pn = MathTex(
            r"p_n(x) = f(x_0) + f'(x_0)(x - x_0) + \frac{f''(x_0)}{2}(x - x_0)^2 +",
            r"\frac{f^{(3)}(x_0)}{3!}(x - x_0)^3 + \dots +",
            r"\frac{f^{(n)}(x_0)}{n!}(x - x_0)^n"
        ).scale(0.6).to_edge(LEFT)

        # Mostrar p2
        self.play(Write(p2))
        self.wait(1.2)

        # Transformar p2 en p3 (añadir el término cúbico)
        self.play(ReplacementTransform(p2, p3))
        self.wait(1.2)

        # Transformar p3 en p4 (añadir el término cuarto)
        self.play(ReplacementTransform(p3, p4))
        self.wait(1.2)

        # Transformar p4 en fórmula general p_n sin sigma
        self.play(ReplacementTransform(p4, pn))
        self.wait(2)



class E6(Scene):
    def construct(self):
        # === Texto lado izquierdo ===
        formulas = [
            MathTex(r"f(x) = e^x"),
            MathTex(r"x_0 = 0"),
            MathTex(r"p_n = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots + \frac{x^n}{n!}"),
            MathTex(r"\displaystyle n \to \infty"),
            MathTex(r"f(x) = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots"),
        ]

        # Posicionar a la izquierda, con algo de espacio entre líneas
        formulas_group = VGroup(*formulas).arrange(DOWN, aligned_edge=LEFT, buff=0.5).to_edge(LEFT, buff=0.7)
        self.play(*[Write(f) for f in formulas_group[:3]])
        self.wait(1)

        # === Plano lado derecho ===
        plane = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-1, 8, 1],
            x_length=7,
            y_length=5,
            background_line_style={"stroke_opacity": 0.2},
        ).to_edge(RIGHT, buff=0.7)

        self.play(Create(plane))
        axes_labels = plane.get_axis_labels(x_label="x", y_label="y")
        self.play(Write(axes_labels))
        self.wait(0.5)

        # Función f(x) = e^x
        graph_fx = plane.plot(lambda x: np.exp(x), x_range=[-3, 3], color=BLUE)
        label_fx = MathTex("f").set_color(BLUE).scale(0.7)
        label_fx.move_to(plane.c2p(2.5, np.exp(2.5)) + LEFT * 0.4 + UP * 0.3)

        self.play(Create(graph_fx), Write(label_fx))
        self.wait(0.7)

        # Colores para los polinomios (ciclo entre varios para que sea colorido)
        colors = [
    RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE, PINK, GOLD, TEAL
]


        # Función para el polinomio de Taylor de grado n en x0=0
        def taylor_poly(n):
            def p(x):
                return sum(x**k / math.factorial(k) for k in range(n+1))
            return p

        # Lista para almacenar las gráficas y etiquetas
        poly_graphs = []
        poly_labels = []

        for n in range(1, 10):
            p_n = taylor_poly(n)
            graph_pn = plane.plot(p_n, x_range=[-3,3], color=colors[(n-1) % len(colors)])
            label_pn = MathTex(f"p_{n}").set_color(colors[(n-1) % len(colors)]).scale(0.7)
            label_pn.move_to(plane.c2p(1.1, p_n(1.1)) + UP * 0.3 + LEFT * 0.3)

            if n == 1:
                # Crear el primer polinomio y etiqueta
                self.play(Create(graph_pn), Write(label_pn))
            else:
                # Transformar el polinomio y etiqueta anterior en el nuevo
                self.play(
                    ReplacementTransform(poly_graphs[-1], graph_pn),
                    ReplacementTransform(poly_labels[-1], label_pn)
                )

            # Guardar para transformar en la siguiente iteración
            if n == 1:
                poly_graphs.append(graph_pn)
                poly_labels.append(label_pn)
            else:
                poly_graphs[-1] = graph_pn
                poly_labels[-1] = label_pn

            self.wait(0.7)

        # Finalmente reemplazar p_7 por p_n
        label_pn_general = MathTex(r"p_n").set_color(colors[8]).scale(0.7)
        label_pn_general.move_to(poly_labels[-1].get_center())

        self.play(Transform(poly_labels[-1], label_pn_general))
        self.wait(0.7)

        # Mostrar las líneas 4 y 5 (n→∞ y la expansión infinita) abajo de la fórmula p_n
        self.play(Write(formulas_group[3]))
        self.wait(0.3)
        self.play(Write(formulas_group[4]))
        self.wait(2)
