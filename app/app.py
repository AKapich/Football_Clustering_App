import streamlit as st
from streamlit_extras.stoggle import stoggle
import openai
import pandas as pd
from PIL import Image
from clustering_functions import *
from process4positions import relevant_features_dict, new_metrics_dict


st.set_page_config(
        page_title="Player Profiles App",
        #page_icon="⚽",
        page_icon = 'https://raw.githubusercontent.com/AKapich/Football_Clustering_App/main/app/alekskapich.ico'
    )

outfield = pd.read_csv('https://raw.githubusercontent.com/AKapich/Football_Clustering_App/main/app/outfield365full.csv')
goalkeepers = pd.read_csv('https://raw.githubusercontent.com/AKapich/Football_Clustering_App/main/app/goalkeepers365full.csv')

st.title("Player Profiles in Top 5 Leagues Analytical Tool")
st.markdown("*Platform providing ML tool to discover player profiles for particular positions in the top 5 european leagues*")
st.markdown("---")

st.markdown(
    """
    <style>
        [data-testid=stSidebar] [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True
)
with st.sidebar:
    st.image("https://raw.githubusercontent.com/AKapich/Football_Clustering_App/main/app/alekskapich.png", width=200)


selected_position = st.sidebar.selectbox("Select position to scrutinize:",     
    ['Goalkeeper', 'Full Back', 'Centre Back', 'Defensive Midfielder', 
    'Central Midfielder', 'Attacking Midfielder', 'Winger', 'Centre Forward'],
      index=7)

if selected_position != 'Goalkeeper':
    adequate_df = outfield
else:
    adequate_df=goalkeepers


# SELECT OPTIONS
selected_range = st.sidebar.slider("Select an age range for the analysed players: ", 16, 43, (16, 43))
minute_threshold = st.sidebar.slider("Select minimum amount of minutes played to be considered in the analysis: ", 180, 1800, 540)
clustered_df = basic_clustering(adequate_df, selected_position, age_lower_threshold=selected_range[0],
                                 age_upper_threshold=selected_range[1], minute_threshold=minute_threshold)
selected_cluster = st.selectbox('Select cluster: ', sorted(clustered_df['Cluster'].unique()), index=0)


# SELECT METRICS FOR THE SWARMPLOTS
select1, select2, select3 = st.columns(3)
# We want to find top 3 metrics where players from the cluster may stand out - method to upgrade!
column_list = relevant_features_dict[selected_position]+new_metrics_dict[selected_position]
our_cluster = clustered_df[clustered_df['Cluster']==selected_cluster][column_list]
others = clustered_df[clustered_df['Cluster']!=selected_cluster][column_list]

perc_columns = others.select_dtypes(include=['object']).columns
our_cluster[perc_columns] = our_cluster[perc_columns].applymap(lambda x: float(str(x).replace('%', '')))
others[perc_columns] = others[perc_columns].applymap(lambda x: float(str(x).replace('%', '')))

diff = our_cluster.mean() - others.mean()
top3metrics = list(diff.sort_values(ascending=False).index)[:3]
with select1:
    selected_items1 = st.selectbox("Metric 1:", column_list, column_list.index(top3metrics[0]))
with select2:
    selected_items2 = st.selectbox("Metric 2:", column_list, column_list.index(top3metrics[1]))
with select3:
    selected_items3 = st.selectbox("Metric 3:", column_list, column_list.index(top3metrics[2]))
selected_items = [selected_items1, selected_items2, selected_items3]


col1, col2 = st.columns(2)
with col1:
    df2display = clustered_df[clustered_df['Cluster']==selected_cluster][['Player', 'Country']]
    df2display = df2display.sort_values(by='Player', key=lambda x: x.str.split().str[-1])
    df2display.index = range(1, len(df2display)+1)
    st.markdown(f"Players categorized into cluster {selected_cluster}:")
    st.write(df2display)
with col2:
    st.write(f"Cluster {selected_cluster} vs other  {selected_position}'s:")
    #for i in range(3):
    st.pyplot(beeswarm_comparison(clustered_df=clustered_df, metric=selected_items[0], cluster2highlight=selected_cluster))
    st.pyplot(beeswarm_comparison(clustered_df=clustered_df, metric=selected_items[1], cluster2highlight=selected_cluster))
    st.pyplot(beeswarm_comparison(clustered_df=clustered_df, metric=selected_items[2], cluster2highlight=selected_cluster))


st.markdown('---')
apikey = st.text_input("Enter your OpenAI API key here:")
openai.api_key = apikey

try:
    if st.button("Generate AI driven analysis!"):
        ai_response= generate_AI_analysis(our_cluster, selected_position)
        stoggle("Here's the analysis:", ai_response)
except Exception:
    st.write('Provide valid API key. You can obtain it from https://beta.openai.com/account/api-keys')
    

#
st.markdown('---')
# opta = opta.resize((1030, 348))
st.image('https://raw.githubusercontent.com/AKapich/Football_Clustering_App/main/app/Opta_by_Stats_Perform_Logo.png',
          caption='App made by Aleks Kapich. Data powered by Opta',
          width=773)


# signature
st.sidebar.markdown('---')
# col1, col2 = st.sidebar.columns(2)
# with col1:
#     logo = Image.open("C:/Users/Aleks/OneDrive/Dokumenty/GitHub/Football_Clustering/app/alekskapich.png")
#     logo = logo.resize((250, 250))
#     st.sidebar.image(logo)
# #st.sidebar.image(Image.open("C:/Users/Aleks/OneDrive/Dokumenty/GitHub/Football_Clustering/app/alekskapich.png"))
# with col2:
st.sidebar.write("[Twitter](https://twitter.com/AKapich)")
st.sidebar.write("[GitHub](https://github.com/AKapich)")
st.sidebar.write("[Buy Me a Coffee](https://www.buymeacoffee.com/akapich)")
