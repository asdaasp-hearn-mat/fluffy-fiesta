from manim import *
from scipy.special import legendre
import random as rd
def disc(axes, *point):
    c= Circle(radius=0.08, color = BLACK, fill_opacity=1, stroke_width = 1).move_to(axes.c2p(point[0], point[1]))
    d= Circle(radius=0.08, color = WHITE, stroke_width = 1.2).move_to(axes.c2p(point[0], point[1]))
    return VGroup(c,d)




class E1(Scene):
    def construct(self):
        axes = Axes(x_range=(-1,10,1),
                  y_range=(-1,20,1),
                  axis_config={"include_numbers": False, "include_tip": False}).shift(0.5*LEFT)
        axes_labels = axes.get_axis_labels(x_label="t", y_label="\$")
        x = np.arange(2,6.5,0.2,dtype=float)
        y = np.array([2*(i-4)**2 +6 + 0.5*rd.random()*rd.choice([1,-1]) for i in x])
        
        baja = VGroup(*[Dot(axes.c2p(_x,_y), color=RED) for _x,_y in zip(x[x<=4],y[x<=4])])
        sube = VGroup(*[Dot(axes.c2p(_x,_y), color=BLUE) for _x,_y in zip(x[x>4],y[x>4])])
        f = lambda x: 2*(x-4)**2+6
        efe = axes.plot(f, color = ORANGE, x_range = [2,4])
        efe2 = axes.plot(f, color = GREEN, x_range = [4,6.5])
        motto = Tex(r"Comprar barato", r", ", r"vender caro").to_edge(UP)
        lines = axes.get_lines_to_point(axes.c2p(3, f(3)), color = YELLOW)
        inver = Tex(r"Compra", font_size = 24).next_to(Dot(axes.c2p(3, 0)), DOWN)
        lines2 = axes.get_lines_to_point(axes.c2p(5.8, f(5.8)), color = YELLOW)
        retiro = Tex(r"Venta", font_size = 24).next_to(Dot(axes.c2p(5.8, 0)), DOWN)       
        dl = DashedLine(axes.c2p(3, f(3)), axes.c2p(5.8, f(3)), color = YELLOW)
        sec = Line(axes.c2p(3, f(3)), axes.c2p(5.8, f(5.8)))
        br = Brace(Line(axes.c2p(5.8, f(3)), axes.c2p(5.8, f(5.8))), direction = RIGHT)
        br_label = Tex(r"Ganancia", font_size = 24).next_to(br, RIGHT)    
        
        self.play(Write(motto))
        self.wait(2)
        self.play(Create(axes))
        self.play(FadeIn(axes_labels))
        self.wait()
        self.play(AnimationGroup([FadeIn(p) for p in baja], lag_ratio = 0.2), run_time =2)
        self.wait(2)
        self.play(Indicate(motto[1]))
        self.wait()
        self.play(Create(efe))
        self.wait()
        self.play(Create(lines))
        self.play(Write(inver))
        self.wait(2)
        self.play(AnimationGroup([FadeIn(p) for p in sube], lag_ratio = 0.2), run_time =1)
        self.wait(2)
        self.play(Indicate(motto[3]))
        self.wait()
        self.play(Create(efe2))
        self.wait()
        self.play(Create(lines2))
        self.play(Write(retiro))
        self.wait(2)
        self.play(Create(dl))
        self.wait()
        self.play(Create(sec))
        self.wait()
        self.play(Create(br))
        self.play(Write(br_label))
        self.wait(2)

