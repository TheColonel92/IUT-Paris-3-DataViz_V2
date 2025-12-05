#pip install streamlit
#python -m streamlit run cv.py
#CTRL+C END
import streamlit as st

# Sidebar
st.logo("https://avatars.githubusercontent.com/u/174519077?v=4", size="Large", link="https://thecolonel92.github.io/")
st.sidebar.title("CV de Leo Jean UNITE")
st.sidebar.header("Contact", divider=True)
st.sidebar.write("""
                 - Email: leounite5@gmail.com
                 - Location : Île-de-France, France
                 """)
st.sidebar.header("Réseaux", divider=True)
st.sidebar.write("""
                 - LinkedIn: https://www.linkedin.com/in/lj-unite/
                 - GitHub: https://github.com/TheColonel92
                 """)
st.sidebar.header("Langues", divider=True)
st.sidebar.write("""
                 - Français : Langue maternelle
                 - Tagalog : Langue maternelle
                 - Anglais : Courant
                 """)
st.sidebar.header("Atouts", divider=True)
st.sidebar.write("""
                 - Compétences en communication et travail d'équipe
                 - Adaptabilité et apprentissage continu
                 - Sens de l'organisation et gestion du temps
                 """)


# Main Page
st.set_page_config(page_title="Cas Pratique - RATP")
# Case Section (RATP)
st.header("Cas Pratique - RATP", divider=True)
## Titre Partie 1
st.subheader("1 - Dashboard d'analyse des données sur le transport")
### Selectionner le contenu Partie 1
part1 = st.selectbox(
    "Sélectionnez le contenu à afficher",
    (
        "Objectif de l'exercice",
        "Données",
        "Consigne",
        "Cadre de l'exercice",
        "Instructions et exigences techniques",
        "Outils de visualisation recommandés",
        "Résultats attendus"
        )
)
#### Option 1 (🎯 Objectif de l’exercice)
if part1 == "Objectif de l'exercice":
    st.write("""
        **🎯 Objectif de lexercice**
        Dans cet exercice, vous allez concevoir une application Streamlit permettant de visualiser et danalyser la régularité / ponctualité du métro parisien (RATP) à partir de données ouvertes.
        
        objectif est de :
            - Charger des données issues de lopen data RATP (ou tout autre source de données sur les transports en France)
            - Les préparer correctement (qualité, formats, granularité)
            - Construire un dashboard clair et lisible (graphique + filtres)
            - Soigner le design de la dataviz (choix des couleurs, légendes, titres)
            - Écrire un code Python simple, structuré et maintenable

        """)

#### Option 2 (📁 Données)
elif part1 == "Données":
    st.write("""
        **📁 Données**
        Vous utiliserez les données disponibles sur l’Open Data RATP :
            - Portail Open Data RATP :
            https://data.ratp.fr/explore/
            - Page d’accès aux données temps réel / voyageurs (API, datasets) :
            https://data.ratp.fr/pages/temps-reel/
            - Plateforme Régionale d'Information pour la Mobilité (PRIM):
            https://prim.iledefrance-mobilites.fr/fr/catalogue-data
        """)

#### Option 3 (Consigne)
elif part1 == "Consigne":
    st.write("""
        **📝 Consigne**
        Le choix de données proposé n'est pas obligatoire. Vous êtes entièrement libres de sélectionner les données de transport qui vous intéressent : métro RATP, trafic IDFM, bus/tram, ou tout autre opérateur disponible en open data. Vous pouvez télécharger un fichier CSV ou utiliser une API si vous êtes à l’aise.
        """)

#### Option 4 (🧩 Cadre de l’exercice)
elif part1 == "Cadre de l'exercice":
    st.write("""
        **🧩 Cadre de lexercice**
        Vous travaillez dans le contexte d’un POC (Proof of Concept) pour une équipe Data & Digital qui souhaite :
            - Suivre la régularité du métro dans le temps
            - Visualiser les lignes les plus perturbées ou les plus régulières
            - Identifier les plages horaires problématiques (heures de pointe, soirées, week-ends, etc.)

        Votre dashboard Streamlit doit permettre à un utilisateur non technique de :
            - Filtrer les données (par ligne, par période, par jour/heure)
            - Comprendre rapidement l’état de la régularité
            - Explorer quelques visualisations interactives (courbes, barres, heatmaps, etc.)
        """)


