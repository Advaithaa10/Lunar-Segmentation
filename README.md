### Welcome to Lunar Terrain Image Segmentation App

This repository is made to segment images of moon

### How to setup the project in your system
1. Download the Repository and open the project directory in your editor (VS Code)
2. Create your virtual environment using ```python -m venv <name_of_the_venv>```
3. Activate your virtual environment using ```.\<name_of_the_venv>\Scripts\activate```
4. Install the requirements using ````python -m pip install -r requirements.txt```
5. You can train your model using the advaithaa-a6.ipynb python notebook via Kaggle
6. Add your trained model
7. In command prompt first run your FastAPI app:- ```uvicorn backend:app --reload```
8. Then again open command prompt and run the streamlit app:- ```streamlit run frontend.py```

### About the Model used
1. This model is trained using UNET with RESNET50 Backbone
2. The data used for the training can be found on Kaggle
3. We used first 8000 images from ```render``` (artificially generted Moon terrain) & ```clean``` (respective masks) directories for training.

### FastAPI
![image](https://github.com/user-attachments/assets/635c108d-1aec-4159-8476-353ddf604057)

### Streamlit WebApp
![image](https://github.com/user-attachments/assets/7558d259-52dd-4bd9-b8b8-ea7a3cca9ad6)
