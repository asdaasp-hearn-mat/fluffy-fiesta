from manim import *
from scipy.special import legendre

def disc(axes, *point):
    c= Circle(radius=0.08, color = BLACK, fill_opacity=1, stroke_width = 1).move_to(axes.c2p(point[0], point[1]))
    d= Circle(radius=0.08, color = WHITE, stroke_width = 1.2).move_to(axes.c2p(point[0], point[1]))
    return VGroup(c,d)




class E1(Scene):
    def construct(self):
        axes = Axes(x_range=(-1,10,1),
                  y_range=(-1,20,1),
                  axis_config={"include_numbers": False, "include_tip": False}).shift(0.5*LEFT)
        axes_labels = axes.get_axis_labels(x_label="tiempo", y_label="precio")
        x = np.arange(2,6.5,0.2,dtype=float)
        y = np.array([2*(i-4)**2 +6 + 0.5*rd.random()*rd.choice([1,-1]) for i in x])
        
        baja = VGroup(*[Dot(axes.c2p(_x,_y), color=RED) for _x,_y in zip(x[x<=4],y[x<=4])])
        sube = VGroup(*[Dot(axes.c2p(_x,_y), color=BLUE) for _x,_y in zip(x[x>4],y[x>4])])
        f = lambda x: 2*(x-4)**2+6
        efe = axes.plot(f, color = ORANGE, x_range = [2,4])
        efe2 = axes.plot(f, color = GREEN, x_range = [4,6.5])
        motto = Tex(r"'" , r"Comprar barato", r", ", r"vender caro'").to_edge(UP)
        lines = axes.get_lines_to_point(axes.c2p(3, f(3)), color = YELLOW)
        inver = Tex(r"Inversión", font_size = 24).next_to(Dot(axes.c2p(3, 0)), DOWN)
        lines2 = axes.get_lines_to_point(axes.c2p(5.8, f(5.8)), color = YELLOW)
        retiro = Tex(r"Retiro", font_size = 24).next_to(Dot(axes.c2p(5.8, 0)), DOWN)       
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
        f1 = axes.plot(lambda t: (t-5)**2, color = BLUE)
        f2 = axes.plot(lambda t: (t-5)**4, color = BLUE)
        f3 = axes.plot(lambda t: 5*abs(t-5), color = BLUE)
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
        teo = Tex(r"\textbf{Definición}. Se dice que $f$ es \textbf{convexa} en un intervalo $I$ \\si dados $a<x<$b$ en $I$, se cumple que: $$\frac{f(x)-f(a)}{x-a} < \frac{f(b)-f(a)}{b-a}$$", font_size = 36)
        self.play(Create(SurroundingRectangle(teo)))
        self.play(Write(teo), run_time = 3)
        self.wait()
class E4(Scene):
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
      
        l1 = DashedLine(axes.c2p(-1.5, func(-1.5)), axes.c2p(-1.5,0), color = YELLOW)
        l2 = DashedLine(axes.c2p(1.5, func(1.5)), axes.c2p(1.5,0), color = YELLOW)
        a = Dot(axes.c2p(-1.5,0))
        a_label = Tex(r"a", color = RED).next_to(a, DOWN)
        b = Dot(axes.c2p(1.5,0))
        b_label = Tex(r"b", color = RED).next_to(b, DOWN) 
        fprim = Tex(r"Si f es diferenciable \\ f' es creciente", font_size = 36).shift(5*RIGHT)
        fprimprim = Tex(r"Si f' es diferenciable \\ f'' es positivo", font_size = 36).next_to(fprim, DOWN)
        
        self.add(axes, axes_labels)
        self.play(Create(f1), Write(f1_label))
        self.play(Create(VGroup(l1, l2)))
        self.play(FadeIn(VGroup(a, a_label)))
        self.play(FadeIn(VGroup(b, b_label))) 
 
        self.wait(2)
        self.play(Create(tang), FadeIn(tp))
        self.play(r.animate.set_value(1.5), run_time = 5)
        self.wait()
        self.play(Create(BackgroundRectangle(fprim)))
        self.play(Write(fprim))
        self.wait()
        self.play(Create(BackgroundRectangle(fprimprim)))
        self.play(Write(fprimprim))        
        self.wait()

