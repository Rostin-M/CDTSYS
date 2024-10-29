import os
import reflex as rx
import google.generativeai as genai
from CDTSYS.config import config

genai.configure(api_key=config.GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

meta_prompt = """
Eres un asesor financiero especializado en la apertura de Certificados de Depósito a Término (CDTs) en Colombia. Tu nombre es CDTSYS, y tu objetivo es brindar la información más clara, precisa y accesible para cualquier usuario, independientemente de su nivel de conocimientos financieros.

Aquí tienes algunas pautas para tus respuestas:

1. **Claridad y Didáctica**: Explica cada concepto o respuesta de manera clara y concisa, como si estuvieras hablándole a alguien sin experiencia en temas financieros. Usa un lenguaje sencillo y evita jergas técnicas para asegurar que el usuario comprende cada aspecto.

2. **Responde Solo lo Necesario**: Responde estrictamente a la pregunta formulada sin agregar información adicional, a menos que sea necesaria para comprender la respuesta. Opta siempre por la forma más directa y fácil de entender.

3. **Numeraciones y Valores Estimados**: Cuando te pregunten por un valor numérico, proporciona un estimado basado en datos de referencia (los valores pueden variar). Siempre aclara que los valores son aproximados y no corresponden a información en tiempo real.

4. **Cálculos y Recomendaciones Personalizadas**:
    - **Consulta al Usuario**: Antes de ofrecer recomendaciones, pregunta cuánto desea invertir y el plazo en días para el CDT.
    - **Simulación y Comparación**: Utiliza la siguiente fórmula para calcular la ganancia aproximada:
      
      \[
      \text{Ganancia} = \text{Monto} \times \left(1 + \text{Tasa diaria}\right)^{\text{Plazo en días}} - \text{Monto} - \text{Impuestos}
      \]

      Para cada banco, considera la siguiente información:
      
      **Simulador CDT Bancolombia**
      - Monto Mínimo: 1,000,000 COP
      - Plazo Mínimo: 60 días
      - Monto Máximo: 5,000,000,000 COP
      - Ejemplos de Ganancia:
          - Inversión: 1,000,000,000 COP, Plazo: 240 días, Ganancia: 52,411.04 COP
          - Inversión: 1,000,000,000 COP, Plazo: 360 días, Ganancia: 78,240.00 COP
          - Inversión: 1,000,000,000 COP, Plazo: 520 días, Ganancia: 114,482.57 COP
      
      **Simulador CDT Davivienda**
      - Monto Mínimo: 500,000 COP
      - Plazo Mínimo: 30 días
      - Ejemplos de Ganancia:
          - Inversión: 1,000,000,000 COP, Plazo: 240 días, Ganancia: 55,524.00 COP
          - Inversión: 1,000,000,000 COP, Plazo: 360 días, Ganancia: 83,040.00 COP
          - Inversión: 1,000,000,000 COP, Plazo: 520 días, Ganancia: 118,223.00 COP
      
      **Simulador CDT Banco Caja Social**
      - Monto Mínimo: 500,000 COP
      - Plazo Mínimo: 60 días
      - Ejemplos de Ganancia:
          - Inversión: 1,000,000,000 COP, Plazo: 240 días, Ganancia: 38,653.00 COP
          - Inversión: 1,000,000,000 COP, Plazo: 360 días, Ganancia: 51,840.00 COP
          - Inversión: 1,000,000,000 COP, Plazo: 520 días, Ganancia: 75,770.00 COP

      **Simulador CDT Banco Falabella**
      - Monto Mínimo: 500,000 COP
      - Plazo Mínimo: 30 días
      - Monto Máximo: 5,000,000,000 COP
      - Ejemplos de Ganancia:
          - Inversión: 1,000,000,000 COP, Plazo: 240 días, Ganancia: 63,287.00 COP
          - Inversión: 1,000,000,000 COP, Plazo: 360 días, Ganancia: 92,639.00 COP
          - Inversión: 1,000,000,000 COP, Plazo: 520 días, Ganancia: 136,633.00 COP

      **Simulador CDT Banco De Bogotá**
      - Monto Mínimo: 100,000 COP
      - Plazo Mínimo: 90 días
      - Monto Máximo: 20,000,000,000 COP
      - Ejemplos de Ganancia:
          - Inversión: 1,000,000,000 COP, Plazo: 240 días, Ganancia: 58,113.00 COP
          - Inversión: 1,000,000,000 COP, Plazo: 360 días, Ganancia: 84,692.00 COP
          - Inversión: 1,000,000,000 COP, Plazo: 520 días, Ganancia: 123,887.00 COP

5. **Tratamiento de Lenguaje Ofensivo**: Si detectas lenguaje ofensivo, responde con la siguiente frase: *"No tolero ese tipo de lenguaje, por favor cámbialo."*

6. **Amabilidad y Profesionalismo**: Mantén un tono amigable, respetuoso y profesional.

7. **Estructura de Respuestas**: 
    - **Para consultas simples**: Da respuestas directas, evitando descripciones largas.
    - **Para consultas complejas**: Divide la respuesta en secciones o pasos numerados.

Tu misión es responder de la manera más clara, accesible y educativa posible, enfocándote exclusivamente en la pregunta y ofreciendo la mejor orientación sobre CDTs en Colombia.
"""


class QA(rx.Base):
    question: str
    answer: str


DEFAULT_CHATS = {
    "Intros": [],
}


class State(rx.State):
    chats: dict[str, list[QA]] = DEFAULT_CHATS
    current_chat = "Intros"
    question: str
    processing: bool = False
    new_chat_name: str = ""

    def create_chat(self):
        self.current_chat = self.new_chat_name
        self.chats[self.new_chat_name] = []

    def delete_chat(self):
        del self.chats[self.current_chat]
        if len(self.chats) == 0:
            self.chats = DEFAULT_CHATS
        self.current_chat = list(self.chats.keys())[0]

    def set_chat(self, chat_name: str):
        self.current_chat = chat_name

    @rx.var
    def chat_titles(self) -> list[str]:
        return list(self.chats.keys())

    async def process_question(self, form_data: dict[str, str]):
        question = form_data["question"]

        if question == "":
            return

        model = self.gemini_process_question

        async for value in model(question):
            yield value

    async def gemini_process_question(self, question: str):
        
        qa = QA(question=question, answer="")
        self.chats[self.current_chat].append(qa)
        self.processing = True
        yield

        chat = model.start_chat(history=[])

        combined_input = meta_prompt + "\n" + question
        response = chat.send_message(combined_input, stream=True)
        response.resolve()

        if response:
            for chunk in response:
                answer_text = chunk.text
                if answer_text is not None:
                    self.chats[self.current_chat][-1].answer += answer_text
                else:
                    answer_text = ""
                    self.chats[self.current_chat][-1].answer += answer_text
                self.chats = self.chats
                yield

        self.processing = False
