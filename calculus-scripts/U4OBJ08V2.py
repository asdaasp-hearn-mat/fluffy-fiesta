    from manim import *

class E1(Scene):
    def construct(self):
        # Texto en rojo en la parte superior
        intro_text = Tex("Determine los valores extremos de la función definida por:", color=YELLOW)
        intro_text.to_edge(UP)
        
        # Función en MathTex
        function_text = MathTex(
            "f(x) = \\frac{1}{3} \\sqrt[3]{x^5} - 3 \\sqrt[3]{x^2}; \\ x \\in [-1,8]"
        )
        function_text.next_to(intro_text, DOWN)
        
        # Texto en amarillo que indica que se deben hallar los puntos críticos
        critical_points_text = Tex("Debemos identificar los puntos críticos de $f$", color=YELLOW)
        critical_points_text.next_to(function_text, DOWN)

        # Texto para puntos de frontera
        boundary_text = Tex("Puntos de frontera", color=YELLOW)
        boundary_text.to_edge(LEFT)
        
        # Valores de x en azul
        x_values_text = VGroup(
            Tex("$x = -1$", color=BLUE),
            Tex("$x = 8$", color=BLUE)
        )
        x_values_text.arrange(DOWN)
        x_values_text.next_to(boundary_text, DOWN, buff=0.2)
        
        # Proceso de hallar la derivada de f
        derivative_process = VGroup(
            MathTex("f'(x) = \\frac{d}{dx} \\left( \\frac{1}{3} \\sqrt[3]{x^5} - 3 \\sqrt[3]{x^2} \\right)"),
            MathTex("= \\frac{d}{dx} \\left( \\frac{1}{3} x^{5/3} - 3 x^{2/3} \\right)"),
            MathTex("= \\frac{5}{9} x^{2/3} - 2 x^{-1/3}")
        )
        derivative_process.arrange(DOWN)
        derivative_process.to_edge(RIGHT)
        
        # Mostrar el texto en rojo y la función
        self.play(Write(intro_text))
        self.play(Write(function_text))
        self.wait(1)
        self.play(Write(critical_points_text))
        self.wait(1)
        
        # Borrar el texto de los puntos críticos
        self.play(FadeOut(critical_points_text))
        
        # Mostrar los puntos de frontera y los valores
        self.play(Write(boundary_text))
        self.play(Write(x_values_text))
        self.wait(1)
        
        # Mostrar las dos primeras líneas del proceso
        self.play(Write(derivative_process[0]))
        self.play(Write(derivative_process[1]))
        self.wait(1)
        
        # Transformar la segunda línea en la tercera
        self.play(ReplacementTransform(derivative_process[1], derivative_process[2]))
        self.wait(1)

        # Agregar la nueva línea debajo de la tercera
        new_line = MathTex("= \\frac{5}{9} x^{2/3} - \\frac{2}{\\sqrt[3]{x}}")
        new_line.next_to(derivative_process[2], DOWN)
        self.play(Write(new_line))
        self.wait(1)

        # Transformar la nueva línea en la forma final
        final_line = MathTex("f'(x) = \\frac{5x - 18}{9 \\sqrt[3]{x}}")
        self.play(ReplacementTransform(new_line, final_line))
        self.wait(1)

        # Borrar todas las líneas excepto la última y centrarla
        self.play(FadeOut(derivative_process))
        self.play(final_line.animate.move_to(ORIGIN).shift(UP))
        self.wait(2)

        
        # Texto "punto crítico estacionario" en amarillo a la izquierda de final_line
        stationary_text = Tex("Punto estacionario", color=YELLOW)
        stationary_text.next_to(final_line, DOWN)

        # $x = 18/5$ debajo del texto "punto crítico estacionario"

        stationary_value = MathTex("f'(x)=0", color=BLUE)
        stationary_value.next_to(stationary_text, DOWN)
        # Mostrar el texto "punto crítico estacionario" y $x = 18/5$
        self.play(Write(stationary_text))
        self.play(Write(stationary_value))
        self.wait(1)
        
        for process in [
            r"\frac{5x - 18}{9 \sqrt[3]{x}}=0",
            r"5x - 18=0",
            r"5x=18",
            r"x=\frac{18}{5}"
        ]:
            new_stationary_value = MathTex(process, color=BLUE).next_to(stationary_text, DOWN)
            self.play(ReplacementTransform(stationary_value, new_stationary_value))
            stationary_value = new_stationary_value
            self.wait(1)
        singular_text = Tex("Punto singular", color=YELLOW)
        singular_text.next_to(final_line, DOWN).shift(4*RIGHT)

        # $x = 0$ debajo del texto "punto crítico singular"
        singular_value = MathTex("x = 0", color=BLUE)
        singular_value.next_to(singular_text, DOWN)



        # Mostrar el texto "punto crítico singular" y $x = 0$
        self.play(Write(singular_text))
        self.play(Write(singular_value))
        self.wait(2)



