import reflex as rx

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium", class_name="text-white hover:text-purple-300 transition-all duration-300"),
        href=url,
        class_name="px-3 py-2 rounded-md hover:bg-gray-700 transition-all duration-300"
    )

def navbar_buttons() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/images/logo.jpg",
                        width="2.5em",
                        height="auto",
                        border_radius="25%",
                        class_name="mr-2"
                    ),
                    rx.heading("CDTSYS", size="7", weight="bold", class_name="text-white tracking-wide"),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Inicio", "/"),
                    navbar_link("Sobre Nosotros", "/about"),
                    navbar_link("Precios", "/pricing"),            
                    spacing="5",
                ),
                rx.hstack(
                    navbar_link("Crear Cuenta", "/signup"),
                    navbar_link("Iniciar Sesión", "/login"),
                    spacing="4",
                    justify="end",
                    class_name="mr-16"
                ),
                justify="between",
                align_items="center",
                width="100%",
            ),
        ),
        
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/images/logo.jpg",
                        width="2.5em",
                        height="auto",
                        border_radius="25%",
                        class_name="mr-2"
                    ),
                    rx.heading("CDTSYS", size="6", weight="bold", class_name="text-white tracking-wide"),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30, class_name="text-white")
                    ),
                    rx.menu.content(
                        rx.menu.item(navbar_link("Inicio", "/")),
                        rx.menu.item(navbar_link("Sobre Nosotros", "/about")),
                        rx.menu.item(navbar_link("Precios", "/pricing")),
                        rx.menu.separator(),
                        rx.menu.item(navbar_link("Crear Cuenta", "/signup")),
                        rx.menu.item(navbar_link("Iniciar Sesión", "/login")),                        
                    ),
                    class_name="mr-6 bg-gray-800 rounded-md p-2 shadow-lg",
                    justify="end",
                ),
                justify="between",
                align_items="center",
                width="100%",
            ),
        ),
        
        style={"background-color": "#6A0DAD"},
        padding="1em",
        position="fixed",
        top="0px",
        z_index="10",
        width="100%",
        justify="center",
        align="center",
        left="0px",
        margin="0px",
        class_name="shadow-lg",
    )