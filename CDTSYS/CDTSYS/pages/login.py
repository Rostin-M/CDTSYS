import reflex as rx
from CDTSYS.config.database import Session
from sqlalchemy.exc import NoResultFound
from sqlalchemy.sql import text

class LoginState(rx.State):
    form_data: dict = {}
    show_dialog: bool = False
    dialog_message: str = ""

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        email = form_data.get("email")
        password = form_data.get("password")
        
        if not email or not password:
            self.dialog_message = "Todos los campos son obligatorios. Por favor completa el email y la contraseña."
            self.show_dialog = True
            return

        session = Session()
        try:
            user = session.execute(
                text("SELECT * FROM usuarios WHERE correo = :email AND contraseña = :password"),
                {"email": email, "password": password}
            ).fetchone()
            if user:
                return rx.redirect("/main_page_chat")
            else:
                self.dialog_message = "Credenciales inválidas. Inténtalo de nuevo."
                self.show_dialog = True
        except NoResultFound:
            self.dialog_message = "Usuario no encontrado. Regístrate primero."
            self.show_dialog = True

    def close_dialog(self, value: bool):
        self.show_dialog = value 

def login() -> rx.Component:
    return rx.fragment( 
        rx.center(
            rx.card(
                rx.form(
                    rx.vstack(
                        rx.center(
                            rx.image(
                                src="/images/logo.jpg",
                                width="10em",
                                height="auto",
                                border_radius="25%",
                            ),
                            rx.heading(
                                "Inicia sesión en tu cuenta",
                                size="6",
                                as_="h2",
                                text_align="center",
                                width="100%",
                            ),
                            direction="column",
                            spacing="5",
                            width="100%",
                        ),
                        rx.vstack(
                            rx.text(
                                "Email",
                                size="3",
                                weight="medium",
                                text_align="left",
                                width="100%",
                            ),
                            rx.input(
                                placeholder="user@reflex.dev",
                                name="email",
                                type="email",
                                size="3",
                                width="100%",
                            ),
                            spacing="2",
                            width="100%",
                        ),
                        rx.vstack(
                            rx.hstack(
                                rx.text(
                                    "Contraseña",
                                    size="3",
                                    weight="medium",
                                ),
                                rx.link(
                                    "¿Olvidaste tu Contraseña?",
                                    href="#",
                                    size="3",
                                ),
                                justify="between",
                                width="100%",
                            ),
                            rx.input(
                                placeholder="Ingresa tu Contraseña",
                                name="password",
                                type="password",
                                size="3",
                                width="100%",
                            ),
                            spacing="2",
                            width="100%",
                        ),
                        rx.button(
                            "Iniciar Sesión", 
                            size="3", 
                            type="submit",
                            align_self="center",
                        ),                        
                        rx.center(
                            rx.text("¿Nuevo Aquí?", size="3"),
                            rx.link("Crea una Cuenta", href="signup", size="3"),
                            opacity="0.8",
                            spacing="2",
                            direction="row",
                            width="100%",
                        ),
                        spacing="6",
                        width="100%",
                    ),
                    on_submit=LoginState.handle_submit,
                    reset_on_submit=True,
                ),
                max_width="28em",
                size="4",
                width="100%",
            ),
            min_height="80vh",
            align_items="center",
            justify="center",
        ),
        rx.dialog.root(
            rx.dialog.content(
                rx.flex(
                    rx.dialog.title("Error"),
                    rx.dialog.description(LoginState.dialog_message),
                    rx.flex(
                        rx.dialog.close(
                            rx.button("Aceptar", size="3"),
                        ),
                        justify="center",
                    ),
                    direction="column",
                    spacing="3",
                    align="center",
                    text_align="center",
                ),
                max_width="450px",
            ),
            open=LoginState.show_dialog,
            on_open_change=LoginState.close_dialog,
        )
    )