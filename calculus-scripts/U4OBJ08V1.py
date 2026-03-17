from manim import *

class E1(Scene):
    def construct(self):
        # Definir la función paramétrica h(t+0.5) y p(t+0.5)
        def h(t):
            return 3 * (np.sqrt(2)/2) * (np.cos(np.pi * (t + 0.5)) + np.sin(np.pi * (t + 0.5))) / (2 + np.cos(np.pi * (t + 0.5)))

        def p(t):
            return 3 * (np.sqrt(2)/2) * (np.sin(np.pi * (t + 0.5)) - np.cos(np.pi * (t + 0.5))) / (2 + np.cos(np.pi * (t + 0.5)))

        def r(t):
            return 3 / (2 + np.cos(np.pi * (t + 0.5)))

        # Crear el primer plano de coordenadas
        plane1 = NumberPlane(
            x_range=[-3.5, 3.5, 1],
            y_range=[-3.5, 3.5, 1],
                        background_line_style={
                "stroke_color": GRAY,
                "stroke_width": 2,
                "stroke_opacity": 0.4
            }
        ).scale(0.70)  
        plane_rect1 = SurroundingRectangle(plane1, color=WHITE, buff=0.70) 
        axes_labels1 = plane1.get_axis_labels(x_label="x", y_label="y")

        # Crear la curva paramétrica en el primer plano
        curve = plane1.plot_parametric_curve(
            lambda t: np.array([h(t), p(t), 0]),
            t_range=[0, 2],
            color=BLUE
        ) 

        # Dibujar el segmento de recta desde el origen al punto inicial en el primer plano
        t = ValueTracker(0)
        dot = always_redraw(
            lambda: Dot(plane1.c2p(h(t.get_value()), p(t.get_value())), color=YELLOW)
        )
        origin_to_point = always_redraw(
            lambda: Line(plane1.c2p(0, 0), plane1.c2p(h(t.get_value()), p(t.get_value())), color=YELLOW)
        )

        # Etiquetas para el primer plano
        point_label = always_redraw(
            lambda: MathTex(r"(x(t),y(t))").next_to(dot.get_center(), RIGHT, buff=0.1)
        )
        line_label = always_redraw(
            lambda: MathTex(r"r(t)").next_to(origin_to_point, LEFT, buff=0.2).set_color(YELLOW)
        )

        # Crear el segundo plano de coordenadas
        plane2 = NumberPlane(
            x_range=[0, 3, 1],
            y_range=[0, 3, 1],
                        background_line_style={
                "stroke_color": GRAY,
                "stroke_width": 2,
                "stroke_opacity": 0.4
            }
        ).to_edge(RIGHT).shift(1.5*LEFT)
        plane_rect2 = SurroundingRectangle(plane2, color=WHITE,buff=0.7) 
        axes_labels2 = plane2.get_axis_labels(x_label="t", y_label=r"r(t)")

        # Crear la gráfica de r(t) en el segundo plano
        graph_r = always_redraw(
            lambda: plane2.plot(
                lambda t_val: r(t_val),
                x_range=[0, t.get_value()],
                color=YELLOW
            )
        )

        # Añadir elementos a la escena
        self.play(Create(plane_rect1), Create(plane1), Write(axes_labels1))
        self.wait(1)
        self.play(Create(curve))
        self.play(Create(origin_to_point), FadeIn(dot))
        self.wait(1)
        self.play(Write(point_label))
        self.wait(1)
        self.play(Write(line_label))
        self.wait(1)
        
 

        # Mover todo el plano 1 y sus elementos hacia la esquina izquierda
        group1 = VGroup(plane_rect1, plane1, curve, origin_to_point, dot, point_label, line_label, axes_labels1)
        self.play(group1.animate.to_corner(UL))
        self.wait(1)
       # Crear y mover el segundo plano de coordenadas
        self.play(Create(plane_rect2), Create(plane2), Write(axes_labels2))
        self.wait(1)
        # Graficar simultáneamente el movimiento del punto y la gráfica de r(t)
        self.play(t.animate.set_value(2), Create(graph_r), run_time=4, rate_func=linear)
        self.wait(2)
        texto_final=Tex(r"¿En qué momentos el asteroide se encuentra más cerca y más lejos de","la Tierra?",font_size=30,arg_separator=" ").to_edge(DOWN).shift(0.1*DOWN)
        #la_Tierra=Tex(r" ",font_size=36).next_to(texto_final,RIGHT)
        self.play(Write(texto_final))
        self.wait(2)

