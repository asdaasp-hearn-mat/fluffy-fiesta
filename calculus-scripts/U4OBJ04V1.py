from manim import *

class E1(Scene):
    def construct(self):
        # Título corregido (más pequeño y bien alineado)
        titulo = Tex(
            "Determine la ecuación de la recta tangente a la función en el punto dado", 
            color=YELLOW
        ).scale(0.8).to_edge(UP)
        self.play(Write(titulo))
        self.wait(1)

        # Líneas iniciales
        linea1 = MathTex("f(x)=\\sqrt{x};\\ x_0=4")
        linea2 = MathTex("f'(x)=\\frac{1}{2\\sqrt{x}}")
        grupo_lineas = VGroup(linea1, linea2).arrange(DOWN)  # Alinea las ecuaciones
        self.play(Write(grupo_lineas))
        self.wait(2)

        # Paso 1: Evaluar f(4)
        eval_f4 = MathTex("f(4) = \\sqrt{4}").move_to(linea1)
        self.play(ReplacementTransform(linea1, eval_f4))
        self.wait(1)

        resultado_f4 = MathTex("f(4) = 2").move_to(eval_f4)
        self.play(ReplacementTransform(eval_f4, resultado_f4))
        self.wait(1)

        # Paso 2: Evaluar f'(4)
        eval_fprima4 = MathTex("f'(4) = \\frac{1}{2\\sqrt{4}}").move_to(linea2)
        self.play(ReplacementTransform(linea2, eval_fprima4))
        self.wait(1)

        resultado_fprima4 = MathTex("f'(4) = \\frac{1}{4}").move_to(eval_fprima4)
        self.play(ReplacementTransform(eval_fprima4, resultado_fprima4))
        self.wait(1)

        # Ecuación de la recta tangente
        ecuacion = MathTex("y-", "f(4)", "=", "f'(4)", "(x-4)").next_to(resultado_fprima4, DOWN, buff=0.7)
        self.play(Write(ecuacion))

        # Reemplazar valores en la ecuación
        ecuacion_final = MathTex("y-","2","=","\\frac{1}{4}","(x-4)").move_to(ecuacion)
        self.play(ReplacementTransform(ecuacion, ecuacion_final))
        self.wait(2)

        # Ecuación simplificada reemplazando a la anterior
        ecuacion_simplificada = MathTex("y=2+\\frac{1}{4}(x-4)").move_to(ecuacion_final)
        self.play(ReplacementTransform(ecuacion_final, ecuacion_simplificada))
        self.wait(1)



