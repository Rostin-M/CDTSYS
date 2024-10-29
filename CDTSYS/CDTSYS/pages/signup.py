import time
import reflex as rx
from CDTSYS.config.database import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql import text

class SignupState(rx.State):
    form_data: dict = {}
    show_success_dialog: bool = False
    dialog_message: str = ""

    def handle_submit(self, form_data: dict):
        self.form_data = form_data
        nombre = form_data.get("nombre")
        correo = form_data.get("correo")
        contraseña = form_data.get("contraseña")
        
        if not nombre or not correo or not contraseña:
            self.dialog_message = "Todos los campos son obligatorios. Por favor completa todos los campos."
            self.show_success_dialog = True
            return

        session = Session()
        try:
            session.execute(
                text("INSERT INTO usuarios (nombre, correo, contraseña) VALUES (:nombre, :correo, :contraseña)"),
                {"nombre": nombre, "correo": correo, "contraseña": contraseña}
            )
            session.commit()
            self.dialog_message = "Te has registrado exitosamente. Por favor inicia sesión ahora."
            self.show_success_dialog = True
        except IntegrityError:
            self.dialog_message = "Error: El correo ya se encuentra registrado. Por favor, intenta con otro correo."
            self.show_success_dialog = True

    def close_dialog(self, _ev=None):
        if "exitosamente" in self.dialog_message:
            time.sleep(0.5)
            return rx.redirect("/")
        self.show_success_dialog = False

def signup() -> rx.Component:
    return rx.box(
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
                                "Crea una Cuenta",
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
                                "Nombre",
                                size="3",
                                weight="medium",
                                text_align="left",
                                width="100%",
                            ),
                            rx.input(
                                placeholder="Tu Nombre",
                                name="nombre",
                                size="3",
                                width="100%",
                            ),
                            spacing="2",
                            width="100%",
                        ),
                        rx.vstack(
                            rx.text(
                                "Correo",
                                size="3",
                                weight="medium",
                                text_align="left",
                                width="100%",
                            ),
                            rx.input(
                                placeholder="user@reflex.dev",
                                name="correo",
                                type="email",
                                size="3",
                                width="100%",
                            ),
                            spacing="2",
                            width="100%",
                        ),
                        rx.vstack(
                            rx.text(
                                "Contraseña",
                                size="3",
                                weight="medium",
                                text_align="left",
                                width="100%",
                            ),
                            rx.input(
                                placeholder="Ingresa tu Contraseña",
                                name="contraseña",
                                type="password",
                                size="3",
                                width="100%",
                            ),
                            spacing="2",
                            width="100%",
                        ),
                        rx.center(
                            rx.button(
                                "Registrar",
                                size="3",
                                type="submit",
                            ),
                            spacing="6",
                            width="100%",
                        ),
                    ),
                    on_submit=SignupState.handle_submit,
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
                    rx.dialog.title("Registro"),
                    rx.dialog.description(SignupState.dialog_message),
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
            open=SignupState.show_success_dialog,
            on_open_change=SignupState.close_dialog,
        )
    )