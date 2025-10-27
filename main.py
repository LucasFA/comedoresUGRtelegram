from telegram.ext import Application

def main():
    print("Hello from comedoresugrtelegram!")
    application = Application.builder().token(token).concurrent_updates(True).read_timeout(30).write_timeout(30).build()
    application.run_polling()


if __name__ == "__main__":
    main()
