import streamlit as st


# ----------------------------------------------------
# Page Config
# ----------------------------------------------------

st.set_page_config(
    page_title="AI Startup Co-Founder",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ----------------------------------------------------
# Styling
# ----------------------------------------------------

st.markdown(
    """
    <style>
        :root {
            --app-surface: rgba(255, 255, 255, 0.84);
            --app-surface-soft: rgba(248, 248, 249, 0.94);
            --app-border: rgba(120, 120, 130, 0.20);
            --app-text-muted: rgba(100, 103, 112, 0.96);
            --app-text-soft: rgba(130, 134, 144, 0.96);
            --app-shadow: 0 18px 50px rgba(20, 20, 30, 0.06);
        }

        .stApp {
            font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        }

        section[data-testid="stSidebar"] {
            border-right: 1px solid var(--app-border);
        }

        section[data-testid="stSidebar"] > div {
            padding: 2rem 1.2rem;
        }

        .block-container {
            max-width: 1180px;
            padding-top: 2.6rem;
            padding-bottom: 2.8rem;
        }

        h1, h2, h3 {
            letter-spacing: 0;
        }

        h1 {
            font-size: clamp(2rem, 4vw, 2.65rem);
            line-height: 1.08;
            font-weight: 720;
            margin-bottom: 0.55rem;
        }

        h2 {
            font-size: 1.35rem;
            font-weight: 680;
            margin-top: 0.5rem;
        }

        h3 {
            font-size: 1rem;
            font-weight: 650;
        }

        p, li, div, span {
            line-height: 1.58;
        }

        .hero {
            padding: 1.35rem 0 1.35rem 0;
            border-bottom: 1px solid var(--app-border);
            margin-bottom: 1.5rem;
        }

        .hero-kicker {
            color: var(--app-text-soft);
            font-size: 0.86rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-bottom: 0.8rem;
        }

        .hero-subtitle {
            color: var(--app-text-muted);
            font-size: 1.08rem;
            max-width: 760px;
            margin-bottom: 0.35rem;
        }

        .hero-description {
            color: var(--app-text-soft);
            font-size: 0.96rem;
            max-width: 720px;
        }

        .sidebar-title {
            font-size: 1.2rem;
            font-weight: 720;
            margin-bottom: 0.25rem;
        }

        .sidebar-muted {
            color: var(--app-text-muted);
            font-size: 0.9rem;
            margin-bottom: 1.25rem;
        }

        .sidebar-section {
            border-top: 1px solid var(--app-border);
            padding-top: 1.1rem;
            margin-top: 1.15rem;
        }

        .sidebar-label {
            color: var(--app-text-soft);
            font-size: 0.76rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-bottom: 0.55rem;
        }

        .stack-list {
            display: flex;
            flex-wrap: wrap;
            gap: 0.42rem;
        }

        .stack-item {
            border: 1px solid var(--app-border);
            border-radius: 999px;
            padding: 0.28rem 0.58rem;
            color: var(--app-text-muted);
            background: var(--app-surface-soft);
            font-size: 0.78rem;
            font-weight: 600;
            line-height: 1.35;
        }

        .input-panel,
        .score-panel {
            background: var(--app-surface);
            border: 1px solid var(--app-border);
            border-radius: 10px;
            padding: 1.35rem;
            box-shadow: var(--app-shadow);
        }

        .input-panel {
            margin-bottom: 1.5rem;
        }

        .score-panel {
            margin-top: 1rem;
            margin-bottom: 1.35rem;
        }

        .section-title {
            font-size: 1.08rem;
            font-weight: 700;
            margin: 0.1rem 0 0.9rem 0;
        }

        .score-value {
            font-size: clamp(2.25rem, 6vw, 3.45rem);
            font-weight: 760;
            line-height: 1.05;
            letter-spacing: 0;
            margin-top: 1.15rem;
            margin-bottom: 0.35rem;
        }

        .score-label {
            color: var(--app-text-soft);
            font-size: 0.86rem;
            font-weight: 650;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-bottom: 0.7rem;
        }

        .score-progress {
            margin-top: 0.35rem;
            margin-bottom: 0.6rem;
        }

        .quiet-list ul {
            margin-top: 0.1rem;
            margin-bottom: 0.1rem;
            padding-left: 1.25rem;
        }

        .quiet-list li {
            margin-bottom: 0.35rem;
            color: var(--app-text-muted);
        }

        div[data-testid="stVerticalBlockBorderWrapper"] {
            border-color: var(--app-border);
            border-radius: 10px;
            background: var(--app-surface);
            padding: 0.15rem;
        }

        div[data-testid="stMetric"] {
            background: var(--app-surface);
            border: 1px solid var(--app-border);
            border-radius: 12px;
            padding: 1.25rem 1.2rem;
            box-shadow: 0 10px 30px rgba(20, 20, 30, 0.04);
            min-height: 132px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            gap: 0.35rem;
        }

        div[data-testid="stMetricLabel"] {
            color: var(--app-text-soft);
            font-size: 0.94rem;
            font-weight: 650;
            line-height: 1.3;
        }

        div[data-testid="stMetricValue"] {
            font-size: clamp(1.35rem, 2vw, 1.7rem);
            font-weight: 740;
            white-space: normal;
            overflow-wrap: anywhere;
            line-height: 1.22;
        }

        .stTextArea textarea {
            border-radius: 10px;
            border-color: var(--app-border);
            font-size: 0.98rem;
            line-height: 1.55;
            min-height: 180px;
        }

        .stButton > button {
            border-radius: 10px;
            min-height: 2.8rem;
            font-weight: 650;
        }

        .stTabs [data-baseweb="tab-list"] {
            gap: 0.7rem;
            border-bottom: 1px solid var(--app-border);
            margin-bottom: 1.25rem;
        }

        .stTabs [data-baseweb="tab"] {
            min-height: 3.15rem;
            border-radius: 12px 12px 0 0;
            color: var(--app-text-muted);
            padding: 0.95rem 1.35rem;
            font-size: 1rem;
            font-weight: 650;
            border: 1px solid transparent;
            transition: background 140ms ease, border-color 140ms ease, color 140ms ease;
        }

        .stTabs [data-baseweb="tab"]:hover {
            background: var(--app-surface-soft);
            border-color: var(--app-border);
            color: inherit;
        }

        .stTabs [aria-selected="true"] {
            border: 1px solid var(--app-border);
            border-bottom-color: transparent;
            background: var(--app-surface);
            font-weight: 720;
        }

        .stTabs [data-baseweb="tab"] p {
            font-size: 1rem;
            line-height: 1.25;
            margin: 0;
        }

        .footer {
            color: var(--app-text-soft);
            font-size: 0.85rem;
            text-align: center;
            border-top: 1px solid var(--app-border);
            padding-top: 1.1rem;
            margin-top: 1.4rem;
        }

        div[data-testid="stExpander"] {
            border-color: var(--app-border);
            border-radius: 10px;
        }

        div[data-testid="stMarkdownContainer"] h4 {
            font-size: 1rem;
            font-weight: 720;
            margin-bottom: 0.45rem;
        }

        @media (max-width: 768px) {
            .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
                padding-top: 1.6rem;
            }

            .input-panel,
            .score-panel {
                padding: 1rem;
            }

            div[data-testid="stMetric"] {
                min-height: 112px;
            }

            .stTabs [data-baseweb="tab-list"] {
                gap: 0.45rem;
            }

            .stTabs [data-baseweb="tab"] {
                min-height: 2.85rem;
                padding: 0.8rem 1rem;
                font-size: 0.95rem;
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# ----------------------------------------------------
# UI Helpers
# ----------------------------------------------------

@st.cache_resource(show_spinner=False)
def get_compiled_graph():
    from graph.workflow import build_graph

    return build_graph()


def render_card(title, body):
    with st.container(border=True):
        st.markdown(f"#### {title}")
        st.write(body)


def render_list(title, items):
    with st.container(border=True):
        st.markdown(f"#### {title}")
        if items:
            bullet_items = "\n".join([f"- {item}" for item in items])
            st.markdown(f'<div class="quiet-list">\n\n{bullet_items}\n\n</div>', unsafe_allow_html=True)
        else:
            st.markdown('<span style="color: var(--app-text-muted);">No items available.</span>', unsafe_allow_html=True)


def render_text_section(title, value):
    with st.container(border=True):
        st.markdown(f"#### {title}")
        st.write(value)


def concise_metric_value(value):
    text = str(value).strip()
    normalized = text.lower()

    for label in ["excellent", "very high", "high", "good", "medium", "moderate", "low", "poor"]:
        if label in normalized:
            return label.title()

    if "/" in text:
        return text.split()[0]

    words = text.replace(".", " ").replace(",", " ").split()
    if len(words) <= 3:
        return text

    return "Review Tab"


def format_overall_score(score):
    text = str(score).strip()

    try:
        value = float(text.split("/")[0].strip())
        return f"{value:g} / 10", value / 10
    except Exception:
        return text, None


# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------

with st.sidebar:
    st.markdown('<div class="sidebar-title">AI Startup Co-Founder</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="sidebar-muted">Multi-Agent AI Startup Validation Platform</div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-label">Technology Stack</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="stack-list">
            <div class="stack-item">LangGraph</div>
            <div class="stack-item">OpenRouter</div>
            <div class="stack-item">RAG</div>
            <div class="stack-item">ChromaDB</div>
            <div class="stack-item">Streamlit</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-label">Project Version</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-muted">Version 1.0</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-label">Short Description</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="sidebar-muted">AI-powered startup validation using multi-agent reasoning, retrieval, and structured review.</div>',
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)


# ----------------------------------------------------
# Header
# ----------------------------------------------------

st.markdown(
    """
    <section class="hero">
        <div class="hero-kicker">Startup Validation Dashboard</div>
        <h1>AI Startup Co-Founder</h1>
        <div class="hero-subtitle">AI-powered startup validation using Multi-Agent AI, RAG, and LangGraph.</div>
        <div class="hero-description">Enter a startup idea to generate a structured evaluation across market, business, marketing, risk, and review dimensions.</div>
    </section>
    """,
    unsafe_allow_html=True,
)


# ----------------------------------------------------
# User Input
# ----------------------------------------------------

with st.container():
    st.markdown('<div class="input-panel">', unsafe_allow_html=True)
    startup_idea = st.text_area(
        "Enter your startup idea",
        height=180,
        placeholder="Describe the startup concept, audience, problem, and intended solution.",
    )

    col1, col2, col3 = st.columns([1.15, 1.4, 1.15])
    with col2:
        analyze = st.button(
            "Analyze Startup",
            use_container_width=True,
            type="primary",
        )
    st.markdown("</div>", unsafe_allow_html=True)


# ----------------------------------------------------
# Analyze
# ----------------------------------------------------

if analyze:
    if startup_idea.strip() == "":
        st.warning("Please enter a startup idea.")
        st.stop()

    try:
        with st.spinner("Generating a structured startup analysis..."):
            graph = get_compiled_graph()

            result = graph.invoke(
                {
                    "startup_idea": startup_idea
                }
            )

    except Exception as e:
        st.error("Failed to generate startup analysis.")

        with st.expander("Error Details"):
            st.code(str(e))

        st.stop()

    review = result["review"]

    # ------------------------------------------------
    # Score Cards
    # ------------------------------------------------

    st.divider()

    with st.container():
        st.markdown('<div class="score-panel">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Overall Startup Evaluation</div>', unsafe_allow_html=True)

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "Business",
            concise_metric_value(review["business_feasibility"]),
        )

        c2.metric(
            "Market",
            concise_metric_value(review["market_potential"]),
        )

        c3.metric(
            "Revenue",
            concise_metric_value(review["revenue_sustainability"]),
        )

        c4.metric(
            "Technical",
            concise_metric_value(review["technical_feasibility"]),
        )

        score = review["overall_score"]
        formatted_score, progress = format_overall_score(score)

        st.markdown('<div class="score-label">Overall Score</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="score-value">{formatted_score}</div>', unsafe_allow_html=True)

        if progress is not None:
            st.markdown('<div class="score-progress">', unsafe_allow_html=True)
            st.progress(progress)
            st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.divider()

    # ------------------------------------------------
    # Tabs
    # ------------------------------------------------

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
        [
            "Idea",
            "Market",
            "Business",
            "Marketing",
            "Risks",
            "Review",
        ]
    )

    # ------------------------------------------------
    # IDEA
    # ------------------------------------------------

    with tab1:
        idea = result["idea_analysis"]

        render_text_section("Problem", idea["problem"])
        render_text_section("Target Customers", idea["target_customers"])
        render_text_section("Value Proposition", idea["value_proposition"])
        render_text_section("Unique Selling Point", idea["unique_selling_point"])
        render_text_section("Revenue Model", idea["revenue_model"])
        render_list("Risks", idea["risks"])

    # ------------------------------------------------
    # MARKET
    # ------------------------------------------------

    with tab2:
        market = result["market_analysis"]

        render_text_section("Market Size", market["market_size"])

        with st.expander("Competitors", expanded=True):
            render_list("Competitors", market["competitors"])

        with st.expander("Industry Trends"):
            render_list("Industry Trends", market["industry_trends"])

        with st.expander("Opportunities"):
            render_list("Opportunities", market["opportunities"])

        with st.expander("Threats"):
            render_list("Threats", market["threats"])

    # ------------------------------------------------
    # BUSINESS
    # ------------------------------------------------

    with tab3:
        business = result["business_model"]

        render_text_section("Business Model", business["business_model"])
        render_list("Revenue Streams", business["revenue_streams"])
        render_list("Cost Structure", business["cost_structure"])
        render_list("Customer Acquisition", business["customer_acquisition"])
        render_list("Key Partnerships", business["key_partnerships"])

    # ------------------------------------------------
    # MARKETING
    # ------------------------------------------------

    with tab4:
        marketing = result["marketing_strategy"]

        render_list("Target Segments", marketing["target_segments"])
        render_list("Marketing Channels", marketing["marketing_channels"])
        render_text_section("Branding Strategy", marketing["branding_strategy"])
        render_text_section("Pricing Strategy", marketing["pricing_strategy"])
        render_list("Growth Strategy", marketing["growth_strategy"])

    # ------------------------------------------------
    # RISK
    # ------------------------------------------------

    with tab5:
        risk = result["risk_analysis"]

        render_list("Business Risks", risk["business_risks"])
        render_list("Technical Risks", risk["technical_risks"])
        render_list("Financial Risks", risk["financial_risks"])
        render_list("Legal Risks", risk["legal_risks"])
        render_list("Mitigation Strategies", risk["mitigation_strategies"])

    # ------------------------------------------------
    # REVIEW
    # ------------------------------------------------

    with tab6:
        render_list("Strengths", review["strengths"])
        render_list("Weaknesses", review["weaknesses"])
        render_list("Recommendations", review["recommendations"])

    st.markdown(
        '<div class="footer">Powered by LangGraph | OpenRouter | RAG | ChromaDB | Streamlit</div>',
        unsafe_allow_html=True,
    )
