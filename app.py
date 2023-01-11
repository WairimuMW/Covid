import streamlit as st
import pycountry
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide", initial_sidebar_state="expanded" )

covid = pd.read_csv("data/covid_cases.csv")

#Function takes in iso_alpha2 country codes and returns the iso_alpha 3 codes
def get_iso3(iso2):
    try:
        return pycountry.countries.get(alpha_2=iso2).alpha_3
    except:
        pass

covid['iso_alpha'] = covid.Country_code.apply(lambda x: get_iso3(x))
total_cases = format((covid["New_cases"].sum()), ",d")
total_deaths = format((covid["New_deaths"].sum()), ",d")

st.sidebar.markdown("# WHO COVID-19 Data")
menu = ['Cummulative Cases','New Cases','Cummulative Deaths', 'New Deaths'] # define the menu options
selection = st.sidebar.selectbox("Global Situation Maps", menu)

st.sidebar.markdown("### Confirmed Cases")
st.sidebar.markdown(total_cases)
st.sidebar.markdown("### Deaths")
st.sidebar.markdown(total_deaths)


st.header("Global Situation")
# maps
# map 1
if selection == "Cummulative Cases":
    fig= px.choropleth(covid,
               title="Cummulative Cases",
               locations="iso_alpha",
               color="Cumulative_cases", 
               hover_name="Country", # column to add to hover information
               color_continuous_scale=px.colors.sequential.Viridis,
               animation_frame="Date_reported")# animation based on the dates
    fig.update_layout(height=600) #Enlarge the figure
    st.plotly_chart(fig, use_container_width=True, theme='streamlit')
    

# map 2
if selection == "New Cases":
    fig= px.choropleth(covid,
               title="New Cases",
               locations="iso_alpha",
               color="New_cases", 
               hover_name="Country", # column to add to hover information
               color_continuous_scale=px.colors.sequential.Inferno,
               animation_frame="Date_reported")# animation based on the dates
    fig.update_layout(height=600) #Enlarge the figure
    st.plotly_chart(fig, use_container_width=True, theme='streamlit')


# map 3
if selection == "Cummulative Deaths":
    fig= px.choropleth(covid,
               title="Cummulative Deaths",
               locations="iso_alpha",
               color="Cumulative_deaths", 
               hover_name="Country", # column to add to hover information
               color_continuous_scale=px.colors.sequential.Cividis,
               animation_frame="Date_reported")# animation based on the dates
    fig.update_layout(height=600) #Enlarge the figure
    st.plotly_chart(fig, use_container_width=True, theme='streamlit')


# map 4
if selection == "New Deaths":
    fig= px.choropleth(covid,
               title="New Deaths",
               locations="iso_alpha",
               color="New_deaths", 
               hover_name="Country", # column to add to hover information
               color_continuous_scale=px.colors.sequential.Turbo,
               animation_frame="Date_reported")# animation based on the dates
    fig.update_layout(height=600) #Enlarge the figure
    st.plotly_chart(fig, use_container_width=True, theme='streamlit')

# description text
st.markdown("### _As of 3rd January 2020 to 20th December 2022, there have been {} confirmed cases of COVID-19 and {} deaths globally._".format(total_cases, total_deaths))

# graphs
# graph of cases per day
fig = px.histogram(covid, x = "Date_reported", y = "New_cases",
            hover_data = ["New_cases", "Date_reported"],
            color_discrete_sequence=['#83919c'],
            labels=dict(Date_reported="Date Reported", New_cases="Cases"),
            title = "Confirmed Cases per Day"
            )
fig.update_layout({'plot_bgcolor':'rgba(0,0,0,0)',
                 'paper_bgcolor':'rgba(0,0,0,0)',
                  'bargap':0.2})
fig.update_yaxes(showgrid=False)
st.plotly_chart(fig, use_container_width=True, theme='streamlit')

# graph of deaths per day
fig = px.histogram(covid, x = "Date_reported", y = "New_deaths",
            hover_data = ["New_deaths", "Date_reported"],
            color_discrete_sequence = ['#83919c'],
            labels=dict(Date_reported="Date Reported", New_deaths="Deaths"),
            title = "Confirmed Deaths per Day"
            )
fig.update_layout({'plot_bgcolor':'rgba(0,0,0,0)',
                 'paper_bgcolor':'rgba(0,0,0,0)',
                  'bargap':0.2})
fig.update_yaxes(showgrid=False)
st.plotly_chart(fig, use_container_width=True, theme='streamlit')


st.header("Situation by Region")
# graph of cases per region
fig = px.histogram(covid, x = "Date_reported", y = "New_cases",
            hover_data = ["New_cases", "Date_reported", "WHO_region"],
            color = 'WHO_region',
            opacity = 0.7,
            labels=dict(Date_reported="Date Reported", New_cases="Cases"),
            title = "Confirmed Cases per Region"
            )
fig.update_layout({'plot_bgcolor':'rgba(0,0,0,0)',
                 'paper_bgcolor':'rgba(0,0,0,0)',
                  'bargap':0.2})
fig.update_yaxes(showgrid=False)
st.plotly_chart(fig, use_container_width=True, theme='streamlit')

# graph of deaths per region
fig = px.histogram(covid, x = "Date_reported", y = "New_deaths",
            hover_data = ["New_deaths", "Date_reported", "WHO_region"],
            color = 'WHO_region',
            opacity = 0.7,
            labels=dict(Date_reported="Date Reported", New_deaths="Deaths"),
            title = "Confirmed Deaths per Region"
            )
fig.update_layout({'plot_bgcolor':'rgba(0,0,0,0)',
                 'paper_bgcolor':'rgba(0,0,0,0)',
                  'bargap':0.2})
