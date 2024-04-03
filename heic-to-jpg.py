import os
import shutil
from PIL import Image
from pillow_heif import register_heif_opener

def convert_heic_to_jpg(input_folder, output_folder, log_file, corrupt_folder):
    successful_conversions = 0
    failed_conversions = 0

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    if not os.path.exists(corrupt_folder):
        os.makedirs(corrupt_folder)

    register_heif_opener()

    for filename in os.listdir(input_folder):
        input_file_path = os.path.join(input_folder, filename)
        print(f"Processing {filename}...")

        try:
            with Image.open(input_file_path) as img:
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                new_filename = filename + ".jpg"
                output_file_path = os.path.join(output_folder, new_filename)
                img.save(output_file_path, "jpeg")
                print(f"Converted {filename} to {new_filename}")
                successful_conversions += 1
        except Exception as e:
            error_message = f"Error processing {filename}: {e}\n"
            print(error_message)
            with open(log_file, 'a') as log:
                log.write(error_message)
            corrupt_file_path = os.path.join(corrupt_folder, filename)
            shutil.move(input_file_path, corrupt_file_path)
            print(f"Moved {filename} to corrupt folder")
            failed_conversions += 1

    # Print summary statistics
    print(f"Summary:")
    print(f"Total files processed: {successful_conversions + failed_conversions}")
    print(f"Successful conversions: {successful_conversions}")
    print(f"Failed conversions: {failed_conversions}")

# Example usage
input_folder = "input"  # Adjust as needed
output_folder = "output"  # Adjust as needed
log_file = "error_log.txt"  # Adjust as needed
corrupt_folder = "corrupt_files"  # Adjust as needed
convert_heic_to_jpg(input_folder, output_folder, log_file, corrupt_folder)
