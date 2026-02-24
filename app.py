import streamlit as st
import matplotlib.pyplot as plt
from io import StringIO
from interpolate import *
import tensorflow as tf
import numpy as np

dnn_model = tf.keras.models.load_model('drug_dnn_model.h5')

def read_data(data):
    vetores_dados = []
    for line in data:
        raw_data = line.split(' ')
        raw_data = [i for i in raw_data if i != '']
        vetores_dados.append((float(raw_data[0]),float(raw_data[1])))
    return vetores_dados

st.image('logo.png')

st.title('AmorphizApp')
st.subheader('Pair Distribution Function Upload, Visualization and Insights')

st.markdown('#### Upload')
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

st.markdown('#### AI Insights')

if upload_file is not None:
    # st.write(data)
    x = np.reshape(data[1], (1,len(data[1])))
    P = dnn_model(x)
    fig2 = plt.figure()
    arr = P.numpy()[0]*100
    st.write(arr)
    plt.bar(['Flubendazole','Verapamil','None'], arr)
    st.pyplot(fig2)

# st.write('TBD')

st.markdown('#### Please cite us:')
st.code('''@article{coelhosilva2024,
  title={Towards a Machine-Learning-Based Application for Amorphous Drug Recognition},
  volume={22}, 
  url={https://latamt.ieeer9.org/index.php/transactions/article/view/8988},
  abstractNote={The amorphous drug structure represents an important feature to be reached in the pharmaceutical field due to its possibility of increasing drug solubility, considering that at least 40% of commercially available   crystalline drugs are poorly soluble in water. However, it is known that the amorphous local structure can vary depending on the amorphization technique used. Therefore, recognizing such variations related to a specific amorphization technique through the pair distribution function (PDF) method, for example, is an important tool for drug characterization concerns. This work presents a method to classify amorphous drugs according to their amorphization techniques and related to the local structure variations using machine learning. We used experimental PDF patterns obtained from low-energy X-rays scattering data to extract information and expanded the data through the Monte Carlo method to create a synthetic dataset. Then, we proposed the evaluation of such a technique using a Deep Neural Network. Based on the results obtained, it is suggested that the proposed technique is suitable for the amorphization technique and local structure recognition task.},
  number={9},
  journal={IEEE Latin America Transactions},
  author={Coelho Silva, Mateus and Castro e Silva, Alcides and T. D. Orlando, Marcos and D. N. Bezzon, Vinicius},
  year={2024},
  month={Aug.},
  pages={755–760}
}
''',language="latex")
