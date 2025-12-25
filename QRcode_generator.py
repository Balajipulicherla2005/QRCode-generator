# QRCode Genertion
import qrcode

qr=qrcode.QRCode(
    version=5,
    box_size=5,
    border=2
)
name=input("Enter your name:")
born=input("Enter your born Year:")
born_place=input("Enter your born place:")
height=input("Enter your height:")
spouse=input("Enter your spouse:")
movie=input("Enter your movie:")
ipl_team=input("Enter your ipl team name:")
country_name=input("Enter your country name:")
Role=input("Enter your role:")
Batsman=input("Enter batsman style:")
Bowling=input("Enter Bowling style:")
ICC_Trophics = input("Enter name and years:")
awards=input("Enter your awards:")
no_of_centuries=int(input("Enter your hundreds:"))
data={"Name":name,"Born":born,"Born_palce":born_place,"Height":height,"Spouse":spouse,"Movie":movie, "Ipl_Team":ipl_team,  "Country_name":country_name,  "iCC_Trophics":ICC_Trophics, "Awards":awards,"No_of_centuries":no_of_centuries}
qr=qrcode.make(data)
qr=qrcode.make(data)
qr.save("QRcode_Dhoni_.png")
qr.show()






