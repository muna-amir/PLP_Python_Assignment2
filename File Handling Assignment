import os

def process_file(input_path: str, output_path: str) -> None:
    """
    Reads the input file, modifies its content, and writes the modified
    content to the output file.

    The modification applied is:
    1. Adding a header line.
    2. Converting all original lines to uppercase and prefixing them with a line number.
    
    Args:
        input_path: The path to the file to be read.
        output_path: The path where the processed file will be written.
        
    Raises:
        FileNotFoundError: If the input file does not exist.
        PermissionError: If the program lacks read/write permissions.
        IOError: For other input/output related issues.
    """
    
    # 1. Read the input file content
    with open(input_path, 'r', encoding='utf-8') as infile:
        original_content = infile.readlines()

    # 2. Modify the content
    modified_content = []
    
    # Add a descriptive header
    modified_content.append(f"--- PROCESSED CONTENT FROM {input_path.upper()} ---\n\n")
    
    # Process each line
    for i, line in enumerate(original_content):
        # Remove leading/trailing whitespace and convert to uppercase
        processed_line = line.strip().upper()
        
        # Add line number and the modified text
        modified_content.append(f"LINE {i + 1}: {processed_line}\n")

    # 3. Write the modified content to the output file
    with open(output_path, 'w', encoding='utf-8') as outfile:
        outfile.writelines(modified_content)


def main():
    """
    Handles user interaction and robust error handling for file operations.
    """
    
    # Define default file names for convenience
    DEFAULT_INPUT = 'input.txt'
    DEFAULT_OUTPUT = 'processed_output.txt'

    print("--- File Read, Write, & Error Handling Program ---")
    print(f"Ensure '{DEFAULT_INPUT}' exists to run the program successfully.")
    
    # Loop until the file processing succeeds or the user quits
    while True:
        # Get filenames from the user, using defaults if input is empty
        input_file = input(f"\nEnter input filename (Default: {DEFAULT_INPUT}): ") or DEFAULT_INPUT
        output_file = input(f"Enter output filename (Default: {DEFAULT_OUTPUT}): ") or DEFAULT_OUTPUT

        try:
            # Attempt to process the file
            process_file(input_file, output_file)
            
            # If successful, print confirmation and exit the loop
            print(f"\n✅ SUCCESS: Content from '{input_file}' was processed.")
            print(f"A new file has been created at: '{output_file}'")
            
            # Print the path for easy locating (useful if running in different environments)
            print(f"Full path check: {os.path.abspath(output_file)}")
            
            break # Exit the loop
            
        except FileNotFoundError:
            # Handle the specific case where the input file does not exist
            print(f"\n❌ ERROR: File Not Found.")
            print(f"The input file '{input_file}' does not exist. Please check the name and try again.")
            
        except PermissionError:
            # Handle cases where the program cannot access the file due to permissions
            print(f"\n❌ ERROR: Permission Denied.")
            print(f"Cannot read '{input_file}' or write to '{output_file}'. Check your file permissions.")
            
        except IOError as e:
            # Handle general I/O errors (e.g., file opened by another program)
            print(f"\n❌ ERROR: An Input/Output error occurred: {e}")
            
        except Exception as e:
            # Catch any other unexpected exceptions
            print(f"\n❌ CRITICAL ERROR: An unexpected error occurred: {e}")
            
        finally:
            # Optional: Add a separator for cleaner loop output
            print("-" * 50)


if __name__ == "__main__":
    main()
