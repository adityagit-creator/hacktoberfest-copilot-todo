# To-Do List

A simple to-do list built with Streamlit. Tasks are kept in Streamlit session state, so they remain available while the current browser session is active.

## Run locally

1. Install Python 3.8 or newer.
2. Open a terminal in this project directory.
3. (Optional) Create and activate a virtual environment:

	```powershell
	python -m venv .venv
	.venv\Scripts\Activate.ps1
	```

4. Install the dependencies:

	```powershell
	pip install -r requirements.txt
	```

5. Start the app:

	```powershell
	streamlit run app.py
	```

Streamlit will open the app in your browser, usually at `http://localhost:8501`.

## Features

- Add tasks with the text field or the Add task button.
- Mark pending tasks as done.
- Delete pending or completed tasks.
- View pending and completed tasks in separate sections.