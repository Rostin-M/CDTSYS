import reflex as rx
from CDTSYS.pages.index import index
from CDTSYS.pages.about import about
from CDTSYS.pages.login import login
from CDTSYS.pages.signup import signup
from CDTSYS.components.chat import main_page_chat
from CDTSYS.pages.pricing import pricing
from CDTSYS.pages.contact import contact_form
from CDTSYS.pages.terminos import terminos

app = rx.App(
    theme=rx.theme(
        appearance="dark",
        accent_color="violet",
    ),
)
app.add_page(index, route="/")
app.add_page(about)
app.add_page(login)
app.add_page(signup)
app.add_page(main_page_chat, route="/main_page_chat")
app.add_page(pricing, route="/pricing")
app.add_page(contact_form, route="/contact")
app.add_page(terminos, route="/terminos")