class E2(MovingCameraScene):
    def construct(self):
        # Texto inicial
        title = Tex("Aproxime el valor de $\\sqrt{4.1}$").to_edge(UP)
        title.set_color(YELLOW)
        self.play(Write(title))
        self.wait(1)

        # Crear el plano con NumberPlane y estilo de fondo
        plane = NumberPlane(
            x_range=[0, 8, 1],
            y_range=[0, 4, 1],
            background_line_style={"stroke_opacity": 0.4},
            axis_config={"color": BLUE},
        ).scale(1.3)
        axes_labels = plane.get_axis_labels(x_label="x", y_label="y")
        self.play(Create(plane), Write(axes_labels))
        self.wait(1)

        # Graficar la función sqrt(x)
        graph = plane.plot(lambda x: np.sqrt(x), color=YELLOW)
        graph_label = MathTex(r"y=\sqrt{x}", color=YELLOW).next_to(graph, DOWN, buff=0.1).shift(UP)
        self.play(Create(graph), Write(graph_label))
        self.wait(1)

        # Punto (4, 2) en la función con etiqueta
        point = Dot(plane.c2p(4, 2), color=YELLOW)
        point_label = MathTex("(4, 2)").next_to(point, DOWN)
        self.play(FadeIn(point), Write(point_label))
        self.wait(1)

        # Líneas que conectan el punto amarillo a los ejes
        h_line = plane.get_horizontal_line(plane.c2p(4, 2), color=WHITE, stroke_width=0.0025)
        v_line = plane.get_vertical_line(plane.c2p(4, 2), color=WHITE, stroke_width=0.0025)
        self.play(Create(h_line), Create(v_line))
        self.wait(1)

        # Recta tangente en el punto (4, 2)
        tangent_line = plane.plot(lambda x: 2 + (1 / 4) * (x - 4), color=RED)
        tangent_label = MathTex(r"y=2+\frac{1}{4} (x-4)", color=RED).next_to(tangent_line, UP, buff=0.1)
        self.play(Create(tangent_line), Write(tangent_label))
        self.wait(1)

        # Punto en x = 4.1 en la función con etiqueta
        point_41 = Dot(plane.c2p(4.1, np.sqrt(4.1)), color=ORANGE) #punto naranja
        point_41_label = MathTex("(4.1, \\sqrt{4.1})").next_to(point_41)
        self.play(FadeIn(point_41))
        self.play(Write(point_41_label))
        self.wait(1)

        scale_fact = 0.001 
        self.camera.frame.save_state() 
        self.play( # Zoom intenso en el punto de tangencia
            self.camera.frame.animate.move_to(plane.c2p(4.1, np.sqrt(4.1))).scale(scale_fact),
            graph.animate.set_stroke(width=4 * scale_fact),  
            tangent_line.animate.set_stroke(width=4 * scale_fact),  
            point_41.animate.set_width(0.1 * scale_fact),
            point.animate.set_width(0.1 * scale_fact)
        )

        # Punto en la recta tangente cuando x = 4.1 con etiquetas escaladas
        tangent_point = Dot(plane.c2p(4.1, 2.025), color=BLUE).scale(scale_fact)
        tangent_point_label = MathTex("(4.1, 2+\\frac{1}{4}(4.1-4))", color=BLUE).move_to(tangent_point).shift(
            scale_fact * UP).scale(scale_fact)
        p41_label = MathTex("(4.1, \\sqrt{4.1})", color=ORANGE).move_to(point_41).shift(scale_fact * DOWN).scale(scale_fact)
        tp_label = MathTex("(4.1, 2+0.25(0.1))", color=BLUE).move_to(tangent_point).shift(scale_fact * UP).scale(scale_fact)
        tp_label_f = MathTex("(4.1,2.025)", color=BLUE).move_to(tangent_point).shift(scale_fact * UP).scale(scale_fact)
        self.play(FadeIn(tangent_point), FadeIn(tangent_point_label), FadeIn(p41_label))
        self.wait(1)
        self.play(ReplacementTransform(tangent_point_label, tp_label))
        self.wait(1)
        self.play(ReplacementTransform(tp_label, tp_label_f))
        self.wait(1)

        # Línea entre el punto naranja y el punto en la recta tangente
        dotted_line = Line(plane.c2p(4.1, np.sqrt(4.1)), plane.c2p(4.1, 2.025), color=GREEN, stroke_width=scale_fact * 4)
        self.play(Create(dotted_line))
        self.wait(1)
 
        self.play(
            Restore(self.camera.frame), # Restaurar la cámara 
            graph.animate.set_stroke(width=4),  # Escalar grosor de la gráfica
            tangent_line.animate.set_stroke(width=4),  # Escalar grosor de la recta tangente
            point_41.animate.set_width(0.1),
            point.animate.set_width(0.1),
            FadeOut(dotted_line), FadeOut(tangent_point), FadeOut(tp_label_f),FadeOut(p41_label)
        )
        self.wait(1)

        # Escribir la aproximación final
        approx_text = MathTex("\\sqrt{4.1} \\approx 2.025").to_edge(DOWN)
        self.play(Write(approx_text))
        self.wait(1)



