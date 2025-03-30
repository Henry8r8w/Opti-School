import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd
from models import fetch_email_data

def plot_email_status():
    data = fetch_email_data()
    if not data:
        print("no data available to plot.")
        return
    
    statuses = [row[3] for row in data]
    status_counts = Counter(statuses)
    
    plt.figure(figsize=(6, 6))
    plt.pie(status_counts.values(), labels=status_counts.keys(), autopct='%1.1f%%', colors=["#99ff99", "#ff9999"])
    plt.title("email success vs failure rate")
    plt.show()

if __name__ == "__main__":
    plot_email_status()
