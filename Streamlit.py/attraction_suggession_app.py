import streamlit as st
import pandas as pd
import joblib

# ------------------------------
# Streamlit App
# ------------------------------
st.title("🎡 Personalized Attraction Recommendations Based on User & content Preferences")


# MAIN TAB
tab1,tab2 = st.tabs(['Recommend attractions Based on User','Recommend attractions Based on content'])

# st.set_page_config(page_title="Attraction Recommendation Engine", page_icon="🌍")

# st.title('🌍 Content-Based Attraction Recommendation System')


# -----------------------COLLABORATIVE FILTERING---------------------#
# Load data
user_attraction_matrix = pd.read_csv('DataSets/Recommendation_Task_DataSet/user_attraction_matrix.csv')

attraction_similarity = pd.read_csv('DataSets/Recommendation_Task_DataSet/attraction_similarity.csv', index_col=0)




attraction_similarity_df = pd.DataFrame(attraction_similarity)

#Function
def recommend_attractions(user_id, user_attraction_matrix, item_similarity_df, top_n=5):
    # Set UserId as index for easier access
    user_attraction_matrix = user_attraction_matrix.set_index('UserId')

    # Get the user's ratings row
    user_ratings = user_attraction_matrix.loc[user_id]

    # Attractions the user has already visited (rated > 0)
    visited = user_ratings[user_ratings > 0].index.tolist()

    # Initialize scores dictionary
    scores = {}

    # Loop over attractions the user visited
    for attraction in visited:
        # Loop over similar attractions
        for similar_attraction, similarity_score in item_similarity_df[attraction].items():
            # Skip attractions the user already visited
            if similar_attraction not in visited:
                # Accumulate scores (weighted by user's rating)
                scores[similar_attraction] = scores.get(similar_attraction, 0) + similarity_score * user_ratings[attraction]

    # Sort attractions by score (highest first)
    sorted_recommendations = []
    for k, v in scores.items():
        sorted_recommendations.append((k, v))

    # Sort descending
    sorted_recommendations.sort(key=lambda x: x[1], reverse=True)

    # Return top N recommendations
    return sorted_recommendations[:top_n]


# Set default values
default_userid = user_attraction_matrix['UserId'].iloc[0]
default_top_n = 5

# Initialize session state for reset
if 'reset' not in st.session_state:
    st.session_state.reset = False

# Reset button function
def reset_form():
    st.session_state.UserId = default_userid
    st.session_state.TopN = default_top_n



with tab1:
  try:
        # Form
        with st.form("recommendation_form"):
            UserId = st.selectbox("Select User ID", sorted(user_attraction_matrix['UserId'].unique()), key="UserId")
            TopN = st.slider("Number of Recommendations", min_value=1, max_value=20, value=default_top_n, key="TopN")

            # Buttons
            recommend_btn = st.form_submit_button("Get Recommendations")
            reset_btn = st.form_submit_button("Reset Form", on_click=reset_form)

        # Display selected inputs
        st.subheader("📋 Selected Input Data")
        input_data = {
            'UserId': [UserId],
            'Top N Recommendations': [TopN]
        }
        input_df = pd.DataFrame(input_data)
        st.table(input_df)

        # After form submit
        if recommend_btn:
            recommendations = recommend_attractions(UserId, user_attraction_matrix, attraction_similarity_df, TopN)

            if not recommendations:
                st.warning("User has no ratings or not found.")
            else:
                st.success(f"✅ Top {TopN} Recommendations recommended by User - {UserId}:")
                for i, (attraction, score) in enumerate(recommendations, start=1):
                    st.write(f"**{i}. {attraction}** (score: {score:.2f})")

  except Exception as e:
        st.error(f"Failed to fetch recommendations: {e}")




# -----------------------CONTENT BASED FILTERING---------------------#
# Load saved models
tfidf = joblib.load('C:/Users/dhars/Downloads/Dhass/codeing/GUVI/2. MainBoot/4.Project_Code/Project4/Project4_Code/Tourism_Experince_Analytics/models/Recommendation_Task_Model/tfidf_vectorizer.joblib')
knn = joblib.load('C:/Users/dhars/Downloads/Dhass/codeing/GUVI/2. MainBoot/4.Project_Code/Project4/Project4_Code/Tourism_Experince_Analytics/models/Recommendation_Task_Model/knn_model.joblib')

# Load lookup table (deduplicated attractions)
df_lookup = pd.read_csv('C:/Users/dhars/Downloads/Dhass/codeing/GUVI/2. MainBoot/4.Project_Code/Project4/Project4_Code/Tourism_Experince_Analytics/DataSets/Recommendation_Task_DataSet/attraction_lookup.csv')

# Build combined_features for df_lookup (must match model training!)
df_lookup['combined_features'] = (
    df_lookup['AttractionType'].fillna('') + ' ' +
    df_lookup['CityName'].fillna('') + ' ' +
    df_lookup['Attraction'].fillna('') + ' ' + 
    df_lookup['Rating'].fillna(0).astype(str)
)

# Build TF-IDF matrix for df_lookup
tfidf_matrix = tfidf.transform(df_lookup['combined_features'])


# Dropdown list of attractions (sorted alphabetically for usability)
attraction_list = sorted(df_lookup['Attraction'].dropna().unique())

with tab2:
    try:
            selected_attraction = st.selectbox('Select Attraction:', options=attraction_list)

            # If user selects something
            if selected_attraction:
                # Find exact matching attraction index in df_lookup
                matching_attractions = df_lookup[df_lookup['Attraction'] == selected_attraction]
    
                if matching_attractions.shape[0] > 0:
                    # Get the correct row number corresponding to tfidf_matrix
                    row_number = matching_attractions.index[0]  # Because df_lookup is not shuffled, this works IF df_lookup is from the original df_attraction
    
                    # Alternative safer way:
                    # row_number = df_lookup.reset_index().index[df_lookup.index == matching_attractions.index[0]].tolist()[0]

                    st.write(f"Showing recommendations for **{df_lookup.iloc[row_number]['Attraction']}**:")

                    # Find similar attractions
                    distances, indices = knn.kneighbors(tfidf_matrix[row_number], n_neighbors=6)  # top 6 incl. itself

                    # Prepare DataFrame of recommendations
                    recommended_attractions = []
                    for i in range(1, len(indices[0])):  # skip first (itself)
                        attraction_idx = indices[0][i]
                        recommended_attractions.append({
                            'Attraction': df_lookup.iloc[attraction_idx]['Attraction'],
                            'City': df_lookup.iloc[attraction_idx]['CityName'],
                            'AttractionType': df_lookup.iloc[attraction_idx]['AttractionType'],
                            'Rating': df_lookup.iloc[attraction_idx]['Rating']
                        })

                    recommended_attractions_df = pd.DataFrame(recommended_attractions)

                    # Display recommendations
                    st.dataframe(recommended_attractions_df)

                else:
                    st.warning("No matching attractions found.")
    except Exception as e:
        st.error(f"Failed to fetch recommendations: {e}")
