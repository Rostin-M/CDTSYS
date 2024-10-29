import reflex as rx

def form_field(label: str, placeholder: str, type: str, name: str) -> rx.Component:
    return rx.form.field(
        rx.flex(
            rx.form.label(label, class_name="text-sm font-semibold text-gray-700 dark:text-gray-300"),
            rx.form.control(
                rx.input(
                    placeholder=placeholder, type=type, class_name="p-2 rounded border border-gray-300 dark:border-gray-600"
                ),
                as_child=True,
            ),
            direction="column",
            spacing="1",
        ),
        name=name,
        width="100%",
    )

def contact_form() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button("Contactarnos", class_name="bg-purple-500 hover:bg-purple-600 text-white font-bold py-2 px-4 rounded-full shadow-md mx-auto mt-4")
        ),
        
        rx.dialog.content(
            rx.dialog.title("Formulario de Contacto", class_name="text-2xl font-bold text-purple-500 text-center mb-4"),
            rx.dialog.description(
                "Rellena el formulario para ponerte en contacto con nosotros.",
                class_name="text-center mb-6 text-gray-600 dark:text-gray-300"
            ),
            rx.form.root(
                rx.flex(
                    rx.flex(
                        form_field("Nombre", "Escribe tu nombre", "text", "first_name"),
                        form_field("Apellido", "Escribe tu apellido", "text", "last_name"),
                        spacing="3",
                        flex_direction=["column", "row", "row"],
                    ),
                    rx.flex(
                        form_field("Correo Electrónico", "correo@ejemplo.com", "email", "email"),
                        form_field("Teléfono", "Teléfono de contacto", "tel", "phone"),
                        spacing="3",
                        flex_direction=["column", "row", "row"],
                    ),
                    rx.flex(
                        form_field("Empresa", "Nombre de tu empresa (opcional)", "text", "company"),
                        spacing="3",
                    ),
                    rx.flex(
                        rx.text("Razón de Contacto", class_name="text-sm font-semibold text-gray-700 dark:text-gray-300"),
                        rx.text_area(
                            placeholder="Escribe tu mensaje",
                            name="message",
                            resize="vertical",
                            class_name="p-2 rounded border border-gray-300 dark:border-gray-600"
                        ),
                        direction="column",
                        spacing="1",
                    ),
                    rx.form.submit(
                        rx.button("Enviar", class_name="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded-full shadow-md mx-auto mt-4"),
                        as_child=True,
                    ),
                    direction="column",
                    spacing="4",
                    width="100%",
                ),
                on_submit=lambda form_data: handle_form_submit(form_data),
                reset_on_submit=True,
            ),
            rx.dialog.close(
                rx.button("Cerrar", class_name="mt-6 bg-gray-400 hover:bg-gray-500 text-white font-bold py-2 px-4 rounded-full shadow-md mx-auto"),
            ),
            size="lg",
        ),
    )

def handle_form_submit(form_data):
    return rx.window_alert(f"Formulario enviado: {form_data.to_string()}")