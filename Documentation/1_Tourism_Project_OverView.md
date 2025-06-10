✅ #*Project Overview Goal:*
      Build a system that predicts: 
                     -> visit modes, 
                     -> attraction ratings, and 
                     -> provides personalized recommendations using machine learning and deploys it via a Streamlit app.

🔧 ##*Key Components:*
**1. Regression Model:**
   ***Goal:*** Predict user rating for an attraction
   ***Target:*** Rating
   ***Model Suggestions:*** Linear Regression, Random Forest Regressor, XGBoost Regressor
   ***Aim:*** predict the rating a user might give to a tourist attraction based on historical data, user demographics, and attraction features

2. **Classification Model**
   ***Goal:*** Predict visit mode (e.g., Family, Business)
   ***Target:*** VisitMode
   ***Model Suggestions:*** Logistic Regression, Random Forest Classifier, LightGBM, XGBoost
   ***Aim:*** predict the mode of visit (e.g., business, family, couples, friends) based on user and attraction data

3. **Recommendation System**
   ***Goal:*** Suggest attractions
   ***Aim:*** suggest tourist attractions based on a user's historical preferences and similar users’ preferences


🚀 ##*Approach Summary*

1. **Data Cleaning**

   * Handle missing values in datasets
   * Resolve discrepancies in city names and categorical fields
   * Standardize date/time formats
   * Address outliers and incorrect entries

2. **Preprocessing**

   * Encode categorical variables
   * Aggregate user-level features
   * Join multiple datasets into a unified format
   * Normalize numerical fields

3. **📊 EDA (Exploratory Data Analysis)**

   * Visualize user distribution across continents, countries, and regions
   * Identify patterns in visit mode by demographic
   * Explore attraction types and their popularity based on user ratings.
   * Investigated correlations between `VisitMode` and user demographics.

4. **Model Training**

   * Regression for rating prediction
   * Classification for visit mode
   * Recommendation using collaborative/content-based filtering

5. **🧪 Model Evaluation**

   * Regression: MSE, RMSE, R²
   * Classification: Accuracy, Precision, Recall, F1 Score
   * Recommendations: MAP, RMSE

6. **💻 Deployment**

   * Streamlit app with user inputs and predictions
   * Visualization of key insights for decision-making


#*Final Output:*
1. **Regression**: Fetch R2 Score & MSE
2. **Classification**: Fetch Accuracy, High precision, recall, and F1-score across all visit modes.
3. **Recommendation**: Fetch RMSE
     