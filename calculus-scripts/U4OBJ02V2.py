from manim import *
class E1(Scene):
    def construct(self):
        # Paso 1: Mostrar el límite inicial
        limite1 = MathTex(r"\lim_{x \to +\infty} \frac{f(x)}{g(x)}").shift(UP + 3*LEFT)
        self.play(Write(limite1))
        self.wait(1)

        # Paso 2: Mostrar el límite que se iguala a 0
        limite2 = MathTex(r"\lim_{x \to +\infty} f(x) = \lim_{x \to +\infty} g(x) = 0").next_to(limite1, DOWN).align_to(limite1, LEFT)
        self.play(Write(limite2))
        self.wait(1)

        # Paso 3: Transformación al límite con t
        limite3 = MathTex(r"\lim_{t \to 0^{+}} \frac{f\left(\frac{1}{t}\right)}{g\left(\frac{1}{t}\right)}").move_to(limite1)
        self.play(ReplacementTransform(limite1, limite3))
        self.wait(2)

        # Paso 4: Mostrar la igualdad de límites con t
        limite4 = MathTex(r"\lim_{t \to 0^{+}} f\left(\frac{1}{t}\right) = \lim_{t \to 0^{+}} g\left(\frac{1}{t}\right)=0").next_to(limite3, DOWN).align_to(limite3, LEFT)
        self.play(ReplacementTransform(limite2, limite4))
        self.wait(2)

        # Paso 5: Desvanecer los límites en t
        self.play(FadeOut(VGroup(limite3, limite4)))
        self.wait(1)

        # Paso 6: Mostrar derivadas
        limite5 = MathTex(
            r"\frac{\frac{d}{dt} f\left(\frac{1}{t}\right)}{\frac{d}{dt} g\left(\frac{1}{t}\right)}", r"= \frac{-\frac{1}{t^{2}} f'\left(\frac{1}{t}\right)}{-\frac{1}{t^{2}} g'\left(\frac{1}{t}\right)}", r"= \frac{f'\left(x\right)}{g'\left(x\right)}"
        ).move_to(ORIGIN)
        self.play(Write(limite5[0]))
        self.play(Write(limite5[1]))
        self.play(Write(limite5[2]))
        self.wait(2)
        self.play(FadeOut(limite5))
        # Paso 7: Transformación al límite final
        limite6 = MathTex(r"\lim_{x \to +\infty} \frac{f(x)}{g(x)} ", r"= \lim_{t \to 0^{+}} \frac{f\left(\frac{1}{t}\right)}{g\left(\frac{1}{t}\right)}", r"= \lim_{x \to +\infty} \frac{f'(x)}{g'(x)}").move_to(limite5)
        self.play(Write(limite6[0]))
        self.play(Write(limite6[1]))
        self.play(Write(limite6[2]))
        self.wait(2)

        # Paso 8: Mostrar la igualdad de límites finales
        limite7 = MathTex(r"\lim_{x \to +\infty} \frac{f(x)}{g(x)} = \lim_{x \to +\infty} \frac{f'(x)}{g'(x)}").move_to(limite6)
        self.play(ReplacementTransform(limite6, limite7))
        self.wait(2)

        # Paso 9: Cuadro alrededor del límite
        cuadro = SurroundingRectangle(limite7, color=YELLOW)
        self.play(Create(cuadro))
        self.wait(2)

        # Paso 10: Mostrar el texto adicional
        texto_normal = Tex(r"siempre que exista y ", color=YELLOW)
        texto_ecuacion = MathTex(r"\lim_{x \to +\infty} f(x) = \lim_{x \to +\infty} g(x) = 0", color=YELLOW)
        full_text = VGroup(texto_normal, texto_ecuacion).arrange(RIGHT).next_to(limite7, DOWN).align_to(limite7, ORIGIN)
        self.play(Write(full_text))
        self.wait(2)

        # Paso 11: Mostrar el texto introductorio
        texto1 = Tex(r"De manera similar... ", color=YELLOW).to_edge(LEFT + UP).shift(DOWN * 1.0)

      # Paso 12: Mostrar el límite negativo
        limite8 = MathTex(r"\lim_{x \to -\infty} \frac{f(x)}{g(x)} = \lim_{x \to -\infty} \frac{f'(x)}{g'(x)}").move_to(limite7)
        texto_e1 = MathTex(r"\lim_{x \to -\infty} f(x) = \lim_{x \to -\infty} g(x) = 0", color=YELLOW)
        full_t = VGroup(texto_normal, texto_e1).arrange(RIGHT).next_to(limite8, DOWN).align_to(limite8, ORIGIN)
        self.play(Write(texto1))
        self.play(TransformMatchingTex(limite7, limite8),TransformMatchingTex(full_text, full_t))
        self.wait(2)  


