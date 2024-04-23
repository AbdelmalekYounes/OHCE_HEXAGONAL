from adapters.console_adapter import run_console_app
from adapters.flask_adapter import app

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'api':
        app.run(port=5000)
    else:
        run_console_app()
