import streamlit as st

def intro():
    st.write("# Welcome to FastLane Forecast! 👋")
    st.sidebar.success("Select a field above.")

    st.markdown(
        """
        Are you a Formula 1 enthusiast who's passionate about predicting race outcomes and tracking your favorite drivers' progress? Look no further! Our website offers a cutting-edge solution that brings together the excitement of Formula 1 racing and the power of data visualization.

        **👈 Select from the dropdown on the left to view predictions or visualization!**

        ### Interested in diving deeper?

        ###### Explore the [FastLane Forecast](https://github.com/shashwatbangar/FastLaneForecast) repository to delve into the source code.
        - Complete source code.
        - Data model design
        - Architecture design
        
        ###### Tech stack used in this project:
        - Hadoop Distributed File System
        - Apache Spark
        - Tableau
        - Machine learning
        
    """
    )
        
################################################################################################################

def prediction():
    import predictor
    
    def predict_driver_position(driver, constructor, grid_position, circuit):
        # Return the predicted result
        prediction = predictor.pred(driver, constructor, grid_position, circuit)
        return prediction
    
    st.title("FastLane Forecast")
    # ... (other code)

    driver = st.selectbox("Driver", [
        "Alexander Albon", "Antonio Giovinazzi", "Carlos Sainz", "Charles Leclerc", "Daniel Ricciardo",
        "Daniil Kvyat", "Esteban Ocon", "George Russell", "Kevin Magnussen", "Kimi Räikkönen", "Lance Stroll",
        "Lando Norris", "Lewis Hamilton", "Max Verstappen", "Nicholas Latifi", "Pierre Gasly", "Romain Grosjean",
        "Sebastian Vettel", "Sergio Pérez", "Valtteri Bottas"
    ])
    
    constructor = st.selectbox("Constructor", [
        "Alfa Romeo", "AlphaTauri", "Ferrari", "Haas F1 Team", "McLaren",
        "Mercedes", "Racing Point", "Red Bull", "Renault", "Williams"
    ])

    
    grid_position = st.selectbox("Grid Position", [
        "Pole", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "P9", "P10", "P11", "P12", "P13", "P14", "P15", "P16", "P17", "P18", "P19", "P20"
    ])
    
    circuit = st.selectbox("Circuit", [
        "Albert Park Grand Prix Circuit", "Autodromo Nazionale di Monza", "Autódromo Hermanos Rodríguez",
        "Autódromo José Carlos Pace", "Bahrain International Circuit", "Baku City Circuit",
        "Buddh International Circui", "Circuit Gilles Villeneuve", "Circuit Paul Ricard",
        "Circuit de Barcelona-Catalunya", "Circuit de Monaco", "Circuit de Spa-Francorchamps",
        "Circuit of the Americas", "Hockenheimring", "Hungaroring", "Istanbul Park", "Korean International Circuit",
        "Marina Bay Street Circuit", "Nürburgring", "Red Bull Ring", "Sepang International Circuit",
        "Shanghai International Circuit", "Silverstone Circuit", "Suzuka Circuit",
        "Valencia Street Circuit", "Yas Marina Circuit"
    ])
    
    result=""
    if st.button("Predict"):
        result = predict_driver_position(driver, constructor, grid_position, circuit)
    st.success('Most probable outcome:  {}'.format(result))
    
###############################################################################################################################

def visualization():
    import streamlit as st
    
    st.title("Tableau Visualization")
    
    st.markdown(
        """
        ### Dashboard 1
        """
    )

    tableau_embed_url = """
    <div class='tableauPlaceholder' id='viz1693170179836' style='position: relative'>
        <noscript><a href='#'>
            <img alt='Final Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;to&#47;topvspointdashboard&#47;FinalDashboard1&#47;1_rss.png' style='border: none' />
            </a>
        </noscript>
        <object class='tableauViz'  style='display:none;'>
            <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
            <param name='embed_code_version' value='3' /> 
            <param name='site_root' value='' />
            <param name='name' value='topvspointdashboard&#47;FinalDashboard1' />
            <param name='tabs' value='no' />
            <param name='toolbar' value='yes' />
            <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;to&#47;topvspointdashboard&#47;FinalDashboard1&#47;1.png' /> 
            <param name='animate_transition' value='yes' />
            <param name='display_static_image' value='yes' />
            <param name='display_spinner' value='yes' />
            <param name='display_overlay' value='yes' />
            <param name='display_count' value='yes' />
            <param name='language' value='en-US' />
            <param name='filter' value='publish=yes' />
        </object>
    </div>                
    <script type='text/javascript'>                    
        var divElement = document.getElementById('viz1693170179836');                    
        var vizElement = divElement.getElementsByTagName('object')[0];                    
        if ( divElement.offsetWidth > 800 ) { 
            vizElement.style.width='100%';
            vizElement.style.height=(divElement.offsetWidth*0.75)+'px';
        } else if ( divElement.offsetWidth > 500 ) { 
            vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} 
        else { 
            vizElement.style.width='100%';vizElement.style.height='1327px';
        }                     
        var scriptElement = document.createElement('script');                    
        scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    
        vizElement.parentNode.insertBefore(scriptElement, vizElement);                
    </script>
    """
    st.components.v1.html(tableau_embed_url, width=1203, height=800)
    
    st.markdown(
        """
        ### Dashboard 2
        """
    )

    tableau_embed_url = "<div class='tableauPlaceholder' id='viz1693182223572' style='position: relative'><noscript><a href='#'><img alt='Circuit&#39;s Dashboard ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;to&#47;topvspointdashboard&#47;FinalDashBoard2&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='topvspointdashboard&#47;FinalDashBoard2' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;to&#47;topvspointdashboard&#47;FinalDashBoard2&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1693182223572');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='977px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"
    st.components.v1.html(tableau_embed_url, width=1203, height=800)
    
################################################ App starts here ################################################

page_names_to_funcs = {
    "Home": intro,
    "Driver's position prediction": prediction,
    "Tableau Visualization": visualization,
}

demo_name = st.sidebar.selectbox("Choose an option", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()

# Footer
footer_style = """
<style>
    footer {
        visibility: visible;
    }
    
    footer:before {
        content:'Copyright © 2023 FastLaneForecast. All rights reserved.';
        display: block;
        position: relative;
        text-align: center;
    }
    position: fixed;
    bottom: 0;
</style>
"""
st.markdown(footer_style, unsafe_allow_html=True)