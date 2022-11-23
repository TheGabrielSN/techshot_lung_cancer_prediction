import streamlit as st
from predict_result import *
from feature_analysis import *

class Main():
    def __init__(self):
        self.placeholder = st.empty()
        
        if "page" not in st.session_state:
            st.session_state.page = 0
            
        if st.session_state.page == 0:
            self.home()
            
        if st.session_state.page == 1:
            PredictResults()
            st.button("Voltar",on_click=lambda:self.set_page(0))
            
        if st.session_state.page == 2:
            st.button("Voltar",on_click=lambda:self.set_page(0))
            st.write("Resultado gerado com o Pandas Profiling")
            FeatureAnalysis()
    
    def set_page(self,num):
        st.session_state.page=num
        
    def home(self):
        
        col1, col3, col5 = st.columns(3)

        with col1:
            st.text("Realizar a predição\nda possibilidade\nde cancer")
            st.button("Predição",on_click=lambda:self.set_page(1))
        
        with col3:
            st.header("O que você deseja fazer?")
            
        with col5:
            st.text("Realizar a analise das\nfeatures utilizadas\nno modelo")
            st.button("Features",on_click=lambda:self.set_page(2))


            
if __name__ == '__main__':
    main = Main()