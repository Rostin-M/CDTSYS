import reflex as rx
import reflex_chakra as rc
from CDTSYS.components import chat
from CDTSYS.components.navbar_chat import navbar

def index_chat() -> rx.Component:
    """The main app."""
    return rc.vstack(
        navbar(),
        chat.chat(),
        chat.action_bar(),
        background_color=rx.color("mauve", 1),
        color=rx.color("mauve", 12),
        min_height="100vh",
        align_items="stretch",
        spacing="0",
    )