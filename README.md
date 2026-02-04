# 🚀 Focus Assistant

A professional-grade, containerized "Deep Work" tracker built with **Python**, **NiceGUI**, and **Docker**. This tool helps users stay productive by locking in session goals and providing a distraction-free environment.

## ✨ Key Features
* **Bento Grid UI:** A modern, high-contrast dashboard inspired by premium productivity tools.
* **Modular Architecture:** Clean separation of concerns between State, UI, and Business Logic.
* **Dark/Light Mode:** Integrated theme switching for day/night focus sessions.
* **Containerized Deployment:** Fully Dockerized to ensure environment consistency across any server.
* **Live Notifications:** Real-time feedback for mission status and completion.

## 🛠️ Tech Stack
* **Language:** Python 3.11
* **Frontend/Backend:** [NiceGUI](https://nicegui.io/) (Vue/Quasar based)
* **Styling:** Tailwind CSS
* **DevOps:** Docker & Docker Compose
* **Hosting:** Render

## 🚀 How to Run Locally
1. Clone the repo: `git clone https://github.com/YOUR_USERNAME/focus-assistant-app.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Launch: `python main.py`

## 🐳 Running with Docker
```bash
docker build -t focus-assistant .
docker run -p 8080:8080 focus-assistant
