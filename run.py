from app import main

from views import main_bp

if __name__ == "__main__":
    main.register_blueprint(main_bp)
    main.run(host='localhost', port=8000)
