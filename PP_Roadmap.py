# =========================================================
# PRODUCT PROPS ROADMAPPER
# =========================================================
#
# An interactive product roadmap visualization tool built
# with Streamlit, Pandas, and Plotly.
#
# =========================================================
# HOW TO RUN THIS APP
# =========================================================
#
# FIRST-TIME SETUP
#
# You will need:
#   • Python 3
#   • Streamlit
#   • Pandas
#   • Plotly
#   • OpenPyXL
#
# ---------------------------------------------------------
# 1. INSTALL PYTHON
# ---------------------------------------------------------
#
# Download and install Python from:
#
# https://www.python.org/downloads/
#
# After installation, open Terminal (Mac) or
# Command Prompt / PowerShell (Windows).
#
# Verify that Python is installed:
#
# Mac:
#     python3 --version
#
# Windows:
#     python --version
#
# You should see a Python version number.
#
#
# ---------------------------------------------------------
# 2. INSTALL THE REQUIRED PYTHON PACKAGES
# ---------------------------------------------------------
#
# Mac:
#
#     python3 -m pip install streamlit pandas plotly openpyxl
#
# Windows:
#
#     python -m pip install streamlit pandas plotly openpyxl
#
# These packages provide:
#
#   Streamlit  → the web application interface
#   Pandas     → spreadsheet and data processing
#   Plotly     → interactive roadmap charts
#   OpenPyXL   → Excel (.xlsx) file support
#
#
# ---------------------------------------------------------
# 3. DOWNLOAD THE PROJECT
# ---------------------------------------------------------
#
# Download or clone the Product Props Roadmapper project
# and save the entire project folder somewhere on your
# computer.
#
# The folder should contain this Python file:
#
#     PP_Roadmap.py
#
#
# ---------------------------------------------------------
# 4. OPEN TERMINAL / COMMAND PROMPT
# ---------------------------------------------------------
#
# Navigate to the folder containing PP_Roadmap.py.
#
# Mac:
#
#     cd
#
# Then drag the project folder from Finder into the
# Terminal window and press Enter.
#
# Windows:
#
#     cd "C:\path\to\your\Roadmap"
#
# You can verify that you are in the correct folder by
# listing the files:
#
# Mac:
#
#     ls
#
# Windows:
#
#     dir
#
# You should see:
#
#     PP_Roadmap.py
#
#
# ---------------------------------------------------------
# 5. RUN THE APP
# ---------------------------------------------------------
#
# Mac:
#
#     python3 -m streamlit run PP_Roadmap.py
#
# Windows:
#
#     python -m streamlit run PP_Roadmap.py
#
# Streamlit should automatically open the Roadmapper
# in your web browser.
#
#
# ---------------------------------------------------------
# 6. USE THE APP
# ---------------------------------------------------------
#
# Upload a roadmap CSV or XLSX file using the file uploader
# in the sidebar.
#
# The Roadmapper will then generate an interactive roadmap
# that can be filtered, grouped, and exported.
#
#
# ---------------------------------------------------------
# 7. STOP THE APP
# ---------------------------------------------------------
#
# To stop the Streamlit application:
#
#     Control + C
#
# in the Terminal / Command Prompt window.
#
#
# ---------------------------------------------------------
# RUNNING THE APP AGAIN LATER
# ---------------------------------------------------------
#
# You only need to install Python and the required packages
# once.
#
# The next time you want to use the Roadmapper:
#
# 1. Open Terminal / Command Prompt.
# 2. Navigate to the project folder.
# 3. Run:
#
# Mac:
#     python3 -m streamlit run PP_Roadmap.py
#
# Windows:
#     python -m streamlit run PP_Roadmap.py
#
#
# =========================================================
# OPTIONAL: USING requirements.txt
# =========================================================
#
# If this project includes a requirements.txt file, you can
# install all dependencies at once instead:
#
# Mac:
#     python3 -m pip install -r requirements.txt
#
# Windows:
#     python -m pip install -r requirements.txt
#
# =========================================================


import streamlit as st
import pandas as pd
import plotly.express as px
import textwrap
import math


# =========================================================
# CONFIGURATION & BRANDING
# =========================================================

st.set_page_config(
    page_title="Product Props Roadmapper",
    layout="wide",
    page_icon="🗼"
)


# =========================================================
# PRODUCT PROPS COLOR PALETTE
# =========================================================

Product_Props__BLUE = "#1F6073"
Product_Props__YELLOW = "#E0B04B"
Product_Props__DARK_BLUE = "#123B4A"
Product_Props__TEAL = "#477F8C"

Product_Props__PURPLE = "#C7837D"
Product_Props__GREEN = "#4F6F4A"
Product_Props__ORANGE = "#C8782C"

Product_Props__DARK_GRAY = "#633F32"
Product_Props__BRIGHT_BLUE = "#79A9A5"

Product_Props__ACC_RED = "#B85F45"
Product_Props__LIGHT_RED = "#DDA6A0"
Product_Props__ACC_GREEN = "#244A3A"
Product_Props__LIGHT_GRAY = "#F3E8D3"

Product_Props__MED_BLUE = "#B5CFCA"
Product_Props__BTN_HOVER = "#123B4A"
Product_Props__BTN_ACTIVE = "#244A3A"

Product_Props__MENU_BLUE = "#2F7FA3"
Product_Props__TITLE_BLUE = "#4FA3D1"


# =========================================================
# CHART PALETTE
# =========================================================

Product_Props__CHART_COLORS = [
    Product_Props__BLUE,
    Product_Props__TEAL,
    Product_Props__PURPLE,
    Product_Props__DARK_BLUE,
    Product_Props__GREEN,
    Product_Props__ORANGE,
    Product_Props__BRIGHT_BLUE,
    Product_Props__DARK_GRAY
]


# =========================================================
# PERCENTAGE / GRADIENT SCALE
# =========================================================

Product_Props__PCT_SCALE = [
    Product_Props__MED_BLUE,
    Product_Props__BRIGHT_BLUE,
    Product_Props__BLUE,
    Product_Props__BTN_HOVER,
    Product_Props__BTN_ACTIVE
]


# =========================================================
# PRODUCT PROPS CSS
# =========================================================

