# 🧠 Chrome Memory Usage Monitor

Ever wondered which Chrome tab is secretly eating up all your memory?  
This project helps you find out — and keeps an eye on things before they get out of hand.

It's a simple yet powerful Python tool that monitors your Chrome processes, shows you how much memory each one is using, and sends you an alert if things go overboard. Plus, there’s a clean Streamlit dashboard to visualize it all in real time.

---

## 💡 Why I Built This

Chrome is fast — until it’s not. I wanted a way to **see which tabs or processes are consuming the most memory**, and potentially catch performance issues early. This script started as an idea and evolved into a full-fledged memory monitor with a UI.

It's beginner-friendly, customizable, and teaches a lot about process monitoring, visualization, and working with system resources in Python.

---

## 🔧 What It Can Do

- 🖥️ List all active Chrome processes
- 📊 Show memory usage (in MB) per process
- ⚠️ Alert if total memory usage crosses a limit (default: 1 GB)
- 📈 Optionally track memory over time and visualize it
- 🌐 Optionally connect to Chrome’s debugging port to show tab titles + URLs
- 🧑‍💻 Built with Streamlit for a simple, clean UI

---

## 🛠 Tech Stack

- Python
- psutil
- matplotlib
- Streamlit
- websocket-client (for optional Chrome debugging)

---

## 🏁 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/vijkaran12/ChromeMemoryUsage.git
cd ChromeMemoryUsage

Install the dependencies

pip install -r requirements.txt


Run with the Streamlit UI (recommended)

streamlit run chrome_monitor.py
