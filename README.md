# PixelPyConverter

Convert your HEIC images to JPEG with ease using PixelPyConverter, a simple yet powerful Python script leveraging the PIL library and pillow_heif. Whether you're dealing with a batch of photos from your iPhone or a collection of images for a project, PixelPyConverter automates the conversion process, saving you time and hassle.

## Features

- **Batch Conversion:** Process an entire folder of HEIC images in one go.
- **Error Handling:** Automatically detects and segregates corrupt HEIC files.
- **Logging:** Maintains a log of conversion errors for troubleshooting.
- **Color Mode Adjustment:** Converts images to RGB color mode for consistent JPEG output.

## Prerequisites

Before you start using PixelPyConverter, ensure you have Python installed on your system. Additionally, you need to install the following packages:

- Pillow
- pillow_heif

You can install these packages using pip:

```bash
pip install Pillow pillow_heif
```

## Usage

1. Clone this repository to your local machine.
2. Ensure your input folder contains the HEIC files you want to convert.
3. Adjust the `input_folder`, `output_folder`, `log_file`, and `corrupt_folder` paths in the script as needed.
4. Run the script:

```bash
python pixel_py_converter.py
```

5. Check the output folder for your converted images, and the corrupt folder for any images that could not be converted.

## Example

After setting your folders accordingly in the script, running the script will process and convert all HEIC files found in the `input_folder`, placing the converted JPEG images in the `output_folder`. Any errors encountered during conversion will be logged in `error_log.txt`, and problematic files will be moved to `corrupt_files`.

## Contributing

Contributions to PixelPyConverter are welcome! Feel free to fork the repository, make your improvements, and submit a pull request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

This script was created to facilitate the conversion of HEIC images to a more universally accepted format, JPEG. Special thanks to the developers of the PIL library and pillow_heif for making image processing accessible and efficient in Python.