class E2(Scene):
    def construct(self):
        # Texto principal 
        texto1 = Tex(r"$\textbf{Definición}$. Sea $f$ una función de variable real y $c$ un punto del dominio de $f$.").scale(0.8).move_to(ORIGIN).shift(2*UP)
        texto2 = Tex(r"$\cdot$ $f(c)$ es un \textbf{máximo} de $f$ si y solo si $f(x) \leq f(c), \forall x \in \mathrm{dom} f$").next_to(texto1,DOWN,buff=0.3).scale(0.8)
        texto3 = Tex(r"$\cdot$ $f(c)$ es un \textbf{mínimo} de $f$ si y solo si $f(x) \geq f(c), \forall x \in \mathrm{dom} f$").next_to(texto2,DOWN,buff=0.3).scale(0.8)
        texto4 = Tex(r"En cualquiera de estos casos, se dice que $f(c)$ es un \textbf{extremo absoluto} de $f$").next_to(texto3,DOWN,buff=0.3).scale(0.8)

        cuadro = SurroundingRectangle(VGroup(texto1,texto2,texto3,texto4), color=YELLOW)
        # Subrayado de las palabras clave 
        subrayado_maximo = Underline(texto2[0][9:16], color=DARK_BLUE)
        subrayado_minimo = Underline(texto3[0][9:16], color=DARK_BLUE)
        resaltado_extremo_absoluto = BackgroundRectangle(texto4[0][42:57], color=DARK_BLUE, fill_opacity=0.5)
        
        self.play(Write(texto1),Write(texto2),Write(texto3),Write(texto4), Create(cuadro))
        self.wait(1)


        self.play(Create(subrayado_maximo), Create(subrayado_minimo))
        self.wait(2)
        self.play(ApplyMethod(texto4[0][42:57].set_color, BLUE))
        self.wait(1)
        self.wait(2)


class E3(Scene):
    def construct(self):
        # Crear el texto
        teorema = Tex(
            r"\textbf{Teorema.} Si $f$ es continua en un intervalo $[a,b]$ entonces $f$ alcanza un mínimo absoluto y un máximo absoluto."
        ).scale(0.8)
        cuadro = SurroundingRectangle(teorema, color=YELLOW, buff=0.5)
        teorema.move_to(cuadro.get_center())

        # Animar el texto
        self.play(Create(cuadro))
        self.play(Write(teorema))
        self.wait(3)


