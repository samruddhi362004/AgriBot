import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import io
from gtts import gTTS
import tempfile
from googletrans import Translator

# trained model
model = load_model("C:/Users/user/Desktop/AI ChatBot/pythonProject/cropdiseasedetection/crop_disease_model.h5", compile=False)


class_names = ["Healthy", "Bacterial Spot", "Leaf Mold", "Yellow Leaf Curl Virus"]


disease_remedies = {
    "Healthy": "Your plant is healthy! Keep up with good agricultural practices.",
    "Bacterial Spot": "Apply copper-based fungicides, avoid overhead watering, and remove infected leaves.",
    "Leaf Mold": "Ensure good air circulation, reduce humidity, and use fungicides like copper sprays.",
    "Yellow Leaf Curl Virus": "Control whiteflies using neem oil or insecticidal soap, and remove infected plants to prevent spread."
}


language_map = {
    "English": "en",
    "Hindi (हिन्दी)": "hi"
}


translator = Translator()

# Function to preprocess the uploaded image
def preprocess_image(img):
    if not isinstance(img, Image.Image):
        img = Image.open(io.BytesIO(img))  # Convert byte data to PIL Image
    img = img.resize((224, 224))
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

#translate text
def translate_text(text, dest_lang):
    try:
        translated = translator.translate(text, dest=dest_lang)
        return translated.text
    except Exception as e:
        return f"(Translation error: {e}) {text}"

#speak text
def speak_text(text, lang='en'):
    tts = gTTS(text, lang=lang)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts.save(fp.name)
        st.audio(fp.name, format='audio/mp3')

# Prediction remedy voice
def predict_disease(img, symptoms="", lang="en"):
    processed_img = preprocess_image(img)
    prediction = model.predict(processed_img)
    predicted_class = class_names[np.argmax(prediction)]
    confidence = np.max(prediction) * 100

    remedy = disease_remedies.get(predicted_class, "No remedy available.")
    if symptoms:
        remedy += f" Since you described '{symptoms}', consider consulting an expert for further guidance."

    # Translate the full response if needed
    response_text = f"The predicted disease is {predicted_class}. Confidence level is {confidence:.2f} percent. Remedy: {remedy}"
    translated_response = translate_text(response_text, lang)

    return predicted_class, confidence, remedy, translated_response

# Streamlit UI
st.title("🌱 Crop Disease Detection Chatbot 🤖")
st.write("Upload a crop leaf image and describe the symptoms. Get disease predictions, remedies, and voice output in your chosen language.")

# LangSelect
selected_lang = st.selectbox("Select language for output (text + voice):", list(language_map.keys()))
lang_code = language_map[selected_lang]


uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "png", "jpeg"])


symptoms = st.text_area("Describe the symptoms (optional)", "")

# Prediction
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    if st.button("Detect Disease"):
        disease, confidence, remedy, translated_response = predict_disease(uploaded_file.getvalue(), symptoms, lang_code)


        st.success(f"Prediction: **{disease}**")
        st.info(f"Confidence Level: {confidence:.2f}%")
        st.warning(f"Suggested Remedy: {remedy}")

        #translated response
        if lang_code != 'en':
            st.markdown(" Translated Output:**")
            st.write(translated_response)

        # Voiceoutput
        speak_text(translated_response, lang=lang_code)
