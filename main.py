import os
import http.server
# from bokeh import export_png
from dotenv import load_dotenv
from telegram import Update, ForceReply
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


def main():
    load_dotenv()
    token = os.getenv("TELEGRAM_TOKEN")
    if not token:
        raise RuntimeError("Telegram token not defined")

    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("lunes", lunes))
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(CommandHandler("help", help))

    app.run_polling()


def screenshot(dia):
    export_png(plot, filename="")


def get_website():
    import requests

    try:
        response = requests.get(
            "https://scu.ugr.es/#__doku_menu_semanal_comedor_pts_-_menu_1"
        )
    except Exception as e:
        raise RuntimeError("Failed to get the menu from the website:", type(e).__name__)
    # if response.codes
    response.raise_for_status()
    return response.text


def target_html():
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, "html.parser")

    # Find the specific h1 by its anchor ID
    anchor = soup.find("a", {"id": "__doku_menu_semanal_comedores_-_menu_11"})
    if not anchor:
        raise ValueError("Could not find the menu anchor in HTML")

    # The <h1> tag itself
    section_h1 = anchor.find_parent("h1")

    # Next div (contains the tables)
    section_div = section_h1.find_next_sibling("div")

    # Combine into one HTML snippet
    target_html = str(section_h1) + str(section_div)

def generate_image_from_html():
    import imgkit
    
    IMG_PATH = "menu.png"
    options = {
        "encoding": "UTF-8",
        "quiet": "",
        "format": "png",
        "zoom": "1.5",  # scale up for readability
    }
    
    imgkit.from_string(target_html, IMG_PATH, options=options)

async def lunes(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_photo(photo=open('lunes.png', "rb"))


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Hello {update.effective_user.first_name}")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hola {user.mention_html()}! Todavía estoy en desarrollo. Vuelve más tarde!",
    )


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


if __name__ == "__main__":
    main()
