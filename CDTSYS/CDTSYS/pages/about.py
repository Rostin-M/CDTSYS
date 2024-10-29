import reflex as rx
from CDTSYS.pages.navbar import navbar_buttons

def about() -> rx.Component:
    return rx.container(
        navbar_buttons(),
        rx.color_mode.button(position="top-right", class_name="absolute right-4 top-4"),
        rx.vstack(
            rx.box(class_name="mt-20"),

            rx.heading(
                "SOBRE NOSOTROS", 
                class_name="text-4xl font-extrabold text-purple-400 text-center py-4"
            ),
            
            rx.image(
                src="/images/equipo_about.jpg", 
                alt="Imagen de CDTSYS", 
                class_name="w-full max-w-xl h-auto mx-auto rounded-lg shadow-lg mb-8"
            ),
            
            rx.hstack(
                rx.box(
                    rx.heading("MISIÓN", class_name="text-2xl font-semibold text-purple-300 text-center mb-2"),
                    rx.text(
                        "Proporcionar herramientas y recursos que faciliten la gestión efectiva de CDTs.",
                        class_name="text-gray-300 text-center italic text-lg"
                    ),
                    class_name="bg-gray-800 p-5 rounded-lg shadow-lg w-1/2 m-2"
                ),
                rx.box(
                    rx.heading("VISIÓN", class_name="text-2xl font-semibold text-purple-300 text-center mb-2"),
                    rx.text(
                        "Ser el referente en soluciones de inversión en CDTs en Colombia, facilitando el acceso a información valiosa.",
                        class_name="text-gray-300 text-center italic text-lg"
                    ),
                    class_name="bg-gray-800 p-5 rounded-lg shadow-lg w-1/2 m-2"
                ),
                class_name="flex justify-center space-x-4"
            ),

            rx.box(
                rx.heading("EQUIPO DE TRABAJO", class_name="text-3xl font-bold text-purple-400 text-center mb-6"),
                
                rx.hstack(
                    rx.box(
                        rx.input.slot(rx.icon("user", size=40, class_name="text-purple-400 mb-3")),
                        rx.text("Rostin", class_name="text-purple-200 text-lg font-semibold text-center"),
                        rx.text("Ingeniería Sistemas", class_name="text-gray-300 text-center italic"),
                        class_name="bg-gray-800 p-4 rounded-lg shadow-lg w-1/5 m-2 flex flex-col items-center"
                    ),
                    rx.box(
                        rx.input.slot(rx.icon("user", size=40, class_name="text-purple-400 mb-3")),
                        rx.text("Meliza", class_name="text-purple-200 text-lg font-semibold text-center"),
                        rx.text("Ingeniería Sistemas", class_name="text-gray-300 text-center italic"),
                        class_name="bg-gray-800 p-4 rounded-lg shadow-lg w-1/5 m-2 flex flex-col items-center"
                    ),
                    rx.box(
                        rx.input.slot(rx.icon("user", size=40, class_name="text-purple-400 mb-3")),
                        rx.text("Daniel", class_name="text-purple-200 text-lg font-semibold text-center"),
                        rx.text("Ingeniería Financiera", class_name="text-gray-300 text-center italic"),
                        class_name="bg-gray-800 p-4 rounded-lg shadow-lg w-1/5 m-2 flex flex-col items-center"
                    ),
                    rx.box(
                        rx.input.slot(rx.icon("user", size=40, class_name="text-purple-400 mb-3")),
                        rx.text("Tomás", class_name="text-purple-200 text-lg font-semibold text-center"),
                        rx.text("Ingeniería Financiera", class_name="text-gray-300 text-center italic"),
                        class_name="bg-gray-800 p-4 rounded-lg shadow-lg w-1/5 m-2 flex flex-col items-center"
                    ),
                    rx.box(
                        rx.input.slot(rx.icon("user", size=40, class_name="text-purple-400 mb-3")),
                        rx.text("Tatiana", class_name="text-purple-200 text-lg font-semibold text-center"),
                        rx.text("Ingeniería Electrónica", class_name="text-gray-300 text-center italic"),
                        class_name="bg-gray-800 p-4 rounded-lg shadow-lg w-1/5 m-2 flex flex-col items-center"
                    ),
                    class_name="justify-center space-x-4"
                ),
                
                class_name="bg-gray-900 p-5 rounded-lg shadow-lg w-11/12 mx-auto my-4"
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