
## ⚠️ Legal warning

This tool is for authorized lab testing only. Do not run it against systems you do not own or have explicit written permission to test. Unauthorized scanning, fuzzing, or uploading files to a target is illegal in most jurisdictions and can lead to criminal charges. The author is not responsible for any misuse or damage caused by this tool.

## upload-extension-enumerator

A small Python tool I wrote to enumerate the file extensions accepted by a file upload form, mainly for ASP.NET extensions. It's a manual alternative to Burp Suite's Sniper attack. To have more control during authorized lab testing.
## Why I built this

While solving the HTB "Bounty" machine, I needed to find out which file formats the upload form would accept. I used Burp Suite to intercept the requests, i made it an snipper attack, but I wanted more control over the payloads, the headers, and the timing. So I wrote my own enumerator to understand how the server validates file uploads and to test different extensions systematically.

## How it works

You need 6 things for this can work in htb Bounty or ASP.NET 
- url upload page
- A diccionary with extension
- The necessesari required parameters of the request (In my case 4, use BurpSuite)

The tool sends a POST request to the upload endpoint with a small test file, changing the file extension on each request. It analyzes the response (status code, response length, error messages, redirects) to determine whether the extension was accepted, rejected, or triggered a different behavior, in this case is the response length that let as know if es accepted or not.
It does not test MIME types or magic bytes. It only tests the extension in the filename, which is enough for many misconfigured upload forms.

## Features

- Configurable extension wordlist
- Custom headers and cookies
- Detects accepted, rejected, and ambiguous responses
- Simple CLI with `pwntools`
- Configurable numbres of Threads with max_workers

## Requirements

- Python 3.10+
- Dictionary extensions
- A target upload endpoint
- A valid session cookie if the form is authenticated

## Installation

```bash
git clone https://github.com/Joel-C-P/upload-extension-enumerator.git
cd upload-extension-enumerator
pip install -r requirements.txt
```
