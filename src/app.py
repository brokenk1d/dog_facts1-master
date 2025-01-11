"""Main module for running the application"""

from start_app import StartApp

_START_COMANDS = ["start", "help", "info", "s", "h", "i"]

if __name__ == '__main__':
    app = StartApp(_START_COMANDS)
    app.start_polling()