#### Option 5 (🛠️ Instructions et exigences techniques)
elif part1 == "Instructions et exigences techniques":
    ##### Selecteur Instructions et exigences techniques
    instructions = st.selectbox(
        "Sélectionnez les instructions et exigences techniques",
        (
            "1. Préparation des données (obligatoire)",
            "2. Application Streamlit",
            "3. Qualité du code Python",
            "4. Choix des couleurs et lisibilité",
        )
    )
    ##### Option 1 (1. Préparation des données (obligatoire))
    if instructions == "1. Préparation des données (obligatoire)":
        st.write("""
            **1. Préparation des données (obligatoire)**
                - Vérifiez les types de colonnes (dates, nombres, catégories).
                - Gérez les valeurs manquantes (suppression ou imputation simple).
                - Renommez les colonnes pour plus de clarté si nécessaire (ex : `date`, `ligne`, `taux_reg`).
                - Créez éventuellement des variables dérivées :
                    - Année, mois, jour à partir d’une colonne de date.
                    - Catégories (heures de pointe vs heures creuses, etc. si pertinent).
            """)

    ##### Option 2 (2. Application Streamlit)
    elif instructions == "2. Application Streamlit":
        st.write("""
            **2. Application Streamlit**
            Créer un fichier Python (par exemple `app.py`) contenant une application Streamlit minimaliste mais propre :
                - Titre et sous-titre de l’application (`st.title`, `st.subheader`).
                - Chargement des données (via `pandas`).
                - Widgets d’interaction :*
                    - `st.selectbox` pour choisir une ligne.
                    - `st.slider` ou `st.date_input` pour filtrer la période.
                - Affichage de plusieurs visualisations :
                    - Graphique d’évolution temporelle.
                    - Graphique comparatif entre lignes.
                - Affichage de tableaux résumés (ex : `st.dataframe`).
            """)

#### Option 6 (Outils de visualisation recommandés)
elif part1 == "Outils de visualisation recommandés":
    st.write("""
        **📊 Outils de visualisation recommandés**
        Vous pouvez utiliser les bibliothèques Python suivantes pour créer vos visualisations dans Streamlit :
            - Matplotlib
            - Seaborn
            - Plotly
            - Altair
        """)
    
#### Option 7 (Résultats attendus)
elif part1 == "Résultats attendus":
    st.write("""
        **🏆 Résultats attendus**
        À la fin de cet exercice, vous devez fournir :
            1. Un fichier Streamlit fonctionnel (`app.py`) qui :
                - se lance avec `streamlit run app.py`,
                - charge les données,
                - propose au moins 2 visualisations principales et 1 tableau de données filtrées.
            2. Des visualisations :
                - lisibles,
                - cohérentes,
                - interprétables sans explication orale supplémentaire.
            3. Un court texte (dans l’app ou dans un fichier séparé `README.md`) résumant :
                - votre choix de visualisations,
                - les principaux enseignements des données.
        """)
