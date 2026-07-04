import qrcode

print("QR Code Generator")

while True:
    data = input("\nEnter text or URL: ")

    filename = input("File name: ")

    img = qrcode.make(data)

    img.save(f"{filename}.png")

    print("✅ QR Saved Successfully!")

    choice = input("\nGenerate another QR? (y/n): ").lower()

    if choice != "y":
        print("Thank you for using QR Generator!")
        break