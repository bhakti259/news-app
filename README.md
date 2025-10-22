Nesa News App - README

Nesa News App
A simple desktop news viewer application built with Python and Tkinter.
It fetches the latest top headlines from the NewsAPI and displays them in a visually appealing interface with images, titles, and descriptions.

Features
Fetches real-time top headlines from NewsAPI
Displays news images, titles, and descriptions
Supports Next / Previous navigation between articles
Read More button opens the full article in your web browser
Handles:
Missing or invalid images
Bad network connections
SSL or certificate issues
Empty API responses
Tech Stack
Python 3.x
Tkinter – for GUI
Requests – for fetching data from API
Pillow (PIL) – for image handling
Webbrowser – for opening article links
Installation
Clone this repository

git clone https://github.com/bhakti259/news-app.git
cd nesa-news-app
Install dependencies

pip install requests pillow
Run the application

python news.py
API Key Setup
This app uses the free NewsAPI service.

If your API key expires or is missing:

Sign up at https://newsapi.org/register
Copy your API key
Replace the key in the code:
self.api_key = "apiKey=YOUR_API_KEY_HERE"
Screenshots
(You can add screenshots here later — e.g. ![App Screenshot](screenshot.png))

Error Handling
The app gracefully handles:

Network errors → shows a retry message
Missing images → displays a placeholder text
SSL/Certificate issues → uses unverified context safely
Out-of-range index → shows "No news available"
Author
Bhakti Kulkarni
📍 Antwerp, Belgium
🌐 Bhakti Kulkarni LinkedIn: https://www.linkedin.com/in/bhaktiskulkarni/ GitHub: https://github.com/bhakti259

🪪 License
This project is open-source and available under the MIT License.

⭐ Contribute
Contributions and suggestions are welcome!
If you’d like to improve the UI, add filters, or categories, feel free to fork this repo and create a pull request.
