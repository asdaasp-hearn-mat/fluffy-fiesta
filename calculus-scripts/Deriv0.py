from manim import *

def disc(axes, *point, color = WHITE):
    c= Circle(radius=0.08, color = BLACK, fill_opacity=1, stroke_width = 1).move_to(axes.c2p(point[0], point[1]))
    d= Circle(radius=0.08, color = color, stroke_width = 1.2).move_to(axes.c2p(point[0], point[1]))
    return VGroup(c,d)

def pp(axes, *point, color = WHITE):
    pl = MathTex(r"(", color = color).move_to(axes.c2p(point[0], point[1]))
    pr = MathTex(r")", color = color).move_to(axes.c2p(point[0], point[1]))
    return VGroup(pl,pr)

def sampling_points(a,b, n_points, axes, f, scaleF = 1):
    p = np.linspace(a, b, n_points)
    return VGroup(*[Dot(axes.c2p(x,0)).scale(scaleF) for x in p]), VGroup(*[axes.get_lines_to_point(axes.input_to_graph_point(x, f)) for x in p]), [axes.input_to_graph_point(x, f) for x in p]    
    
class E1(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-10, 15],
            x_length = 17,
            y_range=[-5, 25],
            y_length = 10,
           
            axis_config={"include_numbers": False, "include_tip": False},
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")

        
        func = lambda x: ((1/10000)*x**5+(1/100)*x**3+(1/200)*x-3)**2
        dfunc = lambda x: ((10 + 60*x**2 + x**4)*(-30000 + 50*x + 100*x**3 + x**5))/10000000
        f = axes.plot(
         func, color = BLUE
        )
        
        t = ValueTracker(0)
        tang = lambda s: dfunc(t.get_value())*(s-t.get_value())+func(t.get_value()) 
        deriv = always_redraw(
            lambda : axes.plot(tang, color = YELLOW)
        )
        
        initial_point = [axes.coords_to_point(t.get_value(), func(t.get_value()))]
        dot = Dot(point=initial_point, color = ORANGE)

        dot.add_updater(lambda x: x.move_to(axes.c2p(t.get_value(), func(t.get_value()))))
        x_0 = always_redraw(
            lambda: MathTex(r"x_0", color = ORANGE).move_to(axes.c2p(t.get_value(), 0)+ 0.33*LEFT)
        )
        l = always_redraw( 
                lambda: DashedLine(axes.c2p(t.get_value(), 0),axes.c2p(t.get_value(), func(t.get_value())), color = ORANGE)
        )
        #deriv = always_redraw(
        #        lambda: TangentLine(f, alpha = f.proportion_from_point(axes.c2p(t.get_value(), func(t.get_value()))), color = YELLOW, length = 15)
        #        )
        
        
        x_space = np.linspace(*axes.x_range[:2],200)
        minimum_index = func(x_space).argmin()
        a = Dot(axes.c2p(x_space[minimum_index], 0), color = RED)
        a_label = MathTex(r"a", color = RED).next_to(a, DOWN)
        
        equis1 = MathTex(r"x_0", r":=", r"x_0", r"+", r"h", r"\cdot", r"G").to_edge(UR)
        equis2 = MathTex(r"x_0", r":=", r"x_0", r"+", r"h", r"\cdot", r"f'(x_0)").to_edge(UR)
        ge = Tex(r"G: La dirección en la que $f$ disminuye.", font_size = 24).next_to(equis1, DOWN)
        ge1 = Tex(r"$f'(x_0)$: La dirección en la que $f$ disminuye.", font_size = 24).next_to(equis1, DOWN)
        h = always_redraw(
            lambda: Arrow(start = dot.get_center(), end = dot.get_center()+RIGHT)
        )
        hf = always_redraw(
            lambda: Arrow(start = dot.get_center(), end = dot.get_center() + LEFT)
        )
        s = ValueTracker(7.5)
        dl = always_redraw(
            lambda: DashedLine(start = axes.c2p(0, -0.5),end= axes.c2p(s.get_value(), -0.5))
        )
        initial_point1 = [axes.coords_to_point(s.get_value(), func(s.get_value()))]
        dot1 = Dot(point=initial_point, color = YELLOW)

        dot1.add_updater(lambda x: x.move_to(axes.c2p(s.get_value(), func(s.get_value()))))
        x_0h = always_redraw(
            lambda: MathTex(r"x_0+h", color = YELLOW).move_to(axes.c2p(s.get_value(), 0)+ 0.33*RIGHT)
        )
        l2 = always_redraw( 
                lambda: DashedLine(axes.c2p(s.get_value(), 0),axes.c2p(s.get_value(), func(s.get_value())), color = YELLOW)
        )
        comp1 = MathTex(r"f(x_0)", r"\leq", r"f(x_0+h)").next_to(ge, DOWN)
        comp1[0].set_color(ORANGE)
        comp1[-1].set_color(YELLOW)
        cross = Cross().scale(0.25).next_to(comp1, LEFT)
        circ = Circle(radius = 0.25, color = GREEN, stroke_width = 8).move_to(cross.get_center())
        smol = Tex(r"Queremos que $h$ sea pequeño.", font_size = 24).next_to(comp1, DOWN)
        x_space = np.linspace(*axes.x_range[:2],200)
        minimum_index = func(x_space).argmin()
        a = Dot(axes.c2p(x_space[minimum_index], 0), color = RED)
        a_label = MathTex(r"a", color = RED).next_to(a, DOWN)
        
        
        
        self.add(
           axes,
           axes_labels,
           f,
           a,
           a_label,
           dot,
           x_0,
            l,
            equis1,
            ge    
        )
        
        self.wait(2)
        self.play(ReplacementTransform(equis1, equis2), ReplacementTransform(ge, ge1))
        self.play(t.animate.set_value(x_space[minimum_index]), run_time = 5, rate_func = there_and_back)
        self.wait()
        self.play(Create(deriv))
        self.wait() 
        self.play(t.animate.set_value(x_space[minimum_index]), run_time = 3)
        self.play(ReplacementTransform(deriv, axes.plot(lambda s: 0, color = YELLOW)))
        self.wait()
        