class E2(Scene):
    def construct(self):
        axes = Axes(x_range=(-1,10,1),
                  y_range=(-1,20,1),
                  axis_config={"include_numbers": False, "include_tip": False}).shift(0.5*LEFT)
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        f = lambda x: 15/(1+np.exp(-rd.random()*(x-3)))
        esto = axes.plot(f, color = RED)
        f1 = axes.plot(lambda t: (t-5)**2, color = BLUE, x_range=[2, 8])
        f2 = axes.plot(lambda t: (t-5)**4, color = BLUE, x_range=[3, 7])
        f3 = axes.plot(lambda t: 5*abs(t-5), color = BLUE, x_range=[2, 8])

        vg = VGroup(esto, f1, f2, f3)
        convex = Tex(r"Funciones ", r"convexas").to_edge(UP)
        l1 = DashedLine(axes.c2p(3, 5*abs(3-5)), axes.c2p(3,0), color = YELLOW)
        l2 = DashedLine(axes.c2p(8, 5*abs(8-5)), axes.c2p(8,0), color = YELLOW)
        a = Dot(axes.c2p(3,0))
        a_label = Tex(r"a", color = RED).next_to(a, DOWN)
        b = Dot(axes.c2p(8,0))
        b_label = Tex(r"b", color = RED).next_to(b, DOWN) 
        sec = Line(axes.c2p(3, 5*abs(3-5)), axes.c2p(8, 5*abs(8-5))).set_length(10)    
        res = axes.plot(lambda t: 5*abs(t-5), color = YELLOW,x_range = [3,8])
        desc = Tex(r"La ", r"función", r"\\ está por debajo de la recta secante", font_size = 24).shift(5*RIGHT)
        
        self.add(axes, axes_labels)
        self.play(Create(esto), run_time =2)
        #self.play(FadeOut(esto))
        self.wait(2)
        #self.play(AnimationGroup([ReplacementTransform(vg[i], vg[i+1]) for i in range(len(vg)-1)], lag_ratio = 1))
        for i in range(len(vg)-1): #Tuve que hacerlo manual porque el automático no funcionaba bien.
            self.play(ReplacementTransform(vg[i], vg[i+1]))
            self.wait()
        
        self.play(Write(convex))    
        self.wait()
        self.play(Create(VGroup(l1, l2)))
        self.play(FadeIn(VGroup(a, a_label)))
        self.play(FadeIn(VGroup(b, b_label)))
        self.wait()
        self.play(Create(sec))
        self.wait()
        self.play(Create(res), run_time = 3)
        self.wait()
        self.play(Create(BackgroundRectangle(desc)))
        self.play(Write(desc))
        self.wait()

class E3(Scene):
    def construct(self):
        # Ejes (sin números) y función convexa
        axes = Axes(
            x_range=(0, 10),
            y_range=(0, 20),
            axis_config={"include_numbers": False}
        ).shift(0.5 * LEFT)
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        f = lambda x: (x - 5)**2
        graph = axes.plot(f, color=BLUE, x_range=[0.8, 8])

        # Puntos x1 y x2
        x1, x2 = 1, 7.5
        y1, y2 = f(x1), f(x2)
        p1 = Dot(axes.c2p(x1, y1), color=YELLOW)
        p2 = Dot(axes.c2p(x2, y2), color=YELLOW)
        label1 = Tex(r"$x_1$", font_size=28).next_to(axes.c2p(x1, 0), DOWN)
        label2 = Tex(r"$x_2$", font_size=28).next_to(axes.c2p(x2, 0), DOWN)

        # Recta secante
        secante = Line(axes.c2p(x1, y1), axes.c2p(x2, y2), color=ORANGE)

        self.play(Create(axes), FadeIn(axes_labels))
        self.play(Create(graph), run_time=2)
        self.wait()
        self.play(FadeIn(p1), FadeIn(p2))
        self.play(Write(label1), Write(label2))
        self.wait()
        self.play(Create(secante))
        self.wait()

        # Pendiente de la secante
        m = (y2 - y1) / (x2 - x1)

        # Helper: escoger x, marcar imagen en secante y luego mover a la curva
        def marcar_x_intermedio():
            x = rd.uniform(x1 + 0.1, x2 - 0.1)
            y_sec = y1 + m * (x - x1)      # imagen en la secante
            y_fun = f(x)                    # imagen en la curva (convexa: estará por debajo)

            base_dot = Dot(axes.c2p(x, 0), color=WHITE)
            base_lab = Tex(r"$x$", font_size=26).next_to(axes.c2p(x, 0), DOWN)

            vline_sec = DashedLine(axes.c2p(x, 0), axes.c2p(x, y_sec), color=YELLOW)
            dot_sec = Dot(axes.c2p(x, y_sec), color=ORANGE)

            self.play(FadeIn(base_dot), Write(base_lab))
            self.play(Create(vline_sec), FadeIn(dot_sec), run_time=0.8)
            self.wait(0.3)

            # Extender la línea vertical hasta la curva y mover el punto desde la secante a la curva
            vline_fun = DashedLine(axes.c2p(x, 0), axes.c2p(x, y_fun), color=YELLOW)
            self.play(Transform(vline_sec, vline_fun), dot_sec.animate.move_to(axes.c2p(x, y_fun)), run_time=0.8)
            self.wait(0.3)

            # Limpiar
            self.play(FadeOut(VGroup(base_dot, base_lab, vline_sec, dot_sec)), run_time=0.5)

        for _ in range(3):
            marcar_x_intermedio()
        self.wait(1.0)
