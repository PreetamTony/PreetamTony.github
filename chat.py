import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier

# Define user data dictionary
users = {
    "prithiv": "pmprithiv"
}

def signup(username, password):
    if username in users:
        return False
    elif not username or not password:
        return False
    else:
        users[username] = password
        return True

def login(username, password):
    if username in users and users[username] == password:
        return True
    else:
        return False

# Load datasets
symptoms_data = pd.read_csv( "C:/Users/preet/OneDrive/Documents/Python Files/Ayurcare/test1.csv")

# Feature extraction
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(symptoms_data['Symptom 1'] + ' ' + symptoms_data['Symptom 2'] + ' ' + symptoms_data['Symptom 3'])
y = symptoms_data['Disease']

# Train Decision Tree Classifier
model = DecisionTreeClassifier()
model.fit(X, y)

def chatbot(input_symptoms):
    input_vector = vectorizer.transform([input_symptoms])
    prediction = model.predict(input_vector)[0]
    remedy = symptoms_data[symptoms_data['Disease'] == prediction]['Ayurvedic Remedies'].values[0]
    utilization = symptoms_data[symptoms_data['Disease'] == prediction]['Utilization'].values[0]
    return prediction, remedy, utilization

def medical():
    st.title("Medical Input")

    with st.form(key='medical_form'):
        # Personal Information
        st.header("Personal Information")
        name = st.text_input("Name", "")
        age = st.number_input("Age", min_value=0, max_value=150, step=1)
        dob = st.date_input("Date of Birth")
        gender = st.radio("Gender", ["Male", "Female", "Other"])

        # Medical History
        st.header("Medical History")
        diabetes = st.selectbox("Do you have diabetes?", ["Yes", "No"])
        hypertension = st.selectbox("Do you have hypertension?", ["Yes", "No"])
        heart_disease = st.selectbox("Do you have heart disease?", ["Yes", "No"])
        asthma = st.selectbox("Do you have asthma?", ["Yes", "No"])
        other_conditions = st.text_area("Other medical conditions", "")

        # Symptoms Input
        st.header("Symptoms")
        symptom1 = st.text_input("Symptom 1", "")
        symptom2 = st.text_input("Symptom 2", "")
        symptom3 = st.text_input("Symptom 3", "")

        # Severity Input
        st.header("Symptoms Severity")
        severity1 = st.slider("Severity of symptom 1 (0-10)", min_value=0, max_value=10, value=5)
        severity2 = st.slider("Severity of symptom 2 (0-10)", min_value=0, max_value=10, value=5)
        severity3 = st.slider("Severity of symptom 3 (0-10)", min_value=0, max_value=10, value=5)

        # Other related queries
        st.header("Other Related Queries")
        other_queries = st.text_area("Other related queries", "")
        st.header("Disease")
        st.write("Predicted Diseas: Iron Deficiency")
        st.header("Remedy")
        st.write("Include spinach and lentils in your diet regularly. Consume jaggery as a natural source of iron.")
        # Submit button
        submit_button = st.form_submit_button(label='Save')

    # Process the input data after form submission
    if submit_button:
        # Combine symptoms
        input_symptoms = symptom1 + ' ' + symptom2 + ' ' + symptom3
        # Predict disease and suggest remedy
        predicted_disease, ayurvedic_remedies, method = chatbot(input_symptoms)
        # Display results
        st.success(f"Predicted disease: {predicted_disease}")
        st.success(f"Ayurvedic remedies: {ayurvedic_remedies}")
        st.success(f"Utilization: {method}")
        # Process the input data here (e.g., store it in a database, perform analysis, etc.)
        st.write("Include spinach and lentils in your diet regularly. Consume jaggery as a natural source of iron.")

def main():
    st.title("Welcome to VedaCare App")
    st.markdown(
        """
        <div style='text-align: center;'><i>Your personalized Ayurveda healthcare companion</i></div>
        <br>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <style>
        body {
            background-color: #F0FFFF; /* Azure color */
        }
        .header-text {
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            color: #003366;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQXaKbzCUzgMV8MJzRDzRqCbmnbqeuQ_UNwZg&s",
             use_column_width=True)

    st.markdown(
        """
        <div class='header-text'>AyurCare is your one-stop destination for all your Ayurvedic healthcare needs.
        From personalized health recommendations to consultations with experienced Ayurvedic practitioners, we've got you covered.</div>
        <br>
        """,
        unsafe_allow_html=True
    )

    page = st.sidebar.radio("Navigation", ["Sign Up", "Login"])

    if page == "Sign Up":
        st.header("Sign Up")
        new_username = st.text_input("Username")
        new_password = st.text_input("Password", type="password")

        if st.button("Sign Up"):
            if signup(new_username, new_password):
                st.success("Sign up successful! Please log in.")
            else:
                st.error(
                    "Username already exists or fields are empty. Please choose a different username and ensure both fields are filled.")

    elif page == "Login":
        st.header("Login")
        username = st.text_input("Username")  # Set default username
        password = st.text_input("Password", type="password")  # Set default password

        if st.button("Login"):
            if login(username, password):
                st.success("Login successful!")
                medical()  # Call medical input form function after successful login
            else:
                st.error("Invalid username or password")

    st.markdown(
        """
        <br><br><br>
        <hr style='border: none; height: 2px; color: #999; background-color: #999;'>
        <div style='text-align: center;'><i>© 2024 AyurCare. All rights reserved.</i></div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
