import streamlit as st
import matplotlib.pyplot as plt
from io import StringIO
from interpolate import *

def read_data(data):
    vetores_dados = []
    for line in data:
        raw_data = line.split(' ')
        raw_data = [i for i in raw_data if i != '']
        vetores_dados.append((float(raw_data[0]),float(raw_data[1])))
    return vetores_dados

st.title('AmorphizApp')
st.subheader('Pair Distribution Function Upload, Visualization and Insights')

st.write('Upload you .XY PDF file. Exclude the headers. The data must follow the displayed example:')
st.write('\"0.0 0.0')
st.write('0.001 0.01') 
st.write('0.003 0.02') 
st.write('...\"')
upload_file = st.file_uploader('Upload your file below')


if upload_file is not None:
    raw_data = StringIO(upload_file .getvalue().decode("utf-8"))
    data = read_data(raw_data)
    data = interpolate(data, end=50.0)
    fig = plt.figure()
    plt.plot(data[0],data[1])
    plt.title('PDF plot (0-50 Å)')
    plt.ylabel('G(r)')
    plt.xlabel('r [Å]')
    st.pyplot(fig)
