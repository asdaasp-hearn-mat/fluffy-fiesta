from manim import *

# HELPERS FOR COMPLEX SCENES, you can always create your own :)
def get_horizontal_line_to_graph(axes, function, x, width, color):
    result = VGroup()
    line = DashedLine(
        start=axes.c2p(0, function.underlying_function(x)),
        end=axes.c2p(x, function.underlying_function(x)),
        stroke_width=width,
        stroke_color=color,
    )
    dot = Dot().set_color(color).move_to(axes.c2p(x, function.underlying_function(x)))
    result.add(line, dot)
    return result


def get_arc_lines_on_function(
    graph, plane, dx=1, line_color=WHITE, line_width=1, x_min=None, x_max=None
):

    dots = VGroup()
    lines = VGroup()
    result = VGroup(dots, lines)

    x_range = np.arange(x_min, x_max, dx)
    colors = color_gradient([BLUE_B, GREEN_B], len(x_range))

    for x, color in zip(x_range, colors):
        p1 = Dot().scale(0.7).move_to(plane.input_to_graph_point(x, graph))
        p2 = Dot().scale(0.7).move_to(plane.input_to_graph_point(x + dx, graph))
        dots.add(p1, p2)
        dots.set_fill(colors, opacity=0.8)

        line = Line(
            p1.get_center(),
            p2.get_center(),
            stroke_color=line_color,
            stroke_width=line_width,
        )
        lines.add(line)

    return result

class E1(Scene):
    def construct(self):
        axes = NumberPlane()
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        func = lambda t: t**2
        f1 = axes.plot(func, color = RED)
        f1_label = MathTex(r"f", color = RED).next_to(Dot(axes.c2p(1.2, func(1.2))), RIGHT)
        r = ValueTracker(-1.5)
        rt = lambda t: 2*r.get_value()*(t-r.get_value())+func(r.get_value())
        
        tang = always_redraw(
               lambda: axes.plot(rt, color = YELLOW)
               )
        tp = always_redraw(
                lambda: Dot(axes.c2p(r.get_value(), func(r.get_value())))
                )       
        a = Dot(axes.c2p(0,0))
        a_label = MathTex(r"a").next_to(a, RIGHT).shift(0.5*DOWN)
        t1 = TangentLine(f1, alpha = f1.proportion_from_point(axes.c2p(-1,1)), color = YELLOW).set_length(15)
        p1 = Dot(axes.c2p(-1,1))
        t2 = TangentLine(f1, alpha = f1.proportion_from_point(axes.c2p(0,0)), color = YELLOW).set_length(15)
        p2 = Dot(axes.c2p(0,0))
        t3 = TangentLine(f1, alpha = f1.proportion_from_point(axes.c2p(1,1)), color = YELLOW).set_length(15)
        p3 = Dot(axes.c2p(1,1))
        ts = VGroup(VGroup(t1, p1), VGroup(t2, p2), VGroup(t3, p3))
        t1_label = MathTex(r"f'<0").next_to(p1, LEFT).shift(0.25*DOWN)
        t2_label = MathTex(r"f'=0").next_to(p2, UP)
        t3_label = MathTex(r"f'>0").next_to(p3, RIGHT).shift(0.25*DOWN)
        texto = Tex(r"$f'$ va de valores negativos \\ a valores positivos.", font_size = 30).to_edge(UR)
        texto2 = Tex(r"Esto significa que \\ $f'$ es \textbf{creciente}.", font_size = 30).next_to(texto, DOWN)
        
        self.add(axes, axes_labels)
        self.play(Create(f1), Write(f1_label))
        self.wait()
        self.play(FadeIn(VGroup(a, a_label)))
        self.wait(2)
        self.play(Create(tang), FadeIn(tp))
        self.play(r.animate.set_value(1.5), run_time = 5)
        self.wait()
        self.play(FadeOut(VGroup(tang, tp)))
        self.wait()
        self.play(AnimationGroup([Create(i) for i in ts], lag_ratio = 1))
        self.wait()
        self.play(AnimationGroup([Write(i) for i in VGroup(t1_label, t2_label, t3_label)], lag_ratio = 1))
        self.wait()
        self.play(Create(BackgroundRectangle(texto)))
        self.play(Write(texto))
        self.wait()
        self.play(Create(BackgroundRectangle(texto2)))
        self.play(Write(texto2))
        self.wait()