##### Selecteur Visualisations attendues
    import streamlit as st
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns

    # Configuration de la page
    st.set_page_config(page_title="Analyse du trafic RATP", layout="wide")

    # Titre principal
    st.title("📊 Visualisation du trafic annuel par station")

    # Importation des données
    data = pd.read_csv("trafic-annuel-entrant-par-station-du-reseau-ferre.csv", sep=";")
    data['Trafic'] = pd.to_numeric(data['Trafic'], errors='coerce')

    # Création des onglets
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Distribution du trafic",
        "Top 15 stations",
        "Tableau résumé",
        "Filtre interactif",
        "Visualisation avancée"
    ])

    # ---------------- TAB 1 ----------------
    with tab1:
        st.subheader("1. Distribution du trafic annuel")
        try:
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.hist(data['Trafic'], bins=30, color='skyblue', edgecolor='black')
            ax.set_title('Distribution du trafic annuel entrant par station')
            ax.set_xlabel('Trafic annuel entrant')
            ax.set_ylabel('Nombre de stations')
            st.pyplot(fig)

            st.markdown("""
            **Interprétation :**
            La majorité des stations ont un trafic inférieur à quelques millions, tandis que certaines concentrent une grande partie du trafic.
            Cela indique des hubs stratégiques dans le réseau.
            """)
        except Exception as e:
            st.error(f"Erreur : {e}")

    # ---------------- TAB 2 ----------------
    with tab2:
        st.subheader("2. TOP 15 des stations les plus fréquentées")
        try:
            top15 = data.nlargest(15, 'Trafic')
            fig2, ax2 = plt.subplots(figsize=(12, 8))
            sns.barplot(x='Trafic', y='Station', data=top15, ax=ax2)
            ax2.set_title('Top 15 des stations les plus fréquentées')
            ax2.set_xlabel('Trafic annuel entrant')
            ax2.set_ylabel('Station')
            st.pyplot(fig2)

            st.markdown("""
            **Interprétation :**
            Les stations en tête sont des hubs majeurs (ex. Châtelet, Gare du Nord).
            Elles concentrent une grande partie du trafic, ce qui peut influencer les décisions d’aménagement.
            """)
        except Exception as e:
            st.error(f"Erreur : {e}")

    # ---------------- TAB 3 ----------------
    with tab3:
        st.subheader("3. Tableau résumé des données")
        st.write("Visualisez les données brutes.")
        try:
            st.dataframe(data)
            st.download_button("📥 Télécharger les données", data.to_csv(index=False), "donnees_trafic.csv")
        except Exception as e:
            st.error(f"Erreur : {e}")

    # ---------------- TAB 4 ----------------
    with tab4:
        st.subheader("4. Filtre interactif par réseau et station")
        try:
            reseaux = data['Réseau'].dropna().unique().tolist()
            selected_reseau = st.selectbox("Sélectionnez un réseau", ['Tous'] + reseaux, key="select_reseau_tab4")

            filtered_data = data if selected_reseau == 'Tous' else data[data['Réseau'] == selected_reseau]

            stations = filtered_data['Station'].dropna().unique().tolist()
            selected_station = st.selectbox("Sélectionnez une station", ['Toutes'] + stations, key="select_station_tab4")

            if selected_station != 'Toutes':
                filtered_data = filtered_data[filtered_data['Station'] == selected_station]

            st.dataframe(filtered_data)
            st.download_button("📥 Télécharger les données filtrées", filtered_data.to_csv(index=False), "donnees_filtrees.csv", key="download_tab4")

            st.markdown("""
            **Interprétation :**
            Ce filtre permet d’analyser le trafic par ligne ou par station spécifique.
            Utile pour des études ciblées.
            """)
        except Exception as e:
            st.error(f"Erreur : {e}")

    # ---------------- TAB 5 ----------------
    with tab5:
        st.subheader("5. Visualisation avancée")
        try:
            choix_visu = st.radio("Type de visualisation :", ["Tableau", "Graphique"], key="radio_visu_tab5")

            reseaux = data['Réseau'].dropna().unique().tolist()
            selected_reseau = st.selectbox("Sélectionnez un réseau", ['Tous'] + reseaux, key="select_reseau_tab5")

            filtered_data = data if selected_reseau == 'Tous' else data[data['Réseau'] == selected_reseau]

            stations = filtered_data['Station'].dropna().unique().tolist()
            selected_station = st.selectbox("Sélectionnez une station", ['Toutes'] + stations, key="select_station_tab5")

            if selected_station != 'Toutes':
                filtered_data = filtered_data[filtered_data['Station'] == selected_station]

            min_trafic = st.slider("Filtrer par trafic minimum :", 0, int(filtered_data['Trafic'].max()), 0, key="slider_trafic_tab5")
            filtered_data = filtered_data[filtered_data['Trafic'] >= min_trafic]

            if choix_visu == "Tableau":
                st.dataframe(filtered_data)
                st.download_button("📥 Télécharger les données filtrées", filtered_data.to_csv(index=False), "donnees_filtrees.csv", key="download_tab5")
            else:
                type_graph = st.selectbox("Type de graphique :", ["Barplot", "Histogramme", "Boxplot", "Scatterplot"], key="select_graph_tab5")
                top_n = st.slider("Nombre de stations à afficher :", 5, 30, 10, key="slider_topn_tab5")

                top_filtered = filtered_data.nlargest(top_n, 'Trafic')

                fig, ax = plt.subplots(figsize=(10, 6))

                if type_graph == "Barplot":
                    sns.barplot(x='Trafic', y='Station', data=top_filtered, ax=ax)
                    ax.set_title(f"Top {top_n} stations")
                    st.markdown("**Interprétation :** Les stations en haut du classement concentrent le trafic.")
                elif type_graph == "Histogramme":
                    ax.hist(filtered_data['Trafic'], bins=30, color='skyblue', edgecolor='black')
                    ax.set_title("Distribution du trafic")
                    st.markdown("**Interprétation :** La distribution montre la concentration du trafic.")
                elif type_graph == "Boxplot":
                    sns.boxplot(x=filtered_data['Trafic'], ax=ax)
                    ax.set_title("Dispersion du trafic")
                    st.markdown("**Interprétation :** Une grande dispersion indique des écarts importants entre stations.")
                elif type_graph == "Scatterplot":
                    sns.scatterplot(x='Trafic', y='Station', data=top_filtered, hue='Réseau', ax=ax)
                    ax.set_title("Trafic vs Station")
                    st.markdown("**Interprétation :** Les points éloignés sont des stations avec un trafic atypique.")

                st.pyplot(fig)

        except Exception as e:
            st.error(f"Erreur : {e}")