class E4(Scene):
    def construct(self):
        # Ejes (sin números) y función cóncava
        axes = Axes(
            x_range=(0, 10),
            y_range=(0, 20),
            axis_config={"include_numbers": False}
        ).shift(0.5 * LEFT)
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        f = lambda x: - (x - 5)**2 + 20
        graph = axes.plot(f, color=RED, x_range=[0.8, 8])

        # Puntos x1 y x2
        x1, x2 = 1, 7.5
        y1, y2 = f(x1), f(x2)
        p1 = Dot(axes.c2p(x1, y1), color=YELLOW)
        p2 = Dot(axes.c2p(x2, y2), color=YELLOW)
        label1 = Tex(r"$x_1$", font_size=28).next_to(axes.c2p(x1, 0), DOWN)
        label2 = Tex(r"$x_2$", font_size=28).next_to(axes.c2p(x2, 0), DOWN)

        # Recta secante
        secante = Line(axes.c2p(x1, y1), axes.c2p(x2, y2), color=ORANGE)

        self.play(Create(axes), FadeIn(axes_labels))
        self.play(Create(graph), run_time=2)
        self.wait()
        self.play(FadeIn(p1), FadeIn(p2))
        self.play(Write(label1), Write(label2))
        self.wait()
        self.play(Create(secante))
        self.wait()

        # Pendiente de la secante
        m = (y2 - y1) / (x2 - x1)

        # Helper: escoger x, marcar imagen en secante y luego mover a la curva
        def marcar_x_intermedio():
            x = rd.uniform(x1 + 0.1, x2 - 0.1)
            y_sec = y1 + m * (x - x1)      # imagen en la secante
            y_fun = f(x)                    # imagen en la curva (cóncava: estará por encima)

            base_dot = Dot(axes.c2p(x, 0), color=WHITE)
            base_lab = Tex(r"$x$", font_size=26).next_to(axes.c2p(x, 0), DOWN)

            vline_sec = DashedLine(axes.c2p(x, 0), axes.c2p(x, y_sec), color=YELLOW)
            dot_sec = Dot(axes.c2p(x, y_sec), color=ORANGE)

            self.play(FadeIn(base_dot), Write(base_lab))
            self.play(Create(vline_sec), FadeIn(dot_sec), run_time=0.8)
            self.wait(0.3)

            # Extender la línea vertical hasta la curva y mover el punto desde la secante a la curva
            vline_fun = DashedLine(axes.c2p(x, 0), axes.c2p(x, y_fun), color=YELLOW)
            self.play(Transform(vline_sec, vline_fun), dot_sec.animate.move_to(axes.c2p(x, y_fun)), run_time=0.8)
            self.wait(0.3)

            # Limpiar
            self.play(FadeOut(VGroup(base_dot, base_lab, vline_sec, dot_sec)), run_time=0.5)

        for _ in range(3):
            marcar_x_intermedio()
        self.wait(1.0)

