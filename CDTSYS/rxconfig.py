import reflex as rx

config = rx.Config(
    app_name="CDTSYS",
    tailwind={
        "theme": {
            "extend": {},
    },
    "plugins": ["@tailwindcss/typography"],
    },
)