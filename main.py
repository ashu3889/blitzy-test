import os

def main():
    app_env = os.getenv("APP_ENV", "development")
    greeting = os.getenv("GREETING", "Hello")
    name = os.getenv("NAME", "World")
    print(f"[{app_env}] {greeting}, {name}!")


if __name__ == "__main__":
    main()