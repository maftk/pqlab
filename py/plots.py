import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def plot_chart(df,interval):
    if interval == 'Daily':
        x = 'reporting_date'
        y = 'infected'

    elif interval == 'Weekly':
        x = 'week'
        y = 'total_infected'
    # 週ごとのデータをプロット
    sns.set_style('whitegrid')
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x=x, y=y, hue='eng_pref_name', marker='o')
    
    plt.title(f'COVID-19 {interval} Infected Cases')
    plt.xlabel(x)
    plt.ylabel(y)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Streamlitでの描画
    st.pyplot(plt)

import plotly.express as px
# import plotly.io as pio
# Set the renderer to browser for animations
# pio.renderers.default = "chrome"
def plot_plotly_chart(df,interval):
    if interval == 'Daily':
        x = 'reporting_date'
        y = 'infected'

    elif interval == 'Weekly':
        x = 'week'
        y = 'total_infected'
    fig = px.line(df, x=x, y=y, color='eng_pref_name', 
                  labels={x:x,y:y, 'eng_pref_name': 'Prefecture'},
                  title=f'COVID-19 {interval} Infected Cases (Plotly)',
                  # animation_frame='week',
                  animation_group='eng_pref_name'
                  )
    
    fig.update_layout(xaxis_title=x, yaxis_title=y, title=f'COVID-19 {interval} Infected Cases')
     # Save the animation as a gif
    # fig.write_html('animation.html')  # or write a gif or mp4
    # Display the saved HTML file in Streamlit
    # st.video('animation.html')
    st.plotly_chart(fig)
