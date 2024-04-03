# @Email:  contact@pythonandvba.com
# @Website:  https://pythonandvba.com
# @YouTube:  https://youtube.com/c/CodingIsFun
# @Project:  Sales Dashboard w/ Streamlit



import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit

import webbrowser




# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="IRN-NORMAL", page_icon=":bar_chart:", layout="wide")

st.title("Indicador de Rendimiento Neto (IRN) de las Siefores")
st.subheader("")
st.subheader("")

#df = pd.read_csv('Glosario.csv', )
#st.dataframe(df)




# ---- READ EXCEL ----
@st.cache_data
def get_data_from_excel():
    df = pd.read_excel(
        io="base-datos.xlsx",
        engine="openpyxl",
        sheet_name="database",
        skiprows=3,
        usecols="B:H",
        nrows=3800,
    )
    # Add 'hour' column to dataframe
    ###df["hour"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.hour
    return df

df = get_data_from_excel()

# ---- SIDEBAR ----
st.sidebar.header("Por favor seleccione un filtro:")

#afore = st.sidebar.multiselect(
#    "Seleccione una afore:",
#    options=df["AFORE"].unique(),
#    default=df["AFORE"].unique()
#)

siefore = st.sidebar.multiselect(
    "Seleccione una siefore:",
    options=df["SIEFORE"].unique(),
    default=df["SIEFORE"].unique(),
)


fecha = st.sidebar.multiselect(
    "Seleccione una fecha:",
    options=df["FECHA"].unique(),
    default=df["FECHA"].unique(),
)


df_selection = df.query(
    "SIEFORE == @siefore & FECHA ==@fecha"
)

# Check if the dataframe is empty:
if df_selection.empty:
    st.warning("¡No hay datos disponibles según la configuración de filtro actual!")
    st.stop() # This will halt the app from further execution.

# ---- MAINPAGE ----

st.subheader("")
st.subheader("")

st.title(":bar_chart: IRN-NORMAL")
st.markdown("##")

# TOP KPI's
t1 = str(df_selection["AFORE"])
t2 = str(df_selection["SIEFORE"])
t3 = str(df_selection["FECHA"])
t4 = round((df_selection["IRN"].sum()),3)
t5 = int(df_selection["RANKING"].sum())



#average_rating = round(df_selection["Rating"].mean(), 1)
#star_rating = ":star:" * int(round(average_rating, 0))
#average_sale_by_transaction = round(df_selection["Total"].mean(), 2)

#left_column, middle_column, right_column = st.columns(3)
#with left_column:
#    st.subheader("AFORE:")
#    st.subheader(f"{t1:}")
#with middle_column:
#    st.subheader("SIEFORE:")
#    st.subheader(f"{t2:}")
#with right_column:
#    st.subheader("FECHA:")
#    st.subheader(f"{t3:}")  
    

    

#with left_column:
#    st.subheader("")
#    st.subheader("")
#    st.subheader("IRN:")
#    st.subheader(f"{t4:,}")
#with middle_column:
#    st.subheader("")
#    st.subheader("")
#    st.subheader("RANKING:")
#    st.subheader(f"{t5:,}")
#with right_column:
#    st.subheader("")
#    st.subheader("")
#    st.subheader("POCUPADA_Hombre:")
#    st.subheader(f"{t9:,}")    
#    st.subheader("")
#    st.subheader("")
#    st.subheader("POCUPADA_Hombre:")
#    st.subheader(f"{t9:,}")    

st.markdown("""---""")

#HASTA AQUI FUNCIONA
###############################################################################################


#GRÁFICAS 1 Y 2



#f1 = df_selection.groupby(by=["SIEFORE"])[["FECHA"]].sum().sort_values(by="FECHA")
#fig1 = px.bar(
#    f1,
#    x="FECHA",
#    y=f1.index,
#    orientation="h",
#    title="<b>IRN y SIEFORE</b>",
#    color_discrete_sequence=["#621132"] * len(f1),
#    template="plotly_white",
#)
#fig1.update_layout(
#    plot_bgcolor="rgba(0,0,0,0)",
#    xaxis=(dict(showgrid=False))
#)


#f2 = df_selection.groupby(by=["SIEFORE"])[["IRN"]].sum().sort_values(by="IRN")
#fig2 = px.bar(
#    f2,
#    x="IRN",
#    y=f2.index,
#    orientation="h",
#    title="<b>IRN y SIEFORE</b>",
#    color_discrete_sequence=["#621132"] * len(f2),
#    template="plotly_white",
#)
#fig2.update_layout(
#    plot_bgcolor="rgba(0,0,0,0)",
#    xaxis=(dict(showgrid=False))
#)


#AQUI TERMINA LAS PRIMERAS 2 GRÁFICAS Y FUNCIONA
############################################################################################
st.subheader("")
st.subheader("")
st.subheader("")
st.subheader("")
############################################################################################
#GRÁFICAS 3 Y 4

#f3 = df_selection.groupby(by=["SIEFORE"])[["RANKING"]].sum().sort_values(by="RANKING")
#fig3 = px.bar(
#    f3,
#    x="RANKING",
#    y=f3.index,
#    orientation="h",
#    title="<b>RANKING y SIEFORE</b>",
#    color_discrete_sequence=["#621132"] * len(f3),
#    template="plotly_white",
#)
#fig3.update_layout(
#    plot_bgcolor="rgba(0,0,0,0)",
#    xaxis=(dict(showgrid=False))
#)



#left_column, right_column = st.columns(2)
#left_column.plotly_chart(fig2, use_container_width=True)
#right_column.plotly_chart(fig3, use_container_width=True)
############################################################################################

############################################################################################
#GRÁFICAS 5 Y 6





f3 = df_selection.groupby(by=["AFORE"])[["IRN"]].sum().sort_values(by="IRN")
fig3 = px.bar(
    f3,
    x="IRN",
    y=f3.index,
    orientation="h",
    title="<b>AFORE e IRN </b>",
    color_discrete_sequence=["#621132"] * len(f3),
    template="plotly_white",
)
fig3.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


#AQUI TERMINA LAS PRIMERAS 2 GRÁFICAS Y FUNCIONA
############################################################################################
st.subheader("")
st.subheader("")
st.subheader("")
st.subheader("")
############################################################################################
#GRÁFICAS 3 Y 4

f4 = df_selection.groupby(by=["AFORE"])[["RANKING"]].sum().sort_values(by="RANKING")
fig4 = px.bar(
    f4,
    x="RANKING",
    y=f4.index,
    orientation="h",
    title="<b>AFORE y RANKING</b>",
    color_discrete_sequence=["#621132"] * len(f4),
    template="plotly_white",
)
fig4.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)



left_column, right_column = st.columns(2)
left_column.plotly_chart(fig3, use_container_width=True)
right_column.plotly_chart(fig4, use_container_width=True)







############################################################################################

#st.link_button("Aguascalientes-mapa", "https://2z6f2lrzc5fegrmyunpt2q.on.drv.tw/html/Aguascalientes-CAP.html")


# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

