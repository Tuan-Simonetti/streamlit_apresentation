import os
from checkLibrariesInstaled.libraries_list import libraries


def execute_home_page():
    os.system("streamlit run streamlitPages/mainPage.py")

def libraries_instaled():
    for library in libraries:
        ### Check library
        print(f"""\n\n\n
                        ------------------------------------------------------------------------------------------------
                        Verificando se a biblioteca {library} encontra-se instalada e faz Upgrade da versão mais recente
                        ------------------------------------------------------------------------------------------------""")
        if library == "pip":
            os.system(f"python install --upgrade pip")
        else:
            os.system(f"pip install {library} -U")
        print(f"""\n\n\n
                        ------------------------------------------------------------------------------------------------
                        A biblioteca {library} encontra-se instalada e atualizada
                        ------------------------------------------------------------------------------------------------""")


    ### Show list of library instaled
    check_lib = os.system("pip list")
    print(f"________________________________\n{check_lib}")
