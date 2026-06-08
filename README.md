# Column to Comma-Separated Converter

A simple Streamlit app that converts column data into comma-separated lists with optional prefix and suffix.

## Features
- Convert column data to comma-separated format
- Add prefix and suffix to each item
- Choose custom separators (comma, semicolon, pipe, newline)
- Copy output to clipboard
- Clean, user-friendly interface

## Installation

### 1. Install Python (if not already installed)
Download from [python.org](https://www.python.org/downloads/)

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

## Running the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Usage

1. Paste your column data (one item per line or tab-separated)
2. Add optional prefix and suffix (e.g., single quotes `'`)
3. Select your separator (comma, semicolon, pipe, etc.)
4. Copy the result!

## Example

**Input:**
```
apple
banana
cherry
```

**With prefix: `'` and suffix: `'` and separator: `, `**

**Output:**
```
'apple', 'banana', 'cherry'
```

## Deploy on Streamlit Cloud

1. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
2. Sign in with GitHub
3. Click "New app"
4. Select this repository
5. Select `app.py` as the main file
6. Deploy!

Your app will be live at: `https://share.streamlit.io/YOUR_USERNAME/column-to-comma-separated`
- Edit files directly within the Codespace and commit and push your changes once you're done.

## What technologies are used for this project?

This project is built with:

- Vite
- TypeScript
- React
- shadcn-ui
- Tailwind CSS

## How can I deploy this project?

Simply open [Lovable](https://lovable.dev/projects/5d1369fd-308c-46d8-87d8-1138cbdf0ceb) and click on Share -> Publish.

## Can I connect a custom domain to my Lovable project?

Yes, you can!

To connect a domain, navigate to Project > Settings > Domains and click Connect Domain.

Read more here: [Setting up a custom domain](https://docs.lovable.dev/tips-tricks/custom-domain#step-by-step-guide)
