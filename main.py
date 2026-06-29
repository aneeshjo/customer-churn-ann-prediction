from src.pipeline.predict_pipeline import PredictPipeline

sample_customer = {

    "Age":42,
    "Gender":"Male",
    "Country":"India",
    "City":"Mumbai",
    "Membership_Years":5,
    "Login_Frequency":18,
    "Session_Duration_Avg":24.3,
    "Pages_Per_Session":8,
    "Cart_Abandonment_Rate":0.15,
    "Wishlist_Items":6,
    "Total_Purchases":35,
    "Average_Order_Value":1850,
    "Days_Since_Last_Purchase":12,
    "Discount_Usage_Rate":0.45,
    "Returns_Rate":0.03,
    "Email_Open_Rate":0.72,
    "Customer_Service_Calls":1,
    "Product_Reviews_Written":5,
    "Social_Media_Engagement_Score":78,
    "Mobile_App_Usage":1,
    "Payment_Method_Diversity":3,
    "Lifetime_Value":125000,
    "Credit_Balance":3200,
    "Signup_Quarter":"Q2"

}

pipeline = PredictPipeline()

result = pipeline.predict(sample_customer)

print(result)