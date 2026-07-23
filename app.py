import streamlit as st

from graph.workflow import build_graph


# ----------------------------------------------------
# Page Config
# ----------------------------------------------------

st.set_page_config(
    page_title="AI Startup Co-Founder",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------

with st.sidebar:

    st.title(" AI Startup")

    st.markdown("---")

    st.subheader("Technology Stack")

    st.success("LangGraph")
    st.success("OpenRouter")
    st.success("RAG")
    st.success("ChromaDB")
    st.success("Streamlit")

    st.markdown("---")

    st.info(
        """
### AI Startup Co-Founder

Version 1.0

Multi-Agent AI Startup Validation Platform
"""
    )

# ----------------------------------------------------
# Header
# ----------------------------------------------------

st.title(" AI Startup Co-Founder")

st.caption(
    "AI-Powered Startup Validation using Multi-Agent AI + RAG + LangGraph"
)

# ----------------------------------------------------
# User Input
# ----------------------------------------------------

startup_idea = st.text_area(
    " Enter Your Startup Idea",
    height=180,
    placeholder="Example: AI-powered platform for university students to improve mental health."
)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:

    analyze = st.button(
        " Analyze Startup",
        use_container_width=True
    )

# ----------------------------------------------------
# Analyze
# ----------------------------------------------------

if analyze:

    if startup_idea.strip() == "":

        st.warning("Please enter a startup idea.")
        st.stop()

    try:

        with st.spinner("Generating AI startup analysis..."):

            graph = build_graph()

            result = graph.invoke(
                {
                    "startup_idea": startup_idea
                }
            )

        st.success("Analysis Completed Successfully!")

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

    st.header(" Overall Startup Evaluation")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Business",
        review["business_feasibility"]
    )

    c2.metric(
        "Market",
        review["market_potential"]
    )

    c3.metric(
        "Revenue",
        review["revenue_sustainability"]
    )

    c4.metric(
        "Technical",
        review["technical_feasibility"]
    )

    score = review["overall_score"]

    try:

        value = float(score.split("/")[0])

        progress = value / 10

        st.progress(progress)

        st.subheader(f" Overall Score : {score}")

    except Exception:

        st.subheader(f" Overall Score : {score}")

    st.divider()

    # ------------------------------------------------
    # Tabs
    # ------------------------------------------------

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        " Idea",
        " Market",
        " Business",
        " Marketing",
        "⚠ Risks",
        " Review"
    ])

    # ------------------------------------------------
    # IDEA
    # ------------------------------------------------

    with tab1:

        idea = result["idea_analysis"]

        st.subheader("Problem")
        st.write(idea["problem"])

        st.subheader("Target Customers")
        st.write(idea["target_customers"])

        st.subheader("Value Proposition")
        st.write(idea["value_proposition"])

        st.subheader("Unique Selling Point")
        st.write(idea["unique_selling_point"])

        st.subheader("Revenue Model")
        st.write(idea["revenue_model"])

        st.subheader("Risks")

        for item in idea["risks"]:
            st.error(item)

    # ------------------------------------------------
    # MARKET
    # ------------------------------------------------

    with tab2:

        market = result["market_analysis"]

        st.subheader("Market Size")
        st.write(market["market_size"])

        with st.expander("Competitors", expanded=True):

            for item in market["competitors"]:
                st.write("•", item)

        with st.expander("Industry Trends"):

            for item in market["industry_trends"]:
                st.write("•", item)

        with st.expander("Opportunities"):

            for item in market["opportunities"]:
                st.success(item)

        with st.expander("Threats"):

            for item in market["threats"]:
                st.error(item)

    # ------------------------------------------------
    # BUSINESS
    # ------------------------------------------------

    with tab3:

        business = result["business_model"]

        st.subheader("Business Model")
        st.write(business["business_model"])

        st.subheader("Revenue Streams")

        for item in business["revenue_streams"]:
            st.success(item)

        st.subheader("Cost Structure")

        for item in business["cost_structure"]:
            st.warning(item)

        st.subheader("Customer Acquisition")

        for item in business["customer_acquisition"]:
            st.write("•", item)

        st.subheader("Key Partnerships")

        for item in business["key_partnerships"]:
            st.info(item)

    # ------------------------------------------------
    # MARKETING
    # ------------------------------------------------

    with tab4:

        marketing = result["marketing_strategy"]

        st.subheader("Target Segments")

        for item in marketing["target_segments"]:
            st.write("•", item)

        st.subheader("Marketing Channels")

        for item in marketing["marketing_channels"]:
            st.write("•", item)

        st.subheader("Branding Strategy")
        st.write(marketing["branding_strategy"])

        st.subheader("Pricing Strategy")
        st.write(marketing["pricing_strategy"])

        st.subheader("Growth Strategy")

        for item in marketing["growth_strategy"]:
            st.success(item)

    # ------------------------------------------------
    # RISK
    # ------------------------------------------------

    with tab5:

        risk = result["risk_analysis"]

        st.subheader("Business Risks")

        for item in risk["business_risks"]:
            st.error(item)

        st.subheader("Technical Risks")

        for item in risk["technical_risks"]:
            st.warning(item)

        st.subheader("Financial Risks")

        for item in risk["financial_risks"]:
            st.warning(item)

        st.subheader("Legal Risks")

        for item in risk["legal_risks"]:
            st.error(item)

        st.subheader("Mitigation Strategies")

        for item in risk["mitigation_strategies"]:
            st.success(item)

    # ------------------------------------------------
    # REVIEW
    # ------------------------------------------------

    with tab6:

        st.subheader("Strengths")

        for item in review["strengths"]:
            st.success(item)

        st.subheader("Weaknesses")

        for item in review["weaknesses"]:
            st.error(item)

        st.subheader("Recommendations")

        for item in review["recommendations"]:
            st.info(item)

    st.divider()

    st.caption(" Powered by LangGraph | OpenRouter | RAG | ChromaDB | Streamlit")