css_style = f"""
<style>

@import url('https://fonts.googleapis.com/css2?family=Lato:wght@400;700&display=swap');

html, body, [class*='css'], .stMarkdown, .stRadio,
.stSelectbox, .stMultiSelect {{
    font-family: 'Lato', sans-serif !important;
}}


/* --- Product Props Header --- */

.product-props-header {{
    background-color: white;
    padding: 1rem 2rem;
    border-bottom: 3px solid {Product_Props__YELLOW};
    border-top: 5px solid {Product_Props__DARK_BLUE};
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}}

.logo-container {{
    display: flex;
    align-items: center;
    font-size: 2.2rem;
    font-weight: 700;
    letter-spacing: -1px;
    color: {Product_Props__DARK_BLUE};
}}

.pipe {{
    font-size: 2.5rem;
    color: {Product_Props__MED_BLUE};
    margin: 0 15px;
    font-weight: 300;
}}

.product-model {{
    color: {Product_Props__DARK_GRAY};
    font-weight: 700;
    text-transform: uppercase;
    font-size: 1.4rem;
    letter-spacing: 1px;
}}

.roadmap-title {{
    font-weight: 700;
    font-size: 32px;
    color: {Product_Props__TITLE_BLUE};
    text-align: center;
    margin-top: 5px;
    margin-bottom: 0px;
}}


/* --- Roadmap Notes --- */

.roadmap-notes {{
    background-color: {Product_Props__LIGHT_GRAY};
    border-left: 5px solid {Product_Props__YELLOW};
    padding: 20px;
    border-radius: 5px;
    height: 100%;
}}

.roadmap-notes h4 {{
    color: {Product_Props__DARK_BLUE};
    margin-top: 0;
    font-weight: 700;
    margin-bottom: 15px;
}}

.note-group-title {{
    font-weight: 700;
    color: {Product_Props__MENU_BLUE};
    margin-top: 10px;
    margin-bottom: 5px;
    font-size: 1.1em;
}}


/* --- Data Health --- */

.health-check {{
    background-color: {Product_Props__LIGHT_RED};
    border-left: 5px solid {Product_Props__ACC_RED};
    padding: 20px;
    border-radius: 5px;
    height: 100%;
}}

.health-check h4 {{
    color: {Product_Props__ACC_RED};
    margin-top: 0;
    font-weight: 700;
    margin-bottom: 15px;
}}


/* --- General text --- */

ul {{
    margin-bottom: 10px;
    color: {Product_Props__DARK_GRAY};
}}


/* --- Streamlit multiselect tags --- */

span[data-baseweb='tag'] {{
    background-color: {Product_Props__BLUE} !important;
}}

span[data-baseweb='tag'] span {{
    color: white !important;
}}


/* =========================================================
   SIDEBAR / MENU LABELS
   ========================================================= */

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] h4,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] .stMarkdown p {{
    color: {Product_Props__MENU_BLUE} !important;
}}

section[data-testid="stSidebar"] div[data-testid="stWidgetLabel"] p,
section[data-testid="stSidebar"] div[data-testid="stWidgetLabel"] label,
section[data-testid="stSidebar"] div[data-testid="stMarkdownContainer"] p {{
    color: {Product_Props__MENU_BLUE} !important;
}}


/* =========================================================
   MAIN CONTROL LABELS
   ========================================================= */

div[data-testid="stWidgetLabel"] p,
div[data-testid="stWidgetLabel"] label {{
    color: {Product_Props__MENU_BLUE} !important;
}}

</style>
"""

st.markdown(
    css_style,
    unsafe_allow_html=True
)


# =========================================================
# HEADER PLACEHOLDER
# =========================================================

header_placeholder = st.empty()


# =========================================================
# DISPLAY MAPPING
# =========================================================

LABEL_MAP = {
    "Lane": "Strategy",
    "Legend": "Ultimate Objective",
    "Container": "Product Objective",
    "Business Unit": "Business Unit",
    "Product": "Product",
    "Target Release": "Target Release",
    "Percent Complete": "Completion %",
    "Title": "Project Name",
}


def format_labels(option):
    return LABEL_MAP.get(option, option)


def format_list_grammatically(items):

    if not items:
        return ""

    if len(items) == 1:
        return items[0]

    return ", ".join(items[:-1]) + " & " + items[-1]


# =========================================================
# SIDEBAR — CONTROLS, FILTERS & FILE UPLOAD
# =========================================================

with st.sidebar:

    st.header("Controls")

    uploaded_file = st.file_uploader(
        "Upload Roadmap (CSV/XLSX)",
        type=["csv", "xlsx"]
    )

    st.divider()

    st.subheader("Getting Started")

    st.caption(
        "New to the Roadmapper? Download the data template "
        "to see the expected structure and example values."
    )

    template_data = pd.DataFrame([
        {
            "Type": "Project",
            "Title": "Example Project",
            "Product": "Example Product",
            "Lane": "Example Strategy",
            "Legend": "Example Ultimate Objective",
            "Container": "Example Product Objective",
            "Business Unit": "Example Business Unit",
            "Target Release": "Release 1",
            "Start Date": "2026-07-01",
            "End Date": "2026-09-30",
            "When": "Now",
            "Percent Complete": 25,
            "Tags": "Example Tag",
            "Roadmap Note": ""
        },
        {
            "Type": "Project",
            "Title": "Another Example Project",
            "Product": "Example Product",
            "Lane": "Example Strategy",
            "Legend": "Example Ultimate Objective",
            "Container": "Example Product Objective",
            "Business Unit": "Example Business Unit",
            "Target Release": "Release 1",
            "Start Date": "",
            "End Date": "",
            "When": "Next",
            "Percent Complete": 0,
            "Tags": "Example Tag",
            "Roadmap Note": ""
        },
        {
            "Type": "Current Cycle Start",
            "Title": "",
            "Product": "",
            "Lane": "",
            "Legend": "",
            "Container": "",
            "Business Unit": "",
            "Target Release": "",
            "Start Date": "2026-07-01",
            "End Date": "",
            "When": "",
            "Percent Complete": "",
            "Tags": "",
            "Roadmap Note": ""
        },
        {
            "Type": "Update Date",
            "Title": "",
            "Product": "",
            "Lane": "",
            "Legend": "",
            "Container": "",
            "Business Unit": "",
            "Target Release": "",
            "Start Date": "2026-08-01",
            "End Date": "",
            "When": "",
            "Percent Complete": "",
            "Tags": "",
            "Roadmap Note": ""
        },
        {
            "Type": "Roadmap Note",
            "Title": "Example roadmap note",
            "Product": "Example Product",
            "Lane": "",
            "Legend": "",
            "Container": "",
            "Business Unit": "",
            "Target Release": "",
            "Start Date": "",
            "End Date": "",
            "When": "",
            "Percent Complete": "",
            "Tags": "",
            "Roadmap Note": ""
        }
    ])

    template_csv = template_data.to_csv(
        index=False
    )

    st.download_button(
        label="Download Roadmap Template",
        data=template_csv,
        file_name="Product_Props_Roadmap_Template.csv",
        mime="text/csv",
        use_container_width=True
    )


