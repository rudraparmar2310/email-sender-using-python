# Email Sender Application - Visual Guide

## Application Interface

The Email Sender application provides a clean, intuitive Tkinter GUI with the following components:

### Main Window (600x700 pixels)
```
┌─────────────────────────────────────────────────┐
│              Email Sender                       │
│                                                 │
│  Sender Email:                                  │
│  ┌───────────────────────────────────────┐     │
│  │ your-email@gmail.com                  │     │
│  └───────────────────────────────────────┘     │
│                                                 │
│  App Password:                                  │
│  ┌───────────────────────────────────────┐     │
│  │ ****************                      │     │
│  └───────────────────────────────────────┘     │
│  Use App Password for Gmail (not regular pwd)  │
│                                                 │
│  Receiver Email:                                │
│  ┌───────────────────────────────────────┐     │
│  │ receiver@example.com                  │     │
│  └───────────────────────────────────────┘     │
│                                                 │
│  Subject:                                       │
│  ┌───────────────────────────────────────┐     │
│  │ Hello from Python Email Sender!       │     │
│  └───────────────────────────────────────┘     │
│                                                 │
│  Message:                                       │
│  ┌───────────────────────────────────────┐     │
│  │ This is a test email sent using       │ ↕   │
│  │ Python and Tkinter.                   │     │
│  │                                       │     │
│  │ It supports:                          │     │
│  │ - Email validation                    │     │
│  │ - SMTP authentication                 │     │
│  │ - File attachments                    │     │
│  │ - Error handling                      │     │
│  │                                       │     │
│  └───────────────────────────────────────┘     │
│                                                 │
│  No file attached  [Attach File]  [Clear]      │
│                                                 │
│              [Send Email]                       │
│                                                 │
│         Email sent successfully! ✓             │
│                                                 │
└─────────────────────────────────────────────────┘
```

## Key Features Visible in the GUI:

1. **Title Bar**: "Email Sender - Python"

2. **Input Fields**:
   - All entry fields are 40 characters wide
   - Password field shows asterisks for security
   - Clean, consistent spacing between elements

3. **Message Area**:
   - Scrollable text box (45 chars wide, 10 lines high)
   - Scrollbar for longer messages
   - Word wrapping enabled

4. **Attachment Section**:
   - Status label showing current attachment or "No file attached"
   - "Attach File" button opens file dialog
   - "Clear" button removes attachment

5. **Action Button**:
   - Centered "Send Email" button
   - Triggers validation and email sending

6. **Status Messages**:
   - Green text for success
   - Red text for errors
   - Blue text for "sending..." status
   - Gray text for informational messages

## Color Scheme:
- Theme: 'clam' (native look and feel)
- Success messages: Green
- Error messages: Red
- Processing messages: Blue
- Info/hints: Gray
- Background: System default (light gray/white)

## Behavior:

### On "Send Email" Click:
1. Validates all required fields are filled
2. Validates email format for sender and receiver
3. Shows "Sending email..." status in blue
4. Attempts SMTP connection and authentication
5. Sends email with optional attachment
6. Shows success message in green OR error in red
7. Clears form on success

### Error Scenarios:
- Missing fields: "Error: Missing required fields"
- Invalid email: "Error: Invalid sender/receiver email"
- Auth failure: "Not sent: Authentication failed"
- SMTP error: "Not sent: SMTP error"
- General error: "Not sent: Error occurred"

### File Attachment:
- Click "Attach File" → File dialog opens
- Select any file → Shows "Attached: filename.ext" in green
- Click "Clear" → Removes attachment, shows "No file attached" in gray

## Window Properties:
- Size: 600x700 pixels
- Fixed size (not resizable)
- Centered on screen
- Clean padding (20px) around all elements
- Professional font: Arial with varied sizes (20pt title, 10pt labels, 8pt hints)
