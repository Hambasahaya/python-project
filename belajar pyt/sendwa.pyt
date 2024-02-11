# # import pywhatkit
# # nomor_tlp = '+62 895-3538-29619'
# # pesan = "ule anj"
# # for i in range(0, 10):
# #     pywhatkit.sendwhatmsg_instantly(
# #         phone_no=nomor_tlp,
# #         message=pesan
# #     )
# from phonenumbers import parse
# from phonenumbers import geocoder
# from geopy.geocoders import Nominatim

# # Nomor telepon
# number = '+6282281506600'
# ch_number = parse(number, "CH")

# # Ekstrak informasi geografis
# location = geocoder.description_for_number(ch_number, "en")

# # Inisialisasi geocoder
# geolocator = Nominatim(user_agent="geoapiExercises")

# # Mendapatkan koordinat berdasarkan deskripsi geografis
# location = location.split(",")[0]  # Mengambil nama negara
# coordinates = geolocator.geocode(location)

# # Mencetak nama kota
# print(coordinates.address)
