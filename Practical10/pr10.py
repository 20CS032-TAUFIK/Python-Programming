import img2pdf
from PIL import Image

# Importing the image file
imp_path = "/Users/Downloads/20cs032_Result.png"

# creating a pdf file.
pdf_path = "/Users/Downloads/20cs032_Result.pdf"

# creating a image file
image = Image.open(imp_path)

# creating a pdf from the image.
pdf_bytes = img2pdf.convert(image.filename)

# opening file
file = open(pdf_path, "wb")

# writing the file.
file.write(pdf_bytes)

# closing an image.
image.close()

# closing an file.
file.close()
print("Success!!")