class E5(Scene):
    def construct(self):       
        axes = NumberPlane()
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        func = lambda t: np.exp(t)
        f1 = axes.plot(func, color=RED)
        f1_label = MathTex(r"f", color=RED).next_to(Dot(axes.c2p(0.2, func(0.2))), RIGHT)
        r = ValueTracker(-1.5)
        rt = lambda t: np.exp(r.get_value()) + np.exp(r.get_value()) * (t - r.get_value())

        tang = always_redraw(lambda: axes.plot(rt, color=YELLOW))
        tp = always_redraw(lambda: Dot(axes.c2p(r.get_value(), func(r.get_value()))))       

        l1 = DashedLine(axes.c2p(-1.5, func(-1.5)), axes.c2p(-1.5, 0), color=YELLOW)
        l2 = DashedLine(axes.c2p(1, func(1)), axes.c2p(1, 0), color=YELLOW)
        a = Dot(axes.c2p(-1.5, 0))
        a_label = Tex(r"$x_1$", color=RED).next_to(a, DOWN)
        b = Dot(axes.c2p(1, 0))
        b_label = Tex(r"$x_2$", color=RED).next_to(b, DOWN)

        # Antecedente y el nuevo texto
        f1_f2 = MathTex(r"f'(x_1) < f'(x_2)", font_size=40).shift(3*RIGHT + UP)
        fpp_only = MathTex(r"f''(x) > 0", font_size=40).move_to(f1_f2)

        self.add(axes, axes_labels)
        self.play(Create(f1), Write(f1_label))
        self.play(Create(VGroup(l1, l2)))
        self.play(FadeIn(VGroup(a, a_label)))
        self.play(FadeIn(VGroup(b, b_label))) 
        self.wait(2)

        self.play(Create(tang), FadeIn(tp))
        self.play(r.animate.set_value(1), run_time=5)
        self.play(Write(f1_f2))
        self.wait(1)  # espera antes de cambiar
        self.play(Transform(f1_f2, fpp_only))
        self.wait()


class E7(Scene):
    def construct(self):
        x0 = 2
        y0 = 1

        axes = Axes(
            x_range=[0, 5],
            y_range=[-1, 2],
            axis_config={"include_tip": False},
        )
        labels = axes.get_axis_labels(x_label="x", y_label="y")

        # Base: punto, proyección y tangente horizontal en (x0, y0)
        punto = Dot(axes.c2p(x0, y0), color=RED)
        punto_label = Tex(r"$x_0$", color=RED).next_to(axes.c2p(x0, 0), DOWN)
        linea_x0 = DashedLine(axes.c2p(x0, 0), axes.c2p(x0, y0), color=YELLOW)
        tangente = Line(axes.c2p(0, y0), axes.c2p(5, y0), color=BLUE)

        self.play(Create(axes), Write(labels))
        self.play(Create(tangente))
        self.play(FadeIn(punto), Write(punto_label), Create(linea_x0))
        self.wait()

        # ====== CASO 1: Máximo local (f''(x0) < 0) ======
        # Varias funciones con máximo en (x0, y0) y tangente horizontal
        def f1(x): return -(x - x0)**4 + y0
        def f2(x): return -(x - x0)**2 + y0
        def f3(x): return np.cos(x - x0) + y0 - 1          # máximo en x0
        def f4(x): return -np.tanh(x - x0)**2 + y0         # tangente horizontal

        curves_max = [
            axes.plot(f1, color=WHITE),
            axes.plot(f2, color=WHITE),
            axes.plot(f3, color=WHITE),
            axes.plot(f4, color=WHITE),
        ]

        etiqueta_max = MathTex(r"f''(x_0)<0", font_size=34)\
            .next_to(axes, UP, buff=0.3)

        # Mostrar secuencia de curvas para el máximo
        self.play(Create(curves_max[0]))
        self.wait()
        for i in range(len(curves_max) - 1):
            self.play(ReplacementTransform(curves_max[i], curves_max[i + 1]))
            self.wait()
        self.play(Write(etiqueta_max))
        self.wait(1.5)

        # Limpiar curvas del caso máximo (dejamos ejes/tangente/punto)
        self.play(FadeOut(VGroup(curves_max[-1], etiqueta_max)))
        self.wait(0.5)

        # ====== CASO 2: Mínimo local (f''(x0) > 0) ======
        # Varias funciones con mínimo en (x0, y0) y tangente horizontal
        def g1(x): return (x - x0)**4 + y0
        def g2(x): return (x - x0)**2 + y0
        def g3(x): return -np.cos(x - x0) + y0 + 1          # mínimo en x0
        def g4(x): return np.tanh(x - x0)**2 + y0           # tangente horizontal

        curves_min = [
            axes.plot(g1, color=WHITE),
            axes.plot(g2, color=WHITE),
            axes.plot(g3, color=WHITE),
            axes.plot(g4, color=WHITE),
        ]

        etiqueta_min = MathTex(r"f''(x_0)>0", font_size=34)\
            .next_to(axes, UP, buff=0.3)

        # Mostrar secuencia de curvas para el mínimo
        self.play(Create(curves_min[0]))
        self.wait()
        for i in range(len(curves_min) - 1):
            self.play(ReplacementTransform(curves_min[i], curves_min[i + 1]))
            self.wait()
        self.play(Write(etiqueta_min))
        self.wait(2)



       
