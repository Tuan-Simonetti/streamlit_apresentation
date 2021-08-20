# -*- coding: utf-8 -*-
import streamlit
from PIL import Image



if streamlit.sidebar.button("Home"):
    image = Image.open('/Users/picpay/PycharmProjects/streamlit_presentation/streamlitPages/images/home.jpg')
    streamlit.image(image, width=1550)

if streamlit.sidebar.button("Quem sou eu?"):
    image = Image.open('/Users/picpay/PycharmProjects/streamlit_presentation/streamlitPages/images/whoami.jpg')
    streamlit.image(image, width=1550)

if streamlit.sidebar.button("O que é Streamlit?"):
    streamlit.title('A maneira mais rápida de criar e compartilhar aplicativos de dados')
    streamlit.header("Streamlit transforma script de dados em aplicativos da web compartilháveis em minutos.")
    streamlit.header("Tudo em Python. Tudo de graça.")
    streamlit.header("Nenhuma experiência de front-end necessário.")

    streamlit.image("/Users/picpay/PycharmProjects/streamlit_presentation/streamlitPages/images/exemple.gif", width=1100)

if streamlit.sidebar.button("Os 3 princípios basilares"):
    # title 1
    streamlit.title("Abraçar scripts")
    streamlit.header("Construa um aplicativo em algumas linhas de código com a API simes. Em seguida, veja-o ser atualizado automaticamente à medida que salva o arquivo de origem de forma iterativa.")
    image1 = Image.open('/Users/picpay/PycharmProjects/streamlit_presentation/streamlitPages/images/exempleCode.jpg')
    streamlit.image(image1)


    # title 2
    streamlit.title("Tecer em interação")
    streamlit.header("Adicionar um widget é o mesmo que *declarar uma variável*. Não há necessidade de escrever um back-end, definir rotas, lidar com solicitações HTTP, conectar um front-end, escrever HTML, CSS, JavaScript,...")

    streamlit.title("")
    streamlit.title("")
    streamlit.title("")

    number = streamlit.slider("Escolha um número", 0, 100)
    streamlit.code("number = streamlit.slider('Pick a number', 0, 100)")

    streamlit.title("")
    streamlit.title("")
    streamlit.title("")

    file = streamlit.file_uploader("Pick a file")
    streamlit.code("file = streamlit.file_uploader('Escolha um arquivo')")

    streamlit.title("")
    streamlit.title("")
    streamlit.title("")

    color = streamlit.color_picker("Escolha uma cor")
    streamlit.code("color = streamlit.color_picker('Escolha uma cor')")

    streamlit.title("")
    streamlit.title("")
    streamlit.title("")

    pets = ["Cachorro", "Gato", "Pássaro"]
    pet = streamlit.radio("Escolha um animal de estimação", pets)
    streamlit.code("""
    pets = ["Cachorro", "Gato", "Pássaro"]
    pet = streamlit.radio("Escolha um animal de estimação", pets)""")

    streamlit.title("")
    streamlit.title("")
    streamlit.title("")

    date = streamlit.date_input("Escolha uma data")
    streamlit.code("date = streamlit.date_input('Escolha uma data')")

    streamlit.title("")
    streamlit.title("")
    streamlit.title("")

    # title 3
    streamlit.title("Implante instantaneamente")
    streamlit.header("Use o recurso de compartilhamento apenas para conidados do Stramlit para compartilhar, gerenciar e colaborar em seus aplicativos sem esforço.")
    image3 = Image.open('/Users/picpay/PycharmProjects/streamlit_presentation/streamlitPages/images/howDeploy.jpg')
    streamlit.image(image3)

    streamlit.header("Heroku Deploy")
    image4 = Image.open('/Users/picpay/PycharmProjects/streamlit_presentation/streamlitPages/images/heroku_deploy_process.png')
    streamlit.image(image4)