fig.update_yaxes(showgrid=False)
st.plotly_chart(fig, use_container_width=True, theme='streamlit')


st.header("Cases per Individual Region")
# graphs of cases per individual region
col1, col2 = st.columns(2)

with col1:
    # Africa
    covid_afro = covid[covid['WHO_region'] == 'AFRO']
    afro_cases = format((covid_afro['New_cases'].sum()), ",d")

    fig = px.histogram(covid_afro, x = "Date_reported", y = "New_cases",
                hover_data = ["New_cases", "Date_reported"],
                color_discrete_sequence=['#05f7a3'],
                labels=dict(Date_reported="Date Reported", New_cases="Cases"),
                title = "Africa: {} confirmed cases".format(afro_cases)
                )
    fig.update_layout({'plot_bgcolor':'rgba(0,0,0,0)',
                    'paper_bgcolor':'rgba(0,0,0,0)',
                    'bargap':0.2})
    fig.update_yaxes(showgrid=False)
    st.plotly_chart(fig, use_container_width=True, theme='streamlit')

with col2:
    # Eastern Mediterranean
    covid_emro = covid[covid['WHO_region'] == 'EMRO']
    emro_cases = format((covid_emro['New_cases'].sum()), ",d")

    fig = px.histogram(covid_emro, x = "Date_reported", y = "New_cases",
                hover_data = ["New_cases", "Date_reported"],
                color_discrete_sequence=['#05c3f7'],
                labels=dict(Date_reported="Date Reported", New_cases="Cases"),
                title = "Eastern Mediterranean: {} confirmed cases".format(emro_cases)
                )
    fig.update_layout({'plot_bgcolor':'rgba(0,0,0,0)',
                    'paper_bgcolor':'rgba(0,0,0,0)',
                    'bargap':0.2})
    fig.update_yaxes(showgrid=False)
    st.plotly_chart(fig, use_container_width=True, theme='streamlit')


col3, col4 = st.columns(2)

with col3:
    # South-East Asia
    covid_searo = covid[covid['WHO_region'] == 'SEARO']
    searo_cases = format((covid_searo['New_cases'].sum()), ",d")

    fig = px.histogram(covid_searo, x = "Date_reported", y = "New_cases",
                hover_data = ["New_cases", "Date_reported"],
                color_discrete_sequence=['#4605f7'],
                labels=dict(Date_reported="Date Reported", New_cases="Cases"),
                title = "South-East Asia: {} confirmed cases".format(searo_cases)
                )
    fig.update_layout({'plot_bgcolor':'rgba(0,0,0,0)',
                    'paper_bgcolor':'rgba(0,0,0,0)',
                    'bargap':0.2})
    fig.update_yaxes(showgrid=False)
    st.plotly_chart(fig, use_container_width=True, theme='streamlit')

with col4:
    # Western Pacific
    covid_wpro = covid[covid['WHO_region'] == 'WPRO']
    wpro_cases = format((covid_wpro['New_cases'].sum()), ",d")

    fig = px.histogram(covid_wpro, x = "Date_reported", y = "New_cases",
                hover_data = ["New_cases", "Date_reported"],
                color_discrete_sequence=['#a305f7'],
                labels=dict(Date_reported="Date Reported", New_cases="Cases"),
                title = "Western Pacific: {} confirmed cases".format(wpro_cases)
                )
    fig.update_layout({'plot_bgcolor':'rgba(0,0,0,0)',
                    'paper_bgcolor':'rgba(0,0,0,0)',
                    'bargap':0.2})
    fig.update_yaxes(showgrid=False)
    st.plotly_chart(fig, use_container_width=True, theme='streamlit')


col5, col6 = st.columns(2)

with col5:
    # Americas
    covid_amro = covid[covid['WHO_region'] == 'AMRO']
    amro_cases = format((covid_amro['New_cases'].sum()), ",d")

    fig = px.histogram(covid_amro, x = "Date_reported", y = "New_cases",
                hover_data = ["New_cases", "Date_reported"],
                color_discrete_sequence=['#f7056a'],
                labels=dict(Date_reported="Date Reported", New_cases="Cases"),
                title = "Americas: {} confirmed cases".format(amro_cases)
                )
    fig.update_layout({'plot_bgcolor':'rgba(0,0,0,0)',
                    'paper_bgcolor':'rgba(0,0,0,0)',
                    'bargap':0.2})
    fig.update_yaxes(showgrid=False)
    st.plotly_chart(fig, use_container_width=True, theme='streamlit')

with col6:
    # Europe
    covid_euro = covid[covid['WHO_region'] == 'EURO']
    euro_cases = format((covid_euro['New_cases'].sum()), ",d")

    fig = px.histogram(covid_euro, x = "Date_reported", y = "New_cases",
                hover_data = ["New_cases", "Date_reported"],
                color_discrete_sequence=['#f7a705'],
                labels=dict(Date_reported="Date Reported", New_cases="Cases"),
                title = "Europe: {} confirmed cases".format(euro_cases)
                )
    fig.update_layout({'plot_bgcolor':'rgba(0,0,0,0)',
                    'paper_bgcolor':'rgba(0,0,0,0)',
                    'bargap':0.2})
    fig.update_yaxes(showgrid=False)
    st.plotly_chart(fig, use_container_width=True, theme='streamlit')




### TASKS
## 1. GENERATE THREE MORE ANIMATED GRAPHS i.e. new cases, cumulative deaths, new deaths
## 2. Give your graphs titles and if possible add explanative text after each graph
## 3. Use widgets in the sidebar to help the user choose between the four animations: e.g. select box, button, radio 
## 4. create bar graphs to show the cumulative cases per day and cumulative deaths per day 
## 5. deploy your app to streamlit cloud
## 6. submit the link to your streamlit app on dexvirtual