class E2(Scene):
    def construct(self):

        k = ValueTracker(-3)  # Tracking the end values of stuff to show

        # Adding Mobjects for the first plane
        plane1 = (
            NumberPlane(x_range=[-3, 4, 1], x_length=5, y_range=[-8, 9, 2], y_length=5)
            
            .shift(LEFT * 3.5)
        )
        axes_labels1 = plane1.get_axis_labels(x_label="x", y_label="y").scale(0.75)
        axes_labels1[0].shift(1*DOWN*plane1.get_y_unit_size())
        axes_labels1[1].shift(0.5*LEFT*plane1.get_x_unit_size())
        func1 = plane1.plot(
            lambda x:  x ** 2, x_range=[-3, 3], color=RED_C
        )
        func1_lab = (
            MathTex(r"f(x)= {x}^{2}")
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
        plane2 = (
            NumberPlane(x_range=[-3, 4, 1], x_length=5, y_range=[-8, 9, 2], y_length=5)
            
            .shift(RIGHT * 3.5)
        )
        axes_labels2 = plane2.get_axis_labels(x_label="x", y_label="y").scale(0.75)
        axes_labels2[0].shift(1*DOWN*plane2.get_y_unit_size())
        axes_labels2[1].shift(0.5*LEFT*plane2.get_x_unit_size())

        func2 = always_redraw(
            lambda: plane2.plot(
                lambda x: 2*x, x_range=[-3, k.get_value()], color=GREEN
            )
        )
        func2_lab = (
            MathTex("f'(x)=2x")
            .set(width=2.5)
            .next_to(plane2, UP, buff=0.2)
            .set_color(GREEN)
        )

        moving_h_line = always_redraw(
            lambda: get_horizontal_line_to_graph(
                axes=plane2, function=func2, x=k.get_value(), width=4, color=YELLOW
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
        down = Tex(r"$f'$", r" Es creciente.").to_edge(DOWN)
        down[0].set_color(GREEN)
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
        self.play(Write(down))
        self.wait()
        
class E3(Scene):
    def construct(self):
        pc = Tex(r"Puntos clave", color = YELLOW).scale(2).to_edge(UP)
        p1 = Tex(r"- $f'$ va de valores negativos a valores positivos.").shift(UP)
        p2 = Tex(r"- $f'$ es creciente.")
        p3 = Tex(r"- Por el criterio de la derivada, la derivada de \\ $f'$ (de existir) es positiva.")
        
        dd = Tex(r"La derivada de la derivada?", color = RED).to_edge(DOWN)
        
        self.play(Write(pc))
        self.wait()
        self.play(AnimationGroup([Write(p) for p in VGroup(p1, p2, p3).arrange(direction=DOWN, aligned_edge=LEFT)], lag_ratio = 2))
        self.wait(2)
        self.play(Write(dd))
        self.wait()    

class E4(Scene):
    def construct(self):
        defo = Tex(r"\textbf{Definición}. (\textit{Segunda derivada}) Sea $f$ una función cuya derivada $f'$ es derivable. \\ Si la derivada de $f'$ existe, se la llama la \textit{segunda derivada} de $f$ y se denota como $f'', f^{(2)}, \frac{d^2 f}{dx^2}$ o $D^2_x f$. \\ Y se dice que $f$ es dos veces derivable."
        , font_size= 30)
        
        self.play(Create(SurroundingRectangle(defo)))
        self.play(Write(defo), run_time = 4)
        self.wait()

class E5(Scene):
    def construct(self):        
        teo = Tex(r"\textbf{Teorema. } (\textit{Criterio de la segunda derivada para mínimos}) Sea $f$ una función dos veces derivable en $a$ tal que $f'(a)=0$ y $f''(a)>0$ \\ Entonces $f$ tiene un mínimo en $a$."
            , font_size = 30)
        
        self.play(Create(SurroundingRectangle(teo)))
        self.play(Write(teo), run_time =4 )
        self.wait()

class E6(Scene):
    def construct(self):
        axes = NumberPlane()
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        func = lambda t: 2*np.cos(t)
        f1 = axes.plot(func, color = RED)
        f1_label = MathTex(r"f", color = RED).next_to(Dot(axes.c2p(1.2, func(1.2))), RIGHT)
        r = ValueTracker(-PI/2)
        rt = lambda t: -2*np.sin(r.get_value())*(t-r.get_value())+func(r.get_value())
        
        tang = always_redraw(
               lambda: axes.plot(rt, color = YELLOW)
               )
        tp = always_redraw(
                lambda: Dot(axes.c2p(r.get_value(), func(r.get_value())))
                )       
        a = Dot(axes.c2p(0,2))
        a_label = MathTex(r"a").next_to(a, RIGHT).shift(0.5*DOWN)
        t1 = TangentLine(f1, alpha = 0.4, color = YELLOW).set_length(15)
        p1 = Dot(f1.point_from_proportion(0.4))
        t2 = TangentLine(f1, alpha = 0.5, color = YELLOW).set_length(15)
        p2 = Dot(axes.c2p(0,2))
        t3 = TangentLine(f1, alpha = 0.6, color = YELLOW).set_length(15)
        p3 = Dot(f1.point_from_proportion(0.6))
        ts = VGroup(VGroup(t1, p1), VGroup(t2, p2), VGroup(t3, p3))
        t1_label = MathTex(r"f'>0").next_to(p1, LEFT).shift(0.25*DOWN)
        t2_label = MathTex(r"f'=0").next_to(p2, UP)
        t3_label = MathTex(r"f'<0").next_to(p3, RIGHT).shift(0.25*DOWN)
        texto = Tex(r"$f'$ va de valores positivos \\ a valores negativos.", font_size = 30).to_edge(UR)
        texto2 = Tex(r"Esto significa que \\ $f'$ es \textbf{decreciente}.", font_size = 30).next_to(texto, DOWN)
        
        self.add(axes, axes_labels)
        self.play(Create(f1), Write(f1_label))
        self.wait()
        self.play(FadeIn(VGroup(a, a_label)))
        self.wait(2)
        self.play(Create(tang), FadeIn(tp))
        self.play(r.animate.set_value(PI/2), run_time = 5)
        self.wait()
        self.play(FadeOut(VGroup(tang, tp)))
        self.wait()
        self.play(AnimationGroup([Create(i) for i in ts], lag_ratio = 1))
        self.wait()
        self.play(AnimationGroup([Write(i) for i in VGroup(t1_label, t2_label, t3_label)], lag_ratio = 1))
        self.wait()
        self.play(Create(BackgroundRectangle(texto)))
        self.play(Write(texto))
        self.wait()
        self.play(Create(BackgroundRectangle(texto2)))
        self.play(Write(texto2))
        self.wait()

class E7(Scene):
    def construct(self):

        k = ValueTracker(-PI/2)  # Tracking the end values of stuff to show

        # Adding Mobjects for the first plane
        plane1 = (
            NumberPlane(x_range=[-3, 4, 1], x_length=5, y_range=[-8, 9, 2], y_length=5)
            
            .shift(LEFT * 3.5)
        )
        axes_labels1 = plane1.get_axis_labels(x_label="x", y_label="y").scale(0.75)
        axes_labels1[0].shift(1*DOWN*plane1.get_y_unit_size())
        axes_labels1[1].shift(0.5*LEFT*plane1.get_x_unit_size())
        func1 = plane1.plot(
            lambda x:  2*np.cos(x), x_range=[-3, 3], color=RED_C
        )
        func1_lab = (
            MathTex(r"f(x)= 2\cos(x)")
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
        plane2 = (
            NumberPlane(x_range=[-3, 4, 1], x_length=5, y_range=[-8, 9, 2], y_length=5)
            
            .shift(RIGHT * 3.5)
        )
        axes_labels2 = plane2.get_axis_labels(x_label="x", y_label="y").scale(0.75)
        axes_labels2[0].shift(1*DOWN*plane2.get_y_unit_size())
        axes_labels2[1].shift(0.5*LEFT*plane2.get_x_unit_size())

        func2 = always_redraw(
            lambda: plane2.plot(
                lambda x: -2*np.sin(x), x_range=[-PI/2-0.01, k.get_value()], color=GREEN
            )
        )
        func2_lab = (
            MathTex("f'(x)=-2\mathrm{sen}(x)")
            .set(width=2.5)
            .next_to(plane2, UP, buff=0.2)
            .set_color(GREEN)
        )

        moving_h_line = always_redraw(
            lambda: get_horizontal_line_to_graph(
                axes=plane2, function=func2, x=k.get_value(), width=4, color=YELLOW
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
        down = Tex(r"$f'$", r" Es decreciente.").to_edge(DOWN)
        down[0].set_color(GREEN)
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
        self.play(k.animate.set_value(PI/2), run_time=15, rate_func=linear)
        self.wait()
        self.play(Write(down))
        self.wait()        

class E8(Scene):
    def construct(self):        
        teo = Tex(r"\textbf{Teorema. } (\textit{Criterio de la segunda derivada para máximos}) Sea $f$ una función dos veces derivable en $a$ tal que $f'(a)=0$ y $f''(a)<0$ \\ Entonces $f$ tiene un máximo en $a$."
            , font_size = 30)
        
        self.play(Create(SurroundingRectangle(teo)))
        self.play(Write(teo), run_time =4 )
        self.wait()        