import reflex as rx
from CDTSYS.pages.navbar import navbar_buttons
from rxconfig import config

def index() -> rx.Component:
    return rx.container(
        navbar_buttons(),
        rx.color_mode.button(position="top-right", class_name="absolute right-4 top-4"),
        rx.vstack(
            rx.box(class_name="mt-20"),

            rx.box(
                rx.heading(
                    "Bienvenido a ¡CDTSYS!", 
                    class_name="text-5xl font-extrabold text-purple-400 text-center"
                ),
                rx.text(
                    "Tu asistente virtual para la gestión de Certificados de Depósito a Término (CDTs).",
                    class_name="text-2xl text-purple-200 text-center mt-2"
                ),
                class_name="bg-gray-800 p-8 rounded-lg shadow-lg mb-8"
            ),
            
            rx.box(
                rx.text(
                    "Facilitamos el proceso de inversión para que encuentres las mejores opciones de CDTs, adaptadas a tus necesidades.",
                    class_name="text-lg text-gray-200 italic text-center"
                ),
                class_name="p-6 bg-gray-700 rounded-lg shadow mb-8 w-11/12 max-w-xl"
            ),
            
            rx.image(
                src="/images/finan_index.gif",
                class_name="w-full max-w-2xl h-auto mx-auto rounded-lg shadow-lg mb-8"
            ),
            
            rx.box(
                rx.text(
                    "Descubre las funcionalidades de CDTSYS y empieza a gestionar tus inversiones con facilidad y confianza.",
                    class_name="text-lg text-purple-300 text-center mb-6"
                ),
                rx.hstack(
                    rx.link(
                        rx.button(
                            "Consulta nuestra documentación", 
                            class_name="bg-purple-500 hover:bg-purple-600 text-white font-bold py-3 px-6 rounded-full shadow-md"
                        ),
                        href="https://github.com/Rostin-M/CDTSYS.git",
                        is_external=True,
                    ),
                    rx.link(
                        rx.button(
                            "Empieza ahora", 
                            class_name="bg-green-500 hover:bg-green-600 text-white font-bold py-3 px-6 rounded-full shadow-md"
                        ),
                        href="/signup",
                    ),
                    spacing="5",
                    justify="center",
                ),
                class_name="bg-gray-800 p-8 rounded-lg shadow-lg w-11/12 max-w-xl text-center"
            ),
            
            rx.box(
                rx.text(
                    "Con CDTSYS, tomar el control de tus inversiones es fácil y seguro. Nuestro asistente te ayudará a encontrar las mejores oportunidades en CDTs, ¡a solo un clic de distancia!",
                    class_name="text-lg text-center text-purple-200"
                ),
                class_name="bg-gray-800 p-6 rounded-lg shadow-lg w-11/12 max-w-2xl mt-8 mb-8"
            ),
            
            rx.box(
                rx.text(
                    "© 2024 CDTSYS. Todos los derechos reservados.",
                    class_name="text-sm text-gray-400 text-center"
                ),
                rx.hstack(
                    rx.link(
                        "Términos de Servicio",
                        href="/terminos",
                        class_name="text-sm text-gray-400 underline cursor-pointer"
                    ),
                    rx.text("|", class_name="text-sm text-gray-400"),
                    rx.link(
                        "Política de Privacidad",
                        href="/terminos",
                        class_name="text-sm text-gray-400 underline cursor-pointer"
                    ),
                    rx.text("|", class_name="text-sm text-gray-400"),
                    rx.link(
                        "Información Legal",
                        href="/terminos",
                        class_name="text-sm text-gray-400 underline cursor-pointer"
                    ),
                    spacing="1em",
                    justify="center",
                    align_items="center",
                ),
                class_name="bg-gray-800 p-4 rounded-lg shadow-lg w-full max-w-2xl text-center mt-8"
            ),

            spacing="10",
            justify="center",
            align_items="center",
            min_height="90vh",

        ),
    )