# =========================================================
# MAIN APP LOGIC
# =========================================================

if uploaded_file is not None:

    # =====================================================
    # LOAD FILE
    # =====================================================

    if uploaded_file.name.lower().endswith(".csv"):

        try:

            df_raw = pd.read_csv(
                uploaded_file,
                encoding="utf-8-sig"
            )

        except UnicodeDecodeError:

            uploaded_file.seek(0)

            df_raw = pd.read_csv(
                uploaded_file,
                encoding="cp1252"
            )

    else:

        df_raw = pd.read_excel(
            uploaded_file
        )


    df_raw.columns = (
        df_raw.columns
        .astype(str)
        .str.strip()
    )


    # =====================================================
    # REQUIRED COLUMNS
    # =====================================================

    required_columns = [
        "Title",
        "Start Date",
        "End Date"
    ]

    missing_columns = [
        col
        for col in required_columns
        if col not in df_raw.columns
    ]

    if missing_columns:

        st.error(
            "The uploaded roadmap is missing required "
            "column(s): "
            + ", ".join(missing_columns)
        )

        st.stop()


    # =====================================================
    # TYPE CLEANUP
    # =====================================================

    if "Type" not in df_raw.columns:

        df_raw["Type"] = "Project"


    df_raw["Type_Clean"] = (
        df_raw["Type"]
        .fillna("Project")
        .astype(str)
        .str.strip()
        .str.lower()
    )


    # =====================================================
    # SEPARATE ENTITIES
    # =====================================================

    df_releases = df_raw[
        df_raw["Type_Clean"] == "release"
    ].copy()

    df_updates = df_raw[
        df_raw["Type_Clean"] == "update date"
    ].copy()

    df_notes = df_raw[
        df_raw["Type_Clean"] == "roadmap note"
    ].copy()

    df_cycle = df_raw[
        df_raw["Type_Clean"] == "current cycle start"
    ].copy()

    df = df_raw[
        df_raw["Type_Clean"] == "project"
    ].copy()


    # =====================================================
    # EXTRACT METADATA
    # =====================================================

    updated_date_str = ""

    if not df_updates.empty:

        dates = pd.to_datetime(
            df_updates["Start Date"],
            errors="coerce"
        )

        if not dates.isna().all():

            updated_date_str = dates.max().strftime(
                "%B %Y"
            )


    if (
        not updated_date_str
        and "Updated" in df_raw.columns
    ):

        dates = pd.to_datetime(
            df_raw["Updated"],
            errors="coerce"
        )

        if not dates.isna().all():

            updated_date_str = dates.max().strftime(
                "%B %Y"
            )


    # =====================================================
    # ROADMAP NOTES
    # =====================================================

    notes_list = []


    if not df_notes.empty:

        for _, row in df_notes.iterrows():

            note_text = row.get(
                "Title",
                ""
            )

            if (
                pd.isna(note_text)
                or str(note_text).strip() == ""
            ):

                note_text = row.get(
                    "Roadmap Note",
                    ""
                )


            if (
                pd.notna(note_text)
                and str(note_text).strip()
            ):

                prod = row.get(
                    "Product",
                    "General"
                )

                if (
                    pd.isna(prod)
                    or str(prod).strip() == ""
                ):

                    prod = "General"


                notes_list.append({
                    "Product": prod,
                    "Note": str(note_text)
                })


    if "Roadmap Note" in df.columns:

        for _, row in df.dropna(
            subset=["Roadmap Note"]
        ).iterrows():

            note_text = row["Roadmap Note"]

            if (
                pd.notna(note_text)
                and str(note_text).strip()
            ):

                prod = row.get(
                    "Product",
                    "General"
                )

                if (
                    pd.isna(prod)
                    or str(prod).strip() == ""
                ):

                    prod = "General"


                notes_list.append({
                    "Product": prod,
                    "Note": str(note_text)
                })


    notes_df = pd.DataFrame(
        notes_list
    )


    # =====================================================
    # CURRENT CYCLE & HORIZON MAPPING
    # =====================================================

    cycle_start_dt = (
        pd.Timestamp.today()
        .to_period("Q")
        .start_time
    )


    if not df_cycle.empty:

        c_dates = pd.to_datetime(
            df_cycle["Start Date"],
            errors="coerce"
        )

        if not c_dates.isna().all():

            cycle_start_dt = c_dates.max()


    now_start = cycle_start_dt

    now_end = (
        now_start
        + pd.DateOffset(months=3)
        - pd.Timedelta(days=1)
    )

    next_start = (
        now_start
        + pd.DateOffset(months=3)
    )

    next_end = (
        next_start
        + pd.DateOffset(months=3)
        - pd.Timedelta(days=1)
    )

    later_start = (
        next_start
        + pd.DateOffset(months=3)
    )

    later_end = (
        later_start
        + pd.DateOffset(months=3)
        - pd.Timedelta(days=1)
    )


    # =====================================================
    # DEFAULT / CLEAN OPTIONAL FIELDS
    # =====================================================

    if "Legend" not in df.columns:

        df["Legend"] = "No Ultimate Objective"

    else:

        df["Legend"] = (
            df["Legend"]
            .fillna("No Ultimate Objective")
            .astype(str)
            .str.strip()
        )


    if "Lane" not in df.columns:

        df["Lane"] = "No Strategy"

    else:

        df["Lane"] = (
            df["Lane"]
            .fillna("No Strategy")
            .astype(str)
            .str.strip()
        )


    if "Container" not in df.columns:

        df["Container"] = "Independent"

    else:

        df["Container"] = (
            df["Container"]
            .fillna("Independent")
            .astype(str)
            .str.strip()
        )


    if "Tags" not in df.columns:

        df["Tags"] = "None"

    else:

        df["Tags"] = (
            df["Tags"]
            .fillna("None")
            .astype(str)
        )


    if "Percent Complete" not in df.columns:

        df["Percent Complete"] = 0


    df["Percent Complete"] = pd.to_numeric(
        df["Percent Complete"],
        errors="coerce"
    ).fillna(0)


    if "Product" not in df.columns:

        df["Product"] = "General"

    else:

        df["Product"] = (
            df["Product"]
            .fillna("General")
            .astype(str)
            .str.strip()
        )


    if "Business Unit" not in df.columns:

        df["Business Unit"] = "No Business Unit"

    else:

        df["Business Unit"] = (
            df["Business Unit"]
            .fillna("No Business Unit")
            .astype(str)
            .str.strip()
        )


    if "Target Release" not in df.columns:

        df["Target Release"] = "Unassigned"

    else:

        df["Target Release"] = (
            df["Target Release"]
            .fillna("Unassigned")
            .astype(str)
            .str.strip()
        )


    # =====================================================
    # WHEN → START / END DATE
    # =====================================================

    if "When" in df.columns:

        df["When_Clean"] = (
            df["When"]
            .fillna("")
            .astype(str)
            .str.strip()
            .str.title()
        )

        start_map = {
            "Now": now_start,
            "Next": next_start,
            "Later": later_start
        }

        end_map = {
            "Now": now_end,
            "Next": next_end,
            "Later": later_end
        }

        df["Start Date"] = (
            df["Start Date"]
            .replace("", pd.NA)
            .fillna(
                df["When_Clean"].map(start_map)
            )
        )

        df["End Date"] = (
            df["End Date"]
            .replace("", pd.NA)
            .fillna(
                df["When_Clean"].map(end_map)
            )
        )


    # =====================================================
    # CLEAN PROJECT DATA
    # =====================================================

    df["Start Date"] = pd.to_datetime(
        df["Start Date"],
        errors="coerce"
    )

    df["End Date"] = pd.to_datetime(
        df["End Date"],
        errors="coerce"
    )


    # =====================================================
    # DATA HEALTH
    # =====================================================

    bad_data_df = df[
        df["Start Date"].isna()
        | df["End Date"].isna()
        | df["Title"].isna()
    ].copy()


    df = df.dropna(
        subset=[
            "Start Date",
            "End Date",
            "Title"
        ]
    ).copy()


    df["Title"] = (
        df["Title"]
        .astype(str)
        .str.strip()
    )


    df = df[
        df["Title"] != ""
    ].copy()


    if df.empty:

        st.warning(
            "No valid project records were found in "
            "the uploaded roadmap."
        )

        st.stop()


    df["Duration_Days"] = (
        df["End Date"]
        - df["Start Date"]
    ).dt.days


    # =====================================================
    # FILTERS & TIME HORIZON
    # =====================================================

    with st.sidebar:

        st.divider()

        presentation_mode = st.toggle(
            "Presentation Mode (PPT Export)",
            value=False
        )


        st.subheader(
            "Time Horizon"
        )


        time_view = st.radio(
            "View:",
            [
                "Full Timeline",
                "Next 6 Months"
            ],
            index=0,
            horizontal=True,
            label_visibility="collapsed"
        )


        show_horizon_labels = st.checkbox(
            "Horizon Labels (Now/Next/Later)",
            value=True
        )


        show_releases = False


        if not df_releases.empty:

            show_releases = st.checkbox(
                "Show Release Milestones",
                value=False
            )


        st.divider()

        st.subheader(
            "Filters"
        )


        all_prods = set(
            df["Product"].unique()
        )


        if not notes_df.empty:

            all_prods.update(
                notes_df["Product"].unique()
            )


        all_prods = sorted(
            list(all_prods)
        )


        selected_products = st.multiselect(
            "Product",
            all_prods,
            default=all_prods
        )


        business_unit_options = sorted(
            df["Business Unit"].unique()
        )


        selected_business_units = st.multiselect(
            "Business Unit",
            business_unit_options,
            default=business_unit_options
        )


        objective_options = sorted(
            df["Legend"].unique()
        )


        selected_objectives = st.multiselect(
            "Ultimate Objective",
            objective_options,
            default=objective_options
        )


        all_releases = set(
            df["Target Release"].unique()
        )


        if not df_releases.empty:

            all_releases.update(
                df_releases[
                    "Title"
                ].dropna().unique()
            )


        all_releases = sorted(
            list(all_releases)
        )


        selected_releases = st.multiselect(
            "Target Release",
            all_releases,
            default=all_releases
        )


        df = df[
            df["Product"].isin(
                selected_products
            )
            & df["Business Unit"].isin(
                selected_business_units
            )
            & df["Legend"].isin(
                selected_objectives
            )
            & df["Target Release"].isin(
                selected_releases
            )
        ].copy()


    # =====================================================
    # CHART SETTINGS — 3-LEVEL GROUPING
    # =====================================================

    col1, col2, col3, col4 = st.columns(4)


    group_options = [
        "Lane",
        "Legend",
        "Container",
        "Business Unit",
        "Product",
        "Target Release"
    ]


    with col1:

        default_ix_1 = group_options.index(
            "Business Unit"
        )


        group_by_1 = st.selectbox(
            "Primary Grouping:",
            group_options,
            index=default_ix_1,
            format_func=format_labels
        )


    with col2:

        group_options_2 = (
            ["None"]
            + [
                g
                for g in group_options
                if g != group_by_1
            ]
        )


        default_ix_2 = (
            group_options_2.index("Lane")
            if "Lane" in group_options_2
            else 0
        )


        group_by_2 = st.selectbox(
            "Secondary Grouping (Optional):",
            group_options_2,
            index=default_ix_2,
            format_func=lambda x:
                "None"
                if x == "None"
                else format_labels(x)
        )


    with col3:

        group_options_3 = (
            ["None"]
            + [
                g
                for g in group_options
                if g not in (
                    group_by_1,
                    group_by_2
                )
            ]
        )


        default_ix_3 = (
            group_options_3.index("Container")
            if "Container" in group_options_3
            else 0
        )


        group_by_3 = st.selectbox(
            "Tertiary Grouping (Optional):",
            group_options_3,
            index=default_ix_3,
            format_func=lambda x:
                "None"
                if x == "None"
                else format_labels(x)
        )


    with col4:

        color_options = [
            "Legend",
            "Lane",
            "Product",
            "Business Unit",
            "Percent Complete",
            "Target Release"
        ]


        default_ix_color = color_options.index(
            "Legend"
        )


        color_by = st.selectbox(
            "Color Bars By:",
            color_options,
            index=default_ix_color,
            format_func=format_labels
        )


    # =====================================================
    # VIEWPORT CLIPPING
    # =====================================================

    if time_view == "Next 6 Months":

        view_start_dt = cycle_start_dt

        view_end_dt = (
            cycle_start_dt
            + pd.DateOffset(months=6)
        )

    else:

        if not df.empty:

            view_start_dt = min(
                df["Start Date"]
                .min()
                .to_period("Q")
                .start_time,
                cycle_start_dt
            )

            view_end_dt = (
                df["End Date"].max()
                + pd.Timedelta(days=15)
            )

        else:

            view_start_dt = cycle_start_dt

            view_end_dt = (
                cycle_start_dt
                + pd.DateOffset(months=6)
            )


    df["Plot_Start"] = df[
        "Start Date"
    ].clip(
        lower=view_start_dt
    )


    df["Plot_End"] = df[
        "End Date"
    ].clip(
        upper=view_end_dt
    )


    df = df[
        df["Plot_End"]
        > df["Plot_Start"]
    ].copy()


    if df.empty:

        st.warning(
            "No projects match the selected filters "
            "or time horizon."
        )

        st.stop()


    # =====================================================
    # APPLY MULTI-LEVEL GROUPING & SORTING
    # =====================================================

    def sort_flag(value):

        value = str(value)

        return (
            1
            if (
                value.startswith("No ")
                or value == "Unassigned"
                or value == "Independent"
            )
            else 0
        )


    df["Sort_1"] = df[
        group_by_1
    ].apply(sort_flag)


    # =====================================================
    # THREE LEVELS OF GROUPING
    # =====================================================

    if (
        group_by_2 != "None"
        and group_by_3 != "None"
    ):

        df["Combined_Group"] = (
            df[group_by_1].astype(str)
            + " | "
            + df[group_by_2].astype(str)
            + " | "
            + df[group_by_3].astype(str)
        )


        active_group_col = (
            "Combined_Group"
        )


        df["Sort_2"] = df[
            group_by_2
        ].apply(sort_flag)


        df["Sort_3"] = df[
            group_by_3
        ].apply(sort_flag)


        df = df.sort_values(
            by=[
                "Sort_1",
                group_by_1,
                "Sort_2",
                group_by_2,
                "Sort_3",
                group_by_3,
                "Start Date"
            ]
        )


    # =====================================================
    # TWO LEVELS OF GROUPING
    # =====================================================

    elif group_by_2 != "None":

        df["Combined_Group"] = (
            df[group_by_1].astype(str)
            + " | "
            + df[group_by_2].astype(str)
        )


        active_group_col = (
            "Combined_Group"
        )


        df["Sort_2"] = df[
            group_by_2
        ].apply(sort_flag)


        df = df.sort_values(
            by=[
                "Sort_1",
                group_by_1,
                "Sort_2",
                group_by_2,
                "Start Date"
            ]
        )


    # =====================================================
    # ONE LEVEL OF GROUPING
    # =====================================================

    else:

        active_group_col = group_by_1


        df = df.sort_values(
            by=[
                "Sort_1",
                group_by_1,
                "Start Date"
            ]
        )


    # =====================================================
    # VIEWPORT-AWARE TRUNCATION ENGINE
    # =====================================================

    total_view_days = max(
        (
            view_end_dt
            - view_start_dt
        ).days,
        1
    )


    CHARS_ACROSS_SCREEN = 175


    def smart_truncate(row):

        title = str(
            row["Title"]
        )


        visible_days = (
            row["Plot_End"]
            - row["Plot_Start"]
        ).days


        pct_of_screen = (
            visible_days
            / total_view_days
        )


        allowed_width = int(
            CHARS_ACROSS_SCREEN
            * pct_of_screen
        )


        if allowed_width < 15:

            return textwrap.shorten(
                title,
                width=15,
                placeholder="..."
            )


        line_width = min(
            max(
                allowed_width,
                15
            ),
            65
        )


        lines = textwrap.wrap(
            title,
            width=line_width,
            break_long_words=False
        )


        if len(lines) > 3:

            return (
                "<br>".join(
                    lines[:3]
                )
                + "..."
            )


        return "<br>".join(
            lines
        )


    df["Display Title"] = df.apply(
        smart_truncate,
        axis=1
    )


    df["Start_Str"] = df[
        "Start Date"
    ].dt.strftime(
        "%b %d, %Y"
    )


    df["End_Str"] = df[
        "End Date"
    ].dt.strftime(
        "%b %d, %Y"
    )


    # =====================================================
    # SPLIT Y-AXIS LABEL FORMATTING
    # =====================================================

    def format_y_label(row):

        val1 = str(
            row[group_by_1]
        )


        if (
            group_by_2 != "None"
            and group_by_3 != "None"
        ):

            val2 = str(
                row[group_by_2]
            )


            val3 = str(
                row[group_by_3]
            )


            l1 = textwrap.wrap(
                f"{val1} | {val2}",
                width=40,
                break_long_words=False
            )


            l1_str = (
                "<br>".join(
                    l1[:2]
                )
                + (
                    "..."
                    if len(l1) > 2
                    else ""
                )
            )


            l2 = textwrap.wrap(
                val3,
                width=40,
                break_long_words=False
            )


            l2_str = (
                "<br>".join(
                    l2[:2]
                )
                + (
                    "..."
                    if len(l2) > 2
                    else ""
                )
            )


            return (
                f"{l1_str}<br>{l2_str}"
            )


        elif group_by_2 != "None":

            val2 = str(
                row[group_by_2]
            )


            lines = textwrap.wrap(
                f"{val1} | {val2}",
                width=45,
                break_long_words=False
            )


            return (
                "<br>".join(
                    lines[:3]
                )
                + (
                    "..."
                    if len(lines) > 3
                    else ""
                )
            )


        else:

            lines = textwrap.wrap(
                val1,
                width=45,
                break_long_words=False
            )


            return (
                "<br>".join(
                    lines[:3]
                )
                + (
                    "..."
                    if len(lines) > 3
                    else ""
                )
            )


    df["Wrapped_Label"] = df.apply(
        format_y_label,
        axis=1
    )


    # =====================================================
    # SMART PACKING
    # =====================================================

    df["SubLane"] = 0


    for name, group in df.groupby(
        active_group_col,
        sort=False
    ):

        tracks = []


        for index, row in group.iterrows():

            assigned = False

            start = row["Plot_Start"]
            end = row["Plot_End"]


            for i, track_end in enumerate(
                tracks
            ):

                if start >= track_end:

                    df.at[
                        index,
                        "SubLane"
                    ] = i


                    tracks[i] = end

                    assigned = True

                    break


            if not assigned:

                df.at[
                    index,
                    "SubLane"
                ] = len(tracks)


                tracks.append(
                    end
                )


    df["Y_Axis_Key"] = (
        df["Wrapped_Label"]
        + ":::"
        + df["SubLane"].astype(str)
    )


    unique_y_keys = pd.unique(
        df["Y_Axis_Key"]
    )


    y_tick_vals = []
    y_tick_text = []


    for key in unique_y_keys:

        label, sublane = key.split(
            ":::"
        )


        y_tick_vals.append(
            key
        )


        y_tick_text.append(
            f"<b>{label}</b>"
            if sublane == "0"
            else ""
        )


    # =====================================================
    # PAGINATION FOR PRESENTATION MODE
    # =====================================================

    current_page = 1
    total_pages = 1


    if presentation_mode:

        with st.sidebar:

            st.divider()

            st.subheader(
                "Slide Slicer"
            )


            rows_per_page = st.number_input(
                "Rows per Slide "
                "(Adjust if chart is too tall)",
                min_value=3,
                max_value=50,
                value=10
            )


            total_pages = max(
                1,
                math.ceil(
                    len(unique_y_keys)
                    / rows_per_page
                )
            )


            if total_pages > 1:

                st.markdown(
                    "**Drag slider to change pages:**"
                )


                current_page = st.slider(
                    "Select Page",
                    min_value=1,
                    max_value=total_pages,
                    value=1,
                    label_visibility="collapsed"
                )


            start_idx = (
                current_page - 1
            ) * rows_per_page


            end_idx = (
                start_idx
                + rows_per_page
            )


            sliced_keys = unique_y_keys[
                start_idx:end_idx
            ]


            y_tick_vals = [
                k
                for k in y_tick_vals
                if k in sliced_keys
            ]


            original_tick_text = y_tick_text


            y_tick_text = [
                t
                for k, t in zip(
                    unique_y_keys,
                    original_tick_text
                )
                if k in sliced_keys
            ]


            unique_y_keys = sliced_keys


            df = df[
                df["Y_Axis_Key"].isin(
                    sliced_keys
                )
            ].copy()


    # =====================================================
    # DYNAMIC CHART TITLE
    # =====================================================

    active_groups = [
        format_labels(group_by_1)
    ]


    if group_by_2 != "None":

        active_groups.append(
            format_labels(group_by_2)
        )


    if group_by_3 != "None":

        active_groups.append(
            format_labels(group_by_3)
        )


    title_group = (
        format_list_grammatically(
            active_groups
        )
    )


    roadmap_base_text = (
        f"{updated_date_str} "
        f"Roadmap by {title_group}"
    ).strip()


    if (
        presentation_mode
        and total_pages > 1
    ):

        roadmap_base_text += (
            f" (Page {current_page} "
            f"of {total_pages})"
        )


    formatted_products = (
        format_list_grammatically(
            selected_products
        )
    )


    if formatted_products:

        chart_title_text = (
            f"{formatted_products}:<br>"
            f"{roadmap_base_text}"
        )

    else:

        chart_title_text = (
            roadmap_base_text
        )


    # =====================================================
    # HTML HEADER
    # =====================================================

    if not presentation_mode:

        header_html = (
            "<div class='product-props-header'>"
            "<div class='logo-container'>"
            "Product Props"
            "<span class='pipe'>|</span>"
            "<span class='product-model'>"
            "Roadmapper"
            "</span>"
            "</div>"
            "</div>"
            f"<div class='roadmap-title'>"
            f"{chart_title_text}"
            f"</div>"
        )


        header_placeholder.markdown(
            header_html,
            unsafe_allow_html=True
        )


    else:

        header_placeholder.empty()


    # =====================================================
    # X-AXIS RANGE
    # =====================================================

    dynamic_x_range = [
        view_start_dt.strftime(
            "%Y-%m-%d"
        ),
        view_end_dt.strftime(
            "%Y-%m-%d"
        )
    ]


    # =====================================================
    # HEIGHT CALCULATION
    # =====================================================

    show_release_lane = (
        show_releases
        and not df_releases.empty
    )


    if show_release_lane:

        y_range_bounds = [
            len(unique_y_keys) - 0.5,
            -1.5
        ]


        dynamic_height = max(
            600,
            (
                len(unique_y_keys)
                + 1
            ) * 75
        )


    else:

        y_range_bounds = [
            len(unique_y_keys) - 0.5,
            -0.5
        ]


        dynamic_height = max(
            600,
            len(unique_y_keys) * 75
        )


    # =====================================================
    # BUILD PLOTLY TIMELINE
    # =====================================================

    if color_by == "Percent Complete":

        df[
            "Percent Complete Numeric"
        ] = pd.to_numeric(
            df["Percent Complete"],
            errors="coerce"
        ).fillna(0)


        fig = px.timeline(
            df,
            x_start="Plot_Start",
            x_end="Plot_End",
            y="Y_Axis_Key",
            color="Percent Complete Numeric",
            color_continuous_scale=(
                Product_Props__PCT_SCALE
            ),
            range_color=[
                0,
                100
            ],
            text="Display Title",
            opacity=1.0,
            height=dynamic_height
        )


        fig.update_coloraxes(
            colorbar_title="Completion %"
        )


    else:

        fig = px.timeline(
            df,
            x_start="Plot_Start",
            x_end="Plot_End",
            y="Y_Axis_Key",
            color=color_by,
            color_discrete_sequence=(
                Product_Props__CHART_COLORS
            ),
            text="Display Title",
            opacity=1.0,
            height=dynamic_height
        )


    # =====================================================
    # MANUAL GRID & EXACT CENTERED LABELS
    # =====================================================

    tick_anchor_ts = cycle_start_dt


    past_boundaries = [
        tick_anchor_ts
        - pd.DateOffset(
            months=3 * i
        )
        for i in range(1, 20)
    ]


    future_boundaries = [
        tick_anchor_ts
        + pd.DateOffset(
            months=3 * i
        )
        for i in range(0, 20)
    ]


    all_boundaries = sorted(
        list(
            set(
                past_boundaries
                + future_boundaries
            )
        )
    )


    x_tickvals = []
    x_ticktext = []


    now_ts = tick_anchor_ts


    next_ts = (
        tick_anchor_ts
        + pd.DateOffset(months=3)
    )


    later_ts = (
        tick_anchor_ts
        + pd.DateOffset(months=6)
    )


    for b in all_boundaries:

        midpoint = (
            b
            + pd.DateOffset(
                months=1,
                days=15
            )
        )


        x_tickvals.append(
            midpoint.strftime(
                "%Y-%m-%d"
            )
        )


        q = (
            (b.month - 1) // 3
        ) + 1


        default_label = (
            f"{b.year} Q{q}"
        )


        if show_horizon_labels:

            if b == now_ts:

                x_ticktext.append(
                    "Now"
                )

            elif b == next_ts:

                x_ticktext.append(
                    "Next"
                )

            elif b == later_ts:

                x_ticktext.append(
                    "Later"
                )

            else:

                x_ticktext.append(
                    ""
                )


        else:

            x_ticktext.append(
                default_label
            )


    fig.update_xaxes(
        side="top",
        type="date",
        tickmode="array",
        tickvals=x_tickvals,
        ticktext=x_ticktext,
        showgrid=False,
        zeroline=False,
        range=dynamic_x_range
    )


    # =====================================================
    # QUARTER BOUNDARY LINES
    # =====================================================

    for b in all_boundaries:

        b_str = b.strftime(
            "%Y-%m-%d"
        )


        if (
            dynamic_x_range[0]
            <= b_str
            <= dynamic_x_range[1]
        ):

            fig.add_vline(
                x=b_str,
                line_width=1,
                line_color=(
                    Product_Props__MED_BLUE
                ),
                layer="below"
            )


    # =====================================================
    # TYPOGRAPHY
    # =====================================================

    axis_font_size = (
        20
        if presentation_mode
        else 18
    )


    y_font_size = (
        18
        if presentation_mode
        else 16
    )


    bar_text_size = (
        16
        if presentation_mode
        else 13
    )


    # =====================================================
    # PRESENTATION / STANDARD LAYOUT
    # =====================================================

    if presentation_mode:

        fig.update_layout(

            title=dict(
                text=chart_title_text,
                font=dict(
                    size=26,
                    color=(
                        Product_Props__TITLE_BLUE
                    ),
                    family="Lato"
                ),
                x=0.5,
                y=0.92,
                xanchor="center",
                yanchor="top"
            ),

            margin=dict(
                t=160,
                b=120,
                r=40
            )
        )


    else:

        fig.update_layout(

            margin=dict(
                t=80,
                b=100,
                r=40
            )
        )


    # =====================================================
    # CORE CHART STYLING
    # =====================================================

    fig.update_layout(

        yaxis=dict(
            title=None,
            tickmode="array",
            tickvals=y_tick_vals,
            ticktext=y_tick_text,

            tickfont=dict(
                size=y_font_size,
                color=(
                    Product_Props__DARK_GRAY
                ),
                family="Lato"
            ),

            categoryorder="array",
            categoryarray=y_tick_vals,
            range=y_range_bounds,
            automargin=True,
            fixedrange=True
        ),


        xaxis=dict(

            tickfont=dict(
                size=axis_font_size,
                color=(
                    Product_Props__DARK_GRAY
                ),
                family="Lato"
            ),

            fixedrange=True
        ),


        legend=dict(

            font=dict(
                size=14,
                family="Lato",
                color=(
                    Product_Props__DARK_GRAY
                )
            ),

            orientation="h",
            yanchor="top",
            y=-0.1,
            xanchor="center",
            x=0.5
        ),


        bargap=0.02,

        plot_bgcolor=(
            Product_Props__LIGHT_GRAY
        ),

        paper_bgcolor=(
            Product_Props__LIGHT_GRAY
        ),

        dragmode=False
    )


    # =====================================================
    # RELEASE MILESTONES
    # =====================================================

    if show_release_lane:

        df_releases["Start Date"] = (
            pd.to_datetime(
                df_releases["Start Date"],
                errors="coerce"
            )
        )


        for idx, release in (
            df_releases
            .dropna(
                subset=["Start Date"]
            )
            .iterrows()
        ):

            if (
                release["Title"]
                in selected_releases
            ):

                release_date = (
                    release["Start Date"]
                    .strftime(
                        "%Y-%m-%d"
                    )
                )


                release_date_ms = (
                    release["Start Date"].timestamp()
                    * 1000
                )


                if (
                    dynamic_x_range[0]
                    <= release_date
                    <= dynamic_x_range[1]
                ):

                    wrapped_release_title = (
                        "<br>".join(
                            textwrap.wrap(
                                str(
                                    release["Title"]
                                ),
                                width=12,
                                break_long_words=False
                            )
                        )
                    )


                    fig.add_vline(

                        x=release_date_ms,

                        line_width=2,

                        line_dash="dash",

                        line_color=(
                            Product_Props__DARK_BLUE
                        ),

                        annotation_text=(
                            f"<b>"
                            f"{wrapped_release_title}"
                            f"</b>"
                        ),

                        annotation_position=(
                            "top right"
                        ),

                        annotation_yshift=-25,

                        annotation_xshift=10,

                        annotation_bgcolor=(
                            "rgba(243,232,211,0.95)"
                        ),

                        annotation_bordercolor=(
                            Product_Props__DARK_BLUE
                        ),

                        annotation_borderwidth=1,

                        annotation_borderpad=4,

                        annotation_font=dict(
                            color=(
                                Product_Props__DARK_BLUE
                            ),
                            size=(
                                16
                                if presentation_mode
                                else 14
                            ),
                            family="Lato"
                        )
                    )


    # =====================================================
    # BAR STYLING & HOVER INFORMATION
    # =====================================================

    fig.update_traces(

        selector=dict(
            type="bar"
        ),

        textposition="inside",

        insidetextanchor="middle",

        marker_line_color="white",

        marker_line_width=1,

        textfont=dict(
            family="Lato",
            size=bar_text_size
        ),

        hovertemplate=(
            "<b>%{customdata[0]}</b>"
            "<br><br>"
            "<b>Start:</b> "
            "%{customdata[5]}"
            "&nbsp;&nbsp;&nbsp;"
            "<b>End:</b> "
            "%{customdata[6]}"
            "<br>"
            "<b>Progress:</b> "
            "%{customdata[1]}%"
            "<br>"
            "<b>Target Release:</b> "
            "%{customdata[4]}"
            "<br>"
            "<b>Tags:</b> "
            "%{customdata[2]}"
            "<br>"
            "<b>Objective:</b> "
            "%{customdata[3]}"
            "<extra></extra>"
        ),

        customdata=df[
            [
                "Title",
                "Percent Complete",
                "Tags",
                "Container",
                "Target Release",
                "Start_Str",
                "End_Str"
            ]
        ]
    )


    # =====================================================
    # DYNAMIC EXPORT HEIGHT
    # =====================================================

    if presentation_mode:

        chart_config = {

            "displayModeBar": True,

            "modeBarButtonsToRemove": [
                "zoom",
                "pan",
                "select",
                "lasso2d",
                "zoomIn2d",
                "zoomOut2d",
                "autoScale2d",
                "resetScale2d"
            ],

            "toImageButtonOptions": {

                "format": "png",

                "filename": (
                    f"Roadmap_Slide_"
                    f"{current_page}"
                ),

                "height": (
                    dynamic_height
                    + 160
                    + 120
                ),

                "width": 1600,

                "scale": 2
            }
        }


    else:

        chart_config = {
            "displayModeBar": False
        }


    # =====================================================
    # DISPLAY CHART
    # =====================================================

    st.plotly_chart(
        fig,
        use_container_width=True,
        config=chart_config
    )


    # =====================================================
    # BOTTOM TEXT — HIDDEN IN PRESENTATION MODE
    # =====================================================

    if not presentation_mode:

        col_notes, col_health = (
            st.columns([2, 1])
        )


        # -------------------------------------------------
        # ROADMAP NOTES
        # -------------------------------------------------

        with col_notes:

            if not notes_df.empty:

                filtered_notes = (
                    notes_df[
                        notes_df["Product"].isin(
                            selected_products
                        )
                    ]
                )


                notes_html = ""


                for prod in (
                    filtered_notes[
                        "Product"
                    ].unique()
                ):

                    p_notes = (
                        filtered_notes[
                            filtered_notes[
                                "Product"
                            ] == prod
                        ]["Note"].unique()
                    )


                    if len(p_notes) > 0:

                        notes_html += (
                            f"<div "
                            f"class='note-group-title'>"
                            f"{prod} Notes"
                            f"</div>"
                            f"<ul>"
                            + "".join(
                                [
                                    f"<li>{n}</li>"
                                    for n in p_notes
                                ]
                            )
                            + "</ul>"
                        )


                if notes_html:

                    st.markdown(

                        f'<div class="roadmap-notes">'
                        f'<h4>'
                        f'Roadmap Notes & Assumptions'
                        f'</h4>'
                        f'{notes_html}'
                        f'</div>',

                        unsafe_allow_html=True
                    )


        # -------------------------------------------------
        # DATA HEALTH
        # -------------------------------------------------

        with col_health:

            if not bad_data_df.empty:

                st.markdown(

                    f'<div class="health-check">'
                    f'<h4>Data Health Check</h4>'
                    f'<p><b>'
                    f'{len(bad_data_df)} items excluded'
                    f'</b> due to missing Dates '
                    f'or Titles.</p>'
                    f'</div>',

                    unsafe_allow_html=True
                )


                with st.expander(
                    "See Excluded Items"
                ):

                    st.dataframe(
                        bad_data_df[
                            [
                                "Title",
                                "Start Date",
                                "End Date"
                            ]
                        ]
                    )


            else:

                st.markdown(

                    f'<div class="health-check" '
                    f'style="'
                    f'border-left-color: '
                    f'{Product_Props__ACC_GREEN}; '
                    f'background-color: '
                    f'{Product_Props__LIGHT_GRAY};'
                    f'">'
                    f'<h4 style="'
                    f'color: '
                    f'{Product_Props__ACC_GREEN};'
                    f'">'
                    f'Data Health Check'
                    f'</h4>'
                    f'<p style="'
                    f'color: '
                    f'{Product_Props__DARK_GRAY};'
                    f'">'
                    f'All items loaded successfully.'
                    f'</p>'
                    f'</div>',

                    unsafe_allow_html=True
                )


# =========================================================
# EMPTY STATE
# =========================================================

else:

    header_html = (

        "<div class='product-props-header'>"

        "<div class='logo-container'>"

        "Product Props"

        "<span class='pipe'>|</span>"

        "<span class='product-model'>"
        "Roadmapper"
        "</span>"

        "</div>"

        "</div>"
    )


    header_placeholder.markdown(
        header_html,
        unsafe_allow_html=True
    )


    st.info(
        "Upload a roadmap CSV or XLSX file to get started."
    )