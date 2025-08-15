# output_module.py
"""
Pre-ULAI Output Module
Handles displaying or exporting results
"""

def display_output(data):
    print("=== Pre-ULAI Output ===")
    for key, value in data.items():
        print(f"{key}: {value}")

