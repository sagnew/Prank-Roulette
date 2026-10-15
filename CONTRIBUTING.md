# Contributing to Prank-Roulette

Thank you for wanting to contribute to **Prank-Roulette** — the Flask-powered prank game using Twilio! Pull requests are welcome.

## Table of Contents

- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [How to Contribute](#how-to-contribute)
- [Pull Request Process](#pull-request-process)
- [Code Style](#code-style)
- [Reporting Bugs](#reporting-bugs)

## Getting Started

1. **Fork** this repository
2. **Clone** your fork: `git clone https://github.com/YOUR-USERNAME/Prank-Roulette.git`
3. **Create a virtual environment** and install dependencies
4. **Configure** your Twilio credentials

## Development Setup

### Prerequisites

- Python >= 3.8
- A [Twilio](https://www.twilio.com) account with a phone number
- [ngrok](https://ngrok.com/) (for local webhook development)

### Install Dependencies

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install packages
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file in the project root (never commit this!):

```
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=+1234567890
```

### Run Locally

```bash
# Start Flask dev server
python app.py

# In another terminal, expose with ngrok
ngrok http 5000
```

Configure your Twilio phone number's webhook to point to your ngrok URL.

## How to Contribute

### What We Welcome

- 🎭 **New prank types** — Creative, funny, harmless additions to the roulette
- 🐛 **Bug fixes** — Fix webhook handling, Twilio API errors, or routing issues
- 🎨 **UI improvements** — Better frontend styling or UX for the web interface
- 📚 **Documentation** — Clearer setup instructions, troubleshooting tips
- 🧪 **Tests** — Unit tests for prank logic or Twilio wrapper
- 🔒 **Security** — Webhook signature validation improvements

## Pull Request Process

1. Branch naming: `feat/new-prank-type` or `fix/webhook-error`
2. Keep PRs focused — one change per PR
3. Test your change end-to-end with a real (or mock) Twilio webhook
4. Describe what the prank does (for new prank additions) or what was broken (for fixes)
5. Add/update `requirements.txt` if you add new packages

### PR Title Format

- `feat: add reverse speech audio prank`
- `fix: handle Twilio webhook timeout gracefully`
- `docs: add ngrok setup instructions to README`

## Code Style

- Follow **PEP 8** — use `flake8` or `black` to format
- Use **meaningful variable names**
- Add **comments** for non-obvious Twilio API calls
- Keep `twilio_wrapper.py` as the single abstraction layer for Twilio calls
- Don't hardcode credentials — always use environment variables

## Reporting Bugs

Please include:
- Python version
- Twilio SDK version (`pip show twilio`)
- The prank type that triggered the bug
- Error message / stack trace
- Steps to reproduce

Open an issue at: https://github.com/sagnew/Prank-Roulette/issues

---

Keep it fun, keep it harmless! 🎉