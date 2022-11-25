import streamlit as st
from streamlit import components
from streamlit_pandas_profiling import st_profile_report

class FeatureAnalysis:           
    def set_page(self,num):
        st.session_state.page=num
        
    def sidebar(self):
        st.sidebar.button("Voltar",on_click=lambda:self.set_page(0), key=5)
        st.sidebar.button("Análise Geral",on_click=lambda:self.set_page(3), key=3)
        st.sidebar.button("Data Drift",on_click=lambda:self.set_page(4), key=4)
    
    def pandas_profile(self):
        self.sidebar()
        
        st.header("Análise Geral e Correlação com Pandas Profile")
        
        with open(r"./results_analysis_features/profile.html", 'r', encoding='utf-8') as HtmlFile:
            source_code = HtmlFile.read()
        
        components.v1.html(source_code, height=5000, width=800, scrolling=True)


    def evidently(self):
        self.sidebar()
        
        st.header("Data Drift com Evidently")

        with open(r"./results_analysis_features/dashboard.html", 'r', encoding='utf-8') as HtmlFile:
            source_code = HtmlFile.read()


        components.v1.html(source_code, height=5000, width=800, scrolling=True)
        
    def main(self):
        self.sidebar()
        
        st.header("Análise das Features do Dataset")
        st.text("Análise geral e correlação com pandas profile")
        st.text("Data drift com Evidently")
        st.write('')
        st.write("*O carregamento dos dados pode demorar um pouco*")
        