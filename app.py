import streamlit as st

from content.data_projects import data_projects
from content.optimization_projects import optimization_projects
from content.software_projects import software_projects


st.set_page_config(
    page_title="Inka Tenhunen Portfolio",
    page_icon="👩‍💻",
    layout="wide",
)

st.title("Inka Tenhunen")
st.subheader("Portfolio")
st.write(
    "Mathematics and Systems Sciences student interested in analytics, optimization, "
    "programming and technical problem-solving."
)

st.markdown("---")

st.header("About Me")
st.write(
    "I am a student at Aalto University with a background in mathematics, systems sciences, "
    "data analysis and programming. I enjoy projects where complex problems are broken down "
    "into practical and structured solutions."
)

st.markdown("---")

st.header("Projects")

tab1, tab2, tab3 = st.tabs(
    ["Data Analysis", "Optimization & Modelling", "Software Development"]
)


def show_projects(projects):
    for project in projects:
        with st.expander(project["title"]):
            st.write(project["summary"])
            st.write("**Tools:** " + ", ".join(project["tools"]))

            st.write("**Details:**")
            for item in project["details"]:
                st.write(f"- {item}")

            # Näytä kuvat jos projektissa on niitä
            if "images" in project:
                st.write("**Visuals:**")

                if len(project["images"]) == 1:
                    st.image(
                        project["images"][0]["path"],
                        caption=project["images"][0].get("caption", ""),
                        use_container_width=True
                    )
                else:
                    cols = st.columns(2)
                    for i, image in enumerate(project["images"]):
                        with cols[i % 2]:
                            st.image(
                                image["path"],
                                caption=image.get("caption", ""),
                                use_container_width=True
                            )

            # Näytä findings jos niitä on
            if "findings" in project:
                st.write("**Key Findings:**")
                for finding in project["findings"]:
                    st.write(f"- {finding}")


with tab1:
    show_projects(data_projects)

with tab2:
    show_projects(optimization_projects)

with tab3:
    show_projects(software_projects)

st.markdown("---")

st.header("Skills")
col1, col2 = st.columns(2)

with col1:
    st.write("**Programming**")
    st.write("- Python")
    st.write("- Scala")
    st.write("- R")
    st.write("- SQL")
    st.write("- Matlab")
    st.write("- Julia")

with col2:
    st.write("**Areas of Interest**")
    st.write("- Data analysis")
    st.write("- Optimization")
    st.write("- Time series analysis")
    st.write("- Technical problem-solving")
    st.write("- AI tools and automation")

st.markdown("---")

st.header("Contact")
st.write("Email: inka.e.tenhunen@gmail.com")