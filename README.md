This is a simple Gemini wrapper chatbot, to be used as a starter pack.

Built with Django and Google Generative AI.

1. Create virtual environment and activate it.
2. Install dependencies: "pip install -r requirements.txt".
3. Create .env in core folder, set SECRET_KEY, ENVIRONMENT (development), GEMINI_API_KEY (https://ai.google.dev/gemini-api)
4. Apply migrations "python manage.py makemigrations && python manage.py migrate"
5. Run server "python manage.py runserver" at http://127.0.0.1:8000/
