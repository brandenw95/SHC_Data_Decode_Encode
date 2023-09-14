# SMART Card QR Code Decoder and Encoder

This program is designed to decode and encode QR codes typically used in SMART Cards. This functionality can be useful in scenarios where data encoded in QR codes needs to be extracted, transformed, or otherwise processed.

**Created on:** September 21st, 2021

## Features

1. Convert Base64Url encoded strings to numeric data that can be transformed into QR format.
2. Convert a complete QR string into its Base64Url representation.
3. Decode a Base64Url encoded string, decompress it, and retrieve the original JSON data.

## Dependencies

- `base64`: Used for base64 operations.
- `re`: Used for regular expression operations.
- `zlib`: Used for decompressing the data.
- `configparser`: Used for parsing configuration files.

## Functions

### `Base64UrltoNumeric(base64data)`

- **Input**: Base64Url encoded string
- **Output**: A string in the format 'shc:/' followed by the SHC data that can be converted to QR.

### `NumericToBase64Url(qr_numeric_data)`

- **Input**: A full QR string.
- **Output**: The Base64Url representation of the input data.

### `Base64UrlToJson(base64Url_data)`

- **Input**: A Base64Url encoded string.
- **Output**: Decompressed plain JSON data.

## Usage

1. Before you run the program, ensure you have a `config.txt` file. It should have the following structure:

```
[example_data]
qr_data = YOUR_NUMERIC_QR_STRING_HERE
base_64_data = YOUR_BASE64_STRING_HERE
```

Replace `YOUR_NUMERIC_QR_STRING_HERE` and `YOUR_BASE64_STRING_HERE` with your data.

1. Run the main script:

```
python your_script_name.py
```

This will process the data in the config file and print the plain JSON extracted from the QR data.

## Known Limitations

- The `Base64UrlToJson` function contains a helper function `decode(data)` which might not be thoroughly understood. Its main purpose is to assist in the decoding process of the `Base64UrltoJson` function.
- The way to reverse the decompression in the `Base64UrlToJson` function is currently unclear. Further research or understanding of the data format and compression method may be needed.

## Contributing

If you have improvements or feedback on this script, feel free to make a pull request or raise an issue.

## License

This project is open-sourced and is available under the [MIT License](https://opensource.org/licenses/MIT).
