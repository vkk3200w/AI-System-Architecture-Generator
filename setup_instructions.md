# Setup Instructions - AI System Architecture Generator

Follow these steps to get the application running on your local machine.

## Prerequisites

- **Python 3.9+**
- **Node.js (v16+)** & **npm**

## 1. Backend Setup (FastAPI)

1.  Navigate to the project root `ai-architecture-generator`:
    ```bash
    cd c:/project/arcgen
    ```

2.  (Optional) Create and activate a virtual environment:
    ```bash
    python -m venv venv
    # Windows:
    .\venv\Scripts\activate
    # Mac/Linux:
    source venv/bin/activate
    ```

3.  Install dependencies:
    ```bash
    pip install -r backend/requirements.txt
    ```

4.  Start the server (from root):
    ```bash
    python -m uvicorn backend.main:app --reload
    ```
    The API will be available at `http://localhost:8000`.

## 2. Frontend Setup (React + Vite)

1.  Navigate to the `frontend` directory:
    ```bash
    cd frontend
    ```

2.  Install dependencies:
    ```bash
    npm install
    ```

3.  Start the development server:
    ```bash
    npm run dev
    ```
    The application will be available at `http://localhost:5173`.

## 3. Configuration (Optional)

To use the real AI generation features:
1.  Obtain a Google Gemini API Key.
2.  Enter it into the input field on the home page.
    *OR*
3.  Create a `.env` file in `backend/` and add:
    ```
    GOOGLE_API_KEY=your_api_key_here
    ```

If no key is provided, the system will run in **Mock Mode** for testing purposes.
