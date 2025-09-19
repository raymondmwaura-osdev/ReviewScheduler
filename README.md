# ReviewScheduler

## Description

ReviewScheduler is a command-line application designed to support spaced-repetition study methods. The program allows a user to record study dates and automatically schedules review dates based on fixed intervals. It further generates review schedules in Markdown format for convenient use and tracking. The application aims to provide a lightweight and transparent approach to reviewing study material, without requiring dependence on large-scale flashcard systems.

---

## Current Status

This project is in **beta stage** and is under slow, incremental development.

+ The program is functional, but lacks a comprehensive test suite.
+ Documentation outside the codebase (docstrings and comments) is minimal.
+ User should expect addition of new features and potential changes in instalation instructions.
+ Development pace is deliberately slow, and updates may occur infrequently.

---

## Installation Instructions

At present, installation uses a simple manual process.

1. Move the program’s source files into `/opt/rs`.  
2. Create a symbolic link from the main executable file to `/usr/local/bin`.  
   ```sh
   sudo ln -s /opt/rs/main.py /usr/local/bin/rs
   ```

3. Ensure the file has executable permissions:

   ```sh
   chmod +x /opt/rs/main.py
   ```

This setup allows the program to be executed globally from any working directory by invoking `reviewscheduler`.

---

## Usage Example

Initialize the program in the current directory:

```sh
$ rs init
```

Record a study date:

```sh
$ rs add 2025-09-15
```

Generate a Markdown file of reviews for today:

```sh
$ rs review today
```

---

## Future Work

Planned improvements include:

* Development of automated unit tests.
* Expansion of external documentation beyond code-level docstrings.
* User configuration for custom review intervals.
* Addition of new features.
* Formal packaging and distribution through `pip`.

---
