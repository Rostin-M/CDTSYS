import reflex as rx

def terminos() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("CDTSYS - Términos y Condiciones", size="4", text_align="center", margin_bottom="1em"),
            
            rx.box(
                rx.text("1. Uso de la Plataforma:", font_weight="bold"),
                rx.text(
                    "Al utilizar CDTSYS, aceptas cumplir con los términos de uso aquí establecidos, aplicables a servicios "
                    "financieros y consultas sobre Certificados de Depósito a Término (CDT) en Colombia.",
                    margin_left="1em",
                    line_height="1.6em",
                ),
                background_color=rx.color("mauve", 3),
                padding="1em",
                border_radius="8px",
                margin_bottom="1em",
            ),
            rx.box(
                rx.text("2. Responsabilidades del Usuario:", font_weight="bold"),
                rx.text(
                    "Eres responsable de mantener la confidencialidad de tus credenciales. Las consultas y recomendaciones "
                    "son personalizadas, y su aplicación es responsabilidad exclusiva del usuario.",
                    margin_left="1em",
                    line_height="1.6em",
                ),
                background_color=rx.color("mauve", 3),
                padding="1em",
                border_radius="8px",
                margin_bottom="1em",
            ),
            rx.box(
                rx.text("3. Limitaciones de Responsabilidad:", font_weight="bold"),
                rx.text(
                    "CDTSYS no garantiza la rentabilidad de inversiones sugeridas y no se hace responsable de pérdidas financieras "
                    "resultantes del uso de nuestras recomendaciones.",
                    margin_left="1em",
                    line_height="1.6em",
                ),
                background_color=rx.color("mauve", 3),
                padding="1em",
                border_radius="8px",
            ),
            
            rx.heading("Política de Privacidad de CDTSYS", size="4", text_align="center", margin_top="2em", margin_bottom="1em"),
            rx.box(
                rx.text("1. Recolección de Datos:", font_weight="bold"),
                rx.text(
                    "Recopilamos datos personales y financieros de usuarios para ofrecer una experiencia personalizada en la "
                    "apertura y gestión de CDTs en Colombia.",
                    margin_left="1em",
                    line_height="1.6em",
                ),
                background_color=rx.color("mauve", 3),
                padding="1em",
                border_radius="8px",
                margin_bottom="1em",
            ),
            rx.box(
                rx.text("2. Uso de Información:", font_weight="bold"),
                rx.text(
                    "La información recolectada será utilizada para proporcionar recomendaciones financieras personalizadas "
                    "y mejorar la calidad de nuestro servicio.",
                    margin_left="1em",
                    line_height="1.6em",
                ),
                background_color=rx.color("mauve", 3),
                padding="1em",
                border_radius="8px",
                margin_bottom="1em",
            ),
            rx.box(
                rx.text("3. Seguridad de los Datos:", font_weight="bold"),
                rx.text(
                    "CDTSYS garantiza la seguridad y confidencialidad de la información personal, aplicando medidas de "
                    "seguridad conforme a estándares del sector financiero en Colombia.",
                    margin_left="1em",
                    line_height="1.6em",
                ),
                background_color=rx.color("mauve", 3),
                padding="1em",
                border_radius="8px",
            ),
            
            rx.heading("Información Legal - CDTSYS", size="4", text_align="center", margin_top="2em", margin_bottom="1em"),
            rx.box(
                rx.text("1. Jurisdicción:", font_weight="bold"),
                rx.text(
                    "Los servicios de CDTSYS se rigen por las leyes colombianas aplicables al sector financiero.",
                    margin_left="1em",
                    line_height="1.6em",
                ),
                background_color=rx.color("mauve", 3),
                padding="1em",
                border_radius="8px",
                margin_bottom="1em",
            ),
            rx.box(
                rx.text("2. Propiedad Intelectual:", font_weight="bold"),
                rx.text(
                    "Todo el contenido, marca y software de CDTSYS son propiedad exclusiva de nuestra empresa y están protegidos "
                    "por las leyes de propiedad intelectual de Colombia.",
                    margin_left="1em",
                    line_height="1.6em",
                ),
                background_color=rx.color("mauve", 3),
                padding="1em",
                border_radius="8px",
                margin_bottom="1em",
            ),
            rx.box(
                rx.text("3. Contacto Legal:", font_weight="bold"),
                rx.text(
                    "Para cualquier consulta legal relacionada con CDTSYS, contáctanos a través de los canales oficiales en nuestra "
                    "sección de contacto.",
                    margin_left="1em",
                    line_height="1.6em",
                ),
                background_color=rx.color("mauve", 3),
                padding="1em",
                border_radius="8px",
            ),
            
            rx.link(
                rx.button(
                    "Regresar",
                    color="white",
                    background_color=rx.color("accent", 11),
                    size="lg",
                    padding_y="0.75em",
                    padding_x="1.5em",
                    border_radius="8px",
                    _hover={"background_color": rx.color("accent", 9)},
                ),
                href="/",
                style={"textDecoration": "none"},
            ),
            align_items="center",
            padding="2em",
            max_width="50em",
            background_color=rx.color("mauve", 1),
            border_radius="8px",
            box_shadow="lg",
        ),
        padding_y="2em",
    )