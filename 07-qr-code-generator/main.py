# install all the libraries needed
# create a fun that collect a text and converts it to a qrcode
# save the qrcode as an image
# run the func

import qrcode, uuid

def generate_qrcode(text):
    id = uuid.uuid4()

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"07-qr-code-generator/qrimg-{id}.png")

while True:
    print("A. Generate QrCode")
    print("E. Exit")
    choice = input("Enter ur Choice: ")
    if choice == "a" or choice == "A":
        link_input = input("Enter Link: ")
        generate_qrcode(link_input)
    elif choice == "e" or choice == "E":
        print("Programe ended")
        exit()
    else:
        print("command not found")