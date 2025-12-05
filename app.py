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

st.set_page_config(page_title="Acceuil")

# Main Page
st.title("CV de Leo Jean UNITE")
st.header("En recherche de contrats d'alternance pour 2025-2026")


with open("CV_Leo-Jean-UNITE_FR.pdf", "rb") as f:
    cv_bytes = f.read()
st.download_button(label="Télécharger CV", data=cv_bytes, file_name="CV_Leo-Jean-UNITE_FR.pdf", mime="application/pdf", type="primary", use_container_width=None, width="content")

# Education Section
st.header("Formation Académique", divider=True)
# Education (selectbox)
education = st.selectbox(
    "Sélectionnez votre niveau d'éducation",
    ("Baccalauréat", "Licence")
)
# Option 1 (BAC)
if education == "Baccalauréat":
    st.image("https://lyceeionesco.fr/modules/kcorrect/sign_ionesco.jpg", width=250)
    st.write("""
            - Lycée : Lycée Eugène Ionesco, Issy-les-Moulineaux
            - Diplôme : Baccalauréat Technologique, Série STI2D (Sciences et Technologies de l'Industrie et du Développement Durable)
            - Année d'obtention : 2021
            - Mention : Assez Bien
            """)
# Option 2 (Licence)
elif education == "Licence":
    st.image("https://thecolonel92.github.io/img/UniversiteParis_IUTParis-RdS.png", width=500)
    st.write("""
            - Université : IUT Paris - Rives de Seine
            - Diplôme : BUT Science des Données
            - Année d'obtention : 2026 (en cours)
            """)
    university_year = st.selectbox(
        "Sélectionnez votre année universitaire actuelle",
        ("1ère année", "2ème année", "3ème année")
    )
    if university_year == "1ère année":
        st.write("""
                - Cours principaux : Programmation (Python, R), Statistiques, Mathématiques, Bases de données (SQL), Visualisation de données
                - Projets notables : Analyse de données sur des ensembles de données réels, Création de tableaux de bord interactifs
                """)
    elif university_year == "2ème année":
        st.write("""
                - Cours principaux : Apprentissage automatique
                - Projets notables : Modélisation prédictive, Analyse de sentiments, Projet de groupe sur un ensemble de données volumineux
                - Stage : Municipalité de Kalibo (OMPDC), Philippines
                        2025 - Mise à jour du Plan d'occupation des sols et à l'évaluation des risques climatiques et de catastrophes pour la municipalité de Kalibo, aux Philippines
                """)
    elif university_year == "3ème année":
        st.write("""
        - Cours principaux : Data-Mining, Dataviz Web, NoSQL
        """)

# Experience Section
st.header("Expériences Professionnelles", divider=True)
# Experience (selectbox)
experience = st.selectbox(
    "Sélectionnez votre expérience professionnelle",
    ("Stages", "Alternances")
)
# Option 1 (Stages)
if experience == "Stages":
    st.subheader("Municipalité de Kalibo (OMPDC), Philippines - 2025")
    st.image("https://upload.wikimedia.org/wikipedia/commons/5/55/KaliboAklanSeal.jpg", width=100)
    st.write("""
             Mise à jour du Plan d'occupation des sols et à l'évaluation des risques climatiques et de catastrophes pour la municipalité de Kalibo, aux Philippines
             """)
    # Documents de stage
    st.write("Documents associés au stage :")
    # Rapport de Stage
    st.link_button("Voir le rapport complet (Anglais)", "https://up75-my.sharepoint.com/:b:/g/personal/leo-jean_unite_etu_u-paris_fr/EWw6QXw0vY5KlF808Be6KOMBRD7lWUHgzS5U0vs0wNrdbw?e=eOeI2Q", icon="📄")
    # Support de présentation du stage
    st.link_button("Voir le support de présentation (Anglais)", "https://up75-my.sharepoint.com/:p:/g/personal/leo-jean_unite_etu_u-paris_fr/ETfDaCFV4WBGkGOjn9UgZQYB6aOGFBlbfLA5pOAo712bcg?e=wqC0T3", icon="📄")
# Option 2 (Alternances)
elif experience == "Alternances":
    st.subheader("En recherche de contrats d'alternance pour 2025-2026")
    st.image("https://www.wpfaster.org/wp-content/uploads/2013/06/loading-gif.gif", width=50)

# Skills Section
st.header("Compétences", divider=True)
competence = st.selectbox(
    "Sélectionnez vos compétences",
    ("Techniques", "Langues de programmation et outils")
)
# Option 1 (Techniques)
if competence == "Techniques":
    st.write("""
            - Collecte de données par Interviews, Sondages, Web Scraping
            - Analyse de données
            - Apprentissage automatique
            - Visualisation de données
            - Nettoyage et préparation des données
            - Modélisation statistique
             """)
# Option 2 (Langages de programmation et outils)
elif competence == "Langues de programmation et outils":
    st.write("""
            - Langages de programmation : Python, R, Microsoft Excel
            - Outils et technologies : Jupyter, Github, Power BI, QGIS, CSPro
            - Compétences analytiques : Analyse statistique, Visualisation de données
            """)