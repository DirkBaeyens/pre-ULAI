# Continuation Guide for pre-ULAI Project

This file explains how to safely continue the project when moving to a new chat session.

---

## 🔹 Purpose
Since chat sessions may get overloaded or reset, this guide ensures smooth continuation of the **pre-ULAI** project without losing context.

---

## 🔹 Steps for Continuing in a New Chat
1. Copy the content of the **latest `sessions/session_summary.md`**.
2. Start a new chat with the assistant.
3. Paste the following handover message:

We are continuing the pre-ULAI project.

Here is the latest project state (from session_summary.md):

[PASTE THE CONTENT OF session_summary.md HERE]

Instructions:

Continue from this point, no need to review past chats.

Keep using the same structure: main.py, core/, tests/, sessions/, etc.

Always add version tags in the format:
# Version: YYYY-MM-DD HH:MM at the top of each file.

Update CHANGELOG.md and session_summary.md whenever major updates are made.

Do not generate or commit __pycache__/ files.


4. The assistant will then be synced up instantly and ready to continue.

---

## 🔹 Notes
- Keep **all session summaries** in the `sessions/` folder (`001`, `002`, … + latest).
- Only `session_summary.md` will be pasted into new chats.
- Older summaries remain as history/reference.
- Manual uploads to GitHub should continue as before.

