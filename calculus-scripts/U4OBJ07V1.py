from manim import *

def disc(axes, *point, color = WHITE):
    c= Circle(radius=0.08, color = BLACK, fill_opacity=1, stroke_width = 1).move_to(axes.c2p(point[0], point[1]))
    d= Circle(radius=0.08, color = color, stroke_width = 1.2).move_to(axes.c2p(point[0], point[1]))
    return VGroup(c,d)

def pp(axes, *point, color = WHITE):
    pl = MathTex(r"(", color = color).move_to(axes.c2p(point[0], point[1]))
    pr = MathTex(r")", color = color).move_to(axes.c2p(point[0], point[1]))
    return VGroup(pl,pr)

class E1(Scene):
    def construct(self):
        # Presentación del problema
        orden = Tex(r"El área entre dos círculos concéntricos variables siempre es igual a 9 $\pi$ $\mathrm{cm}^2$. La tasa de cambio del área del círculo exterior es de 10 $\pi \, \mathrm{cm}^2/s$ ¿A qué velocidad varía la longitud de la circunferencia del círculo interior cuando su área es de 16 $\pi \, \mathrm{cm}^2?$", color=YELLOW, font_size=30).to_edge(UP)
        orden2 = Tex(r"- Calculus, Michael Spivak 10.9", color=YELLOW, font_size=30).next_to(orden, DOWN).align_to(orden, LEFT)        
        # Visualización de los círculos
        c1 = Circle(radius=5, color=RED).to_edge(LEFT).scale(0.25)
        c2 = Circle(radius=4, color=BLUE, fill_color=BLUE, fill_opacity=1).move_to(c1.get_center()).scale(0.25)
        cs = VGroup(c1, c2)   
        cs.shift(2*LEFT)   
        c1_label = always_redraw(lambda: MathTex(r"C_1", color=RED).next_to(c1, RIGHT, buff=0.1))
        c2_label = always_redraw(lambda: MathTex(r"C_2", color=BLUE).next_to(c1, LEFT, buff=0.1))
  
        # Parte del área
        dif = MathTex(r"A_1", r"-", r"A_2", r"=", r"9\pi").next_to(cs,RIGHT,buff=1.5).shift(UP)
        linea_innecesaria = MathTex(r"A_1'(t)=10 \pi ").next_to(dif,DOWN).align_to(dif, LEFT)
        linea_innecesaria2 =Tex(r"¿$C_{2}'(t_0)$ si  $A_2(t_0)= 16 \pi$?").next_to(linea_innecesaria,DOWN).align_to(dif, LEFT)
        difdift = MathTex(r"D_t", r"\left(", r"A_1(t)", r"-", r"A_2(t)", r"\right)", r"=", r"D_t", r"9\pi").next_to(linea_innecesaria2, DOWN, buff=0.5).align_to(dif, LEFT)
        difdiftres0 = MathTex(r"10\pi", r"-", r"D_t (2\pi (r_2(t))^2)", r"=", r"0", font_size=34).next_to(difdift, DOWN).align_to(difdift, LEFT)
        difdiftres = MathTex(r"10\pi", r"-", r"2\pi r_2(t) r_2'(t)", r"=", r"0", font_size=34).move_to(difdiftres0).align_to(difdift, LEFT)
        razon = MathTex(r"10\pi", r"=", r"2\pi r_2(t) r_2'(t)", font_size=34).move_to(difdiftres0).align_to(difdift, LEFT)
        form = MathTex(r"r_2'(t)", r"=", r"\frac{10}{r_2(t)}", font_size=34).next_to(difdiftres0,DOWN).align_to(difdift, LEFT)

        # Determinación de r2(t_0)
        area = MathTex(r"A_2(t_0)", r"=", r"16\pi").next_to(cs,RIGHT,buff=2)
        area1 = MathTex(r"\pi(r_2(t_0))^2", r"=", r"16\pi").next_to(area, DOWN).align_to(area, LEFT)
        rado = MathTex(r"r_2(t_0)", r"=", r"4").next_to(area1, DOWN).align_to(area, LEFT)
        
        # Cálculo de r2'(t_0)
        form2 = MathTex(r"r_2'(t_0)", r"=", r"\frac{10}{2 \cdot 4}", font_size=34).next_to(rado, DOWN).align_to(rado, LEFT)
        form3 = MathTex(r"r_2'(t_0)", r"=", r"\frac{5}{4}", font_size=34).next_to(rado, DOWN).align_to(rado, LEFT)

        # Cálculo final
        dperi0 = MathTex(r"C_2'(t_0)", r"=", r"2\pi r_2'(t_0)", font_size=30).next_to(cs, RIGHT, buff=2).shift(1*UP)
        res = MathTex(r"=", r"2\pi", r"\frac{5}{4}", font_size=30).next_to(dperi0, DOWN).align_to(dperi0[1], LEFT)
        resul = MathTex(r"=", r"\frac{5 \pi}{2}", font_size=30).next_to(res, DOWN).align_to(dperi0[1], LEFT)
        
        # Animaciones
        self.play(Write(orden))
        self.play(Write(orden2))
        self.wait()
        self.play(Create(cs))
        self.play(Write(VGroup(c1_label, c2_label)))
        self.wait()
        # Parte del área
        self.play(Write(dif))
        self.wait()
        self.play(Write(linea_innecesaria))
        self.wait()
        self.play(Write(linea_innecesaria2))
        self.play(TransformMatchingTex(dif.copy(), difdift))
        self.wait()
        self.play(Write(difdiftres0))
        self.wait()
        self.play(ReplacementTransform(difdiftres0, difdiftres))
        self.wait()
        self.play(TransformMatchingTex(difdiftres, razon))
        self.wait()
        self.play(TransformMatchingTex(razon.copy(), form))
        self.wait()
        self.play(FadeOut(VGroup(dif,linea_innecesaria,linea_innecesaria2, difdift, razon, form)))
        # Determinación de r2(t_0)
        self.play(Write(area))
        self.wait()
        self.play(Write(area1))
        self.wait()
        self.play(Write(rado))
        self.wait()
        

        # Cálculo de r2'(t_0)
        self.play(ReplacementTransform(rado, form2))
        self.wait()
        self.play(TransformMatchingTex(form2, form3))
        self.wait()
        
        # Pausa y limpieza
        self.play(FadeOut(VGroup(area, area1)))
        self.wait()
        
        # Cálculo final
        self.play(ReplacementTransform(form3, dperi0))
        self.wait()
        self.play(Write(res))
        self.wait()
        self.play(Write(resul))
        self.wait()
        self.play(Create(SurroundingRectangle(resul[1])))
        self.wait()