class E2(Scene):
    def construct(self):
        # Crear los textos
        intro_text = Tex("Determine los valores extremos de la función definida por:", color=YELLOW).to_edge(UP)
        function_text = MathTex("f(x) = \\frac{1}{3} \\sqrt[3]{x^5} - 3 \\sqrt[3]{x^2}; \\ x \\in [-1,8]").next_to(intro_text, DOWN)
        critical_points_text = Tex("Puntos críticos", color=YELLOW).to_edge(LEFT)
        critical_values = MathTex("\\{-1, 0, \\frac{18}{5}, 8\\}",color=BLUE).next_to(critical_points_text, DOWN)

        # Evaluaciones de f(x) en diferentes puntos
        eval_steps = [
            ("f(-1)", ["\\frac{1}{3} \\sqrt[3]{(-1)^5} - 3 \\sqrt[3]{(-1)^2}", "= \\frac{1}{3} (-1) - 3 (1)", "= -\\frac{1}{3} - 3", "=-\\frac{10}{3}"]),
            ("f(0)", ["\\frac{1}{3} \\sqrt[3]{0^5} - 3 \\sqrt[3]{0^2}", "= \\frac{1}{3} (0) - 3 (0)", "= 0"]),
            ("f\\left(\\frac{18}{5}\\right)", ["\\frac{1}{3} \\sqrt[3]{\\left(\\frac{18}{5}\\right)^5} - 3 \\sqrt[3]{\\left(\\frac{18}{5}\\right)^2}", "= \\frac{1}{3} \\left(\\frac{18}{5}\\right) - 3 \\left(\\frac{18}{5}\\right)^{2/3}","= - \\left(\\frac{27}{5}\\right) \\left(\\frac{12}{25}\\right)^{1/3}"]),
            ("f(8)", ["\\frac{1}{3} \\sqrt[3]{8^5} - 3 \\sqrt[3]{8^2}", "= \\frac{1}{3} (32) - 3 (4)", "= -\\frac{4}{3}"])
        ]

        # Mostrar el texto de introducción y la función
        self.play(Write(intro_text), Write(function_text))
        self.wait(1)

        # Mostrar puntos críticos
        self.play(Write(critical_points_text), Write(critical_values))
        self.wait(1)

        # Función para evaluar y transformar expresiones sin mover la parte izquierda de la ecuación
        def eval_and_transform(left_side, right_exprs, pos):
            left_text = MathTex(left_side).shift(UP).next_to(critical_points_text, RIGHT, buff=1).shift(DOWN * pos)
            right_text = MathTex(f"={right_exprs[0]}").next_to(left_text, RIGHT)

            self.play(Write(left_text), Write(right_text))

            # Transformar solo la parte derecha en cada paso
            for step in right_exprs[1:]:
                new_right_text = MathTex(f" {step}").next_to(left_text, RIGHT)
                self.play(Transform(right_text, new_right_text))
                self.wait(1)

            return left_text, right_text

        # Lista para almacenar todas las expresiones
        all_expressions = []

        # Realizar las evaluaciones
        for i, (label, steps) in enumerate(eval_steps):
            left_text, right_text = eval_and_transform(label, steps, i)
            all_expressions.extend([left_text, right_text])

        # Esperar antes de eliminar las expresiones no deseadas
        self.wait(2)

        # Crear un rectángulo amarillo alrededor de las expresiones deseadas (segunda y tercera)
        box_max=SurroundingRectangle(VGroup(all_expressions[2],all_expressions[3]))
        box_min=SurroundingRectangle(VGroup(all_expressions[4],all_expressions[5]))

        self.play(Create(box_max))
        self.play(FadeOut(VGroup(all_expressions[0],all_expressions[1],all_expressions[6],all_expressions[7])))
        max_text=Tex(r"Máximo",color=YELLOW).next_to(box_max,RIGHT, buff=0.5)
        self.play(Create(max_text))
        self.play((Create(box_min)))
        min_text=Tex(r"Mínimo",color=YELLOW).next_to(box_min,RIGHT, buff=0.5)
        self.play(Create(min_text))
        # Esperar un poco para que se vea el resultado final
        self.wait(2)

