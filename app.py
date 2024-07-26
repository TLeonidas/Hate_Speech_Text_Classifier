import gradio as gr
import joblib as joblib

# Load your serialized objects
model = joblib.load('random_forest_model_3labels2.joblib')
encoder = joblib.load('label_encoder2.joblib')
vectorizer = joblib.load('count_vectorizer2.joblib')

def predict(input_text):
    # Preprocess the input with your vectorizer and encoder as needed
    vectorized_text = vectorizer.transform([input_text])
    
    # Make a prediction
    prediction = model.predict(vectorized_text)
    
    # Decode the prediction into a readable label
    decoded_prediction = encoder.inverse_transform(prediction)
    
    # Return the decoded prediction
    return decoded_prediction[0]  #

# Setup the Gradio interface
iface = gr.Interface(fn=predict,
                     inputs=gr.Textbox(lines=2, placeholder="Enter Text Here..."),
                     outputs="text",
                     description="Detects hate speech AGAINST GROUPS. Outputs 'Neutral or Ambiguous', 'Not Hate', or 'Offensive or Hate Speech'.")

# Launch the app
iface.launch()


"""
import gradio as gr

def greet(name):
    return "Hello " + name + "!!"

iface = gr.Interface(fn=greet, inputs="text", outputs="text")
iface.launch()
"""