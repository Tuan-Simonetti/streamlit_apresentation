# -*- coding: utf-8 -*-
import os
from checkLibrariesInstaled.libraries_list import libraries


def execute_home_page():
    os.system("streamlit run ./streamlitPages/mainPage.py")

def libraries_instaled():
    for library in libraries:
        ### Check library
        #print(f"""\n\n\n------------------------------------------------------------------------------------------------\nVerificando se a biblioteca {library} encontra-se instalada e faz Upgrade da versao mais recente\n------------------------------------------------------------------------------------------------""")
        if library == "pip":
            os.system(f"python install --upgrade pip")
        else:
            os.system(f"pip install {library} -U")
        #print(f"""\n\n\n------------------------------------------------------------------------------------------------\nA biblioteca {library} encontra-se instalada e atualizada\n------------------------------------------------------------------------------------------------""")


    ### Show list of library instaled
    check_lib = os.system("pip list")
    #print(f"________________________________\n{check_lib}")
