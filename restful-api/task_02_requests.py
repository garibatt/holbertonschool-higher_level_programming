#!/usr/bin/python3
"""
commit for task
"""

import requests
import csv


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    # If request successful
    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        # Prepare list of dictionaries
        formatted_posts = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            }
            for post in posts
        ]

        # Write into CSV
        with open("posts.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(formatted_posts)

