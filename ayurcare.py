import streamlit as st

# Define user data dictionary
users = {
    "prithiv": "pmprithiv",
    "tony":"preetamtony",
    "karolin":"tony"
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


def medical():
    st.title("VedaCare Chatbot")
    st.markdown(
        """
        <iframe width="350" height="430" allow="microphone;" src="https://console.dialogflow.com/api-client/demo/embedded/8eca1481-460d-4a51-aa6a-181398265096"></iframe>
        <br>
        """,
        unsafe_allow_html=True
    )


    st.title("Medical Information")

    with st.form(key='medical_form'):
        st.header("Personal Information")
        name = st.text_input("Name", "")
        age = st.number_input("Age", min_value=0, max_value=150, step=1)
        dob = st.date_input("Date of Birth")
        gender = st.radio("Gender", ["Male", "Female", "Other"])

        st.header("Medical History")
        diabetes = st.selectbox("Do you have diabetes?", ["Yes", "No"])
        hypertension = st.selectbox("Do you have hypertension?", ["Yes", "No"])
        heart_disease = st.selectbox("Do you have heart disease?", ["Yes", "No"])
        asthma = st.selectbox("Do you have asthma?", ["Yes", "No"])
        other_conditions = st.text_area("Other medical conditions", "")

        st.header("Symptoms")
        symptom1 = st.text_input("Symptom 1", "")
        symptom2 = st.text_input("Symptom 2", "")
        symptom3 = st.text_input("Symptom 3", "")

        st.header("Symptoms Severity")
        severity1 = st.slider("Severity of symptom 1 (0-10)", min_value=0, max_value=10, value=5)
        severity2 = st.slider("Severity of symptom 2 (0-10)", min_value=0, max_value=10, value=5)
        severity3 = st.slider("Severity of symptom 3 (0-10)", min_value=0, max_value=10, value=5)

        st.header("Other Related Queries")
        other_queries = st.text_area("Other related queries", "")

        submit_button = st.form_submit_button(label='Save')

    if submit_button:
        # Process the input data here (e.g., store it in a database, perform analysis, etc.)
        st.success("Your information has been saved successfully!")


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
        From personalized health recommendations to consultations with experienced Ayurvedic practitioners, we've got you covered.

        </div>
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