from manim import *  # asegúrate de tener MovingCameraScene disponible

class E8(MovingCameraScene):
    def construct(self):
        # Ejes con etiquetas t y $
        axes = Axes(
            x_range=(0, 10),
            y_range=(-10, 10, 1),
            axis_config={"include_numbers": False}
        ).shift(0.5 * LEFT)
        axes_labels = axes.get_axis_labels(x_label="t", y_label="\\$")

        # Función cúbica con punto de inflexión en t=4
        f = lambda t: -0.2 * (t - 4)**3 + (t - 4) + 3
        graph = axes.plot(f, color=BLUE, x_range=[0, 7])

        # Punto de inflexión
        t_inf = 4
        y_inf = f(t_inf)
        p_inf = Dot(axes.c2p(t_inf, y_inf), color=YELLOW)
        label_inf = Tex("Punto de inflexión", font_size=24, color=YELLOW)\
            .next_to(p_inf, UP, buff=0.25)

        # Intro
        self.play(Create(axes), FadeIn(axes_labels))
        self.play(Create(graph), run_time=3)
        self.play(FadeIn(p_inf), Write(label_inf))
        self.wait()

        # === ZOOM centrado en el punto de inflexión ===
        frame = self.camera.frame
        frame.save_state()  # para poder deshacer el zoom luego

        target = axes.c2p(t_inf, y_inf)
        zoom_width = 2.5  # más pequeño => más zoom

        self.play(frame.animate.move_to(target).set(width=zoom_width), run_time=2.0)
        self.play(Indicate(p_inf), run_time=1.2)
        self.wait()

        # (Opcional) volver a la vista original
        self.play(Restore(frame), run_time=2.0)
        self.wait()

class E6(Scene):
    def construct(self):
        # Definición de cóncavidad
        teo = Tex(
            r"\textbf{Definición}. Se dice que $f$ es \textbf{cóncava} en un intervalo $I$, ",
            r"si dados $a < x < b$ en $I$, se cumple que:",
            r"\[\frac{f(x) - f(a)}{x - a} > \frac{f(b) - f(a)}{b - a}\]",
            font_size=36
        ).to_edge(UP)

        # Primer teorema
        teo1 = Tex(
            r"\textbf{Teorema}. Si $f$ es dos veces diferenciable y $f'' > 0$, ",
            r"entonces $f$ es cóncava hacia arriba.",
            font_size=36
        ).next_to(teo, DOWN, buff=0.5)

        # Segundo teorema
        teo2 = Tex(
            r"\textbf{Teorema}. Si $f$ es dos veces diferenciable y $f'' < 0$, ",
            r"entonces $f$ es cóncava hacia abajo.",
            font_size=36
        ).next_to(teo1, DOWN, buff=0.5)

        # Animaciones
        #self.play(Create(SurroundingRectangle(teo)))
        #self.play(Write(teo), run_time=3)
        #self.wait()

        self.play(Create(SurroundingRectangle(teo1)))
        self.play(Write(teo1), run_time=3)
        self.wait()

        self.play(Create(SurroundingRectangle(teo2)))
        self.play(Write(teo2), run_time=3)
        self.wait()
