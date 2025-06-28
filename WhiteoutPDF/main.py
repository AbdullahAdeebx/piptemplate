import sys
import os
from pdf2image import convert_from_path
from PIL import Image, ImageOps

def convert_pdf_to_print_friendly(input_pdf):
    if not os.path.exists(input_pdf):
        print(f"File not found: {input_pdf}")
        return

    # Convert PDF to list of PIL images
    print("Converting PDF pages to images...")
    images = convert_from_path(input_pdf)

    print("Processing pages...")
    processed_images = []
    for img in images:
        gray = img.convert("L")
        inverted = ImageOps.invert(gray)
        processed_images.append(inverted.convert("RGB"))

    output_pdf = input_pdf.replace(".pdf", "_print_friendly.pdf")
    print(f"Saving to {output_pdf}...")
    processed_images[0].save(
        output_pdf,
        save_all=True,
        append_images=processed_images[1:]
    )
    print("✅ Done!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py input.pdf")
    else:
        convert_pdf_to_print_friendly(sys.argv[1])