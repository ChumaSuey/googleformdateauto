# Google Forms Date Auto-Filler

Automated script to fill today's date in multiple Google Forms.

## 🚀 Quick Start

### Prerequisites

- Node.js installed on your system

### Installation

1. Install dependencies:

```bash
npm install
```

1. Install Playwright browsers:

```bash
npm run install-playwright
```

### Running the Script

```bash
npm start
```

Or directly:

```bash
node gfdauto.js
```

## 📝 What It Does

The script automatically:

1. Opens 3 Google Forms in separate tabs
2. Fills in today's date in each form
3. Keeps the browser open for you to review/submit

## 🔧 Files

### JavaScript (New)

- **`gfdauto.js`** - Main Playwright script. Faster, more reliable, and doesn't require manual driver management.

### Python (Legacy)

The original Selenium implementations are preserved for reference:

- **`googleformdateauto.py`** - Full version with comments explain the logic. Good for learning how the Selenium implementation works.
- **`gfdauto2.py`** - Clean version without comments.

## 💡 Key Features

- ✅ Uses Playwright for modern browser automation
- ✅ Async/await for clean, readable code
- ✅ Automatically manages browser drivers
- ✅ Keeps browser open after completion

## 🐍 Python vs JavaScript

The new JavaScript version replaces the Python scripts but functionality remains the same:

- **Python**: Uses `selenium` + `chromedriver` (requires matching driver version)
- **JavaScript**: Uses `playwright` (auto-manages binaries, handles multi-tabs natively)

---

*Created by Chuma and Nepta*