class E3(Scene):
    def construct(self):
        # Primera línea de texto
        linea1 = Tex("En general, si $f$ es diferenciable en $x_0$,")
        linea1.to_edge(UP).shift(DOWN)
        self.play(Write(linea1))
        self.wait(1)
        
        # Segunda línea de texto
        linea2 = MathTex("y - f(x_0) = f'(x_0)(x - x_0)")
        linea2.next_to(linea1, DOWN).shift(DOWN)
        self.play(Write(linea2))
        self.wait(1)
        
        # Transformación de la segunda línea a la nueva versión
        lineanueva = MathTex("y = f'(x_0)(x - x_0) + f(x_0)")
        lineanueva.move_to(linea2)
        self.play(ReplacementTransform(linea2, lineanueva))
        self.wait(1)
        
        # Texto amarillo más abajo
        x_h = MathTex("x = x_0 + h", color=YELLOW)
        x_h.next_to(lineanueva, DOWN, buff=1)
        self.play(Write(x_h))
        self.wait(1)
        
        # Última línea de aproximación
        ultima_linea = MathTex(r"f(x_0 + h) \approx  f(x_0)+f'(x_0) h")
        ultima_linea.next_to(x_h, DOWN, buff=1)
        
        # Eliminar líneas anteriores y dejar solo la última encerrada en un rectángulo
        self.play(FadeOut(linea1, lineanueva))
        self.play(Write(ultima_linea))
        self.wait(1)
        # Agregar rectángulo amarillo alrededor de la última línea
        rect = SurroundingRectangle(ultima_linea, color=YELLOW)
        self.play(Create(rect),FadeOut(x_h))
        self.wait(2)



class E4(Scene):
    def construct(self):
        # Título
        titulo = Tex("Determine aproximadamente el valor de ", "$(2.01)^5$")
        titulo[1].set_color(YELLOW)
        titulo.scale(0.8).to_edge(UP)
        self.play(Write(titulo))
        self.wait(1)

        # Definir f(x) y valores iniciales
        fx = MathTex("f(x) = x^5")
        valores = MathTex("x_0 = 2, \\quad h = 0.01").set_color(YELLOW)
        grupo_fx = VGroup(fx, valores).arrange(DOWN)
        self.play(Write(grupo_fx))
        self.wait(2)

        # Evaluar f(2)
        eval_f2 = MathTex("f(2) = 2^5").next_to(fx, RIGHT)
        self.play(Write(eval_f2))
        self.wait(1)

        resultado_f2 = MathTex("f(2) = 32").move_to(eval_f2)
        self.play(TransformMatchingTex(eval_f2, resultado_f2))
        self.wait(1)

        # Derivada f'(x) y evaluación en x_0=2
        derivada = MathTex("f'(x) = 5x^4").next_to(valores, DOWN)
        self.play(Write(derivada))
        self.wait(1)

        eval_fprima2 = MathTex("f'(2) = 5(2^4)").next_to(derivada, RIGHT)
        self.play(Write(eval_fprima2))
        self.wait(1)

        resultado_fprima2 = MathTex("f'(2) = 80").move_to(eval_fprima2)
        self.play(ReplacementTransform(eval_fprima2, resultado_fprima2))
        self.wait(1)

        # Fórmula de aproximación
        formula = MathTex("f(x_0 + h) \\approx f'(x_0) h + f(x_0)").next_to(resultado_fprima2, DOWN, buff=0.7)
        self.play(Write(formula))
        self.wait(1)

        # Sustitución de valores en la fórmula
        paso1 = MathTex("f(2.01) \\approx 80(0.01) + 32").move_to(formula)
        self.play(ReplacementTransform(formula, paso1))
        self.wait(1)

        paso2 = MathTex("f(2.01) \\approx 0.8 + 32").move_to(paso1)
        self.play(ReplacementTransform(paso1, paso2))
        self.wait(1)

        resultado_final = MathTex("f(2.01) \\approx 32.8").move_to(paso2)
        self.play(ReplacementTransform(paso2, resultado_final))
        self.wait(2)