if streamlit.sidebar.button("Relatos de quem usa em Produção"):
    streamlit.title('Usados nos principais grupos de ciência de dados do mundo')

    streamlit.header("""*Neil Treat* -  **Google X**""")
    streamlit.text_area("", """ "Escreva código de nível de produção enquanto produz artefatos compartilháveis." """)

    streamlit.title("")
    streamlit.title("")
    streamlit.header("""*Koen Havlik* - **UBER**""")
    streamlit.text_area("", """ "O Stramlit democratiza a construção de aplicativos de dados." """)

    streamlit.title("")
    streamlit.title("")
    streamlit.header("""*Dominik Moritz* - **Vega-Lite**""")
    streamlit.text_area("", """ "É a próxima etapa nas ferramentas de ML e ciência de dados." """)

    streamlit.title("")
    streamlit.title("")
    streamlit.header("""*Danny Nguyen* - **Yelp**""")
    streamlit.text_area("", """ "Os aplicativos Streamlit são muito mais fáceis de montar e iterar." """)


if streamlit.sidebar.button("Compatível com"):
    image_bokeh = Image.open('/Users/picpay/PycharmProjects/streamlit_presentation/streamlitPages/images/bokeh.png')
    image_altair = Image.open('/Users/picpay/PycharmProjects/streamlit_presentation/streamlitPages/images/altair.png')
    image_PyTorch = Image.open('/Users/picpay/PycharmProjects/streamlit_presentation/streamlitPages/images/pytorch.png')
    image_OpenCV = Image.open('/Users/picpay/PycharmProjects/streamlit_presentation/streamlitPages/images/opencv.png')
    image_Deck = Image.open('/Users/picpay/PycharmProjects/streamlit_presentation/streamlitPages/images/deck-gl.png')
    image_Pandas = Image.open('/Users/picpay/PycharmProjects/streamlit_presentation/streamlitPages/images/pandas.png')
    image_vega_lite = Image.open('/Users/picpay/PycharmProjects/streamlit_presentation/streamlitPages/images/vega-lite.png')
    image_matplotlib = Image.open('/Users/picpay/PycharmProjects/streamlit_presentation/streamlitPages/images/matplotlib.png')
    image_numPy = Image.open('/Users/picpay/PycharmProjects/streamlit_presentation/streamlitPages/images/numpy.png')
    image_learn = Image.open('/Users/picpay/PycharmProjects/streamlit_presentation/streamlitPages/images/scikitlearn.png')
    image_tensorflow = Image.open('/Users/picpay/PycharmProjects/streamlit_presentation/streamlitPages/images/tensorflow.png')
    image_plotly = Image.open('/Users/picpay/PycharmProjects/streamlit_presentation/streamlitPages/images/keras.png')

    streamlit.image(image_altair, width=100)
    streamlit.title("")
    streamlit.image(image_PyTorch, width=100)
    streamlit.title("")
    streamlit.image(image_OpenCV, width=100)
    streamlit.title("")
    streamlit.image(image_Deck, width=100)
    streamlit.title("")
    streamlit.image(image_Pandas, width=100)
    streamlit.title("")
    streamlit.image(image_vega_lite, width=100)
    streamlit.title("")
    streamlit.image(image_matplotlib, width=100)
    streamlit.title("")
    streamlit.image(image_numPy, width=100)
    streamlit.title("")
    streamlit.image(image_learn, width=100)
    streamlit.title("")
    streamlit.image(image_tensorflow, width=100)
    streamlit.title("")
    streamlit.image(image_plotly, width=100)

if streamlit.sidebar.button("Modelos criados"):
    #Uber Graficos
    streamlit.title("**UBER Gráficos**")
    streamlit.subheader("""Página: https://share.streamlit.io/streamlit/demo-uber-nyc-pickups/""")
    streamlit.subheader("""GitHub: https://github.com/streamlit/demo-uber-nyc-pickups""")

    #twitter
    streamlit.title("**Twitter**")
    streamlit.subheader("""Página: https://twittertreasures.herokuapp.com/""")
    streamlit.subheader("""GitHub: https://github.com/VenkateshDas/TwitterTreasures""")

    #Business
    streamlit.title("**Dashboard**")
    streamlit.subheader("""Página: https://share.streamlit.io/larryprato/projectcontroldashboard/main/pc_db.py""")
    streamlit.subheader("""GitHub: https://github.com/LarryPrato/projectcontroldashboard""")

    #Control Painel

    streamlit.title("**Painel de Controle**")
    streamlit.subheader("""Página: https://share.streamlit.io/crosstabkite/worst-case-analysis/app.py""")
    streamlit.subheader("""GitHub: https://github.com/CrosstabKite/worst-case-analysis""")