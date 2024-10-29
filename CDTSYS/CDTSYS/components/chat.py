import reflex as rx
import reflex_chakra as rc
from CDTSYS.components import loading_icon
from CDTSYS.state.state import QA, State
from CDTSYS.components.navbar_chat import navbar

message_style = dict(display="inline-block", padding="1em", border_radius="8px", max_width=["30em", "30em", "50em", "50em", "50em", "50em"])

def message(qa: QA) -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.markdown(
                qa.question,
                background_color=rx.color("mauve", 4),
                color=rx.color("mauve", 12),
                **message_style,
            ),
            text_align="right",
            align_self="flex-end",
            margin_top="1em",
        ),
        rx.box(
            rx.markdown(
                qa.answer,
                background_color=rx.color("accent", 4),
                color=rx.color("accent", 12),
                **message_style,
            ),
            text_align="left",
            align_self="flex-start",
            padding_top="1em",
        ),
        width="100%",
    )

def chat() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.vstack(
                rx.foreach(State.chats[State.current_chat], message),
            ),
            width="70%",
            padding="1em",
        ),
        rx.box(
            rx.video(
                url="https://youtu.be/St8mZG5ONL0?si=YsI520_AZ4CTVKMi",
                width="400px",
                height="auto",
                playing=True,
                loop=True,
                controls=False,
                muted=True,
            ),
            position="fixed",
            right="0",
            top="0",
            width="30%",
            padding="1em",
        )
    )


def action_bar() -> rx.Component:
    """The action bar to send a new message."""
    return rx.container(
        rc.form(
            rc.form_control(
                rx.hstack(
                    rx.input(
                        placeholder="Pregúntame algo...",
                        id="question",
                        width=["15em", "20em", "45em", "50em", "50em", "50em"],
                    ),
                    rx.button(
                        rx.cond(
                            State.processing,
                            loading_icon(height="1em"),
                            rx.text("Preguntar"),
                        ),
                        type="submit",
                    ),
                    align_items="center",
                ),
                is_disabled=State.processing,
            ),
            on_submit=State.process_question,
            reset_on_submit=True,
        ),
        position="fixed",
        bottom="0",
        left="0",
        padding="16px",
        backdrop_filter="auto",
        backdrop_blur="lg",
        border_top=f"1px solid {rx.color('mauve', 3)}",
        background_color=rx.color("mauve", 2),
        width="100%",
        z_index="1000",
    )

def page_content() -> rx.Component:
    """Footer content with logo, informational text, and copyright."""
    return rx.container(
        rx.vstack(
            rx.center(
                rx.image(
                    src="/images/logo.jpg",
                    width="5em",
                    height="auto",
                    margin_bottom="1em",
                )
            ),
            rx.text(
                "Puedo generar respuestas incorrectas o engañosas. Utilízame con cuidado.",
                text_align="center",
                font_size=".75em",
                color=rx.color("mauve", 10),
            ),
            rx.text(
                "CDSYS, tu asistente financiero",
                text_align="center",
                font_size=".75em",
                color=rx.color("mauve", 10),
            ),
            rx.spacer(),
            rx.text(
                "© 2024 CDTSYS. Todos los derechos reservados.",
                text_align="center",
                class_name="text-sm text-gray-400 text-center",
                margin_top="2em",
            ),
            rx.link(
                "Términos y Condiciones",
                href="/terminos",
                font_size=".75em",
                color=rx.color("accent", 11),
                text_align="center",
                margin_top="0.5em",
                opacity="0.8",
            ),
            align_items="center",
            padding="2em",
        ),
        margin_top="5em",
    )

def main_page_chat() -> rx.Component:
    """Main layout combining the navbar, chat, action bar, and footer content."""
    return rx.container(
        rx.vstack(
            navbar(),
            chat(),
            page_content(), 
            action_bar(),
            align_items="center",
            stack_children_full_width=True,
        ),
    )
