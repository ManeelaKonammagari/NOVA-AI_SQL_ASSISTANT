# NOVA - run now

## Backend (Terminal 1)
cd backend
.\venv\Scripts\activate
python -m uvicorn app.main:app --reload

If your existing venv is one folder above/elsewhere, activate that existing venv instead.

## Frontend (Terminal 2)
cd frontend
npm install
npm run dev

If Windows says 'vite is not recognized', run:
npm install -D vite
npm run dev

## Important
Do NOT copy or create another venv. The Python venv and frontend node_modules are separate.
Use Chrome/Edge for microphone/wake-word testing.