class E2(Scene):
    def construct(self):
        # Paso 1: Mostrar el enunciado
        texto1 = Tex(r"Calcule, de existir, el siguiente límite.", color=YELLOW).to_edge(UP)
        self.play(Write(texto1))
        self.wait(1)

        # Paso 2: Mostrar el límite inicial
        limite1 = MathTex(r"\lim_{x \to +\infty} x\sin\left(\frac{1}{x}\right)").next_to(texto1, DOWN)
        self.play(Write(limite1))
        self.wait(1)

        # Paso 3: Transformación a la expresión desglosada
        nfinito = MathTex(r" \to \infty", color=PURPLE).next_to(limite1,RIGHT)
        cero = MathTex(r"\cdot 0", color=PURPLE).next_to(nfinito, RIGHT)
        grupito = VGroup(nfinito, cero)
 
        self.wait(1)

        # Paso 4: Mostrar los límites individuales
        limite2 = MathTex(r"\lim_{x \to +\infty} x = +\infty ").next_to(grupito, LEFT).shift(DOWN*2)
        limite3 = MathTex(r"\lim_{x \to +\infty} \sin\left(\frac{1}{x}\right) = 0").next_to(limite2, DOWN).align_to(limite2, LEFT)
        self.play(Write(limite2))
        self.wait(1)
        # Paso 5: Mostrar el texto de equivalencia
        texto = MathTex(r"\iff \lim_{x \to +\infty} \frac{1}{x} = 0").next_to(limite2,RIGHT)
 
        self.wait(1)
        self.play(Write(limite3))
        self.play(Write(grupito))        
        self.play(Write(texto))
        self.wait(1)
        # Paso 6: Fade out de los límites
        self.play(FadeOut(VGroup(texto1, grupito, texto, limite2, limite3)))
        self.wait(1)

        # Paso 7: Mostrar la expresión factorizada
        limite4 = MathTex(r" \lim_{x \to +\infty} \frac{\sin\left(\frac{1}{x}\right)}{\frac{1}{x}} \to \frac{0}{0}", color=YELLOW).move_to(ORIGIN)
        self.play(Write(limite4))
        self.wait(1)
        #hola
        # Paso 8: Fade out de la expresión factorizada
        self.play(FadeOut(VGroup(limite4)))
        self.wait(1)

        # Paso 9: Mostrar el límite final
        limite5 = MathTex(r"\lim_{x \to +\infty} \frac{\sin\left(\frac{1}{x}\right)}{\frac{1}{x}}").move_to(ORIGIN)
        self.play(Write(limite5))
        self.wait(1)

        # Paso 10: Mostrar el límite de coseno
        limite6 = MathTex(r"= \lim_{x \to +\infty} \frac{-\frac{1}{x^2}\cos\left(\frac{1}{x}\right)}{-\frac{1}{x^2}}").next_to(limite5, DOWN).align_to(limite5, LEFT)
        self.play(Write(limite6))    
        self.wait(1)    
        limite6b = MathTex(r"= \lim_{x \to +\infty} \cos\left(\frac{1}{x}\right)").next_to(limite5, DOWN).align_to(limite5, LEFT)
        self.play(ReplacementTransform(limite6,limite6b))
        self.wait(2)

        # Paso 11: Transformación al valor final
        limite7 = MathTex(r"= \cos(0)").move_to(limite6).align_to(limite6, LEFT)
        self.play(ReplacementTransform(limite6b, limite7))
        self.wait(2)
        limite8 =MathTex(r"= 1").move_to(limite6).align_to(limite6, LEFT)
        self.play(ReplacementTransform(limite7, limite8))

