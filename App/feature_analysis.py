import streamlit as st
import streamlit.components.v1 as components
import os

class FeatureAnalysis:
    def __init__(self):
        ##os.system("start \"\" ./pandas_profiling_report/profile.html")
        st.write(f'''
                 <a target="_blank" href="{os.path.abspath(os.getcwd())}\\pandas_profiling_report\\profile.html">
                    <button class="css-5uatcg edgvbvh10" kind="secondary">
                        <div data-testid="stMarkdownContainer" class="css-1fv8s86 e16nr0p34">
                            <p> Features </p>
                        </div>
                    </button>
                 </a>
                 ''', unsafe_allow_html=True)