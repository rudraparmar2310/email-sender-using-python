#!/usr/bin/env python3
"""
Example Usage Script for Email Sender Application

This script demonstrates how to run and use the email sender application.
It also provides example configurations for different email providers.
"""

import sys
import os

# Example configurations for different email providers
EMAIL_PROVIDERS = {
    'gmail': {
        'smtp_server': 'smtp.gmail.com',
        'smtp_port': 587,
        'instructions': '''
        Gmail Setup:
        1. Enable 2-Step Verification in your Google Account
        2. Go to Security → App passwords
        3. Generate an app password for "Mail"
        4. Use that 16-character password in the app
        '''
    },
    'outlook': {
        'smtp_server': 'smtp-mail.outlook.com',
        'smtp_port': 587,
        'instructions': '''
        Outlook/Hotmail Setup:
        1. Use your regular email password
        2. May need to enable "Let apps use SMTP" in settings
        '''
    },
    'yahoo': {
        'smtp_server': 'smtp.mail.yahoo.com',
        'smtp_port': 587,
        'instructions': '''
        Yahoo Setup:
        1. Go to Account Security
        2. Generate app password
        3. Use that password in the app
        '''
    }
}


def print_usage():
    """Print usage information"""
    print("=" * 70)
    print("Email Sender Application - Usage Guide")
    print("=" * 70)
    print()
    print("RUNNING THE APPLICATION:")
    print("-" * 70)
    print("  python3 email_sender.py")
    print()
    print("REQUIREMENTS:")
    print("-" * 70)
    print("  - Python 3.6 or higher")
    print("  - tkinter (usually pre-installed with Python)")
    print("  - Internet connection")
    print()
    print("EMAIL PROVIDER SETUP:")
    print("-" * 70)
    
    for provider, config in EMAIL_PROVIDERS.items():
        print(f"\n{provider.upper()}:")
        print(f"  SMTP Server: {config['smtp_server']}")
        print(f"  Port: {config['smtp_port']}")
        print(f"  {config['instructions']}")
    
    print()
    print("QUICK START:")
    print("-" * 70)
    print("  1. Set up your email provider (see above)")
    print("  2. Run: python3 email_sender.py")
    print("  3. Enter your email credentials")
    print("  4. Compose your message")
    print("  5. Click 'Send Email'")
    print()
    print("FEATURES:")
    print("-" * 70)
    print("  ✓ Email validation")
    print("  ✓ Secure SMTP authentication")
    print("  ✓ TLS encryption")
    print("  ✓ File attachments")
    print("  ✓ Error handling")
    print("  ✓ Success/failure feedback")
    print()
    print("SECURITY TIPS:")
    print("-" * 70)
    print("  • Always use app passwords, not your main password")
    print("  • Never share your app password")
    print("  • The app doesn't store any credentials")
    print("  • Use 2-Step Verification for better security")
    print()
    print("TROUBLESHOOTING:")
    print("-" * 70)
    print("  Authentication Failed:")
    print("    → Check app password is correct")
    print("    → Verify 2-Step Verification is enabled")
    print()
    print("  Invalid Email Address:")
    print("    → Check email format: user@domain.com")
    print("    → Remove extra spaces")
    print()
    print("  SMTP Error:")
    print("    → Check internet connection")
    print("    → Verify SMTP port isn't blocked")
    print("    → Try again in a few moments")
    print()
    print("=" * 70)


def check_environment():
    """Check if the environment is ready to run the app"""
    print("Checking environment...")
    print()
    
    # Check Python version
    version = sys.version_info
    print(f"✓ Python {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 6):
        print("✗ Python 3.6 or higher is required")
        return False
    
    # Check for required modules
    try:
        import smtplib
        print("✓ smtplib available")
    except ImportError:
        print("✗ smtplib not available")
        return False
    
    try:
        from email.mime.text import MIMEText
        print("✓ email module available")
    except ImportError:
        print("✗ email module not available")
        return False
    
    try:
        import tkinter
        print("✓ tkinter available")
    except ImportError:
        print("⚠ tkinter not available (required for GUI)")
        print("  Install tkinter:")
        print("    Ubuntu/Debian: sudo apt-get install python3-tk")
        print("    Fedora: sudo dnf install python3-tkinter")
        print("    macOS: tkinter should be included with Python")
        return False
    
    # Check if email_sender.py exists
    if os.path.exists('email_sender.py'):
        print("✓ email_sender.py found")
    else:
        print("✗ email_sender.py not found in current directory")
        return False
    
    print()
    print("✓ Environment is ready!")
    return True


def main():
    """Main entry point"""
    print()
    
    # Check if user wants help
    if len(sys.argv) > 1 and sys.argv[1] in ['-h', '--help', 'help']:
        print_usage()
        return 0
    
    # Check environment
    if check_environment():
        print()
        print("To run the application:")
        print("  python3 email_sender.py")
        print()
        print("For detailed usage information:")
        print("  python3 example_usage.py --help")
        print()
        return 0
    else:
        print()
        print("✗ Environment check failed")
        print("  Please fix the issues above and try again")
        print()
        return 1


if __name__ == "__main__":
    sys.exit(main())
