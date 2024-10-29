import reflex as rx
from CDTSYS.pages.navbar import navbar_buttons
from CDTSYS.pages.contact import contact_form

def pricing() -> rx.Component:
    return rx.container(
        navbar_buttons(),
        rx.color_mode.button(position="top-right", class_name="absolute right-4 top-4"),
        rx.vstack(
            rx.box(class_name="mt-20"),

            rx.heading(
                "Planes y Precios",
                class_name="text-5xl font-extrabold text-gray-900 dark:text-purple-400 text-center mb-6"
            ),

            rx.text(
                "Selecciona el plan que mejor se adapte a las necesidades de tu equipo. Cada plan está diseñado para brindarte acceso a las funcionalidades de CDTSYS de acuerdo con el tamaño de tu empresa.",
                class_name="text-lg text-gray-700 dark:text-gray-300 text-center mb-8 max-w-2xl mx-auto"
            ),

            rx.hstack(
                rx.box(
                    rx.image(
                        src="/images/basic_plan.jpg",
                        class_name="w-32 h-32 mx-auto mb-4 rounded-lg"
                    ),
                    rx.heading("Plan Básico", class_name="text-2xl font-bold text-gray-900 dark:text-purple-300 text-center"),
                    rx.text(
                        "Ideal para pequeños equipos o empresas que comienzan.",
                        class_name="text-gray-700 dark:text-gray-200 text-center italic mb-4"
                    ),
                    rx.text(
                        "0 - 50 personas",
                        class_name="text-lg text-gray-600 dark:text-gray-400 text-center"
                    ),
                    rx.text(
                        "COP $300,000 / mes",
                        class_name="text-xl font-bold text-gray-900 dark:text-white text-center mb-4"
                    ),
                    class_name="bg-gray-200 dark:bg-gray-800 p-8 rounded-lg shadow-lg w-80 h-104 flex flex-col items-center justify-between m-4"
                ),

                rx.box(
                    rx.image(
                        src="/images/business_plan.jpg",
                        class_name="w-32 h-32 mx-auto mb-4 rounded-lg"
                    ),
                    rx.heading("Plan Empresarial", class_name="text-2xl font-bold text-gray-900 dark:text-purple-300 text-center"),
                    rx.text(
                        "Para medianas empresas que necesitan más control y acceso.",
                        class_name="text-gray-700 dark:text-gray-200 text-center italic mb-4"
                    ),
                    rx.text(
                        "51 - 100 personas",
                        class_name="text-lg text-gray-600 dark:text-gray-400 text-center"
                    ),
                    rx.text(
                        "COP $500,000 / mes",
                        class_name="text-xl font-bold text-gray-900 dark:text-white text-center mb-4"
                    ),
                    class_name="bg-gray-200 dark:bg-gray-800 p-8 rounded-lg shadow-lg w-80 h-104 flex flex-col items-center justify-between m-4"
                ),

                rx.box(
                    rx.image(
                        src="/images/corporate_plan.jpg",
                        class_name="w-32 h-32 mx-auto mb-4 rounded-lg"
                    ),
                    rx.heading("Plan Corporativo", class_name="text-2xl font-bold text-gray-900 dark:text-purple-300 text-center"),
                    rx.text(
                        "Perfecto para grandes empresas que requieren funcionalidades avanzadas.",
                        class_name="text-gray-700 dark:text-gray-200 text-center italic mb-4"
                    ),
                    rx.text(
                        "101 - 500 personas",
                        class_name="text-lg text-gray-600 dark:text-gray-400 text-center"
                    ),
                    rx.text(
                        "COP $1,200,000 / mes",
                        class_name="text-xl font-bold text-gray-900 dark:text-white text-center mb-4"
                    ),
                    class_name="bg-gray-200 dark:bg-gray-800 p-8 rounded-lg shadow-lg w-80 h-104 flex flex-col items-center justify-between m-4"
                ),

                rx.box(
                    rx.image(
                        src="/images/custom_plan.jpg",
                        class_name="w-32 h-32 mx-auto mb-4 rounded-lg"
                    ),
                    rx.heading("Plan Personalizado", class_name="text-2xl font-bold text-gray-900 dark:text-purple-300 text-center"),
                    rx.text(
                        "Para organizaciones con necesidades únicas y grandes volúmenes de usuarios.",
                        class_name="text-gray-700 dark:text-gray-200 text-center italic mb-4"
                    ),
                    rx.text(
                        "Más de 1000 personas",
                        class_name="text-lg text-gray-600 dark:text-gray-400 text-center mb-2"
                    ),
                    rx.text(
                        "Para una valoración",
                        class_name="text-gray-800 dark:text-gray-300 text-center italic mb-2"
                    ),
                    class_name="bg-gray-200 dark:bg-gray-800 p-8 rounded-lg shadow-lg w-80 h-104 flex flex-col items-center justify-between m-4"
                ),

                class_name="flex flex-wrap justify-center"
            ),

            rx.box(
                rx.text(
                    "¿Necesitas una asesoría o mentoría para aprender a usar el software?",
                    class_name="text-xl text-gray-800 dark:text-gray-300 text-center mt-8 mb-2"
                ),
                rx.text(
                    "Ofrecemos entrenamientos adaptados a tus necesidades, con tarifas según el número de personas a capacitar.",
                    class_name="text-lg text-gray-600 dark:text-gray-400 text-center mb-4"
                ),
                class_name="bg-gray-200 dark:bg-gray-800 p-8 rounded-lg shadow-lg w-full max-w-3xl mx-auto mt-10"
            ),

            rx.box(
                rx.text(
                    "¿Ya decidiste cómo te ayudaremos?",
                    class_name="text-xl text-gray-800 dark:text-gray-300 text-center mt-8 mb-4"
                ),
                rx.dialog.root(
                    rx.dialog.trigger(
                        rx.button(
                            "Puedes"
                        )
                    ),
                    contact_form()
                ),
                class_name="flex flex-col items-center justify-center mt-4"
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
        )
    )