class E2(Scene):
    def construct(self):    
        axes = NumberPlane()
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")

        func = lambda x: (x-2)**2-1
        gunc = lambda x: (x-2)**3-1
        f = axes.plot(func, color = RED)
        g = axes.plot(gunc, color = RED)
        fc = f.copy()
        t= ValueTracker(0)
        tang = always_redraw(
                lambda : axes.plot(lambda x: (2*(t.get_value()-2)*(x-t.get_value())) + func(t.get_value()), color = YELLOW)
        )
        dot = always_redraw(
                lambda: Dot(axes.c2p(t.get_value(), func(t.get_value()))))
        a = always_redraw(
                lambda: MathTex(r"a").next_to(dot, DOWN)
                )        
        hyp = Tex(r"Si ", r"$f'(a)$", r"=", r"0", r" $f(a)$", r" es un " , r"mínimo.").to_edge(UL)
        hyp1 = Tex(r"Si ", r"$f'(a)$", r"=", r"0", r" $f(a)$", r" es un " , r"máximo.").next_to(hyp, DOWN, buff =1)
        hyp2 = Tex(r"Si ", r"$f'(a)$", r"=", r"0", r" $f(a)$", r" es... " , r"algo distinto.").next_to(hyp1, DOWN, buff =1).align_to(hyp1, LEFT)
        questao = Tex(r"¿Cómo sabemos si $f(a)$ es máximo o mínimo?").next_to(hyp2, DOWN, buff = 1).align_to(hyp1, LEFT)
        
        self.add(axes, axes_labels)
        self.play(Create(f))
        self.wait()
        self.play(Create(tang))
        self.play(FadeIn(VGroup(dot, a)))
        self.wait()
        self.play(t.animate.set_value(2), run_time = 4)
        self.wait()
        self.play(Create(BackgroundRectangle(hyp)))
        self.play(Write(hyp))
        self.wait()
        self.play(Rotate(f, angle= PI, about_point = axes.c2p(t.get_value(), func(t.get_value()))))
        self.wait()
        self.play(Create(BackgroundRectangle(hyp1)))
        self.play(ReplacementTransform(hyp.copy(), hyp1))
        self.wait()
        self.play(ReplacementTransform(f, g))
        self.wait()
        self.play(Create(BackgroundRectangle(hyp2)))
        self.play(ReplacementTransform(hyp1.copy(), hyp2))
        self.wait(2)
        self.play(Create(SurroundingRectangle(VGroup(hyp, hyp1))))
        self.wait()
        self.play(ReplacementTransform(g, fc))
        self.play(fc.copy().animate.set_color(BLUE).rotate(PI, about_point = axes.c2p(2, func(2))))
        self.wait()
        self.play(Create(BackgroundRectangle(questao)))
        self.wait()
        self.play(Write(questao))
        self.wait() 

class E3(Scene):
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
        derecha = Tex(r"$f$ Decrece").next_to(eme, DOWN)
        emedos = MathTex(r"m", r">", r"0", tex_to_color_map = {r"m": RED}).next_to(derecha, DOWN)
        izquierda = Tex(r"$f$ Crece.").next_to(emedos, DOWN)
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

class E4(Scene):
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
        texto = Tex(r"Si", r"$f'(a)$", r"$<$", r"$0$", r", " , "$f$", r" Decrece").to_edge(UL)
        texto1 = Tex(r"Si", r"$f'(a)$", r"$>$", r"$0$", r", " , "$f$", r" Crece").next_to(texto, DOWN, buff = 2)
        
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

class E5(Scene):
    def construct(self):
        teo = Tex(r"\textbf{Teorema} (\textit{criterio de la derivada}) Sea $f$ una función diferenciable en $(a,b)$, entonces Si $f'(x) > 0$ para todo $x \in (a,b)$, entonces, $f$ es creciente en $(a,b)$. Si $f'(x) < 0$ para todo $x \in (a,b)$, entonces, $f$ es decreciente en $(a,b)$.", font_size = 30)
        
        self.play(Create(SurroundingRectangle(teo)))
        self.play(Write(teo), run_time = 3)
        self.wait(2)
        