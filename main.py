import pandas as pd

uri = "https://raw.githubusercontent.com/CarlosWall/DataScienceSelfLerning/main/Os%20de%20Acesso%20Dificil.csv"

osad_setor = pd.read_csv(uri)
osad_setor.columns = ["Setor", "Janeiro", "Fevereiro", "Março", "Abril", "Maio"]
osad_setor.Janeiro.plot(kind="bar")