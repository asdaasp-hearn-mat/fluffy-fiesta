from manim import *

def transform_texts(scene, texts, static_text="", initial_position=ORIGIN, text_color=WHITE, scale_factor=1.0, font_size=30):
    """
    Muestra una lista de textos en la misma posición, transformando cada texto en el lugar del anterior
    mientras mantiene un texto estático constante en pantalla.

    Parameters:
    - scene: La escena de Manim en la que se realiza la animación.
    - texts: Lista de cadenas de texto para mostrar y transformar.
    - static_text: Texto que permanecerá constante en pantalla (opcional).
    - initial_position: La posición inicial donde se mostrará el primer texto.
    - text_color: Color del texto (opcional).
    - scale_factor: Factor de escala para el texto (opcional).
    - font_size: Tamaño de la fuente del texto (opcional).
    """
    if not texts:
        raise ValueError("La lista de textos no puede estar vacía.")
    
    # Crear el texto estático si se proporciona
    if static_text:
        static_tex = MathTex(static_text, color=text_color).scale(scale_factor).move_to(initial_position)
        scene.add(static_tex)
    else:
        static_tex=initial_position
    # Crear el primer texto
    current_text = MathTex(texts[0], color=text_color).scale(scale_factor).next_to(static_tex,RIGHT)
    scene.play(Write(current_text))
    
    # Transformar los textos sucesivos
    for next_text in texts[1:]:
        next_tex = MathTex(next_text, color=text_color).scale(scale_factor).next_to(static_tex,RIGHT,buff=0.1)
        scene.play(ReplacementTransform(current_text, next_tex))
        current_text = next_tex 
    # Retornar el texto final
    if static_tex:
        return VGroup(static_tex,current_text) 
    else: 
        return current_text
class DerivadaEscena(Scene):
    def construct(self):
         # Definir el texto inicial y el texto a transformar
        textos = [
            r"x \cos(x)",
            r"\frac{d}{dx} (x \cos(x))",
            r"\cos(x) + x(-\sin(x))",
            r"\cos(x) - x \sin(x)"
        ]
        
        # Texto estático que permanece constant
        
        # Mostrar y transformar los textos
        resultado_final = transform_texts(
            self, 
            textos, 
            initial_position=ORIGIN, 
            text_color=WHITE, 
            scale_factor=1.0, 
            font_size=30
        )
        
        # Si necesitas hacer algo con el resultado final
        self.wait(2)
