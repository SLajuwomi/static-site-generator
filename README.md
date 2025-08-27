# Static Site Generator

This project is a simple static site generator written in Python. It converts Markdown files into a static HTML website using a template.

The code was written for the [Build a Static Site Generator](https://www.boot.dev/courses/build-static-site-generator-python) course on Boot.dev.

## View the Live Website

You can view the generated website directly in your browser without installing anything.

**[https://slajuwomi.github.io/static-site-generator/](https://slajuwomi.github.io/static-site-generator/)**

## How It Works

The script automates website creation from text files. The process is:

1.  **Deletes old files**: It removes the previous build directory (`docs/`) for a clean start.
2.  **Copies static files**: It copies assets like CSS and images from `static/` to `docs/`.
3.  **Scans content**: It finds all Markdown (`.md`) files in the `content/` directory.
4.  **Converts Markdown**: It converts each Markdown file to HTML. It supports headings, lists, styled text, code blocks, links, and images.
5.  **Applies template**: It injects the HTML content and page title into the `template.html` file.
6.  **Builds pages**: It saves the final HTML pages to the `docs/` directory, matching the `content/` folder structure.

## Running the Project Locally

Follow these steps to build and view the website on your own computer.

### Prerequisites

You need **Python 3** installed. To check if you have it installed, open a terminal and run `python3 --version`.

### Instructions

**Step 1: Build the Website**

Run the build command in your terminal from the project's root directory.

```bash
python3 src/main.py "/"
```

This command runs the script to generate the website. The output files are placed in the `docs/` folder.

**Step 2: Start a Local Server**

To view the site, you must run a local web server. Run this command in your terminal.

```bash
cd docs && python3 -m http.server 8888
```

This command moves into the `docs` directory and starts the server. You will see a message like `Serving HTTP on 0.0.0.0 port 8888`.

**Step 3: View the Site in a Browser**

Open a web browser and go to this address:

[http://localhost:8888](http://localhost:8888)

You will see the website homepage. You can navigate between pages.

To stop the server, return to your terminal and press `Ctrl + C`.

## Customizing Content

You can change the website's content:

- **Edit pages**: Modify any `.md` file in the `content/` directory.
- **Add pages**: Create new `.md` files or folders inside `content/`.
- **Rebuild**: Run the build command from **Step 1** again. Refresh your browser to see the updates.

## For Developers

### Building for Deployment

The project is configured for deployment to a subdirectory. The `build.sh` script passes a `basepath` to the main script to handle this.

```bash
# This command builds the site with links prefixed by "/static-site-generator/"
sh build.sh
```

You can change the `basepath` argument in `build.sh` to match your hosting path.

### Running Tests

The project includes unit tests for the parsing and generation logic. To run the tests, execute the `test.sh` script.

```bash
sh test.sh
```
