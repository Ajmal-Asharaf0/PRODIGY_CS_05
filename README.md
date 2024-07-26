# PRODIGY_CS_05

Comprehensive Keylogger

A Python-based keylogger that logs keystrokes with timestamps, encrypts the log file, and optionally sends logs to a remote server. This tool is intended for educational purposes and should only be used in environments where you have explicit permission.
Features

    Keystroke Logging: Captures keystrokes and logs them with timestamps.
    File Encryption: Encrypts the log file to secure captured data.
    Optional Remote Logging: Sends logs to a remote server (requires configuration).

Requirements

    Python 3.x
    Libraries:
        pynput: For capturing keystrokes.
        cryptography: For encrypting the log file.
        requests: For sending logs to a remote server (optional).

Installation

    Clone the Repository

    bash

git clone https://github.com/your-repo/keylogger.git
cd keylogger

Install Required Libraries

Install the necessary Python libraries using pip:

bash

    pip install pynput cryptography requests

Usage

    Edit the Script

    If you want to enable remote logging, replace the placeholder URL in the send_log function with your server’s URL. Ensure the server is set up to handle incoming POST requests.

    Run the Keylogger

    Open your terminal or command prompt, navigate to the directory where keylogger.py is located, and execute:

    bash

python keylogger.py

If you encounter issues with Python 2.x, try:

bash

python3 keylogger.py

Stopping the Keylogger

To stop the keylogger, press the Esc key. The keylogger will stop capturing keystrokes and encrypt the log file upon exit.

Check the Log File

After the keylogger stops, the log file named keylog.txt will be encrypted. You can use the provided decrypt_file function to decrypt it if needed.

Ethical Considerations

    Permission: Ensure you have explicit permission before running this tool on any system. Unauthorized use of keyloggers is illegal and unethical.
    Legal Compliance: Follow all relevant laws and regulations regarding monitoring and data privacy.
    Privacy: Handle all data responsibly. Encrypt and securely store log files to prevent unauthorized access.

License

This project is licensed under the MIT License. See the LICENSE file for details.
Contributing

Contributions are welcome! To contribute:

    Fork the repository.
    Make your changes.
    Submit a pull request.

Disclaimer

This tool is for educational purposes only. Unauthorized use may be illegal and unethical. Always use responsibly and with proper consent.
Contact

For any questions or support, please contact email- ajmalshraf511@gmail.com
