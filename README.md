# Potd
# 🌟 Pokémon of the Day (POTD)

A daily Discord bot that posts a randomly selected Pokémon with stats, abilities, flavor text, and evolution chain — powered by [PokéAPI](https://pokeapi.co) and GitHub Actions.

---

## 🔧 How It Works

- **Script:** `POTD.py` fetches a random Pokémon using PokéAPI and formats the data for Discord
- **Automation:** GitHub Actions runs the script every day at **7 45 AM Gmt**
- **Delivery:** Posts directly to a Discord channel via webhook

---

## 📦 Features

- Random Pokémon selection (up to Gen IX)
- Full stat breakdown
- Evolution chain traversal
- English flavor text
- Sprite image link
- Discord-friendly formatting

---

## 🚀 Setup

1. Clone this repo or fork it
2. Add your Discord webhook URL to `POTD.py`:

   ```python
   webhook_url = "https://discord.com/api/webhooks/..."
Commit and push

🤖 GitHub Actions
The workflow file is located at:

Code
.github/workflows/potd.yml
It runs daily using:

yaml
on:
  schedule:
    - cron: '0 7 * * *'  # 8 AM BST
  workflow_dispatch:
Dependencies are installed via:

yaml
run: python -m pip install requests pillow
🧪 Testing
To manually trigger the workflow:

Go to the Actions tab

Select Daily Pokémon Drop

Click Run workflow

🛡️ Notes
No local JSON files required — all data is fetched live

If PokéAPI is down, the script will fail gracefully

Timing may vary slightly due to GitHub runner availability

🐛 Issues & Contributions
Feel free to open issues or submit pull requests for:

Embed formatting

Shiny variants

Logging enhancements

Alternate data sources

📜 License
MIT — free to use, modify, and share.

Built by Dean, automated with flair, and themed for fans. Gotta drop 'em all.

Code

---

Let me know if you want to add badges, a sample Discord screenshot, or a changelog section. We
