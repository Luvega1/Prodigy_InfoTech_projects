from PIL import Image


def encrypt_image(input_path, output_path, key):
  img = Image.open(input_path)
  pixels = img.load()
  
  width, height = img.size
  
  for i in range(width):
    for j in range(height):
      r, g, b = pixels[i, j]
      
      #Example encryption: swappping red and blue channels
      encrypted_pixel = (b, g, r)
      
      
      pixels[i, j] = encrypted_pixel
      
  img.save(output_path)
  print("Image encrypted successfully!")
  
  
  
def decrypt_image(input_path, output_path, key):
  img = Image.open(input_path)
  pixels = img.load() 
  
  width, height = img.size 
    
  
  for i in range(width):
    for j in range(height):
      r, g, b = pixels[i, j]
      
      #exam0ple decryption: swapping red and blue channels back
      decrypted_pixel = (b, g, r)
      
      pixels[i, j] = decrypted_pixel
      
  img.save(output_path)
  print("Image decrypted successfuly!")
  
# example usage
input_image = r"images/input image.jpeg"
encrypted_image = r"encrypt.jpeg"
decrypted_image = r"decrypt.jpeg"


#encrypt the image
encrypt_image(input_image, encrypted_image, key=None)

#decrypted the image
decrypt_image(encrypted_image, decrypted_image, key=None)

