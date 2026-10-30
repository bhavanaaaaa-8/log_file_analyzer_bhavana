# Server Log Analyzer

## 1. Project Description

The Server Log Analyzer is a Python command-line application that reads server log files and extracts useful information about server requests.

It identifies total requests, error responses, frequently accessing IP addresses, commonly requested endpoints, and malformed log entries.

## 2. Features

- Counts total HTTP requests.
- Identifies error responses (4xx and 5xx).
- Tracks HTTP status codes.
- Finds the top 5 most frequent IP addresses.
- Identifies the top 5 commonly accessed endpoints.
- Detects and skips malformed log lines.
- Handles missing files and permission errors.
- Separates log parsing from log analysis.

## 3. Technologies Used

- Python 3
- Regular Expressions (`re`)
- Collections (`Counter`)

## 4. Project Structure

```text
ServerLogAnalyzer/
│
├── server_analyzer.py
├── server.log
└── README.md
```

## 5. Requirements

- Python 3.x
- No external libraries required.

## 6. How to Run

1. Save the Python program as `server_analyzer.py`.
2. Create a file named `server.log`.
3. Add server log entries to the file.
4. Place both files in the same directory.
5. Run the following command:

```bash
python server_analyzer.py
```

## 7. Log Format

The program supports the Common/Combined-style server log format.

Example:

```text
192.168.1.10 - - [30/Oct/2026:10:00:00 +0000] "GET /home HTTP/1.1" 200 1024
192.168.1.11 - - [30/Oct/2026:10:01:00 +0000] "GET /login HTTP/1.1" 404 256
```

## 8. Functions

| Function | Purpose |
|---|---|
| `parse_log_line()` | Extracts information from individual log lines. |
| `analyze_logs()` | Analyses valid log entries and generates statistics. |

## 9. Error Handling

The application handles:

- Missing log files.
- Permission errors.
- Malformed log entries.
- Invalid log formats.

Malformed lines are skipped without interrupting the analysis.

## 10. Expected Output

The application displays:

- Total requests.
- Error responses.
- Malformed log lines.
- HTTP status code counts.
- Top 5 IP addresses.
- Top 5 endpoints.

## 11. Conclusion

This project demonstrates file handling, dictionaries, counters, regular expressions, functions, exception handling, and modular programming in Python. It helps identify basic traffic patterns and error statistics from server logs.
