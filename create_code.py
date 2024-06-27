# All used imports -> look in README.md to import all libraries
import segno


# Give data to save the QR code
data = {
    "link": str(input("Enter the link you want to make a QR code of: ")),
    "name": str(input("Enter the name of the QR code (WARNING: will override QR codes with the same name): ")).replace(' ', '-')
}

# Make a QR code based on the given data
qrcode = segno.make_qr(data['link'])
qrcode.save(
    f"codes/{data['name']}.png",
    scale=5,
)
