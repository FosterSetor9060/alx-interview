Log Parsing: Analyzing Web Server Logs
Overview
Welcome to the “Log Parsing” project! In this algorithmic challenge, we’ll focus on parsing and processing data streams from web server logs. Our goal is to read input data from standard input (stdin), handle it in a specific format, and compute relevant metrics based on the processed data.

Learning Objectives
By completing this project, you’ll gain knowledge in the following areas:

File I/O in Python: Reading from sys.stdin line by line.
Signal handling in Python: Handling keyboard interruptions (CTRL + C) using signal handling.
Data processing: Parsing strings to extract specific data points and aggregating data for summaries.
Regular expressions: Using regex to validate the format of each log entry.
Dictionaries in Python: Counting occurrences of status codes and accumulating file sizes.
Exception handling: Managing possible exceptions during file reading and data processing.
Project Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.4.3).
All your files should end with a new line.
The first line of all your files should be exactly #!/usr/bin/python3.
A README.md file, at the root of the project folder, is mandatory.
Your code should follow the PEP 8 style (version 1.7.x).
All your files must be executable.
The length of your files will be tested using wc.
Input Format
Each line of input follows this format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
If the format is not as specified, the line must be skipped.
Metrics to Compute
After every 10 lines or a keyboard interruption (CTRL + C), print the following statistics from the beginning:
Total file size: <total size> (sum of all previous <file size> values).
Number of lines by status code (possible status codes: 200, 301, 400, 401, 403, 404, 405, and 500):
Format: <status code>: <number>
Status codes should be printed in ascending order.
Example
Sample input and output are provided in the prompt. Note that your actual output may vary due to random values.

Usage Example
$ ./0-generator.py | ./0-stats.py
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
...
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6


GitHub repository: alx-interview

Directory: 0x03-log_parsing

Let’s dive into analyzing those web server logs! 📊🔍 edge browser The user has the page open in a Microsoft Edge browser window whose metadata is:

JSON

<EMPTY>
AI-generated code. Review and use carefully. More info on FAQ.
Windows The user is operating Windows whose current runtime environment metadata is:

JSON

{"OS Version":"Windows 10 Professional","Preferred Languages":["en-US"],"Installed Apps":["Google Chrome","YouTube","Slack","Git Bash","Performance Monitor","Computer Management","Task Manager","Event Viewer","Local Security Policy","Task Scheduler","Resource Monitor","Excel","Access","Publisher","OneNote","Outlook (classic)","PowerPoint","Word","OneDrive","Visual Studio Code","Control Panel","File Explorer","Windows Media Player","Remote Desktop Connection","Run","Microsoft Edge","Zoom","Character Map","Disk Cleanup","Command Prompt","Component Services","Defragment and Optimize Drives","iSCSI Initiator","Windows Memory Diagnostic","System Configuration","Paint","Notepad","ODBC Data Sources (64-bit)","On-Screen Keyboard","Print Management","Steps Recorder","Quick Assist",
