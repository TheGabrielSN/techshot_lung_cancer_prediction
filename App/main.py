import streamlit as st
from predict_result import *
from feature_analysis import *
from PIL import Image


class Main():
    def __init__(self):
        image = Image.open('./App/icon/1881195.png')
        st.set_page_config(
            page_title="Câncer de Pulmão",
            page_icon=image
        )
        
        self.placeholder = st.empty()
        self.fa = FeatureAnalysis()
        
        if "page" not in st.session_state:
            st.session_state.page = 0
            
        if st.session_state.page == 0:
            self.home()
            
        if st.session_state.page == 1:
            PredictResults()
            st.button("Voltar",on_click=lambda:self.set_page(0))
            
        if st.session_state.page == 2:
            self.fa.main()
        
        if st.session_state.page == 3:
            self.fa.pandas_profile()
            
        if st.session_state.page == 4:
            self.fa.evidently()
    
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

        st.markdown("""
                    <br/>
                    <br/>
                    <center>
                            <a href="https://github.com/TheGabrielSN/techshot_lung_cancer_prediction">
                                <div class="row-widget stButton" style="width: 600px;">
                                    <button kind="secondary" class="css-5uatcg edgvbvh10">
                                        <div data-testid="stMarkdownContainer" class="css-1fv8s86 e16nr0p34">
                                            <p>Github</p>
                                        </div>
                                    </button>
                                </div>
                            </a>
                    </center>
                    """,unsafe_allow_html=True)
        

            
if __name__ == '__main__':
    main = Main()