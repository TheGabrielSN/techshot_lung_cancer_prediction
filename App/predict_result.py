import pickle
import pandas as pd
import streamlit as st

class PredictResults:
    def __init__(self):
        self.air_pollution = None
        self.alcohol = None
        self.genetic = None
        self.dpc = None
        self.smoking = None
        self.smoking_passive = None
            
        self.header()
        
        self.sidebar_itemns()
        
        self.predict_result()

    def predict_result(self):
        
        df = pd.DataFrame({
            'Air Pollution':[self.air_pollution],
            'Alcohol use':[self.alcohol],
            'Genetic Risk':[self.genetic],
            'chronic Lung Disease':[self.dpc],
            'Smoking':[self.smoking],
            'Passive Smoker':[self.smoking_passive]
        })

        with open(r"./models/model.pickle", "rb") as input_file:
            model = pickle.load(input_file)

        response = model.predict(df)

        if response == 0:
            st.info(f"Chances de ter cancer de pulmão: BAIXA")
        if response == 1:
            st.warning(f"Chances de ter cancer de pulmão: MÉDIA")
        if response == 2:
            st.error(f"Chances de ter cancer de pulmão: ALTA")
            
        st.markdown('---')
        
    def sidebar_itemns(self):
        st.sidebar.write("### Selecione a resposta que mais se adequa, sendo:")
        st.sidebar.write("###### 0 - Baixo")
        st.sidebar.write("###### 5 - Moderado")
        st.sidebar.write("###### 10 - Alto")

        self.air_pollution = st.sidebar.slider('Nível de poluição do ar:',
                                min_value=0, max_value=10, step=1
                                )

        self.alcohol = st.sidebar.slider('Consumo de álcool:',
                            min_value=0, max_value=10, step=1
                            )

        self.genetic = st.sidebar.slider('Riscos geneticos:',
                                    min_value=0, max_value=10
                                    )

        self.dpc = st.sidebar.slider('Doença pulmonar crônica:',
                        min_value=0, max_value=10, step=1
                        )

        self.smoking = st.sidebar.slider('Fumante ativo:',
                                min_value=0, max_value=10, step=1
                                )

        self.smoking_passive = st.sidebar.slider('Fumante passivo:',
                                    min_value=0, max_value=10, step=1
                                    )

        
    def header(self):
        
        st.header("Predição da possibilidade de cancer de pulmão")
        st.text("Analise as suas possibilidades de cancer de pulmão")
        
        col1, col2, col3 = st.columns(3)

        with col1:
            st.write(' ')
        with col2:
            st.image('https://bhtorax.com.br/wp-content/uploads/2021/01/o-que-e-o-cancer-de-pulmao-foto-4.jpg',
                 width=200)
        with col3:
            st.write(' ')
            
        st.text('\n')