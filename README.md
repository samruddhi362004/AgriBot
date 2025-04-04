# Crop Disease Detection Chatbot

## Overview
The **Crop Disease Detection Chatbot** is an AI-powered tool that helps farmers and agricultural experts identify crop diseases from leaf images. The chatbot uses a deep learning model to predict diseases and suggests remedies based on symptoms. It also supports multilingual voice responses using **Google Translate and gTTS**.

## Features
- **Image-based Disease Detection**: Upload a crop leaf image to detect diseases.
- **Symptom-based Remedy Suggestions**: Enter symptoms for additional recommendations.
- **Voice Response**: Get an audio response for predictions and remedies.
- **Multilingual Support**: Convert remedy suggestions to different languages, including Hindi.
- **Interactive UI**: Built using **Streamlit** for an intuitive interface.

## Technologies Used
- **Python**: Core programming language
- **TensorFlow/Keras**: Deep learning model for disease classification
- **PIL (Pillow)**: Image processing
- **gTTS**: Text-to-Speech conversion
- **Google Translate API**: Multilingual support
- **Streamlit**: Frontend framework for chatbot UI

## Installation
### Prerequisites
Ensure you have Python 3.7+ installed. You also need the following libraries:
```bash
pip install tensorflow streamlit pillow gtts googletrans==4.0.0-rc1 numpy
```

### Running the Chatbot
Navigate to the project directory and run:
```bash
streamlit run app.py
```

## Usage
1. **Upload an Image**: Select a leaf image for analysis.
2. **Describe Symptoms (Optional)**: Enter additional symptoms for better recommendations.
3. **Disease Detection**: The chatbot predicts the disease and confidence level.
4. **Remedy Suggestions**: The chatbot provides remedies based on the detected disease.
5. **Voice Output**: Listen to the prediction and remedy in English or your chosen language.
6. **Multilingual Support**: Select a language to translate the remedy.

## Project Flowchart
(Attach Flowchart Image)

## Future Enhancements
- **Expand disease database**: Train on more crop diseases.
- **Live Camera Support**: Enable real-time leaf scanning.
- **Community Support**: Add expert consultation and farmer discussions.
- **Mobile App Version**: Develop a mobile-friendly version.

## Contributors
- **Samruddhi Thakur**
- **Ketaki Modi**  

## License
This project is open-source and available under the MIT License.


