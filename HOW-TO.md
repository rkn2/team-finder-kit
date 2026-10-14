---
title: "Build Your Own Team Finder in ChatGPT (or Claude)"
subtitle: "Penn State Digital Twin Hub"
---

The Hub's Twin Team Finder takes a funding call and suggests three possible research teams from a network of people, each with reasons, the expertise still missing, and a draft intro email. You can set up the same thing in your own ChatGPT or Claude account in about 15 minutes.

This kit comes with **made-up sample data** (fictional people, `@example.edu` emails, and a fictional funding call) so you can try it right away. Swap in your own people when it works.

# What's in the kit

| File | What it is |
|---|---|
| `instructions.md` | The instructions you paste into ChatGPT or Claude. They tell it how to build teams and write the email. |
| `sample-roster.csv` | 10 fictional researchers. Use it as a test and as a template for your own list. |
| `sample-call.txt` | A fictional funding call to test with. |
| `dashboard.html` | A dashboard you open in any web browser to review the teams, mark people in or out, keep notes, and copy the email. No account or install. |

# Option 1: ChatGPT (Custom GPT)

You need ChatGPT Plus, Team, Enterprise, or Edu to make a Custom GPT.

1. Go to **chatgpt.com**, then **Explore GPTs** (or **GPTs**) → **+ Create**.
2. Click the **Configure** tab. Don't use the chat builder on the left.
3. **Name:** `Team Finder`. **Description:** `Suggests research teams for a funding call.`
4. **Instructions:** open `instructions.md`, copy everything, and paste it in.
5. **Knowledge:** click **Upload files** and add `sample-roster.csv`.
6. **Capabilities:** turn on **Code Interpreter & Data Analysis** so it can read the whole CSV. Web search is optional (helps if you paste only a link).
7. Click **Create**, and pick **Only me** (or share inside your workspace).
8. Test it: paste the text of `sample-call.txt` and send.

**No Custom GPTs on your plan?** Use a **Project** instead: in the left sidebar, **New project** → upload `sample-roster.csv` to the project files → **Instructions** → paste `instructions.md`. Then start chats inside that project.

**Quickest version (any plan):** start a new chat, attach `sample-roster.csv`, paste `instructions.md`, then paste the call. You'll have to redo this for each new chat.

# Option 2: Claude (Project)

1. Go to **claude.ai** → **Projects** → **Create project**, named `Team Finder`.
2. **Set project instructions:** paste `instructions.md`.
3. **Add content:** upload `sample-roster.csv`.
4. Start a chat in the project and paste the call.

# Using it

Paste a call with as much of its own wording as you can (title, deadline, link, and the synopsis or full text). The more of the call's text, the better the match. You'll get:

- a one-line summary of what the call wants
- **Options A, B, C**: three different team strategies, each with a lead, roles, reasons, evidence, and the gaps nobody covers
- a few more people worth a look
- a draft intro email for each option

Then steer it in plain language:

- "Make Option B smaller."
- "Swap Lena for someone with more AI."
- "Who else has worked with drones?"
- "Rewrite the email for Option A without Theo."

**It never sends anything.** Copy the email, check it, and send it yourself.

# The dashboard

The chat gives you the teams as text. To work with them like the Hub's own Team Finder, use `dashboard.html`:

1. **Double-click `dashboard.html`.** It opens in your web browser with a made-up example already loaded, so you can click around first.
2. **Load roster (CSV or JSON)**: pick the same roster file you uploaded to ChatGPT or Claude. The example goes away.
3. In the chat, after it builds the teams, type **"Give me the dashboard JSON."** Copy the block it returns.
4. Paste it into **Add results** and click **Add to dashboard**.

On the dashboard you can:

- switch between **Options A, B, C**
- mark each person **✓ In**, **? Maybe**, or **✗ Out**. People marked Out drop off the email's To line.
- add a note on each person, plus **Team notes**
- **add anyone** from your roster by name
- see the **network**: dots colored by department, bigger dots for a stronger digital twin connection, lines for co-authored papers, and the current team outlined. Click a dot for the person's profile.
- **Copy email** or **Open in my mail app**

Your work is saved in that browser on that computer only. Nothing is sent anywhere. To move it to another computer or hand it to a colleague, click **Save everything to a file** and have them use **Open a saved file**. Keep the dashboard file and the saved file together with your roster. They contain the same people.

# Putting in your own people

Replace the sample rows with real ones, keeping the same column headings:

| Column | What to put |
|---|---|
| `id` | A short unique tag, like `firstname-lastname` |
| `name`, `email`, `department`, `title` | The basics |
| `dt_connection` | `Strong`, `Moderate`, or `Light` (how much their work involves digital twins) |
| `research` | Two or three sentences in their own words. This matters most. |
| `keywords` | A few terms separated by semicolons |
| `recent_papers` | A few titles with years, separated by semicolons |
| `coauthors` | `id`s of people in the list they've published with, separated by semicolons |

Tips:

- **Self-described research beats everything.** A short survey ("describe your research in 2 to 3 sentences") gives much better matches than job titles.
- **Paper titles help it explain why.** Google Scholar, ORCID, or OpenAlex (openalex.org, free) are quick places to get recent titles.
- Leave someone's research blank and they won't be put on teams.
- Keep it to a few hundred people. Beyond that, split by area or trim.
- After editing, **re-upload the file** in the GPT or Project settings (delete the old one first).

# Privacy

- **Use only information people have agreed to share.** Uploading a roster sends it to OpenAI or Anthropic.
- If you're at Penn State, use the University-licensed version of your tool when you can, since the University's data agreement covers it. Don't upload anything confidential to a personal account.
- Don't include people who asked not to be listed, or private mailing lists. You can leave the `email` column blank and add addresses yourself when you send.
- If you share your GPT or Project, everyone you share it with can ask it about everyone in the roster.

# Questions

Rebecca Napolitano, Associate Director, Penn State Digital Twin Hub, nap@psu.edu
