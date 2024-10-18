import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
from config import api_key, cloud_name, api_secret
from cloudinary import CloudinaryImage

# Configuration       
cloudinary.config(
    cloud_name=cloud_name,
    api_key=api_key,
    api_secret=api_secret,
    secure=True
)

# Upload an image
upload_result = cloudinary.uploader.upload("https://img.paisawapas.com/ovz3vew9pw/2024/01/29182036/HRITHIK-ROSHAN.jpg", public_id="hrx")

print(upload_result["secure_url"])

# # Optimize delivery by resizing and applying auto-format and auto-quality
# optimize_url, _ = cloudinary_url("shoes", fetch_format="auto", quality="auto")
# print(optimize_url)

# # Transform the image: auto-crop to square aspect_ratio
# auto_crop_url, _ = cloudinary_url("shoes", width=500, height=500, crop="auto", gravity="auto")
# print(auto_crop_url)


# a = CloudinaryImage("hrx").image(aspect_ratio="1:1", gravity="center", background="gen_fill", crop="pad")

a = CloudinaryImage("hrx").image(effect="gen_background_replace:prompt_make the subject stand in times square new york")

print(a)