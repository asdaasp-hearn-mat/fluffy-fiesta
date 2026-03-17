from manim import *

class E1(Scene):
    def construct(self):    
        axes = NumberPlane()
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        func = lambda x: (x-2)**2-1
        gunc = lambda x: (x-2)**3-1
        f = axes.plot(func, color = RED)
        g = axes.plot(gunc, color = RED)
        
        
        dot = Dot(axes.c2p(2,-1))
        a = MathTex(r"a").next_to(dot, DOWN)    
        hyp = Tex(r"Si ", r"$f'(a)$", r"=", r"0", r" $f(a)$", r" es un " , r"mínimo.").to_edge(UL)
        hyp1 = Tex(r"Si ", r"$f'(a)$", r"=", r"0", r" $f(a)$", r" es un " , r"máximo.").next_to(hyp, DOWN, buff =1)
        hyp2 = Tex(r"Si ", r"$f'(a)$", r"=", r"0", r" $f(a)$", r" es... " , r"algo distinto.").next_to(hyp1, DOWN, buff =1).align_to(hyp1, LEFT)
        linea = Line(axes.c2p(2,-1), axes.c2p(3,-1), color = YELLOW).set_length(20)
        box = SurroundingRectangle(hyp2)
        sec1 = Line(axes.c2p(2,-1), axes.c2p(0.5, gunc(0.5)), color = ORANGE)
        g1 = axes.plot(gunc, x_range = [0.5,2], color = ORANGE)
        cambio = Tex(r"$f$ es cóncava para $x<a$").to_edge(UR)
        ambio = Tex(r"$f$ es convexa para $x<a$").to_edge(UR)
        sec2 = Line(axes.c2p(2,-1), axes.c2p(3.5, gunc(3.5)), color = GREEN)
        g2 = axes.plot(gunc, x_range = [2, 3.5], color = GREEN)
        cambio1 = Tex(r"$f$ es convexa para $x>a$").next_to(cambio, DOWN)
        ambio1 = Tex(r"$f$ es cóncava para $x>a$").next_to(cambio, DOWN)
        
        self.add(axes, axes_labels, g, hyp, hyp1, hyp2, dot, a, linea)
        self.wait()
        self.play(Create(box))
        self.play(FadeOut(linea))
        self.wait()
        self.play(Create(sec1))
        self.play(Create(g1))
        self.play(FadeIn(BackgroundRectangle(cambio)))
        self.play(Write(cambio))
        self.wait(2)
        self.play(Create(sec2))
        self.play(Create(g2))
        self.play(FadeIn(BackgroundRectangle(cambio1)))
        self.play(Write(cambio1))
        self.wait(2)    
        self.play(Rotate(VGroup(g, g1, g2, sec1, sec2), angle = TAU/2, axis = [0,1,0]))
        self.play(VGroup(g, g1, g2, sec1, sec2).animate.shift(4*RIGHT))
        self.play(ReplacementTransform(cambio, ambio), ReplacementTransform(cambio1, ambio1))
        self.wait()
class E2(Scene):
    def construct(self):        
        defo = Tex(r"\textbf{Definición}. (\textit{Punto de inflexión}.) Dada una función $f$ deinida en un intervalo, \\ se dice que $a$ es un punto de inflexión si $f(x)$ es cóncava para $x<a$ y convexa para $x>a$ o \\ $f(x)$ es convexa para $x<a$ y cóncava para $x>a$", font_size =36)
        nota = Tex(r"\textbf{NOTA}: $f'(a)$ no necesita ser 0, de hecho, ni necesita existir", font_size = 24).next_to(defo, DOWN, buff = 1).align_to(defo, LEFT)
        self.play(Create(SurroundingRectangle(defo)))
        self.play(Write(defo), run_time = 3)
        self.wait()
        self.play(Write(nota))
        self.wait(2)

class E3(Scene):
    def construct(self):
        axes = NumberPlane()
        func = lambda t: np.arctan(t)
        f = axes.plot(func, color = RED)
        a = Dot(axes.c2p(0,0))
        a_label = MathTex(r"a").next_to(a, DOWN)
        ffpos = MathTex(r"f''>0", color = ORANGE).shift(2*LEFT+1*UP)
        f1 = axes.plot(func, color = ORANGE, x_range = [-1,-0.01])
        ffneg = MathTex(r"f''<0", color = GREEN).shift(2*RIGHT+1*UP)
        f2 = axes.plot(func, color = GREEN, x_range = [0.01,1])        
        self.add(axes)
        self.play(Create(f))
        self.play(FadeIn(VGroup(a, a_label)))
        self.wait()
        self.play(Create(f1))
        self.play(Create(BackgroundRectangle(ffpos)))
        self.play(Write(ffpos))
        self.wait()
        self.play(Create(f2))
        self.play(Create(BackgroundRectangle(ffneg)))
        self.play(Write(ffneg))
        self.wait()        

class E4(Scene):
    def construct(self):        
        teo = Tex(r"\textbf{Teorema}. Dada una función $f$ dos veces derivable deinida en un intervalo, \\ si $f''$ cambia de signo alrededor de un punto $a$, entonces $a$ es un punto de inflexión.", font_size =36)
        
        self.play(Create(SurroundingRectangle(teo)))
        self.play(Write(teo), run_time = 2.5)
        self.wait()
        
        
        
class PruebaPatrick(Scene):
    def construct(self):    
        axes = NumberPlane()
        f = axes.plot(lambda t: t, x_range = [-4,4],color = RED)
        vg = VGroup(axes, f)
        cosa = Tex(r"$\delta>0$").to_edge(UR)
        
        self.wait()
        self.play(Create(axes))
        self.wait()
        self.play(Create(f))
        self.wait()
        #self.play(vg.animate.scale(0.25).to_edge(UL).shift(LEFT))
        self.wait()
        self.play(FadeIn(BackgroundRectangle(cosa)))
        self.play(FadeIn(cosa))
        self.wait()
        self.play(FadeOut(cosa))
        self.wait()
        self.play(Write(cosa))
        self.wait()