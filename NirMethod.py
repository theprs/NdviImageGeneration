import numpy as np
import matplotlib.pyplot as plt
import rasterio

def calculate_ndvi(nir_band, red_band):
    # Calculate NDVI
    ndvi = (nir_band - red_band) / (nir_band + red_band)
    return ndvi

def mask_vegetation(ndvi, threshold=0.35):
    # Create a mask for vegetation
    mask = ndvi > threshold
    return mask

def main(nir_image_path, red_image_path):
    # Read the NIR and Red bands
    with rasterio.open(nir_image_path) as nir_src:
        nir_band = nir_src.read(1).astype('float32')
    
    with rasterio.open(red_image_path) as red_src:
        red_band = red_src.read(1).astype('float32')

    # Calculate NDVI
    ndvi = calculate_ndvi(nir_band, red_band)

    # Mask vegetation
    vegetation_mask = mask_vegetation(ndvi)

    # Calculate percentage vegetation cover
    vegetation_percentage = (np.sum(vegetation_mask) / vegetation_mask.size) * 100

    return ndvi, vegetation_mask, vegetation_percentage

nir_image_path = 'nir.jpg'
red_image_path = 'red.jpg'
ndvi, vegetation_mask, vegetation_percentage = main(nir_image_path, red_image_path)

print(f'Vegetation cover: {vegetation_percentage:.2f}%')

# Display the NDVI image and the vegetation mask
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('NDVI Image')
plt.imshow(ndvi, cmap='RdYlGn')
plt.colorbar()

plt.subplot(1, 2, 2)
plt.title('Vegetation Mask')
plt.imshow(vegetation_mask, cmap='RdYlGn')

plt.show()
