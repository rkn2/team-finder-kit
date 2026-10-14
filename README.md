# Team Finder Kit

Build your own research **Team Finder** in ChatGPT or Claude. Paste in a funding call and get three possible teams from your own network of researchers, each with reasons, the expertise still missing, and a draft intro email. Then review the teams in a dashboard that opens in any web browser.

From the [Penn State Digital Twin Hub](https://digitaltwin.psu.edu). Everything in this kit is **made-up sample data** (fictional people with `@example.edu` emails and a fictional funding call), so you can try it right away and swap in your own people later.

## Get started

1. **[Download the kit (zip)](https://github.com/rkn2/team-finder-kit/raw/main/team-finder-kit.zip)** and unzip it.
2. Open **`HOW-TO.pdf`**. It walks you through setup in about 15 minutes.

## What's inside

| File | What it is |
|---|---|
| `HOW-TO.pdf` / `HOW-TO.md` | Step-by-step setup for a ChatGPT Custom GPT or Project, or a Claude Project |
| `instructions.md` | What you paste into ChatGPT or Claude as its instructions |
| `sample-roster.csv` | 10 fictional researchers, and a template for your own list |
| `sample-call.txt` | A fictional funding call to test with |
| `dashboard.html` | Double-click to open in a browser. Paste the chat's results, mark people ✓ In / ? Maybe / ✗ Out, keep notes, see the co-author network, and copy the email. Nothing leaves your computer. |

## Privacy

Uploading a roster to ChatGPT or Claude sends it to OpenAI or Anthropic. Use only information people have agreed to share, and use your institution's licensed version of the tool when you can.

## For maintainers

`dashboard.html` is built from `dashboard.src.html` with the sample data embedded: `python3 build_dashboard.py`. `sample-result.json` is the made-up example the dashboard shows on first open.

Questions: Rebecca Napolitano, nap@psu.edu
