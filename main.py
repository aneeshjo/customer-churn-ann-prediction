from src.pipeline.predict_pipeline import PredictPipeline

sample_customer = {

    "Age":45,
    "Gender":"Male",
    "Country":"India",
    "City":"Mumbai",
    "Membership_Years":5,
    "Login_Frequency":12,
    "Session_Duration_Avg":20.5,
    "Pages_Per_Session":7,
    "Cart_Abandonment_Rate":0.20,
    "Wishlist_Items":5,
    "Total_Purchases":50,
    "Average_Order_Value":1800,
    "Days_Since_Last_Purchase":10,
    "Discount_Usage_Rate":0.30,
    "Returns_Rate":0.05,
    "Email_Open_Rate":0.60,
    "Customer_Service_Calls":1,
    "Product_Reviews_Written":3,
    "Social_Media_Engagement_Score":70,
    "Mobile_App_Usage":1,
    "Payment_Method_Diversity":3,
    "Lifetime_Value":120000,
    "Credit_Balance":3000,
    "Signup_Quarter":"Q2"

}

pipeline = PredictPipeline()

result = pipeline.predict(sample_customer)

print(result)