class E3(Scene):
    def construct(self):
        # Paso 1: Mostrar el enunciado
        texto1 = Tex(r"Calcule el siguiente límite.", color=YELLOW).to_edge(UP)
        self.play(Write(texto1))
        self.wait(1)

        # Paso 2: Mostrar el límite inicial
        limite1 = MathTex(r"\lim_{x \to +\infty} \frac{x}{x - \sin(x)}").next_to(texto1, DOWN).shift(0.5 * DOWN)
        self.play(Write(limite1))
        self.wait(1)

        # Paso 3: Mostrar derivada en numerador y denominador
        limite2 = MathTex(r"\frac{\frac{d}{dx} x}{\frac{d}{dx}(x - \sin(x))} =").next_to(limite1, DOWN).shift(2*LEFT + DOWN)
        limite3 = MathTex(r"\frac{1}{1 - \cos(x)}").next_to(limite2, RIGHT).align_to(limite2)
        self.play(Write(VGroup(limite2, limite3)))
        self.wait(1)

        # Paso 4: Añadir cuadro alrededor del límite
        cuadro = SurroundingRectangle(limite3, color=PURPLE)
        self.play(Create(cuadro))
        self.wait(1)

        # Paso 5: Mostrar el texto adicional
        texto = Tex(r"no existe el límite \\ cuando $x \to +\infty$", color=PURPLE).next_to(limite3, RIGHT)
        self.play(Write(texto))
        self.wait(1)

        # Paso 6: Fade out del cuadro y texto
        self.play(FadeOut(VGroup(cuadro, texto,limite2, limite3)))
        self.wait(1)
        # Paso 8: Transformación al nuevo límite
        limite5 = MathTex(r"\lim_{x \to +\infty} \frac{x}{x - \sin(x)} =").move_to(limite2)
        limite6 = MathTex(r"\lim_{x \to +\infty} \frac{1}{1 - \frac{\sin(x)}{x}}").next_to(limite5, RIGHT)
        self.play(Write(limite5))
        self.play(Write(limite6))
        self.wait(1)
        limite4 = MathTex(r"= 1").next_to(limite1,RIGHT)
        self.play(Write(limite4))
        self.wait(1)

class E4(Scene):
    def construct(self):
        # Paso 1: Mostrar el enunciado
        #texto1 = Tex(r"La regla de L'Hopital también \\ es válida en los casos que ", color=BLUE).to_edge(LEFT).shift(2 * UP)
        #self.play(Write(texto1))
        #self.wait(1)

        # Paso 2: Mostrar las condiciones iniciales
        limite1 = MathTex(r"\text{Si } \lim_{x \to c} f(x) = \lim_{x \to c} g(x) = \infty", color=YELLOW).shift(UP)
        self.play(Write(limite1))
        self.wait(1)

        # Paso 3: Mostrar las condiciones adicionales
        palabra = Tex(r"y").next_to(limite1, DOWN)
        palabra2 = MathTex(r"\lim_{x \to c} \frac{f'(x)}{g'(x)}").next_to(palabra, RIGHT)
        palabra3 = Tex(r"existe, entonces").next_to(palabra2, RIGHT)
        palabra.add(palabra2, palabra3).next_to(limite1, DOWN)
        self.play(Write(palabra))
        self.wait(1)

        # Paso 4: Mostrar el límite final
        limite3 = MathTex(r"\lim_{x \to c} \frac{f(x)}{g(x)} = \lim_{x \to c} \frac{f'(x)}{g'(x)}", color=YELLOW).next_to(palabra, DOWN)
        self.play(Write(limite3))
        self.wait(1)

