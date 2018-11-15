import csv

#colunas
# ID #internal kickstarter id - int
# name #name of project - A project is a finite work with a clear goal that you’d like to bring to life. Think albums, books, or films.
# category #category
# main_category #category of campaign
# currency #currency used to support
# deadline #deadline for crowdfunding
# goal #fundraising goal - The funding goal is the amount of money that a creator needs to complete their project. - int
# launched #date launched
# pledged #amount pledged by "crowd" - int
# backers #number of backers
# country #country pledged from
# usd_pledged amount of money pledged - int
# state #Current condition the project is in

#colunas do fragmento de dados baseado nos dados de 2016
# ID ,name ,category ,main_category ,currency ,deadline ,goal ,launched ,pledged ,state ,backers ,country ,usd_pledged

def exibir_fragmento_dados():
    arquivo = open('dados.csv')
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)

def carregar_dados_2018():
    X = [] # array de features
    Y = [] # array de label

    arquivo = open('ks-projects-201801.csv')
    leitor = csv.reader(arquivo)

    #pula a linha de cabecalho
    next(leitor)

    #popula os arrays de features e label
    for ID, name, category, main_category, currency, deadline, goal, launched, pledged, state, backers, country, usd_pledged, usd_pledged_real, usd_goal_real in leitor:
        X.append([ID, name, category, main_category, currency, deadline, goal, launched, pledged, backers, country, usd_pledged, usd_pledged_real, usd_goal_real])
        Y.append(state)

    return X, Y

#exemplo: X, Y = carregar_dados_2018()
