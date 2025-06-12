# 🧳 Tourism Experience Analytics: Classification, Prediction, and Recommendation System

## 🌐 Project Overview

This project is a full-fledged **Tourism Analytics System** that predicts:
- 🏷️ **Visit Mode** (e.g., Family, Business, Couples, Solo)
- 🌟 **Attraction Ratings** (1 to 5 scale)
- 📍 **Personalized Attraction Recommendations**

The solution integrates **Machine Learning** models with a **Streamlit-based web application** to deliver actionable insights and interactive features for users, travel platforms, and tourism professionals.

---

## 🧠 Skills Takeaway from This Project

- 📊 Data Cleaning and Preprocessing  
- 🔍 Exploratory Data Analysis (EDA)  
- 📈 Data Visualization  
- 🧠 Machine Learning (Regression, Classification, Recommendation)  
- 💻 SQL (Data Integration & Joins)  
- 🌐 Streamlit Web App Deployment  

---

## 🗺️ Domain

**Tourism & Travel Analytics**  
Focused on understanding tourist behavior and optimizing user satisfaction through predictive insights.

---

## 🛠️ Technical Tags

- Data Cleaning  
- Data Preprocessing  
- Exploratory Data Analysis (EDA)  
- Machine Learning (Regression, Classification, Recommendation)  
- Streamlit Web App  

---

## 🚀 Project Structure

### 📌 Key Components

#### 1. **Regression Model**
- **Goal**: Predict user rating for an attraction.
- **Models**: Linear Regression, Random Forest, XGBoost.
- **Target**: `Rating`

#### 2. **Classification Model**
- **Goal**: Predict mode of visit (e.g., Family, Business).
- **Models**: Logistic Regression, Random Forest, XGBoost, LightGBM.
- **Target**: `VisitMode`

#### 3. **Recommendation System**
- **Goal**: Provide personalized attraction suggestions.
- **Techniques**: Collaborative Filtering, Content-Based Filtering.

---

## 📂 Project Phases

1. **Data Cleaning**: Handle missing values, outliers, formatting inconsistencies.
2. **Preprocessing**: Feature encoding, aggregation, merging geographical and user data.
3. **EDA**: User distribution, attraction popularity, correlations.
4. **Model Training**: Regression, Classification, Recommendation systems.
5. **Model Evaluation**: R², MSE, Accuracy, Precision, Recall, F1, RMSE.
6. **Deployment**: Streamlit-based interactive applications.

---

## 📊 Streamlit Web Apps

### 👉 Live Applications

