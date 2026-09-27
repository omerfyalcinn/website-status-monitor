# Website Status Monitor

A Python command-line tool that checks website availability and response times.

## Features

- Reads website URLs from a text file
- Sends an HTTP request to each website
- Displays HTTP status codes
- Measures response times
- Handles connection and timeout errors

## Installation

Clone the repository:

```bash
git clone https://github.com/omerfyalcinn/website-status-monitor.git
cd website-status-monitor
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the required packages:

```bash
python -m pip install -r requirements.txt
```

## Usage

Add the websites you want to monitor to `websites.txt`, one URL per line:

```text
https://example.com
https://www.python.org
```

Run the program:

```bash
python monitor.py
```

Example output:

```text
URL: https://example.com
Status code: 200
Response time: 0.245 seconds
----------------------------------------
```

## Technologies

- Python
- Requests
- Git and GitHub

## License

This project is licensed under the MIT License.