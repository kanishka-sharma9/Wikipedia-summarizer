# 📚 Wikipedia Summarizer

A Python project that intelligently parses any Wikipedia page and generates a **section-wise summary**—all while preserving citations and sources for accuracy and traceability.

---

## ✨ Features

- **Section-wise Summaries:** Get concise overviews for each section of a Wikipedia article.
- **Citation Integrity:** All references and sources are preserved in the summaries.
- **Easy to Use:** Just point to any Wikipedia URL and let the script do the rest.
- **Powered by [BeautifulSoup (bs4)](https://www.crummy.com/software/BeautifulSoup/):** Robust HTML parsing for reliability.

---

## 🚀 How It Works

1. **Scraping:**  
   The script `scraper.py` fetches and parses the Wikipedia article.

2. **Summarization:**  
   Section-wise summaries are generated, keeping references and citations intact.

3. **Output:**  
   - 📝 Example of `scraper.py` output: [`output1.md`](output1.md)
   - 🏁 Final summarized result: [`summary_output.md`](summary_output.md)

---

## 📰 Example Article

- [Alexander the Great — Wikipedia](https://en.wikipedia.org/wiki/Alexander_the_Great)

---

## 📂 Files Overview

- `scraper.py` — Main script for scraping.
- `smmarizer.py` — Main script for summarizing.
- `output1.md` — Raw output example from the scraper.
- `summary_output.md` — Final formatted summary.

---

## 🛠️ Requirements

- Python 3.x
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
- [Langchain](https://python.langchain.com/docs/introduction/)
- [Requests](https://pypi.org/project/requests/)

Install dependencies with:
```bash
pip install beautifulsoup4 requests langchain
```

---

## 💡 Usage

```bash
setx GROQ_API_KEY <Your API Key>
python scraper.py
python smmarizer.py
```

---

*Happy summarizing!*