class E9(Scene):
    def construct(self):
        defin = Tex(
            r"\textbf{Definición}. Sea $f:(a,b)\to\mathbb{R}$ y $c\in(a,b)$.",
            r"Se dice que $(c,f(c))$ es un \textbf{punto de inflexión} si y solo si",
            r"$(a,c)$ y $(c,b)$ tienen distinta concavidad.",
            font_size=36
        ).move_to(ORIGIN)  # centrado

        box = SurroundingRectangle(defin, color=YELLOW, buff=0.25)
        self.play(Create(box), run_time=1.5)  # más lento
        self.play(Write(defin), run_time=4)   # escritura lenta
        self.wait(3)


class EX(Scene):
    def construct(self):
        # Funciones
        f = lambda x: x * abs(x)
        fprime = lambda x: abs(2 * x)

        # 1) f centrado con NumberPlane (sin reducir el plano)
        plane1 = NumberPlane(
            x_range=[-4.1, 4.1, 1],
            y_range=[-4.1, 4.1, 1],
            background_line_style={"stroke_opacity": 0.4}
        ).scale(0.70).move_to(ORIGIN)
        axes_labels1 = plane1.get_axis_labels(x_label="x", y_label="y")

        # Limitar SOLO el dominio del plot para no salirse verticalmente
        graph_f = plane1.plot(f, x_range=[-2, 2], color=BLUE)
        label_f = MathTex(r"f(x)=x|x|").set_color(BLUE).next_to(plane1, UP, buff=0.4)

        self.play(Create(plane1), Write(axes_labels1))
        self.play(Create(graph_f), Write(label_f))
        self.wait(0.5)

        # Punto de inflexión (0,0)
        p_inf = Dot(plane1.c2p(0, 0), color=YELLOW)
        inf_label = Tex("Punto de inflexión", font_size=26, color=YELLOW)\
            .next_to(p_inf, DOWN, buff=0.2)
        self.play(FadeIn(p_inf), Write(inf_label))
        self.wait(0.6)

        # 2) Mover todo el bloque de f a la IZQUIERDA
        left_group = VGroup(plane1, axes_labels1, graph_f, label_f, p_inf, inf_label)
        self.play(left_group.animate.to_edge(LEFT, buff=1.0), run_time=1.0)
        self.wait(0.2)

        # 3) Derivada a la DERECHA (plano igual; solo dominio acotado del plot)
        plane2 = NumberPlane(
            x_range=[-4.1, 4.1, 1],
            y_range=[-4.1, 4.1, 1],
            background_line_style={"stroke_opacity": 0.4}
        ).scale(0.70).to_edge(RIGHT, buff=1.0)
        axes_labels2 = plane2.get_axis_labels(x_label="x", y_label="y")

        graph_fp = plane2.plot(fprime, x_range=[-2, 2], color=RED)
        label_fp = MathTex(r"f'(x)=|2x|").set_color(RED).next_to(plane2, UP, buff=0.4)
        note = Tex(r"$f''(0)$ no existe", font_size=28).next_to(plane2, DOWN, buff=0.35)

        self.play(Create(plane2), Write(axes_labels2))
        self.play(Create(graph_fp), Write(label_fp))
        self.wait(2)
        self.play(Write(note))
        self.wait(1.0)
