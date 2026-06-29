import streamlit as st

from src.pipeline.predict_pipeline import PredictPipeline

# --------------------------------------------------------
# Page Configuration
# --------------------------------------------------------

st.set_page_config(

    page_title="Customer Churn Prediction",

    page_icon="📈",

    layout="wide"

)

# --------------------------------------------------------
# Title
# --------------------------------------------------------

st.title("📈 Customer Churn Prediction Dashboard")

st.write(
    "Predict whether a customer is likely to churn using an Artificial Neural Network."
)

# --------------------------------------------------------
# Customer Information
# --------------------------------------------------------

st.header("Customer Information")

col1, col2 = st.columns(2)

with col1:

    age = st.number_input("Age", 18, 100, 45)

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    country = st.text_input(
        "Country",
        "India"
    )

    city = st.text_input(
        "City",
        "Mumbai"
    )

    membership_years = st.number_input(
        "Membership Years",
        0,
        30,
        5
    )

    login_frequency = st.number_input(
        "Login Frequency",
        0,
        100,
        12
    )

    session_duration = st.number_input(
        "Session Duration Average",
        value=20.5
    )

    pages = st.number_input(
        "Pages Per Session",
        value=7
    )

    abandonment = st.number_input(
        "Cart Abandonment Rate",
        value=0.20
    )

    wishlist = st.number_input(
        "Wishlist Items",
        value=5
    )

    purchases = st.number_input(
        "Total Purchases",
        value=50
    )

    avg_order = st.number_input(
        "Average Order Value",
        value=1800.0
    )

with col2:

    last_purchase = st.number_input(
        "Days Since Last Purchase",
        value=10
    )

    discount = st.number_input(
        "Discount Usage Rate",
        value=0.30
    )

    returns = st.number_input(
        "Returns Rate",
        value=0.05
    )

    email = st.number_input(
        "Email Open Rate",
        value=0.60
    )

    service = st.number_input(
        "Customer Service Calls",
        value=1
    )

    reviews = st.number_input(
        "Product Reviews Written",
        value=3
    )

    engagement = st.number_input(
        "Social Media Engagement Score",
        value=70
    )

    mobile = st.selectbox(
        "Mobile App Usage",
        [0, 1]
    )

    payment = st.number_input(
        "Payment Method Diversity",
        value=3
    )

    lifetime = st.number_input(
        "Lifetime Value",
        value=120000.0
    )

    credit = st.number_input(
        "Credit Balance",
        value=3000.0
    )

    quarter = st.selectbox(
        "Signup Quarter",
        ["Q1", "Q2", "Q3", "Q4"]
    )

# --------------------------------------------------------
# Prediction Button
# --------------------------------------------------------

if st.button("Predict Churn"):

    customer = {

        "Age": age,

        "Gender": gender,

        "Country": country,

        "City": city,

        "Membership_Years": membership_years,

        "Login_Frequency": login_frequency,

        "Session_Duration_Avg": session_duration,

        "Pages_Per_Session": pages,

        "Cart_Abandonment_Rate": abandonment,

        "Wishlist_Items": wishlist,

        "Total_Purchases": purchases,

        "Average_Order_Value": avg_order,

        "Days_Since_Last_Purchase": last_purchase,

        "Discount_Usage_Rate": discount,

        "Returns_Rate": returns,

        "Email_Open_Rate": email,

        "Customer_Service_Calls": service,

        "Product_Reviews_Written": reviews,

        "Social_Media_Engagement_Score": engagement,

        "Mobile_App_Usage": mobile,

        "Payment_Method_Diversity": payment,

        "Lifetime_Value": lifetime,

        "Credit_Balance": credit,

        "Signup_Quarter": quarter

    }

    pipeline = PredictPipeline()

    result = pipeline.predict(customer)

    st.divider()

    st.subheader("Prediction")

    probability = result["probability"]

    if result["prediction"] == 1:

        st.error("🔴 Customer Will Churn")

    else:

        st.success("🟢 Customer Will Stay")

    st.metric(

        "Churn Probability",

        f"{probability*100:.2f}%"

    )

    st.progress(probability)