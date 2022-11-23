import pickle
import pandas as pd
import streamlit as st
from random import randint

class PredictResults:
    def __init__(self):
        self.age = None
        self.sex = None
        self.air_pollution = None
        self.alcohol = None
        self.dust = None
        self.occuPational = None
        self.genetic = None
        self.dpc = None
        self.iet = None
        self.obesity = None
        self.smoking = None
        self.smoking_passive = None
        self.pain = None
        self.coughing = None
        self.fatigue = None
        self.weight = None
        self.shortness = None
        self.wheezing = None
        self.swallowing = None
        self.nails = None
        self.cold = None
        self.dry = None
        self.snoring = None
            
        self.header()
        
        self.sidebar_itemns()
        
        self.predict_result()

    def predict_result(self):
        
        df = pd.DataFrame({
            'Age':[self.age],
            'Gender':[self.sex],
            'Air Pollution':[self.air_pollution],
            'Alcohol use':[self.alcohol],
            'Dust Allergy':[self.dust],
            'OccuPational Hazards':[self.occuPational],
            'Genetic Risk':[self.genetic],
            'chronic Lung Disease':[self.dpc],
            'Balanced Diet':[self.diet],
            'Obesity':[self.obesity],
            'Smoking':[self.smoking],
            'Passive Smoker':[self.smoking_passive],
            'Chest Pain':[self.pain],
            'Coughing of Blood':[self.coughing],
            'Fatigue':[self.fatigue],
            'Weight Loss':[self.weight],
            'Shortness of Breath':[self.shortness],
            'Wheezing':[self.wheezing],
            'Swallowing Difficulty':[self.swallowing],
            'Clubbing of Finger Nails':[self.nails],
            'Frequent Cold':[self.cold],
            'Dry Cough':[self.dry],
            'Snoring':[self.snoring],
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
        
        st.sidebar.markdown('---')
        st.sidebar.write('##### Os valores padrões são definidos aleatoriamente (apenas para deixar mais dinâmico)')
        st.sidebar.write('##### Pressione R para gerar os valores novamente)')
        st.sidebar.markdown('---')
        
        self.age = st.sidebar.number_input('Idade:',
                        min_value=10, max_value=80, value=randint(10,80)
                        )

        self.sex = st.sidebar.selectbox(
            'Genêro:',
            ['Feminino', 'Masculino'],
            )
        

        self.sex = 1 if self.sex == "Masculino" else 0

        st.sidebar.write("### Selecione a resposta que mais se adequa, sendo:")
        st.sidebar.write("###### 0 - Baixo")
        st.sidebar.write("###### 5 - Moderado")
        st.sidebar.write("###### 10 - Alto")

        self.air_pollution = st.sidebar.slider('Nível de poluição do ar:',
                                min_value=0, max_value=10, step=1, value=randint(0,10)
                                )

        self.alcohol = st.sidebar.slider('Consumo de álcool:',
                            min_value=0, max_value=10, step=1, value=randint(0,10)
                            )

        self.dust = st.sidebar.slider('Alergia á poeira:',
                        min_value=0, max_value=10, step=1, value=randint(0,10)
                        )

        self.occuPational = st.sidebar.slider('Riscos ocupacionais:',
                                        min_value=0, max_value=10, step=1, value=randint(0,10)
                                        )

        self.genetic = st.sidebar.slider('Riscos geneticos:',
                                    min_value=0, max_value=10, step=1, value=randint(0,10)
                                    )

        self.dpc = st.sidebar.slider('Doença pulmonar crônica:',
                        min_value=0, max_value=10, step=1, value=randint(0,10)
                        )

        self.diet = st.sidebar.slider('Dieta balanceada:',
                        min_value=0, max_value=10, step=1, value=randint(0,10)
                        )

        self.obesity = st.sidebar.slider('Nível da obesidade:',
                            min_value=0, max_value=10, step=1, value=randint(0,10)
                            )

        self.smoking = st.sidebar.slider('Fumante ativo:',
                                min_value=0, max_value=10, step=1, value=randint(0,10)
                                )

        self.smoking_passive = st.sidebar.slider('Fumante passivo:',
                                    min_value=0, max_value=10, step=1, value=randint(0,10)
                                    )

        self.pain = st.sidebar.slider('Nível da dor no peito:',
                        min_value=0, max_value=10, step=1, value=randint(0,10)
                        )

        self.coughing  = st.sidebar.slider('Nível de tosse de sangue:',
                        min_value=0, max_value=10, step=1, value=randint(0,10)
                        )

        self.fatigue = st.sidebar.slider('Nível da fadiga:',
                        min_value=0, max_value=10, step=1, value=randint(0,10)
                        )

        self.weight  = st.sidebar.slider('Nível da perca de peso:',
                        min_value=0, max_value=10, step=1, value=randint(0,10)
                        )

        self.shortness = st.sidebar.slider('Nível da falta de ar:',
                    min_value=0, max_value=10, step=1, value=randint(0,10)
                    )

        self.wheezing = st.sidebar.slider('Nível do chiado:',
                        min_value=0, max_value=10, step=1, value=randint(0,10)
                        )

        self.swallowing  = st.sidebar.slider('Nível da dificuldade de deglutição (dificuldade para engolir):',
                            min_value=0, max_value=10, step=1, value=randint(0,10)
                            )

        self.nails = st.sidebar.slider('Nível de branqueamento das unhas:',
                        min_value=0, max_value=10, step=1, value=randint(0,10)
                        )

        self.cold = st.sidebar.slider('Nível de fruquência dos refriados:',
                        min_value=0, max_value=10, step=1, value=randint(0,10)
                        )

        self.dry = st.sidebar.slider('Nível da tosse seca:',
                        min_value=0, max_value=10, step=1, value=randint(0,10)
                        )

        self.snoring = st.sidebar.slider('Nível do ronco:',
                        min_value=0, max_value=10, step=1, value=randint(0,10)
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