class E5(Scene):
    def construct(self):
        texto1 = Tex(r"Calcule, de ser posible, el siguiente límite. ",color=YELLOW).to_edge(UP)
        limite1=MathTex(r"\lim_{x \to +\infty} (\ln(x)-x)").next_to(texto1,DOWN).align_to(ORIGIN).shift(DOWN)
        limite2=MathTex(r"\lim_{x \to +\infty} \ln(x) = +\infty").next_to(limite1 ,DOWN).shift(DOWN)
        limite3=MathTex(r"\lim_{x \to +\infty} x = +\infty").next_to(limite2,DOWN).shift(DOWN)
        infinitos= MathTex(r"+\infty -\infty").move_to(limite1)
        limite4= MathTex(r"\ln(x)-x = x \left(\frac{\ln(x)}{x}-1\right)").move_to(infinitos).align_to(ORIGIN)
        limite5=MathTex(r"\lim_{x \to +\infty} \frac{\ln(x)}{x} ", color=YELLOW).next_to(limite4,DOWN).shift(DOWN)
        limite6=MathTex(r"\frac{+\infty}{+\infty}", color=YELLOW).next_to(limite4,DOWN).shift(DOWN)
        limite7=MathTex(r"\lim_{x \to +\infty} \frac{\ln(x)}{x} = \lim_{x \to +\infty} \frac{\frac{1}{x}}{1}", color=YELLOW).next_to(limite4,DOWN).shift(DOWN)
        limite8=MathTex(r"\lim_{x \to +\infty} \frac{\ln(x)}{x} = \lim_{x \to +\infty} \frac{1}{x} = 0", color=YELLOW).next_to(limite4,DOWN).shift(DOWN)
        limite9=MathTex(r"\lim_{x \to +\infty} (\ln(x)-x) =\lim_{x \to +\infty} x \left(\frac{\ln(x)}{x}-1\right) ").move_to(limite4).align_to(ORIGIN)
        limite10=MathTex(r"=\lim_{x \to +\infty} x \lim_{x \to +\infty} \left(\frac{\ln(x)}{x}-1\right)").next_to(limite9,DOWN).shift(2.6*RIGHT)
        limite11=MathTex(r"=(+\infty)(0-1)").next_to(limite10,DOWN).shift(1.6*LEFT)
        limite12=MathTex(r"= -\infty").next_to(limite10,DOWN).shift(2.5*LEFT)
        self.play(Write(texto1))
        self.wait(2)
        self.play(Write(limite1))
        self.wait(2)
        self.play(Write(limite2))
        self.wait(2)
        self.play(Write(limite3))
        self.wait(2)
        self.play(FadeOut(VGroup(limite2,limite3)))
        self.wait(1)
        self.play(ReplacementTransform(limite1,infinitos))
        self.wait(2)
        self.play(FadeOut(infinitos))
        self.wait(2)
        self.play(FadeOut(texto1))
        self.wait(1)
        self.play(Write(limite4))
        self.wait(2)
        self.play(Write(limite5))
        self.wait(2)
        self.play(ReplacementTransform(limite5, limite6))
        self.wait(2)
        self.play(ReplacementTransform(limite6, limite7))
        self.wait(2)
        self.play(ReplacementTransform(limite7, limite8))
        self.wait(2)
        self.play(FadeOut(limite8))
        self.wait(2)
        self.play(ReplacementTransform(limite4,limite9))
        self.wait(1)
        self.play(Write(limite10))
        self.wait(2)
        self.play(Write(limite11))
        self.wait(2)
        self.play(ReplacementTransform(limite11,limite12))
        self.wait(2)

