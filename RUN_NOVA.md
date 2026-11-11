# NOVA — Authentication + Voice Verification

## 1. Backend

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
```

Set `NOVA_SECRET_KEY` in `.env` to a long random value, then start:

```powershell
python -m uvicorn app.main:app --reload
```

Swagger: `http://localhost:8000/docs`

## 2. Frontend

```powershell
cd frontend
npm install
npm run dev
```

## 3. Authentication flow

1. Sign up or log in with email/password.
2. NOVA redirects to Voice Authentication.
3. First-time users enroll a 4–5 second voice sample.
4. Existing users verify their enrolled voice.
5. Only the JWT containing `voice_verified=true` can pass the protected voice gate.

Voice signatures are stored under `backend/data/voice_profiles/` and user accounts persist in `backend/data/nova_auth.db`.

## 4. Wake word

On supported Chromium browsers, NOVA listens for **Hey NOVA**. In the authenticated workspace it opens the AI SQL Chat page. On the voice-authentication page it triggers voice verification.

Browser speech recognition support varies. Microphone permission must be granted.

## Security note

The voice matcher is a project/demo biometric gate, not anti-spoofing-grade identity proofing. Do not use it as the sole security control for sensitive production systems.
