# 📸 Image Super Resolution

![Image-Super-Resolution](https://github.com/FerasAlshash/Image-Super-Resolution/blob/main/Image%20Super%20Resolution.jpg)




Welcome to the **Image Super Resolution** project! This repository contains a Flask-based web application that enhances the resolution of images using a pre-trained deep learning model. The project leverages the `enhanced_sequential_sr_model.h5` file, stored with Git LFS, to upscale low-resolution images to high-resolution outputs.

---

## 🌟 Project Overview

This application uses a TensorFlow/Keras model to perform super-resolution on uploaded images. The model is integrated into a Flask server, allowing users to upload images via a simple web interface (built with HTML templates) and download the enhanced versions.

- **📂 Repository Structure**:
  - `app.py`: The main Flask application script.
  - `templates/index.html`: The HTML template for the web interface.
  - `enhanced_sequential_sr_model.h5`: The pre-trained model file (stored with Git LFS, ~418 MB).

- **🔧 Technologies Used**:
  - Python
  - Flask (Web Framework)
  - TensorFlow/Keras (Deep Learning)
  - PIL (Image Processing)
  - Git LFS (Large File Storage)

---

## 🚀 Features

- 🌄 Enhance low-resolution images to high-resolution.
- 📤 Upload images via a user-friendly web interface.
- 📥 Download the enhanced image as a JPEG file.
- ⚡ Real-time processing using a pre-trained model.

---

## 📋 Prerequisites

Before running the project, ensure you have the following installed:

- **Python 3.7+**
- **Git** (for cloning the repository)
- **Git LFS** (to handle the large model file)
- Required Python packages (listed in `requirements.txt`)

### Installation of Dependencies

1. Clone the repository:
   ```bash
   git clone https://github.com/FerasAlshash/Image-Super-Resolution.git
   cd Image-Super-Resolution


## Install Git LFS (if not already installed):

Download from git-lfs.github.com and follow the installation instructions.

## Pull the large model file using Git LFS:

git lfs pull

## 🛠️ Setup and Running

Ensure all prerequisites are met.

## Run the Flask application:

python app.py

Open your browser and go to http://127.0.0.1:5000/ to access the web interface.

## 📝 Usage

## Upload an Image:


Click the upload button and select a low-resolution image.

## Enhance the Image:

The application will process the image using the pre-trained model.

Wait for the enhancement to complete (depending on image size and system performance).

## Download the Result:

Download the enhanced image as enhanced_image.jpg.

## 📦 Model Details

File Name: enhanced_sequential_sr_model.h5

Size: ~418 MB (stored with Git LFS)

Framework: TensorFlow/Keras

Purpose: Trained to upscale images while preserving details.

Note: The model file is large and requires Git LFS to be downloaded. Ensure you have sufficient disk space and internet bandwidth.

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact Information 📞

For any questions or feedback, feel free to reach out:

- **Email**: [ferasalshash@gmail.com](mailto:ferasalshash@gmail.com)  
- **GitHub**: [FerasAlshash](https://github.com/FerasAlshash)  
- **LinkedIn**: [Feras Alshash](https://www.linkedin.com/in/feras-alshash-bb3106a9/)  

