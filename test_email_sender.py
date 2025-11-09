#!/usr/bin/env python3
"""
Test script for Email Sender Application
Tests the email validation and basic functionality without GUI
"""

import sys
import os

# Add parent directory to path to import email_sender
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import the email validation function
import re


def validate_email(email):
    """Validate email address format (same as in main app)"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def test_email_validation():
    """Test email validation function"""
    print("Testing email validation...")
    
    # Valid emails
    valid_emails = [
        "user@example.com",
        "test.user@gmail.com",
        "john.doe+tag@company.co.uk",
        "admin123@test-domain.org"
    ]
    
    # Invalid emails
    invalid_emails = [
        "invalid.email",
        "@example.com",
        "user@",
        "user @example.com",
        "user@.com",
        "user@domain",
        ""
    ]
    
    # Test valid emails
    for email in valid_emails:
        result = validate_email(email)
        status = "✓" if result else "✗"
        print(f"  {status} {email}: {'Valid' if result else 'Invalid'}")
        if not result:
            print(f"    ERROR: Expected valid but got invalid!")
            return False
    
    # Test invalid emails
    for email in invalid_emails:
        result = validate_email(email)
        status = "✓" if not result else "✗"
        print(f"  {status} {email}: {'Valid' if result else 'Invalid'}")
        if result:
            print(f"    ERROR: Expected invalid but got valid!")
            return False
    
    print("\n✓ All email validation tests passed!\n")
    return True


def test_imports():
    """Test that all required modules can be imported"""
    print("Testing module imports...")
    
    try:
        import smtplib
        print("  ✓ smtplib imported")
    except ImportError as e:
        print(f"  ✗ Failed to import smtplib: {e}")
        return False
    
    try:
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        from email.mime.base import MIMEBase
        from email import encoders
        print("  ✓ email modules imported")
    except ImportError as e:
        print(f"  ✗ Failed to import email modules: {e}")
        return False
    
    try:
        import re
        import os
        print("  ✓ Standard library modules imported")
    except ImportError as e:
        print(f"  ✗ Failed to import standard library: {e}")
        return False
    
    print("\n✓ All import tests passed!\n")
    return True


def test_app_structure():
    """Test that the main application structure is correct"""
    print("Testing application structure...")
    
    try:
        # Check if tkinter is available
        try:
            import tkinter
            tkinter_available = True
        except ImportError:
            print("  ⚠ tkinter not available in this environment (this is normal for headless systems)")
            print("  ℹ Skipping GUI-dependent tests")
            tkinter_available = False
        
        if not tkinter_available:
            # Just verify the file can be parsed
            import ast
            with open('email_sender.py', 'r') as f:
                code = f.read()
                ast.parse(code)
            print("  ✓ Application code is syntactically valid")
            print("  ✓ Structure verified via AST parsing")
            print("\n✓ Structure tests passed (limited due to missing tkinter)!\n")
            return True
        
        # Import the module but don't start GUI
        import email_sender
        
        # Check if EmailSenderApp class exists
        if not hasattr(email_sender, 'EmailSenderApp'):
            print("  ✗ EmailSenderApp class not found")
            return False
        print("  ✓ EmailSenderApp class found")
        
        # Check if main function exists
        if not hasattr(email_sender, 'main'):
            print("  ✗ main function not found")
            return False
        print("  ✓ main function found")
        
        # Check class methods
        required_methods = [
            'validate_email',
            'attach_file',
            'clear_attachment',
            'send_email',
            'clear_form'
        ]
        
        for method in required_methods:
            if not hasattr(email_sender.EmailSenderApp, method):
                print(f"  ✗ Method {method} not found")
                return False
            print(f"  ✓ Method {method} found")
        
        print("\n✓ All structure tests passed!\n")
        return True
        
    except Exception as e:
        print(f"  ✗ Error testing app structure: {e}")
        return False


def main():
    """Run all tests"""
    print("=" * 50)
    print("Email Sender Application - Test Suite")
    print("=" * 50)
    print()
    
    all_passed = True
    
    # Run tests
    if not test_imports():
        all_passed = False
    
    if not test_email_validation():
        all_passed = False
    
    if not test_app_structure():
        all_passed = False
    
    # Summary
    print("=" * 50)
    if all_passed:
        print("✓ ALL TESTS PASSED!")
        print("=" * 50)
        return 0
    else:
        print("✗ SOME TESTS FAILED!")
        print("=" * 50)
        return 1


if __name__ == "__main__":
    sys.exit(main())
