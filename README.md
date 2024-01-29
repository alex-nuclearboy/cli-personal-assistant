# Personal Assistant Bot

[Introduction](#introduction) · [Documentation](#documentation) · [Features](#features) · [Getting Started](#getting-started) · [All Commands](#all-commands) · [Original Concept](#original-concept)

## Introduction

Welcome to the "Personal Assistant" bot project! This bot is crafted with a focus on efficiency and intuitiveness, it enables users to manage contacts, notes, and files through a natural language interface.

Distinguished by its user information presentation and command flexibility, this project stands as a testament to the versatility and power of Python-based solutions.
From streamlined contact management to intelligent note-taking and file organization, every aspect of the bot is designed to make daily digital interactions more productive and seamless.

## Documentation

In addition to the source code, this repository includes UML diagrams of the project, providing a visual representation of the system's architecture and interactions.
These diagrams are available in both PNG and [draw.io](https://app.diagrams.net/) formats, allowing for easy viewing.

## Features

-   **Contact Management:** Manage your contacts with details like names, phone numbers, emails, addresses and birthdays.
-   **Birthday Notifications:** Get notifications for contacts whose birthdays are approaching.
-   **Data Validation:** Validate phone numbers and email addresses during contact creation or editing.
-   **Contact Book Operations:** Search, edit, and delete contact entries.
-   **Note Management:** Save and manage notes with text information.
-   **Tagging and Sorting:** Organize notes effectively with tags, and find them easily.
-   **File Organization:** Automatically sort files in a specified folder by type.
-   **Smart Analysis:** The bot analyzes user inputs to understand intent and offer relevant suggestions.

## Getting Started

```bash
# Clone this project
$ git clone https://github.com/alex-nuclearboy/cli-personal-assistant.git

# Install dependencies
$ pip install -e .

# Run the project
$ personal-assistant

# Create or upload a file by entering its name
$ <filename>

# Display the list of commands
$ help

# Uninstall
$ pip uninstall Personal-Assistant
```

## All Commands

-   `hello`: Greet the bot with a friendly hello. 😃
-   `help`: Display a list of available commands and instructions.
-   `add contact`: Add a new contact with options to include phone number, email, address, and birthday.
-   `add phone`: Append an additional phone number to an existing contact.
-   `add email`: Append an additional email address to an existing contact.
-   `add address`: Add an extra address to an existing contact.
-   `change phone`: Modify the phone number associated with a contact.
-   `change birthday`: Update or add a birthday for a contact.
-   `change name`: Edit the name of an existing contact.
-   `change email`: Update the email address of a contact.
-   `change address`: Change the address details for a contact.
-   `remove phone`: Delete a phone number from a contact.
-   `remove email`: Remove an email address from a contact.
-   `remove address`: Delete an address from a contact.
-   `clear all`: Erase all contacts from the database.
-   `search by birthday`: Find contacts with birthdays on a specific date or within a date range.
-   `days to birthday`: Calculate the days remaining until a contact's next birthday.
-   `delete contact`: Permanently remove a contact from the database.
-   `search`: Look for contacts by name or phone number based on a search query.
-   `find phone`: Retrieve all phone numbers associated with a specific contact.
-   `show all contacts`: Display all contacts in the database, including their phone numbers, emails, addresses, and birthdays.
-   `sort folder`: Organize files in a specified folder into categories based on file type.
-   `create note`: Create a new note in the digital notebook.
-   `change title`: Alter the title of an existing note.
-   `add tags`: Associate tags with a note for categorization and easier retrieval.
-   `edit note`: Edit the text content of a note.
-   `delete note`: Remove a note from the notebook.
-   `find note`: Search for notes based on title, content, or author.
-   `show all notes`: Display all the notes stored in the notebook.
-   `find tags`: Look for notes categorized under specific tags.
-   `sort notes`: Arrange notes alphabetically based on their tags.
-   `delete tags`: Remove a tag from a note.
-   `show note`: Display the full content of a specific note.
-   `good bye`, `close`, `exit`, `.`: Exit the program.

## Original Concept

This project takes its inspiration from and serves as an extensive enhancement of the [original work](https://github.com/ArleKinG44/GOIT_Projekt_group_3) created by the "Hufflepuff" team during the Python Core course at [GoIT](https://goit.global/ua/). It builds upon the foundational concepts and functionalities introduced in the original project, adding significant improvements and innovative features to enrich the user experience and demonstrate advanced capabilities in Python programming.

[Back to Top](#personal-assistant-bot)
