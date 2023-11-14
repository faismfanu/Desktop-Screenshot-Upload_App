import tkinter as tk
from tkinter import filedialog
from Screenshot import screenshot,api_request


def take_screenshot_and_upload():
    remarks_value = remarks.get()
    phone_value = phone.get()
    # Check if the column has value and phone contains 10 digit
    if not remarks_value or not phone_value or not phone_value.isdigit() or len(phone_value) != 10:
        # Error Message
        error_label.config(text="Invalid input.Please check phone is 10 digit")
        return
    screenshot_path = screenshot()
    response_data = api_request(screenshot_path, remarks_value, phone_value)
    # Checking Api rsponse is success or not
    if response_data.get('status') == 'success':
        success_label.config(text=f"Screenshot Upload Successfull")
    else:
        error_label.config(text=f"Screenshot Upload Failed")

# GUI setup
root = tk.Tk()
root.title("Desktop Screenshot Upload")

remarks = tk.StringVar()
phone = tk.StringVar()

tk.Label(root, text="Remarks:").pack()
tk.Entry(root, textvariable=remarks).pack()

tk.Label(root, text="Phone").pack()
tk.Entry(root, textvariable=phone).pack()

error_label = tk.Label(root, text="", fg="red")
error_label.pack()

success_label = tk.Label(root, text="", fg="green")
success_label.pack()

tk.Button(root, text="Take Screenshot", command=take_screenshot_and_upload).pack()

root.mainloop()