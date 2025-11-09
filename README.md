# Email Sender Using Python

A simple Python mail-sender with a clean Tkinter GUI that guides the user through entering sender email, app password, and receiver email, validates inputs, lets the user compose the message, performs SMTP authentication, and then sends the email (or shows "not sent" on failure).

## Features

- 🎨 Clean and intuitive Tkinter GUI
- ✉️ Send emails via SMTP (Gmail by default)
- 🔒 Secure authentication with app passwords
- ✅ Email validation for sender and receiver
- 📎 Optional file attachment support
- 📝 Message composition with text area
- 🔔 Success/failure feedback with detailed error messages
- 🎯 User-friendly error handling

## Tech Stack

- **Python 3.x** - Programming language
- **Tkinter** - GUI framework (included with Python)
- **smtplib** - SMTP protocol client (standard library)
- **email** - Email handling package (standard library)

## Requirements

- Python 3.6 or higher
- Tkinter (usually comes pre-installed with Python)

All required modules are part of the Python standard library, so no external dependencies need to be installed.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/rudraparmar2310/email-sender-using-python.git
cd email-sender-using-python
```

2. Ensure Python 3 is installed:
```bash
python3 --version
```

## Usage

### Running the Application

Simply run the main script:

```bash
python3 email_sender.py
```

### Using Gmail

To use Gmail for sending emails, you need to:

1. **Enable 2-Step Verification** on your Google account
2. **Generate an App Password**:
   - Go to your Google Account settings
   - Navigate to Security → 2-Step Verification → App passwords
   - Generate a new app password for "Mail"
   - Use this 16-character password in the application (not your regular Gmail password)

### Step-by-Step Guide

1. **Launch the application**: Run `python3 email_sender.py`

2. **Enter sender details**:
   - Sender Email: Your Gmail address (e.g., `your-email@gmail.com`)
   - App Password: Your generated app password (16 characters)

3. **Enter receiver details**:
   - Receiver Email: Recipient's email address

4. **Compose your email**:
   - Subject: Email subject line
   - Message: Write your email message in the text area

5. **Attach files (optional)**:
   - Click "Attach File" to select a file from your computer
   - Click "Clear" to remove the attachment

6. **Send the email**:
   - Click "Send Email"
   - Wait for confirmation (success or failure message)

### Input Validation

The application validates:
- ✅ Email format for sender and receiver addresses
- ✅ All required fields are filled
- ✅ Message is not empty
- ✅ Authentication credentials are correct

### Error Handling

The application provides clear feedback for:
- ❌ Authentication failures
- ❌ Invalid email addresses
- ❌ Missing required fields
- ❌ SMTP connection errors
- ❌ File attachment errors

## Features in Detail

### Email Validation
The application uses regex pattern matching to ensure email addresses are properly formatted before attempting to send.

### SMTP Authentication
Uses secure TLS encryption (STARTTLS) for connecting to the SMTP server, ensuring your credentials are transmitted securely.

### File Attachments
Supports attaching any file type. Files are encoded using base64 encoding and attached to the email as MIME parts.

### User Feedback
- Real-time status updates during email sending
- Success/failure messages with detailed error information
- Form clearing after successful send

## Troubleshooting

### "Authentication failed"
- Ensure you're using an app password, not your regular Gmail password
- Verify that 2-Step Verification is enabled on your Google account
- Check that the app password is entered correctly (no spaces)

### "Invalid email address"
- Ensure email addresses are in the correct format: `username@domain.com`
- Remove any extra spaces before or after the email address

### "Not sent: SMTP error"
- Check your internet connection
- Verify that Gmail SMTP is accessible from your network
- Some networks may block SMTP ports

## Security Notes

- Never share your app password
- The application does not store any credentials
- App passwords are more secure than regular passwords for third-party apps
- Always use app passwords instead of your main Gmail password

## License

This project is open source and available for educational purposes.

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## Author

Rudra Parmar

## Acknowledgments

- Built with Python's standard library
- Uses Gmail's SMTP server for email delivery
