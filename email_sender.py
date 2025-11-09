#!/usr/bin/env python3
"""
Email Sender Application with Tkinter GUI
A simple Python mail-sender with a clean GUI for sending emails via SMTP
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import smtplib
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os


class EmailSenderApp:
    """Main Email Sender Application with Tkinter GUI"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Email Sender - Python")
        self.root.geometry("600x700")
        self.root.resizable(False, False)
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Store attachment path
        self.attachment_path = None
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="Email Sender", 
                                font=('Arial', 20, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Sender Email
        ttk.Label(main_frame, text="Sender Email:", 
                  font=('Arial', 10, 'bold')).grid(row=1, column=0, 
                                                    sticky=tk.W, pady=5)
        self.sender_email = ttk.Entry(main_frame, width=40)
        self.sender_email.grid(row=2, column=0, columnspan=2, pady=(0, 10))
        
        # App Password
        ttk.Label(main_frame, text="App Password:", 
                  font=('Arial', 10, 'bold')).grid(row=3, column=0, 
                                                    sticky=tk.W, pady=5)
        self.app_password = ttk.Entry(main_frame, width=40, show="*")
        self.app_password.grid(row=4, column=0, columnspan=2, pady=(0, 10))
        
        # Info label for app password
        info_label = ttk.Label(main_frame, 
                               text="Use App Password for Gmail (not your regular password)",
                               font=('Arial', 8), foreground='gray')
        info_label.grid(row=5, column=0, columnspan=2, pady=(0, 10))
        
        # Receiver Email
        ttk.Label(main_frame, text="Receiver Email:", 
                  font=('Arial', 10, 'bold')).grid(row=6, column=0, 
                                                    sticky=tk.W, pady=5)
        self.receiver_email = ttk.Entry(main_frame, width=40)
        self.receiver_email.grid(row=7, column=0, columnspan=2, pady=(0, 10))
        
        # Subject
        ttk.Label(main_frame, text="Subject:", 
                  font=('Arial', 10, 'bold')).grid(row=8, column=0, 
                                                    sticky=tk.W, pady=5)
        self.subject = ttk.Entry(main_frame, width=40)
        self.subject.grid(row=9, column=0, columnspan=2, pady=(0, 10))
        
        # Message
        ttk.Label(main_frame, text="Message:", 
                  font=('Arial', 10, 'bold')).grid(row=10, column=0, 
                                                    sticky=tk.W, pady=5)
        
        # Create text widget with scrollbar
        text_frame = ttk.Frame(main_frame)
        text_frame.grid(row=11, column=0, columnspan=2, pady=(0, 10))
        
        scrollbar = ttk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.message = tk.Text(text_frame, width=45, height=10, 
                               wrap=tk.WORD, yscrollcommand=scrollbar.set)
        self.message.pack(side=tk.LEFT)
        scrollbar.config(command=self.message.yview)
        
        # Attachment section
        attachment_frame = ttk.Frame(main_frame)
        attachment_frame.grid(row=12, column=0, columnspan=2, pady=(10, 10))
        
        self.attachment_label = ttk.Label(attachment_frame, 
                                          text="No file attached",
                                          foreground='gray')
        self.attachment_label.pack(side=tk.LEFT, padx=5)
        
        attach_button = ttk.Button(attachment_frame, text="Attach File", 
                                   command=self.attach_file)
        attach_button.pack(side=tk.LEFT, padx=5)
        
        clear_button = ttk.Button(attachment_frame, text="Clear", 
                                  command=self.clear_attachment)
        clear_button.pack(side=tk.LEFT, padx=5)
        
        # Send button
        send_button = ttk.Button(main_frame, text="Send Email", 
                                 command=self.send_email)
        send_button.grid(row=13, column=0, columnspan=2, pady=20)
        
        # Status label
        self.status_label = ttk.Label(main_frame, text="", 
                                      font=('Arial', 10))
        self.status_label.grid(row=14, column=0, columnspan=2)
        
    def validate_email(self, email):
        """Validate email address format"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def attach_file(self):
        """Open file dialog to select attachment"""
        file_path = filedialog.askopenfilename(
            title="Select a file to attach",
            filetypes=[("All Files", "*.*")]
        )
        if file_path:
            self.attachment_path = file_path
            filename = os.path.basename(file_path)
            self.attachment_label.config(text=f"Attached: {filename}", 
                                        foreground='green')
    
    def clear_attachment(self):
        """Clear the selected attachment"""
        self.attachment_path = None
        self.attachment_label.config(text="No file attached", 
                                    foreground='gray')
    
    def send_email(self):
        """Send email via SMTP"""
        # Get values
        sender = self.sender_email.get().strip()
        password = self.app_password.get().strip()
        receiver = self.receiver_email.get().strip()
        subject = self.subject.get().strip()
        message_text = self.message.get("1.0", tk.END).strip()
        
        # Validate inputs
        if not sender or not password or not receiver:
            messagebox.showerror("Error", "Please fill in all required fields!")
            self.status_label.config(text="Error: Missing required fields", 
                                    foreground='red')
            return
        
        if not self.validate_email(sender):
            messagebox.showerror("Error", "Invalid sender email address!")
            self.status_label.config(text="Error: Invalid sender email", 
                                    foreground='red')
            return
        
        if not self.validate_email(receiver):
            messagebox.showerror("Error", "Invalid receiver email address!")
            self.status_label.config(text="Error: Invalid receiver email", 
                                    foreground='red')
            return
        
        if not subject:
            messagebox.showwarning("Warning", "Subject is empty. Continue?")
        
        if not message_text:
            messagebox.showerror("Error", "Message cannot be empty!")
            self.status_label.config(text="Error: Empty message", 
                                    foreground='red')
            return
        
        # Update status
        self.status_label.config(text="Sending email...", foreground='blue')
        self.root.update()
        
        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = sender
            msg['To'] = receiver
            msg['Subject'] = subject
            
            # Attach message body
            msg.attach(MIMEText(message_text, 'plain'))
            
            # Attach file if selected
            if self.attachment_path and os.path.exists(self.attachment_path):
                try:
                    with open(self.attachment_path, 'rb') as attachment:
                        part = MIMEBase('application', 'octet-stream')
                        part.set_payload(attachment.read())
                    
                    encoders.encode_base64(part)
                    filename = os.path.basename(self.attachment_path)
                    part.add_header('Content-Disposition', 
                                   f'attachment; filename= {filename}')
                    msg.attach(part)
                except Exception as e:
                    messagebox.showerror("Error", 
                                       f"Failed to attach file: {str(e)}")
                    self.status_label.config(text="Error: File attachment failed", 
                                           foreground='red')
                    return
            
            # Connect to SMTP server and send email
            # Using Gmail SMTP server as default
            smtp_server = "smtp.gmail.com"
            smtp_port = 587
            
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()  # Enable TLS encryption
            
            # Login
            server.login(sender, password)
            
            # Send email
            text = msg.as_string()
            server.sendmail(sender, receiver, text)
            
            # Close connection
            server.quit()
            
            # Success
            messagebox.showinfo("Success", "Email sent successfully!")
            self.status_label.config(text="Email sent successfully!", 
                                    foreground='green')
            
            # Clear form after successful send
            self.clear_form()
            
        except smtplib.SMTPAuthenticationError:
            messagebox.showerror("Error", 
                               "Authentication failed! Check your email and app password.")
            self.status_label.config(text="Not sent: Authentication failed", 
                                    foreground='red')
        except smtplib.SMTPException as e:
            messagebox.showerror("Error", f"SMTP error: {str(e)}")
            self.status_label.config(text="Not sent: SMTP error", 
                                    foreground='red')
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send email: {str(e)}")
            self.status_label.config(text="Not sent: Error occurred", 
                                    foreground='red')
    
    def clear_form(self):
        """Clear all form fields"""
        self.sender_email.delete(0, tk.END)
        self.app_password.delete(0, tk.END)
        self.receiver_email.delete(0, tk.END)
        self.subject.delete(0, tk.END)
        self.message.delete("1.0", tk.END)
        self.clear_attachment()


def main():
    """Main entry point for the application"""
    root = tk.Tk()
    app = EmailSenderApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
