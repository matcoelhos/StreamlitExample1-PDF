import streamlit as st
import matplotlib.pyplot as plt
from io import StringIO
from interpolate import *

def read_data(data):
    vetores_dados = []
    for line in data:
        raw_data = line.split(' ')
        raw_data = [i for i in raw_data if i != '']
        # x_data.append(float(raw_data[0]))
        # y_data.append(float(raw_data[1]))
        vetores_dados.append((float(raw_data[0]),float(raw_data[1])))

    # vetores_dados.append(x_data)
    # vetores_dados.append(y_data)
    return vetores_dados

st.title('Farmacos APP')
st.subheader('Upload e visualização de PDFs')

st.write('Carregue seus dados em txt')
upload_file = st.file_uploader('Escolha seu arquivo .xy em txt')


if upload_file is not None:
    raw_data = StringIO(upload_file .getvalue().decode("utf-8"))
    data = read_data(raw_data)
    data = interpolate(data, end=50.0)
    fig = plt.figure()
    plt.plot(data[0],data[1])
    st.pyplot(fig)