- 🎯 [Attraction Rating Predictor](https://touristattractionratings.streamlit.app/)
- 👥 [Visit Mode Classifier](https://tourismvisitmode.streamlit.app/)
- 💡 [Attraction Recommender](https://tourismattractionsuggession.streamlit.app/)

---

## 📌 Final Output Highlights

- **Regression**: Fetch R² Score & MSE  
- **Classification**: Fetch Accuracy, Precision, Recall, and F1-score across visit modes  
- **Recommendation**: Generate personalized ranked list & evaluate with RMSE  

---


## ✨ Demo & Usage
# Step1: Data Cleaning:
- Importing Uncleaned Dataset.
- Fetching csv files information.
- Data Cleaning:
    - 1. Normalize Formatting:
         - Stripping the white spaces.
    - 2. Verifying How many null values are present in each columns.
    - 3. Handling Missing data/values: City and User csv file has null values on the columns of CityName and CityId:
         - 1. Replacing the nan values in CityName column of City csv file:
         - 2. Replacing the nan values in CityId column of User csv file:
         - 3. Mapping the values for AttractionTypeId in Item csv:
    - 4. Validating Data Relationships Between Tables - Data Model:
         - ER Model
         - Validate all Relationships
    - 5. Standardize date and time format.
    - 6. Handle outliers:
         - To Handle Outlier, either use Domain-based rules (e.g., Rating should be between 1 and 5) or use Statistical rules(e.g., IQR)
            - Domain-based rules (e.g., Rating should be between 1 and 5)
    - 7. Handle any incorrect entries other columns
- Saving the cleaned DataSet

# Step2: Data PreProcessing:
- importing libraries
- Load cleaned datasets
> *Feature Engineering*
  - Encode categorical variables such as VisitMode, Continent, Country, and AttractionTypeId
      - 1. Performing a Label Encoder for necessary columns.
  - Aggregate user-level features to represent each user's profile (e.g., average ratings per visit mode).
      - 1. Finding Average rating per user
      - 2. Finding Count of visits per VisitMode per user
      - 3. Finding Average rating per attraction
      - 4. Finding Total visits per user
      - 5. Merge the above findings in  Transaction table
      - 6. Merging the Trasction Table and Model Table as Merged_data1
      - 7. Merging Item and Type Table as Merged_data2
      - 8. Merging Merged_data1 & Merged_data2 as Merged_data3
  - Join with User (UserId) ──┬─→ City (CityId) ──→ Country (CountryId) ──→ Region (RegionId) ──→ Continent (ContinentId)
      - 1. Merging City and Country as geographical_features
      - 2. Merging geographical_features and Region
      - 3. Merging geographical_features and Continent
      - 4. Dropping null values in geographical_features. If there is 1 nan value, then the whole row will be dropped
      - 5. Merging Merged_data3 and User as Merged_data
      - 6. Finaly Merging Merged_data & geographical_features as Final_Merged_data
      - 7. Fetching only necessary columns
> *Normalization:*
  - Scale numerical features such as Rating for better model convergence
      - 1. Select numerical columns to normalize.
      - 2. Using MinMaxScaler
- Saving the pre-processed DataSet

# Step3: EDA:
- Importing necessary Libraries
- Load preprocessed dataset
- ○	Visualize user distribution across continents, countries, and regions
     - Count of users by continent
     - Count of users by region
     - Count of users by Country
     - Count of users by City
- ○	Explore attraction types and their popularity based on user ratings.
     - Popularity of Attraction Types by Visits
     - Average ratings of Attraction Type
- ○	Investigate correlation between VisitMode and user demographics to identify patterns.
     - Number of Users by Visit Mode Across Continents
- ○	Analyze distribution of ratings across different attractions and regions.
     - Distribution of Top 100 Ratings Across Attractions and Regions

# Step4: Model Training and Evaluation:
## 1. Regression:
### 🎯 **Use Case: Predicting Attraction Ratings**
> *📌 Objective*
- To predict the rating (1–5 scale) a user will assign to a tourist attraction using a regression model based on:
    - Historical visit data
    - User demographics
    - Attraction characteristics

> *🧠 Why This Matters*
- Travel platforms can enhance recommendation systems and satisfaction predictions.
- Tour operators can identify potentially low-rated attractions and proactively improve them.
- Personalized travel guides can rank attractions based on predicted satisfaction, increasing user engagement.

> *📥 Input Features*
- Category	                    Example Features
- User Demographics	            Continent, Region, Country, City
- Visit Details	                Year, Month, Mode of Visit (business, family, solo, etc.)
- Attraction Details	        Attraction Type, Location, Historical Avg Rating

> *🎯 Target Variable:*
- Rating (1 to 5) – A continuous numerical value representing satisfaction or experience.

> *🤖 Model Options:*
- Baseline: 
    - DecisionTreeRegressor
- Advanced: 
    - Random Forest Regressor
    - XGBoost , GradientBoostingRegressor, lightgbm
    - Hyper Paramter Tuning: RandomizedSearchCV


## 2. Classification:
### 🎯 **Use Case: Predicting Visit Mode**
> *📌 Objective*
- To predict the visit mode of a tourist (Business, Family, Couples, Friends, etc.) using a classification model based on:
    - User demographics
    - Attraction characteristics
    - Historical visit data

> *🧠 Why This Matters*
- Travel platforms can tailor marketing campaigns (e.g. promote family-friendly packages to users predicted to travel with family).
- Hotels can optimize offerings and amenities based on likely visitor types (business travelers need fast Wi-Fi, families want extra beds, etc.).
- Attraction organizers can plan resources and experiences more effectively (guided tours for couples, play areas for families).

> *📥 Input Features*
- Category	                       Example Features
- User Demographics	              Continent, Region, Country, City
- Attraction Characteristics	  Attraction Type, Popularity score
- Historical Visit Data	          Month, Year, Previous visit modes (user’s history), Visit frequency

> *🎯 Target Variable:*
- Visit Mode (categorical): Business, Family, Couples, Friends, Solo, Other

> *🤖 Model Options:*
- Advanced:
    - Random Forest Classifier
    - XGBoost Classifier
    - LightGBM Classifier
    - Hyper Paramter Tuning: RandomizedSearchCV


## 3. Recommendation:
### 🎯 **Use Case: Personalized Attraction Recommendations**
> *📌 Objective*
- Develop a recommendation system to suggest tourist attractions based on:
- user’s historical preferences

> *🧠 Why This Matters*
- 🏖️ Travel Platforms → Guide users to attractions they will likely enjoy → increase engagement, satisfaction, and retention.
- 🗺️ Destination Management Organizations (DMOs) → Identify emerging trends, promote targeted attractions.
- 🎯 Marketing Teams → Personalize campaigns based on user segments and preferences.

> *🤖 Types of Recommendation Approaches*
- 1️⃣ Collaborative Filtering
    - Recommend attractions based on preferences of similar users.
    - Uses user-item interaction matrix (user–attraction ratings or visits).

- 2️⃣ Content-Based Filtering
    - Suggest attractions similar to those already liked/visited by the user.
    - Uses attraction features: type, location, popularity, amenities.

> *🎯 Output*
- Ranked list of recommended attractions personalized for the user.

# Step5: Deployment - Streamlit:
- Deploying below 3 files in Streamlit:
    - Streamlit.py\attraction_ratings_app.py
    - Streamlit.py\user_visit_mode_app.py
    - Streamlit.py\attraction_suggession_app.py
