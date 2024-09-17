import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def plot_chart(df):
    # 週ごとのデータをプロット
    sns.set_style('whitegrid')
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x='week', y='total_infected', hue='eng_pref_name', marker='o')
    
    plt.title('COVID-19 Weekly Infected Cases')
    plt.xlabel('Week')
    plt.ylabel('Total Infected')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Streamlitでの描画
    st.pyplot(plt)

import plotly.express as px
# import plotly.io as pio
# Set the renderer to browser for animations
# pio.renderers.default = "chrome"
def plot_plotly_chart(df):
    fig = px.line(df, x='week', y='total_infected', color='eng_pref_name', 
                  labels={'week': 'Week', 'total_infected': 'Total Infected', 'eng_pref_name': 'Prefecture'},
                  title='COVID-19 Weekly Infected Cases (Plotly)',
                  # animation_frame='week',
                  animation_group='eng_pref_name'
                  )
    
    fig.update_layout(xaxis_title='Week', yaxis_title='Total Infected', title='COVID-19 Weekly Infected Cases')
     # Save the animation as a gif
    # fig.write_html('animation.html')  # or write a gif or mp4
    # Display the saved HTML file in Streamlit
    # st.video('animation.html')
    st.plotly_chart(fig)
