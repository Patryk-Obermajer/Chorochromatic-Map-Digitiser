# Chorochromatic Map Digitiser

## Description
This project uses Convolutional Neural Networks (CNNs) to digitise scanned historical chorochromatic maps, converting them into digital spatial data. Traditional GIS vectorisation methods are inefficient due to noise and imperfections in scanned images. The approach is applied to the Winter Rainfall Availability Potential (WRAP) map.

## Project Structure

1. **01-map-tiler.ipynb**: Divides the georeferenced map into small tiles for further processing.
2. **02-classifier-training.ipynb**: Trains a CNN to classify the map tiles into predefined classes.
3. **03-map-tiles-classifier-with-tflite.ipynb**: Applies the trained CNN model to classify the map tiles using TensorFlow Lite.
4. **04-map-recreator-from-tiles.ipynb**: Recreates the map from the classified tiles and re-integrates it into a GIS platform.
5. **config.py**: Contains global variables and configuration settings.

## Data Directory Structure

The `data/` directory contains all the data used and generated in the project.

- **01-source-map**: Contains the original scanned map images.
- **02-source-map-tiles**: Stores the tiles generated from the original map.
- **03-training-data**: Contains the data used for training the CNN model - it's zipped.

## Workflow

### 1. Scan Georeferencing
We use the Georeferencer Plugin in QGIS to align the scanned map with real-world coordinates.

### 2. Data Preparation and Image Tiling
The georeferenced raster is divided into small tiles, each 6x6 pixels, resulting in approximately 1.5 million tiles. The script for this process is included in the repository.

### 3. Training the Neural Network
We prepare our training dataset by categorising tiles into 6 classes: Class-0-water and WRAP classes 1 through 5. The CNN is trained to recognise these classes despite the noise and clutter.

### 4. Running the Model
The trained model is run on the tiles from the original georeferenced map, and each tile is attributed the most likely class, saved into a log file.

### 5. Recreating the Image
The image is recreated from the log file, using the original georeferenced raster's world file, and then imported back into QGIS for tidying up.

### 6. Tidying Up
The initial 6x6 pixel tiles resulted in some rogue polygons, so we repeated the process using 15x15 pixel tiles for better classification certainty. A combination of both tile sizes was used to produce the final vector layer.

## Final Output
The algorithm has proven effective on the WRAP map and has significantly reduced the amount of manual labour required. The digitised vector map layer is available and integrated into a WRAP Web Map.

## Dependencies
- QGIS
- TensorFlow
- NumPy
- Python 3.x
- Jupyter Notebook

## How to Use

1. Clone the repository.
2. Install the necessary dependencies.
3. Follow the notebooks in the provided order:
   - `01-map-tiler.ipynb` for tiling the map.
   - `02-classifier-training.ipynb` for training the classifier.
   - `03-map-tiles-classifier-with-tflite.ipynb` for classifying the tiles.
   - `04-map-recreator-from-tiles.ipynb` for recreating the map from classified tiles.
4. Review the results in QGIS.

## Conclusion
This project demonstrates an effective method for digitising scanned maps using CNNs. It requires high-quality, high-resolution scans for optimal results and can be replicated on other chorochromatic maps. Future work could involve streamlining the process and maybe automation of training data collection methods to make it easier to apply to other chorochromatic maps.


---

## WRAP Web Map
I've also built a WRAP Web Map with the output digitised vector layer here: [WRAP Web Map](https://obermajer.co.uk/WRAP-Web-Map/)
