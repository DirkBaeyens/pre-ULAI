---

# README\_CONTINUE

## 🔄 Continuing the pre-ULAI Project Across Sessions

Since the pre-ULAI project is developed in conversation, sometimes chats need to be restarted (e.g., due to session limits or switching between GPT versions). This guide explains how to **continue the project smoothly**.

---

## 📂 Session Summaries

All context needed to resume work is stored in the `sessions/` folder.

* Each session summary has a numbered file:

  * `session_summary-001.md`
  * `session_summary-002.md`
  * …
* The **latest summary** is always saved as:

  * `session_summary.md`

When starting a new chat:

1. Copy the content of the latest `session_summary.md`
2. Paste it into the new chat to restore context
3. Inform the assistant that this is a continuation of the pre-ULAI project

---

## 🛠 Steps to Resume Development

1. Ensure the **repository structure** remains intact:

   * `main.py`
   * `core/`
   * `tests/`
   * `sessions/`

2. Run a quick test to confirm functionality:

```bash
python3 main.py
python3 test_observations.py
```

3. Check that the universal rules load and the reasoning engine responds.

---

## 📌 Good Practices

* Always save updates to `sessions/session_summary.md` after major progress
* Add new numbered summaries (`session_summary-003.md`, etc.) for **history tracking**
* Use `CHANGELOG.md` to record file updates, new features, or bug fixes

---

## 🧭 Purpose of This File

This file acts as a **hand-off manual** so that anyone (or a new AI session) can pick up where things left off without confusion.

---

