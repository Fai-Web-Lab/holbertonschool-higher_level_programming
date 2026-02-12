#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    """
    Fetches posts from JSONPlaceholder and prints their titles.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post.get('title'))
    else:
        print("Failed to retrieve posts.")


def fetch_and_save_posts():
    """
    Fetches posts and saves specific fields (id, title, body) into a CSV file.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        structured_data = [
            {'id': post['id'], 'title': post['title'], 'body': post['body']}
            for post in posts
        ]

        keys = ['id', 'title', 'body']

        try:
            with open('posts.csv', 'w', newline='',
                      encoding='utf-8') as output_file:
                dict_writer = csv.DictWriter(output_file, fieldnames=keys)
                dict_writer.writeheader()
                dict_writer.writerows(structured_data)
        except IOError as e:
            print(f"An error occurred while writing the CSV: {e}")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