class E4(Scene):
    def construct(self):
        # Ejes
        axes = NumberPlane(
            axis_config={"include_numbers": False, "include_tip": False},
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        # Etiquetas para los puntos a, b, c
        a = MathTex(r"a", color=ORANGE, font_size=40).next_to(Dot(axes.c2p(-4, 0)), RIGHT).shift(0.25 * DOWN).shift(0.25 * LEFT)
        b = MathTex(r"b", color=ORANGE, font_size=40).next_to(Dot(axes.c2p(3, 0)), RIGHT).shift(0.25 * DOWN).shift(0.25 * LEFT)
        c = MathTex(r"c", color=ORANGE, font_size=40).next_to(Dot(axes.c2p(1, 0)), RIGHT).shift(0.25 * DOWN).shift(0.25 * LEFT)

        # Función f y puntos iniciales y finales
        f = axes.plot(lambda x: (x-1)**2/5 - 2, color=YELLOW, x_range=[-4, 3])
        p_initial = Dot(axes.c2p(-4, f.underlying_function(-4)), color=YELLOW)
        p_final = Dot(axes.c2p(3, f.underlying_function(3)), color=YELLOW)

        # Etiqueta f(c)
        f_c = MathTex(r"f(c)", color=ORANGE, font_size=40).next_to(Dot(axes.c2p(0,f.underlying_function(1))), LEFT)
        
        # Líneas punteadas para (c, f(c))
        c_point = axes.c2p(1, f.underlying_function(1))
        dotted_line_x = DashedLine(start=axes.c2p(1, 0), end=c_point, color=GREEN, stroke_width=4)
        dotted_line_y = DashedLine(start=axes.c2p(0, f.underlying_function(1)), end=c_point, color=GREEN, stroke_width=4)
        
        # Animaciones iniciales
        self.play(Create(axes), Write(axes_labels))
        self.play(Write(a), Write(b), Write(c))
        self.play(Create(f), Create(p_initial), Create(p_final))
        self.play(Create(f_c))
        self.play(Create(dotted_line_x), Create(dotted_line_y))
        self.wait(2)

        # Nueva función p y transformación de los puntos
        p = axes.plot(lambda x: -1/10 * ((x/2)**2 + 1)**2 * (x/2 + 2) * (x/2 - 1) + 2, color=RED, x_range=[-4, 3])
        p_initial_new = Dot(axes.c2p(-4, p.underlying_function(-4)), color=RED)
        p_final_new = Dot(axes.c2p(3, p.underlying_function(3)), color=RED)

        # Nuevas líneas punteadas y actualización de f_c
        f_c_new = MathTex(r"g(c)", color=ORANGE, font_size=40).next_to(Dot(axes.c2p(0,p.underlying_function(3))), LEFT)
        b_point = axes.c2p(3, p.underlying_function(3))
        dotted_line_x_new = DashedLine(start=axes.c2p(3, 0), end=b_point, color=GREEN, stroke_width=4)
        dotted_line_y_new = DashedLine(start=axes.c2p(0, p.underlying_function(3)), end=b_point, color=GREEN, stroke_width=4)

        # Animación de transformación a p
        b_c = MathTex(r"b=c", color=ORANGE, font_size=40).next_to(Dot(axes.c2p(3, 0)), RIGHT).shift(0.25 * DOWN).shift(0.25 * LEFT)
        self.play(
            FadeOut(c),
            ReplacementTransform(b, b_c),
            ReplacementTransform(f, p),
            ReplacementTransform(p_initial, p_initial_new),
            ReplacementTransform(p_final, p_final_new),
            ReplacementTransform(f_c, f_c_new),
            ReplacementTransform(dotted_line_x, dotted_line_x_new),
            ReplacementTransform(dotted_line_y, dotted_line_y_new)
        )
        self.wait(2)

        # Transformación de nuevo a c y b
        c_new = MathTex(r"c", color=ORANGE, font_size=40).next_to(Dot(axes.c2p(2, 0)), RIGHT).shift(0.25 * DOWN).shift(0.25 * LEFT)
        b_new = MathTex(r"b", color=ORANGE, font_size=40).next_to(Dot(axes.c2p(3, 0)), RIGHT).shift(0.25 * DOWN).shift(0.25 * LEFT)

        # Nueva función g
        g = axes.plot(lambda x: 1/2 * abs(x/2 - 1)*(x + 5) -1, color=DARK_BLUE, x_range=[-4, 3])
        p_initial_new_g = Dot(axes.c2p(-4, g.underlying_function(-4)), color=DARK_BLUE)
        p_final_new_g = Dot(axes.c2p(3, g.underlying_function(3)), color=DARK_BLUE)

        # Nuevas líneas punteadas para g
        f_c_new_g = MathTex(r"h(c)", color=ORANGE, font_size=40).next_to(Dot(axes.c2p(0,g.underlying_function(2))), LEFT)
        c_point_new = axes.c2p(2, g.underlying_function(2))
        dotted_line_x_g = DashedLine(start=axes.c2p(2, 0), end=c_point_new, color=GREEN, stroke_width=4)
        dotted_line_y_g = DashedLine(start=axes.c2p(0, g.underlying_function(2)), end=c_point_new, color=GREEN, stroke_width=4)

        # Animación de transformación a g
        self.play(
            FadeIn(c_new),
            ReplacementTransform(b_c, b_new),
            ReplacementTransform(p, g),
            ReplacementTransform(p_initial_new, p_initial_new_g),
            ReplacementTransform(p_final_new, p_final_new_g),
            ReplacementTransform(f_c_new, f_c_new_g),
            ReplacementTransform(dotted_line_x_new, dotted_line_x_g),
            ReplacementTransform(dotted_line_y_new, dotted_line_y_g)
        )
        self.wait(2)

        # Última función r y nueva posición de c
        r = axes.plot(lambda x: 1/10 * (((-1-x)/2)**2 + 1)**2 * ((-1-x)/2 + 2) * ((-1-x)/2 - 1), color=PURPLE, x_range=[-4, 3])
        p_initial_final_r = Dot(axes.c2p(-4, r.underlying_function(-4)), color=PURPLE)
        p_final_final_r = Dot(axes.c2p(3, r.underlying_function(3)), color=PURPLE)

        # Nueva posición de c y líneas punteadas para r
        c_final = MathTex(r"c", color=ORANGE, font_size=40).next_to(Dot(axes.c2p(2.09717, 0)), RIGHT).shift(0.25 * DOWN).shift(0.25 * LEFT)
        f_c_final = MathTex(r"p(c)", color=ORANGE, font_size=40).next_to(Dot(axes.c2p(0,r.underlying_function(2.09717))), LEFT)
        c_point_final = axes.c2p(2.09717, r.underlying_function(2.09717))
        dotted_line_x_r = DashedLine(start=axes.c2p(2.09717, 0), end=c_point_final, color=GREEN, stroke_width=4)
        dotted_line_y_r = DashedLine(start=axes.c2p(0, r.underlying_function(2.09717)), end=c_point_final, color=GREEN, stroke_width=4)

        # Animación final de transformación a r
        self.play(
            ReplacementTransform(g, r),
            ReplacementTransform(p_initial_new_g, p_initial_final_r),
            ReplacementTransform(p_final_new_g, p_final_final_r),
            ReplacementTransform(c_new, c_final),
            ReplacementTransform(f_c_new_g, f_c_final),
            ReplacementTransform(dotted_line_x_g, dotted_line_x_r),
            ReplacementTransform(dotted_line_y_g, dotted_line_y_r)
        )
        self.wait(2)



class E5(Scene):
    def construct(self):

        # Texto inicial
        texto_inicial = Tex(r"$\textbf{Definición}$. Sea $f$ una función definida en un intervalo ", 
                            "$I$ que contiene a $c$. \\",
                            "\\ Se dice que $c$ es un punto crítico de $f$ en el intervalo $I$ cuando se cumple alguna de las siguientes condiciones:",
                            tex_environment="flushleft").scale(0.8).shift(2*UP)    
        
        # Teorema con las viñetas
        teorema = BulletedList(
            r"$c$ es un punto de frontera, es decir, $c$ es uno de los extremos del intervalo.",
            r"$c$ es un punto singular, esto es, $f'(c)$ no existe.",
            r"$c$ es un punto estacionario en caso de que $f'(c)=0$.",
            dot_scale_factor=1.2,  # Tamaño de los puntos
        ).scale(0.8)

        # Alinear el teorema al texto inicial
        teorema.next_to(texto_inicial, DOWN, buff=0.5).align_to(texto_inicial, LEFT)

        # Crear un cuadro amarillo alrededor del texto y el teorema
        cuadro = SurroundingRectangle(
            VGroup(texto_inicial, teorema),
            color=YELLOW,
            buff=0.25
        )

        # Crear un cuadro rojo alrededor de la palabra 'I'
        cuadro_rojo = SurroundingRectangle(texto_inicial[1], color=RED, buff=0.1)

        # Animar el texto y los rectángulos
        self.play(Write(texto_inicial))
        self.play(Create(cuadro))
        self.wait(1)

        # Escribir cada viñeta en blanco y luego cambiar parte a azul
        self.play(Write(teorema[0]))
        self.wait(1)
        self.play(ApplyMethod(teorema[0][30:].set_color, BLUE))
        self.wait(1)
        self.play(Write(teorema[1]))
        self.wait(1)
        self.play(ApplyMethod(teorema[1][27:].set_color, BLUE))
        self.wait(1)
        self.play(Write(teorema[2]))
        self.wait(1)
        self.play(ApplyMethod(teorema[2][34:].set_color, BLUE))
        self.wait(2)
        self.play(Write(cuadro_rojo))
        self.wait(2)



class E6(Scene):
    def construct(self):
        # Crear el texto del teorema 
        teorema = Tex(
            r"\textbf{Teorema.} Sea $f$ una función definida en un intervalo $I$. Si $f(c)$ es un valor extremo de $f$ en $I$, entonces $c$ es un punto crítico de $f$",
            font_size=36
        )        
        # Crear el cuadro alrededor del teorema
        cuadro = SurroundingRectangle(teorema, color=YELLOW, buff=0.5)
        
        # Agrupar teorema y cuadro en un VGroup
        grupo_teorema = VGroup(teorema, cuadro)
        teorema.move_to(cuadro.get_center())
        grupo_teorema_copia=grupo_teorema.copy().shift(UP)
        # Animar la creación del cuadro y el teorema
        self.play(Create(cuadro))
        self.play(Write(teorema))
        self.wait(3)

        # Mover el grupo a la esquina superior izquierda y reducir su tamaño
        self.play(grupo_teorema.animate.scale(0.5).to_edge(UL))
        self.wait(2)

        # Crear la demostración debajo del cuadro, alineada, con tamaño de fuente 36
        demostracion1 = Tex(r"En caso de que", font_size=36).next_to(grupo_teorema, DOWN, aligned_edge=LEFT).shift(DOWN)
        demostracion2 = Tex(r"$c$ sea un extremo de $I$", font_size=36).next_to(demostracion1, DOWN, aligned_edge=LEFT)
        demostracion3 = Tex(r"tenemos que $c$", font_size=36).next_to(demostracion2, DOWN, aligned_edge=LEFT)
        demostracion4 = Tex(r"es un punto fronterizo.", font_size=36).next_to(demostracion3, DOWN, aligned_edge=LEFT)

        demostracion5 = Tex(r"Suponga que $a < c < b$", font_size=36).to_edge(UR).shift(2*DOWN)
        demostracion6 = Tex(r"Luego $f'(c)$ puede o no existir.", font_size=36).next_to(demostracion5, DOWN, aligned_edge=RIGHT)
        demostracion7 = Tex(r"En caso de que $f'(c)$ no exista", font_size=36).next_to(demostracion6, DOWN, aligned_edge=RIGHT)
        demostracion8 = Tex(r"$c$ es un punto singular.", font_size=36).next_to(demostracion7, DOWN, aligned_edge=RIGHT)

        demostracion = VGroup(
            demostracion1, demostracion2, demostracion3, demostracion4,
            demostracion5, demostracion6, demostracion7, demostracion8
        )

        # Animar la escritura de la demostración
        self.play(Write(demostracion[0:4]))
        self.wait(3)
        self.play(Write(demostracion[4:]))
        self.wait(3)

        # Borrar todo excepto el teorema y su cuadro
        self.play(FadeOut(demostracion))
        self.wait(2)

        # Parte difícil de la prueba
        # Texto en la arista izquierda
        izquierda1 = Tex(r"En caso de que $f'(c)$ exista", font_size=36)
        izquierda2 = Tex(r"debemos verificar que", font_size=36)
        izquierda3 = MathTex(r"f'(c)=0.", font_size=36)
        izquierda4 = Tex(r"Supongamos que $f(c)$ es un máximo de $f$,", font_size=36)
        izquierda5 = Tex(r"es decir que: $f(c) \geq f(x)$ para todo $x \in \text{dom } f$.", font_size=36)
        izquierda6= Tex(r"Luego $f(x) - f(c) \leq 0$.", font_size=36)
        grupo_izquierda = VGroup(izquierda1, izquierda2, izquierda3, izquierda4, izquierda5,
                                 izquierda6
                                 ).arrange(DOWN,aligned_edge=LEFT).to_edge(LEFT)

        self.play(
            AnimationGroup(
                *[Write(mobj) for mobj in grupo_izquierda],
                lag_ratio=1  # Ajusta el tiempo de retraso entre las animaciones
            )
        )


        # Texto en la arista derecha 
        derecha2 = Tex(r"Cuando $x < c$, $x - c < 0$", font_size=36)
        #derecha3 = Tex(r"Por lo tanto", font_size=36).next_to(derecha2, DOWN, aligned_edge=RIGHT)
        derecha4 = MathTex(r"\frac{f(x) - f(c)}{x - c} \geq 0", font_size=36)
        derecha5 = Tex(r"lo que implica que:", font_size=36)
        derecha6 = MathTex(r"f'_-(c) = \lim_{x \to c^-} \frac{f(x) - f(c)}{x - c} \geq 0", font_size=36)
        derecha7 = Tex(r"cuando $x > c$, $x - c > 0$", font_size=36)
        derecha8 = MathTex(r"\frac{f(x) - f(c)}{x - c} \leq 0", font_size=36)
        derecha9 = Tex(r"lo que implica que:", font_size=36)
        derecha10 = MathTex(r"f'_+(c) = \lim_{x \to c^+} \frac{f(x) - f(c)}{x - c} \leq 0", font_size=36)
        grupo_derecha = VGroup(
 derecha2, derecha4, derecha5, derecha6, 
            derecha7, derecha8, derecha9, derecha10
        ).arrange(DOWN,aligned_edge=RIGHT).to_edge(RIGHT)

        # Animar el texto de la derecha de forma más gradual
        self.play(
            AnimationGroup(
                *[Write(mobj) for mobj in grupo_derecha],
                lag_ratio=0.5  
            )
        )
        self.wait(2)

        # Borrar el texto de la izquierda
        self.play(FadeOut(grupo_izquierda))
        self.wait(2)

        # Nuevo texto en la izquierda
        izquierda_nueva1 = Tex(r"Pero como $f'(c)$ existe,", font_size=36)
        izquierda_nueva2 = Tex(r"entonces $f'_+(c) = f'_-(c)$ \\ y por tanto:", font_size=36).next_to(izquierda_nueva1, DOWN, aligned_edge=LEFT)
        izquierda_nueva3 = MathTex(r"0 \leq f'_-(c) = f'(c) = f'_+(c) \leq 0", font_size=36).next_to(izquierda_nueva2, DOWN, aligned_edge=LEFT)
        izquierda_nueva4 = Tex(r"por lo tanto $f'(c) = 0$, es decir, \\ $c$ es un punto estacionario.", font_size=36).next_to(izquierda_nueva3, DOWN, aligned_edge=LEFT)

        grupo_izquierda_nueva = VGroup(izquierda_nueva1, izquierda_nueva2, izquierda_nueva3, izquierda_nueva4
                                       ).arrange(DOWN,aligned_edge=LEFT).to_edge(LEFT)

        # Animar el nuevo texto en la izquierda
        self.play(
            AnimationGroup(
                *[Write(mobj) for mobj in grupo_izquierda_nueva],
                lag_ratio=0.5  # Ajusta el tiempo de retraso entre las animaciones
            )
        )

        self.wait(2)
        self.play(FadeOut(grupo_derecha,grupo_izquierda_nueva))
        self.play(Transform(grupo_teorema,grupo_teorema_copia))
        proposicion = Tex(
            r"\textbf{Proposición.} Si $f$ es una función diferenciable en $(a,b)$ y $f(c)$ es un valor extremo de $f$ en $(a,b)$ entonces: $$f'(c)=0$$",
            font_size=36
        ).next_to(grupo_teorema_copia,DOWN,buff=1).align_to(grupo_teorema_copia,ORIGIN)
        cuadro2=SurroundingRectangle(proposicion,buff=0.5,color=YELLOW)
        self.play(Write(proposicion),Create(cuadro2))





class E7(Scene):
    def construct(self):
        # Crear el sistema de coordenadas
        axes = NumberPlane(
            axis_config={"include_numbers": False, "include_tip": False},
        ).scale(2.3)
        
        # Etiquetas de los ejes
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        # Etiquetas para los puntos a, b
        a_label = MathTex(r"a", color=ORANGE, font_size=40).next_to(Dot(axes.c2p(-2, 0)), RIGHT).shift(0.25 * DOWN).shift(0.25 * LEFT)
        b_label = MathTex(r"b", color=ORANGE, font_size=40).next_to(Dot(axes.c2p(2, 0)), RIGHT).shift(0.25 * DOWN).shift(0.25 * LEFT)
        
        # Función f(x) para x < 1
        f_left = axes.plot(lambda x: -x * (x + 1) * (x - 2) / 5, color=YELLOW, x_range=[-2, 1])
        
        # Función f(x) para x >= 1
        f_right = axes.plot(lambda x: 1.4 - x, color=YELLOW, x_range=[1, 2])
        f_label = MathTex(r"f", color=YELLOW).next_to(f_right, UP)

        # Puntos inicial y final
        p_inicial = Dot(axes.c2p(-2, f_left.underlying_function(-2)), color=BLACK,
                        fill_opacity=1, stroke_color=YELLOW, stroke_width=3)
        p_final = Dot(axes.c2p(2, f_right.underlying_function(2)), color=BLACK,
                      fill_opacity=1, stroke_color=YELLOW, stroke_width=3)

        # Añadir los ejes, etiquetas y gráficas
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(f_left), Create(f_right), Create(f_label))
        self.play(Create(p_inicial), Create(p_final))
        self.play(Write(a_label), Write(b_label))
        
        # Calcular c = 1/3 - sqrt(7)/3
        c = (1 / 3 - np.sqrt(7) / 3)
        f_c = -c * (c + 1) * (c - 2) / 5  # Evaluar f(c)
        f_c_label = MathTex(r"f(c)", color=ORANGE, font_size=40).next_to(Dot(axes.c2p(c, f_c)), RIGHT)
        
        # Etiqueta para el punto c
        c_label = MathTex(r"c", color=ORANGE, font_size=40).next_to(Dot(axes.c2p(c, 0)), RIGHT).shift(0.25 * DOWN).shift(0.25 * LEFT)
        c_point = Dot(axes.c2p(c, f_c), color=RED)

        # Añadir línea punteada desde (c, 0) a (c, f(c))
        dashed_line_c = DashedLine(axes.c2p(c, 0), axes.c2p(c, f_c), color=WHITE)
        self.play(Create(dashed_line_c))

        # Recta tangente en (c, f(c))
        tangent_slope = (-3 * c**2 + 2 * c + 2) / 5  # Derivada de f(x)
        tangent_line = axes.plot(
            lambda x: tangent_slope * (x - c) + f_c,
            color=GREEN,
            x_range=[c - 1, c + 1]
        )

        # Punto (1, f(1))
        f_1 = 1.4 - 1  # Evaluar f(1)
        point_at_1 = Dot(axes.c2p(1, f_1), color=RED)
        d_label = MathTex(r"d", color=ORANGE, font_size=40).next_to(Dot(axes.c2p(1, 0)), RIGHT).shift(0.25 * DOWN).shift(0.25 * LEFT)
        
        # Añadir línea punteada desde (d, 0) a (d, f(d))
        dashed_line_d = DashedLine(axes.c2p(1, 0), axes.c2p(1, f_1), color=WHITE)
        self.play(Create(dashed_line_d))

        # Mostrar la recta tangente y los puntos
        self.play(Create(tangent_line), Create(c_point), Write(c_label))
        self.play(Create(point_at_1), Write(d_label))

        self.wait(2)
        
        # Añadir el punto azul (1.5, f_right(1.5))
        x2 = 1.8
        f_x2 = 1.4 - x2  # Evaluar f(x2)
        x2_point = Dot(axes.c2p(x2, f_x2), color=BLUE)
        x2_label = MathTex(r"x_2", color=BLUE, font_size=40).next_to(Dot(axes.c2p(x2,0))).shift(0.25 * DOWN).shift(0.25 * LEFT)
        
        # Añadir línea punteada desde (x2, 0) a (x2, f(x2))
        dashed_line_x2 = DashedLine(axes.c2p(x2, 0), axes.c2p(x2, f_x2), color=WHITE)
        
        # Mostrar el punto x2, su etiqueta y la línea punteada
        self.play(Create(x2_point), Write(x2_label))
        self.play(Create(dashed_line_x2))
        
        # Mostrar cuadro de texto que indique f(x_2) < f(c)
        comparison_text = MathTex(r"f(x_2) < f(c)", color=WHITE, font_size=40)
        comparison_box = SurroundingRectangle(comparison_text, color=BLACK, buff=0.2, fill_opacity=0.8)
        comparison_text_group = VGroup(comparison_box, comparison_text).to_edge(UP + RIGHT)
        self.play(Create(comparison_text_group))
        
        # Esperar un momento
        self.wait(2)
        
        # Borrar el punto x2, su etiqueta, línea punteada y cuadro de texto
        self.play(FadeOut(x2_point), FadeOut(x2_label), FadeOut(dashed_line_x2), FadeOut(comparison_text_group))

        # Esperar después de eliminar los elementos anteriores
        self.wait(2)

        # Añadir el punto en (x1, f_left(x1)) con x1 = -1.5
        x1 = -1.8
        f_x1 = -x1 * (x1 + 1) * (x1 - 2) / 5  # Evaluar f(x1) en el primer segmento
        x1_point = Dot(axes.c2p(x1, f_x1), color=BLUE)
        x1_label = MathTex(r"x_1", color=BLUE, font_size=40).next_to(Dot(axes.c2p(x1,0))).shift(0.25 * DOWN).shift(0.25 * LEFT)
        
        # Añadir línea punteada desde (x1, 0) a (x1, f(x1))
        dashed_line_x1 = DashedLine(axes.c2p(x1, 0), axes.c2p(x1, f_x1), color=WHITE)
        
        # Mostrar el punto x1, su etiqueta y la línea punteada
        self.play(Create(x1_point), Write(x1_label))
        self.play(Create(dashed_line_x1))
        
        # Mostrar cuadro de texto que indique f(x_1) > f(d)
        comparison_text_x1 = MathTex(r"f(x_1) > f(d)", color=WHITE, font_size=40)
        comparison_box_x1 = SurroundingRectangle(comparison_text_x1, color=BLACK, buff=0.2, fill_opacity=0.8)
        comparison_text_group_x1 = VGroup(comparison_box_x1, comparison_text_x1).to_edge(UP + RIGHT)
        self.play(Create(comparison_text_group_x1))
        
        # Esperar un momento
        self.wait(2)
        
        # Borrar el punto x1, su etiqueta, línea punteada y cuadro de texto
        self.play(FadeOut(x1_point), FadeOut(x1_label), FadeOut(dashed_line_x1), FadeOut(comparison_text_group_x1))