class E5(Scene):
    def construct(self):        
        teo = Tex(r"\textbf{Teorema}. Si $f$ es diferenciable y $f'$ es creciente en $I$. \\ Entonces, $f$ es convexa en $I$.", font_size = 36).shift(UP)
        teo2 = Tex(r"\textbf{Teorema}. Si $f$ es dos veces diferenciable y $f''$ es positiva. \\ Entonces, $f$ es convexa.", font_size = 36).next_to(teo)
        self.play(Create(SurroundingRectangle(teo)))
        self.play(Write(teo), run_time =3)
        self.wait()
        self.play(Create(SurroundingRectangle(teo2)))
        self.play(Write(teo2), run_time =3)        
        self.wait(3)   


class E6(Scene):
    def construct(self):
        axes = Axes(x_range=(-1,10,1),
                  y_range=(-1,20,1),
                  axis_config={"include_numbers": False, "include_tip": False}).shift(0.5*LEFT)
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        f1 = axes.plot(lambda t: -(t-5)**2+15, color = BLUE)
        f2 = axes.plot(lambda t: -(t-5)**4+15, color = BLUE)
        f3 = axes.plot(lambda t: -5*abs(t-5)+15, color = BLUE)
        vg = VGroup(f1, f2, f3)
        convex = Tex(r"Funciones ", r"cóncavas").to_edge(UP)
        l1 = DashedLine(axes.c2p(3, -5*abs(3-5)+15), axes.c2p(3,0), color = YELLOW)
        l2 = DashedLine(axes.c2p(8, -5*abs(8-5)+15), axes.c2p(8,0), color = YELLOW)
        a = Dot(axes.c2p(3,0))
        a_label = Tex(r"a", color = RED).next_to(a, DOWN)
        b = Dot(axes.c2p(8,0))
        b_label = Tex(r"b", color = RED).next_to(b, DOWN) 
        sec = Line(axes.c2p(3, -5*abs(3-5)+15), axes.c2p(8, -5*abs(8-5)+15)).set_length(10)    
        res = axes.plot(lambda t: -5*abs(t-5)+15, color = YELLOW,x_range = [3,8])
        desc = Tex(r"La ", r"función", r"\\ está por arriba de la recta secante", font_size = 24).shift(5*RIGHT)
        
        self.add(axes, axes_labels)
        
        #self.play(FadeOut(esto))
        self.wait()
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

class E8(Scene):
    def construct(self):
        teo = Tex(r"\textbf{Definición}. Se dice que $f$ es \textbf{cóncava} en un intervalo $I$ \\si dados $a<x<$b$ en $I$, se cumple que: $$\frac{f(x)-f(a)}{x-a} > \frac{f(b)-f(a)}{b-a}$$", font_size = 36).to_edge(UP)
        teo1 = Tex(r"\textbf{Teorema}. Si $f$ es diferenciable y $f'$ es decreciente en $I$. \\ Entonces, $f$ es cóncava en $I$.", font_size = 36).next_to(teo, DOWN)
        teo2 = Tex(r"\textbf{Teorema}. Si $f$ es dos veces diferenciable y $f''$ es negativa. \\ Entonces, $f$ es cóncava.", font_size = 36).next_to(teo1, DOWN)
        self.play(Create(SurroundingRectangle(teo)))
        self.play(Write(teo), run_time =3)
        self.wait()
        self.play(Create(SurroundingRectangle(teo2)))
        self.play(Write(teo1), run_time =3)        
        self.wait() 
        
        self.play(Create(SurroundingRectangle(teo)))
        self.play(Write(te2), run_time = 3)
        self.wait()        