import webbrowser
import time

def open_links():
    links = [
        "https://example.com/link1",
        "https://example.com/link2",
        # Add more links as needed
    ]

    while True:
        for link in links:
            webbrowser.open(link)
            time.sleep(20)

if __name__ == "__main__":
    open_links()
