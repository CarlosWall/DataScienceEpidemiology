import pandas as pd

uri = "https://raw.githubusercontent.com/CarlosWall/DataScienceSelfLerning/main/Os%20de%20Acesso%20Dificil.csv"

dados = pd.read_csv(uri)
dados.columns = ["Setor", "Janeiro", "Fevereiro", "Março", "Abril", "Maio"]
dados.Janeiro.plot(kind="bar")