class E6(Scene):
    def construct(self):
        linea=Tex(r"Determine las asíntotas de la función", color=YELLOW).to_edge(UP)
        self.play(Write(linea))
        self.wait(2)
        funcion= MathTex(r"f(x)=ln(1+e^{x})").next_to(linea,DOWN).shift(DOWN)
        self.play(Write(funcion))
        self.wait(2)
        texto_continuidad = Tex(r"Note que $f$ es continua en $\mathbb{R}$, \\ así que f no posee asíntotas verticales.").next_to(funcion, DOWN).align_to(linea).shift(DOWN)
        self.play(Write(texto_continuidad))
        self.wait(2)
        grupote=VGroup(linea,funcion,texto_continuidad)
        self.play(FadeOut(grupote))
        self.wait(2)
        funcion1= MathTex(r"\lim_{x \to -\infty} ln(1+e^{x}) = ln(\lim_{x \to -\infty} 1+e^{x})").next_to(linea,DOWN).shift(DOWN)
        self.play(Write(funcion1))
        self.wait(2)
        funcion2= MathTex(r"= ln(1+e^{-\infty})").next_to(funcion1,DOWN).shift(DOWN+1.5*RIGHT)
        self.play(Write(funcion2))
        self.wait(2)
        funcion3= MathTex(r"= ln(1+0)").next_to(funcion1,DOWN).shift(DOWN+1.1*RIGHT)
        self.play(ReplacementTransform(funcion2,funcion3))
        self.wait(2)
        funcion4= MathTex(r"= ln(1)").next_to(funcion1,DOWN).shift(DOWN+RIGHT+0.3*LEFT)
        self.play(ReplacementTransform(funcion3,funcion4))
        self.wait(2)
        funcion5= MathTex(r"= 0").next_to(funcion1,DOWN).shift(DOWN+RIGHT+0.7*LEFT)
        self.play(ReplacementTransform(funcion4,funcion5))
        self.wait(2)
        textual = Tex(r"Asi que ").next_to(funcion5, DOWN).align_to(ORIGIN).shift(DOWN+4*LEFT)
        textualM = MathTex(r"y=0").next_to(textual,RIGHT)
        textos = Tex(r"es una asíntota horizontal.").next_to(textualM,RIGHT)
        group= VGroup(textual,textualM,textos)
        self.play(Write(group))
        self.wait(2)
        self.play(FadeOut(funcion5))
        self.wait(2)
        self.play(FadeOut(group))
        self.wait(2)
        funcion6= MathTex(r"\lim_{x \to +\infty} ln(1+e^{x}) = ln(\lim_{x \to +\infty} 1+e^{x})").next_to(linea,DOWN).shift(DOWN)
        self.play(ReplacementTransform(funcion1,funcion6))
        self.wait(2)
        funcion7= MathTex(r"= ln(1+e^{+\infty})").next_to(funcion6,DOWN).shift(DOWN+1.5*RIGHT)
        self.play(Write(funcion7))
        self.wait(2)
        funcion8= MathTex(r"= ln(+\infty)").next_to(funcion6,DOWN).shift(DOWN+1.1*RIGHT)
        self.play(ReplacementTransform(funcion7,funcion8))
        self.wait(2)
        funcion9= MathTex(r"= +\infty").next_to(funcion6,DOWN).shift(DOWN+RIGHT+0.3*LEFT)
        self.play(ReplacementTransform(funcion8,funcion9))
        self.wait(2)
        triki = Tex(r"Por tanto, $f$ solamente posee una asíntota horizontal \\ que ocurre cuando  $x \to -\infty$").next_to(funcion9, DOWN).align_to(ORIGIN).shift(DOWN)
        self.play(Write(triki))
        self.wait(2)
        self.play(FadeOut(VGroup(funcion6,funcion9,triki)))
        self.wait(2)
        Norden= Tex(r"verifiquemos si $f$ tiene una asintota oblicua $y=mx+b$ \\ cuando  $x \to +\infty$").to_edge(UP)
        self.play(Write(Norden))
        self.wait(2)
        #otorden=Tex(r"recordemos que ", color=BLUE).align_to(Norden,LEFT).shift(UP)
        #self.play(Write(otorden))
        #self.wait(2)
        creor= MathTex(r"m=\lim_{x \to +\infty}\frac{f(x)}{x} , b=\lim_{x \to +\infty}f(x)-mx", color=(YELLOW)).align_to(Norden,ORIGIN).shift(2*DOWN)
        self.play(Write(creor))
        self.wait(2)
        self.play(FadeOut(Norden,creor))
        self.wait(2)
        Nuevolim=MathTex(r"\lim_{x \to +\infty} \frac{ln(1+e^{x})}{x} \to \frac{+\infty}{+\infty}").align_to(ORIGIN)
        self.play(Write(Nuevolim))
        self.wait(2)
        self.play(FadeOut(Nuevolim))
        self.wait(2)
        Nunu=MathTex(r"\lim_{x \to +\infty} \frac{ln(1+e^{x})}{x} = \lim_{x \to +\infty} \frac{1}{e^{-x}+1} = \frac{1}{e^{-\infty}+1}").to_edge(UP).shift(DOWN)
        self.play(Write(Nunu))
        self.wait(2)
        willump=MathTex(r"\lim_{x \to +\infty} \frac{ln(1+e^{x})}{x} = \lim_{x \to +\infty} \frac{1}{e^{-x}+1} = \frac{1}{0+1}").move_to(Nunu).align_to(Nunu,LEFT)
        self.play(TransformMatchingTex(Nunu,willump))
        self.wait(2)
        Jax=MathTex(r"\lim_{x \to +\infty} \frac{ln(1+e^{x})}{x} = \lim_{x \to +\infty} \frac{1}{e^{-x}+1} = 1").move_to(Nunu).align_to(Nunu,LEFT)
        self.play(TransformMatchingTex(willump,Jax))
        self.wait(2)
        morga=MathTex(r"\frac{\frac{d}{dx} (ln(1+e^{x}))}{\frac{d}{dx}(x)} = \frac{\frac{e^{x}}{1+e^{x}}}{1} = \frac{1}{e^{-x}+1}}",color=YELLOW).next_to(Jax,DOWN).shift(DOWN)
        self.play(Write(morga))
        self.wait(2)
        self.play(FadeOut(morga))
        self.wait(2)
        Voli=MathTex(r"b = \lim_{x \to +\infty} \ln(1+e^{x})-x ").to_edge(UP).shift(LEFT+2*DOWN)
        self.play(ReplacementTransform(Jax,Voli))
        self.wait(2)
        Volim=MathTex(r"b = \lim_{x \to +\infty} \ln(1+e^{x})-ln(e^{x}) ").to_edge(UP).shift(LEFT+2*DOWN)
        self.play(ReplacementTransform(Voli,Volim))
        self.wait(2)
        rias=MathTex(r"= \lim_{x \to +\infty} \frac{\ln(1+e^{x})}{e^{x}}").next_to(Volim,RIGHT)
        self.play(Write(rias))
        self.wait(2)
        akeno=MathTex(r"= \ln(\lim_{x \to +\infty} \frac{1}{e^{-x}}+\frac{e^{x}}{e^{x}}) ").next_to(rias,DOWN).align_to(ORIGIN).shift(DOWN)
        self.play(Write(akeno))
        self.wait(2)
        sayo=MathTex(r"= \ln(\lim_{x \to +\infty} e^{-x}+1)").next_to(rias,DOWN).align_to(ORIGIN).shift(DOWN)
        self.play(ReplacementTransform(akeno,sayo))
        self.wait(2)
        palo=MathTex(r"= \ln(e^{-\infty}+1)").next_to(rias,DOWN).align_to(ORIGIN).shift(DOWN)
        self.play(ReplacementTransform(sayo,palo))
        self.wait(2)
        perico=MathTex(r"= \ln(0+1)").next_to(rias,DOWN).align_to(ORIGIN).shift(DOWN)
        self.play(ReplacementTransform(palo,perico))
        self.wait(2)
        per=MathTex(r"= \ln(1)").next_to(rias,DOWN).align_to(ORIGIN).shift(DOWN)
        self.play(ReplacementTransform(perico,per))
        self.wait(2)
        perita=MathTex(r"= 0").next_to(rias,DOWN).align_to(ORIGIN).shift(DOWN)
        self.play(ReplacementTransform(per,perita))
        self.wait(2)
        self.play(FadeOut(Voli,Volim,perita,rias))
        self.wait(2)
        chori=Tex(r"En conclusión,").to_corner(UL)
        self.play(Write(chori))
        self.wait(2)
        sulfa=Tex(r"$f$ no tiene asíntotas verticales").next_to(chori,DOWN).align_to(chori,LEFT)
        self.play(Write(sulfa))
        self.wait(2)
        cob=Tex(r"$y=0$ es una asintota horizontal \\ cuando  $x \to -\infty$ ").next_to(sulfa,DOWN).align_to(chori,LEFT)
        self.play(Write(cob))
        self.wait(2)
        au=Tex(r"$y=x$ es una asíntota oblícua \\  cuando  $x \to +\infty$ ").next_to(cob,DOWN).align_to(chori,LEFT)
        self.play(Write(au))
        self.wait(2)
        plane = NumberPlane(x_range=[-5, 5, 1],  # Rango en el eje x
        y_range=[-5, 5, 1],  # Rango en el eje y
        background_line_style={"stroke_color": BLUE,"stroke_width": 2,"stroke_opacity": 0.5})
        # Crear el plano cartesiano
        plane = NumberPlane(
            x_range=[-3.5, 3.5, 1],
            y_range=[-3.5, 3.5, 1],
            background_line_style={"stroke_opacity": 0.4}
        ).scale(0.70).to_edge(RIGHT)
        axes_labels = plane.get_axis_labels(x_label="x", y_label="y")
        # Graficar la función f(x) = log(1 + exp(x)) en color azul
        f_graph = plane.plot(lambda x: np.log(1 + np.exp(x)), color=BLUE)
            
        # Etiqueta para la gráfica "f"
        f_label = MathTex("f").next_to(f_graph, buff=0.2).set_color(BLUE)
        self.play(Create(VGroup(plane,f_graph,f_label)))
        self.wait()
        asint_1=plane.plot(lambda x: x,x_range=[0,3.5], color=YELLOW)
        asint_2=plane.plot(lambda x: 0*x,x_range=[-3.5,0], color=YELLOW)
        self.play(Create(VGroup(asint_2,asint_1)))