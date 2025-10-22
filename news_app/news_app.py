from io import BytesIO
import webbrowser
import ssl
import requests
from tkinter import *
from urllib.request import Request, urlopen
from PIL import Image, ImageTk


class NewsApp:
    """Simple desktop news viewer using the NewsAPI."""

    def __init__(self):
        # Basic app info
        self.name = "Nesa News App"
        self.version = "1.0.0"

        # API setup
        self.api_url = "https://newsapi.org/v2/top-headlines?country=us&"
        self.api_key = "apiKey=7e5630f1d6e64bb3800fccd056e1443a"
        self.full_api_url = self.api_url + self.api_key

        # Internal state
        self.news_data = []
        self.current_article_index = 0

        # Initialize app
        self.fetch_news_data()
        self.load_ui()
        self.load_news_item(0)

    def fetch_news_data(self):
        """Fetch top headlines from the NewsAPI and store them in self.news_data."""
        print("Fetching news data from API...")

        try:
            response = requests.get(self.full_api_url, timeout=10)
            response.raise_for_status()  # raises HTTPError for 4xx/5xx
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch news data: {e}")
            self.news_data = []
            return

        # Parse JSON response
        data = response.json()
        self.news_data = data.get("articles", [])
        print(f"News data fetched successfully. Total articles: {len(self.news_data)}")

    def load_ui(self):
        """Initialize and configure the Tkinter window."""
        self.root = Tk()
        self.root.title(self.name)
        self.root.geometry("350x600")
        self.root.configure(bg="black")
        self.root.resizable(False, False)

    def load_news_item(self, index):
        """Load and display a specific news article by index."""
        try:
            # Clear previous content
            self.clear_ui()

            # Validate index and data
            if not self.news_data or index < 0 or index >= len(self.news_data):
                Label(self.root, text="No news available.", bg="black", fg="white").pack(pady=20)
                return

            article = self.news_data[index]
            image_url = article.get("urlToImage")
            print(f"\n========== Article {index} ==========")
            print(f"Image URL: {image_url}")

            # Try to load image safely
            photo = None
            if image_url:
                try:
                    req = Request(image_url, headers={"User-Agent": "Mozilla/5.0"})
                    context = ssl._create_unverified_context()  # ignore SSL cert errors
                    raw_data = urlopen(req, context=context, timeout=5).read()
                    image_open = Image.open(BytesIO(raw_data)).resize((300, 250))
                    photo = ImageTk.PhotoImage(image_open)
                except Exception as e:
                    print(f"Failed to load image: {e}")
                    photo = None
            else:
                print("No image found for this article.")

            # Show image or placeholder
            if photo:
                label = Label(self.root, image=photo, bg="black")
                label.image = photo  # prevent garbage collection
            else:
                label = Label(self.root, text="[Image not available]", bg="black", fg="grey")
            label.pack(pady=(10, 10))

            # Display title
            heading = Label(
                self.root,
                text=article.get("title", "No title"),
                bg="black",
                fg="white",
                wraplength=300,
                justify="center",
                font=("Verdana", 15, "bold"),
            )
            heading.pack(pady=(10, 20))

            # Display description
            description = Label(
                self.root,
                text=article.get("description", "No description"),
                bg="black",
                fg="white",
                wraplength=300,
                justify="center",
            )
            description.pack(pady=(10, 20))

            # Buttons section
            frame = Frame(self.root, bg="black")
            frame.pack(expand=True, fill=BOTH, pady=(20, 10))
            frame.columnconfigure(0, weight=1)
            frame.columnconfigure(1, weight=1)
            frame.columnconfigure(2, weight=1)

            # Navigation buttons
            if index != 0:
                Button(
                    frame,
                    text="<< Previous",
                    bg="grey",
                    fg="white",
                    command=lambda: self.load_news_item((index - 1) % len(self.news_data)),
                ).grid(row=0, column=0, sticky="ew", padx=10)

            Button(
                frame,
                text="Read More",
                bg="grey",
                fg="white",
                command=lambda: self.openInWebBrowser(article.get("url", "#")),
            ).grid(row=0, column=1, sticky="ew", padx=10)

            if index < len(self.news_data) - 1:
                Button(
                    frame,
                    text="Next >>",
                    bg="grey",
                    fg="white",
                    command=lambda: self.load_news_item((index + 1) % len(self.news_data)),
                ).grid(row=0, column=2, sticky="ew", padx=10)

        except Exception as e:
            print(f"Unexpected error while loading article {index}: {e}")
            Label(
                self.root,
                text="Network or data error. Please try again.",
                bg="black",
                fg="red",
                wraplength=300,
            ).pack(pady=20)

        self.root.mainloop()

    def clear_ui(self):
        """Clear all widgets currently packed in the main window."""
        for widget in self.root.pack_slaves():
            widget.destroy()

    def openInWebBrowser(self, url):
        """Open the given article URL in the system’s default browser."""
        if url and url != "#":
            webbrowser.open_new(url)
        else:
            print("Invalid or missing URL.")


# Run the app
if __name__ == "__main__":
    news_app = NewsApp()