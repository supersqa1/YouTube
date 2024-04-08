import csv
import os
import random
import string

def generate_large_csv(file_name, size_in_mb, row_length=10):
    """Generates a large CSV file with random data.

    Args:
    - file_name: Name of the file to create.
    - size_in_mb: Desired approximate size of the file in megabytes.
    - row_length: Number of columns in each row.
    """
    size_in_bytes = size_in_mb * 4024 * 4024  # Convert MB to bytes
    total_size = 0

    # Define a function to generate a random string of fixed length
    def random_string(length=10):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        # Write header row
        writer.writerow(['Number'] + [f'String{i}' for i in range(1, row_length)])

        # Keep writing rows until the file reaches the desired size
        while total_size < size_in_bytes:
            row = [random.randint(0, 100)] + [random_string(10) for _ in range(row_length - 1)]
            writer.writerow(row)
            # Update total size by estimating the size of the row in bytes
            total_size += sum(len(str(item)) for item in row) + row_length - 1  # Add length of the commas

    print(f"Generated file {file_name} of approximate size {os.path.getsize(file_name) / (1024*1024):.2f} MB")

# Example usage:
generate_large_csv('large_file.csv', 50)  # Generates a CSV file of approximately 50 MB
