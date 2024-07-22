# Motivational Quote Generator

This project displays a motivational quote as a notification every time the computer starts. It uses a Python script that is set to run at startup via a batch file placed in the Windows Startup folder.

## Prerequisites

- Python 3.6 or higher
- `plyer` library

## Installation

1. **Clone the Repository**

   ```sh
   git clone https://github.com/rutaganda-salim/quote generator.git
   cd quote generator
   ```
2. **Install the required dependency**
   
   ```bash
   pip install plyer
   ```
## Setting Up the Startup Script



1.Create a new text file and add the following content:

```sh
@echo off
"C:\Path\To\Python\python.exe" "D:\quote generator\python.py"
```

2.Replace C:\Path\To\Python\python.exe with the path to your Python executable and
 D:\quote generator\python.py with the path to your Python script.

3.Save the file with a .bat extension, such as run_quote_generator.bat.

4.Place the Batch File in the Startup Folder

5.Press Win + R to open the Run dialog.


6.Type ``` shell:startup``` and press Enter. 

7.This opens the Startup folder.
Move the batch file you created (run_quote_generator.bat) into this Startup folder.


## Verify and Test

Ensure the batch file is in the Startup folder.
Optionally, run the batch file manually to verify it works.
Restart your computer to confirm the script runs at startup.
