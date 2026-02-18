import streamlit as st

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Data Career Path Quiz",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# -------------------------------------------------
# BEAUTIFUL CSS STYLING
# -------------------------------------------------
st.markdown("""
    <style>
        /* Full page background gradient */
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        }
        
        /* Main content area */
        [data-testid="stMainBlockContainer"] {
            padding: 40px 20px !important;
            background: transparent !important;
        }
        
        /* White card container - use block-container class */
        .block-container {
            max-width: 750px !important;
            margin: 0 auto !important;
            background: white !important;
            border-radius: 16px !important;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3) !important;
            padding: 50px 40px !important;
            color: #333 !important;
        }
        
        /* Force text color to dark */
        .block-container p, 
        .block-container h1, 
        .block-container h2, 
        .block-container h3,
        .block-container span,
        .block-container div {
            color: #333 !important;
        }
        
        /* Remove Streamlit header/footer */
        #MainMenu { visibility: hidden; }
        footer { visibility: hidden; }
        header { visibility: hidden; }
        [data-testid="stDecoration"] { display: none; }
        
        /* Header styling */
        .header-title {
            text-align: center;
            margin-bottom: 30px;
            margin-top: -20px;
        }
        
        .header-title h1 {
            color: #333;
            font-size: 32px;
            font-weight: 700;
            margin: 0 0 10px 0 !important;
        }
        
        .header-title p {
            color: #666;
            font-size: 16px;
            margin: 0;
        }
        
        /* Progress bar */
        .progress-section {
            margin-bottom: 30px;
            margin-top: 10px;
        }
        
        .progress-text {
            color: #667eea;
            font-size: 12px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.6px;
            margin-bottom: 12px;
        }
        
        .progress-bar {
            width: 100%;
            height: 6px;
            background: #eee;
            border-radius: 3px;
            overflow: hidden;
        }
        
        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        }
        
        /* Question styling */
        .question-number {
            color: #667eea;
            font-size: 12px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.6px;
            margin-bottom: 12px;
        }
        
        .question-text {
            font-size: 20px;
            color: #333;
            margin-bottom: 30px;
            font-weight: 600;
            line-height: 1.4;
        }
        
        /* Answer buttons */
        .stButton > button {
            width: 100% !important;
            padding: 16px 20px !important;
            margin-bottom: 12px !important;
            border: 2px solid #ddd !important;
            background-color: white !important;
            border-radius: 10px !important;
            font-size: 15px !important;
            font-weight: 500 !important;
            color: #333 !important;
            text-align: left !important;
            transition: all 0.2s ease !important;
        }
        
        .stButton > button:hover {
            border-color: #667eea !important;
            background-color: #f8f9ff !important;
        }
        
        /* Result title */
        .result-title {
            color: #667eea;
            font-size: 32px;
            font-weight: 700;
            margin: 0 0 20px 0;
            margin-top: 20px;
        }
        
        /* Result description */
        .result-description {
            background: #f8f9ff;
            border-left: 4px solid #667eea;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 40px;
            margin-top: 30px;
            color: #555;
            font-size: 16px;
            line-height: 1.6;
        }
        
        /* Section titles */
        .section-title {
            color: #667eea;
            font-size: 12px;
            font-weight: 600;
            margin-top: 25px;
            margin-bottom: 15px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        /* Section content */
        .section-content {
            color: #555;
            line-height: 1.6;
            margin-bottom: 20px;
            font-size: 15px;
        }
        
        /* Tags */
        .tags {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-bottom: 20px;
        }
        
        .tag {
            background: white;
            border: 1px solid #ddd;
            color: #555;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 14px;
            display: inline-block;
        }
        
        /* Score breakdown */
        .score-breakdown {
            background: #f8f9ff;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 25px;
        }
        
        .score-item {
            display: flex;
            align-items: center;
            margin-bottom: 15px;
            font-size: 14px;
        }
        
        .score-item:last-child {
            margin-bottom: 0;
        }
        
        .score-label {
            font-weight: 600;
            color: #333;
            min-width: 140px;
        }
        
        .score-bar-container {
            flex: 1;
            height: 20px;
            background: #ddd;
            border-radius: 10px;
            overflow: hidden;
            margin: 0 15px;
        }
        
        .score-bar-fill {
            height: 100%;
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        }
        
        .score-percent {
            font-weight: 600;
            color: #667eea;
            min-width: 40px;
            text-align: right;
        }
        
        /* Styled Container */
        .st-key-styled_container {
            background-color: grey;
            border-radius: 1rem;
            padding: 1rem;
            min-height: 100px;
            box-shadow: 3px 5px 15px 0px rgba(128, 128, 128, 0.245);
        }
        
        .st-key-styled_container div[data-testid="stText"] div {
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# QUIZ DATA
# -------------------------------------------------
quiz = [
    {
        "question": "You're handed a messy dataset. What's your first instinct?",
        "answers": [
            {"text": "Clean it, document assumptions, and make it usable for others", "role": "engineer"},
            {"text": "Explore it to see what patterns jump out", "role": "analyst"},
            {"text": "Ask why this data exists and what decision it should inform", "role": "business_partner"},
            {"text": "Think about how to model or automate insights from it", "role": "scientist"},
            {"text": "Think about how to explain it to someone non-technical", "role": "communicator"}
        ]
    },
    {
        "question": "Which part of a project gives you the biggest energy boost?",
        "answers": [
            {"text": "Building something reliable that just works", "role": "engineer"},
            {"text": "Finding a surprising insight no one noticed", "role": "analyst"},
            {"text": "Influencing a decision or strategy", "role": "business_partner"},
            {"text": "Optimizing accuracy or performance", "role": "scientist"},
            {"text": "Crafting a story that makes people get it", "role": "communicator"}
        ]
    },
    {
        "question": "A stakeholder asks for 'all the data.' You…",
        "answers": [
            {"text": "Push back and define requirements", "role": "engineer"},
            {"text": "Pull everything and explore freely", "role": "analyst"},
            {"text": "Clarify the business question first", "role": "business_partner"},
            {"text": "Think about scalable pipelines or models", "role": "scientist"},
            {"text": "Ask who the audience is and what they need to understand", "role": "communicator"}
        ]
    },
    {
        "question": "How do you feel about ambiguity?",
        "answers": [
            {"text": "I prefer structure and clear specs", "role": "engineer"},
            {"text": "I like exploring unknowns", "role": "analyst"},
            {"text": "I'm okay with ambiguity if it leads to clarity", "role": "business_partner"},
            {"text": "I enjoy complex, undefined problems", "role": "scientist"},
            {"text": "I tolerate ambiguity if I can shape the narrative", "role": "communicator"}
        ]
    },
    {
        "question": "Pick the sentence that sounds most like you",
        "answers": [
            {"text": "\"Data should be clean, consistent, and trustworthy.\"", "role": "engineer"},
            {"text": "\"There's something interesting in here — we just haven't found it yet.\"", "role": "analyst"},
            {"text": "\"What decision will this change?\"", "role": "business_partner"},
            {"text": "\"We can predict or automate this.\"", "role": "scientist"},
            {"text": "\"If people don't understand it, it doesn't matter.\"", "role": "communicator"}
        ]
    },
    {
        "question": "Which skill do you enjoy sharpening the most?",
        "answers": [
            {"text": "SQL optimization, data modeling, pipelines", "role": "engineer"},
            {"text": "Analysis, slicing data different ways", "role": "analyst"},
            {"text": "Framing problems and metrics", "role": "business_partner"},
            {"text": "Algorithms, experimentation, ML", "role": "scientist"},
            {"text": "Visualization, storytelling, communication", "role": "communicator"}
        ]
    },
    {
        "question": "You're most proud of work when…",
        "answers": [
            {"text": "Others rely on it daily", "role": "engineer"},
            {"text": "It reveals something new", "role": "analyst"},
            {"text": "It drives real-world action", "role": "business_partner"},
            {"text": "It scales or improves accuracy", "role": "scientist"},
            {"text": "It changes how people think", "role": "communicator"}
        ]
    },
    {
        "question": "What frustrates you the most?",
        "answers": [
            {"text": "Messy, unreliable data", "role": "engineer"},
            {"text": "Not enough time to explore", "role": "analyst"},
            {"text": "Insights going unused", "role": "business_partner"},
            {"text": "Technical limitations", "role": "scientist"},
            {"text": "People misinterpreting data", "role": "communicator"}
        ]
    },
    {
        "question": "Your ideal meeting looks like…",
        "answers": [
            {"text": "Technical deep-dive", "role": "engineer"},
            {"text": "Whiteboarding patterns", "role": "analyst"},
            {"text": "Strategic discussion", "role": "business_partner"},
            {"text": "Debating models or approaches", "role": "scientist"},
            {"text": "Presenting insights", "role": "communicator"}
        ]
    },
    {
        "question": "If you had to choose, you'd rather…",
        "answers": [
            {"text": "Build the foundation", "role": "engineer"},
            {"text": "Discover insights", "role": "analyst"},
            {"text": "Guide decisions", "role": "business_partner"},
            {"text": "Build intelligence", "role": "scientist"},
            {"text": "Tell the story", "role": "communicator"}
        ]
    },
    {
        "question": "How do you feel about writing code all day?",
        "answers": [
            {"text": "Love it", "role": "engineer"},
            {"text": "Like it in bursts", "role": "analyst"},
            {"text": "As a means to an end", "role": "business_partner"},
            {"text": "Absolutely yes", "role": "scientist"},
            {"text": "Only if it supports the story", "role": "communicator"}
        ]
    },
    {
        "question": "Which phrase excites you most?",
        "answers": [
            {"text": "\"Single source of truth\"", "role": "engineer"},
            {"text": "\"Exploratory analysis\"", "role": "analyst"},
            {"text": "\"Business impact\"", "role": "business_partner"},
            {"text": "\"Predictive model\"", "role": "scientist"},
            {"text": "\"Compelling narrative\"", "role": "communicator"}
        ]
    },
    {
        "question": "You'd rather be known as…",
        "answers": [
            {"text": "The reliable builder", "role": "engineer"},
            {"text": "The curious analyst", "role": "analyst"},
            {"text": "The strategic partner", "role": "business_partner"},
            {"text": "The technical expert", "role": "scientist"},
            {"text": "The translator", "role": "communicator"}
        ]
    },
    {
        "question": "When learning something new, you prefer…",
        "answers": [
            {"text": "Step-by-step structure", "role": "engineer"},
            {"text": "Hands-on experimentation", "role": "analyst"},
            {"text": "Real-world use cases", "role": "business_partner"},
            {"text": "Technical depth", "role": "scientist"},
            {"text": "Examples and stories", "role": "communicator"}
        ]
    },
    {
        "question": "Your dream feedback sounds like…",
        "answers": [
            {"text": "\"This data is rock solid.\"", "role": "engineer"},
            {"text": "\"We didn't know this before.\"", "role": "analyst"},
            {"text": "\"This changed our decision.\"", "role": "business_partner"},
            {"text": "\"This system is powerful.\"", "role": "scientist"},
            {"text": "\"That finally makes sense.\"", "role": "communicator"}
        ]
    }
]

roles = {
    "engineer": {
        "title": "Data Engineer",
        "emoji": "🏗️",
        "description": "You're the architect behind the scenes. You build the infrastructure, pipelines, and systems that make data accessible and reliable. You take pride in creating foundations that others depend on.",
        "whatYouDo": "Design and maintain data pipelines, build data warehouses, optimize databases, ensure data quality and consistency, create APIs and infrastructure for data access",
        "dayToDay": "Writing production code, debugging data issues, optimizing performance, collaborating with other engineers, ensuring the data pipeline runs smoothly",
        "skills": ["SQL", "Python/Scala", "Data modeling", "ETL/ELT", "Cloud platforms", "System design"],
        "tools": ["Python", "SQL", "Spark", "Airflow", "dbt", "AWS/GCP/Azure", "Git"],
        "bestFor": "People who love building things, want code to be their primary tool, and find satisfaction in creating reliable systems others depend on",
        "careerPath": ["Junior Data Engineer (1-2 years) → Mid-level Data Engineer (3-5 years) → Senior Data Engineer (5+ years) → Lead/Staff Engineer → Engineering Manager"],
        "companies": "Tech companies (Google, Meta, Netflix), Finance (JPMorgan, Goldman Sachs), Cloud providers (AWS, Databricks), E-commerce (Amazon, Shopify), Streaming services (Spotify, Disney+)",
        "challenges": "Handling petabyte-scale data, real-time processing of millions of events, ensuring 99.99% uptime, optimizing cloud costs, managing data quality across complex systems",
        "resources": ["Apache Spark & PySpark Documentation", "dbt Fundamentals Course (free)", "DataCamp - Data Engineering Track", "Cloud certifications (AWS Solutions Architect, GCP Associate)", "GitHub - awesome-data-engineering"],
        "jobKeywords": ["ETL/ELT Pipeline", "Data Warehouse", "Data Lake", "Apache Spark", "Airflow", "dbt", "Real-time Processing", "Stream Processing", "Data Infrastructure", "Cloud Data Platform", "Data Quality", "Schema Design", "Data Modeling", "API Development", "Database Optimization", "Distributed Systems"]
    },
    "analyst": {
        "title": "Data Analyst",
        "emoji": "🔍",
        "description": "You're the explorer and pattern-finder. You dig into datasets to uncover insights, slice data different ways, and find what others missed. You love the discovery phase.",
        "whatYouDo": "Explore datasets, identify patterns and trends, perform ad-hoc analyses, answer business questions, create exploratory reports and visualizations",
        "dayToDay": "Writing queries to explore data, analyzing results, spotting patterns, prototyping analyses, collaborating with other analysts",
        "skills": ["SQL", "Python/R", "Excel", "Exploratory analysis", "Data visualization", "Curiosity"],
        "tools": ["SQL", "Python/R", "Excel", "Jupyter", "Tableau", "Looker"],
        "bestFor": "People who get excited about discovery, like exploring data freely, and are energized by finding surprising insights",
        "careerPath": ["Junior Analyst (1-2 years) → Data Analyst (3-4 years) → Senior Analyst (5+ years) → Analytics Lead → Director of Analytics"],
        "companies": "Consulting firms (McKinsey, Deloitte), Retail (Walmart, Target), Tech (Google, Slack), Finance (Stripe, Square), Media (New York Times, Spotify)",
        "challenges": "Finding signal in noisy data, communicating findings to non-technical stakeholders, working with inconsistent data sources, meeting tight reporting deadlines",
        "resources": ["Mode Analytics - SQL Tutorial (free)", "Tableau Public - Gallery & Learning", "Google Analytics Academy (free certification)", "DataCamp - Data Analysis with Python", "Coursera - Business Analytics Specialization"],
        "jobKeywords": ["Ad-hoc Analysis", "Business Intelligence", "Exploratory Data Analysis", "Reporting", "Dashboard Creation", "Trend Analysis", "Data Visualization", "Statistical Analysis", "Query Writing", "Business Metrics", "KPI Tracking", "Data Storytelling", "Insights Generation", "Cross-functional Analysis", "Tableau/Power BI Proficiency"]
    },
    "scientist": {
        "title": "Data Scientist",
        "emoji": "🤖",
        "description": "You're the optimizer and builder of intelligent systems. You love models, algorithms, and testing hypotheses. You want to push technical boundaries and create systems that get smarter.",
        "whatYouDo": "Develop predictive models, build ML systems, run experiments and A/B tests, optimize accuracy and performance, solve complex technical problems",
        "dayToDay": "Feature engineering, model development, running experiments, evaluating performance, debugging models",
        "skills": ["Python", "Machine Learning", "Statistics", "SQL", "Experimentation", "Algorithms"],
        "tools": ["Python", "scikit-learn", "TensorFlow/PyTorch", "SQL", "Jupyter", "Git"],
        "bestFor": "People who love algorithms, want to push technical boundaries, and are motivated by optimizing performance and accuracy",
        "careerPath": ["Junior Data Scientist (1-2 years) → Data Scientist (3-5 years) → Senior Data Scientist (5+ years) → ML Researcher → Head of Data Science"],
        "companies": "AI/ML focused (OpenAI, Anthropic, Hugging Face), Tech giants (Google, Microsoft, Apple), Finance (Citadel, Jane Street), Ride-sharing (Uber, Lyft), Healthcare (CVS, UnitedHealth)",
        "challenges": "Getting clean training data, avoiding model overfitting, deploying models to production, explaining model decisions, keeping up with new techniques",
        "resources": ["Andrew Ng - Machine Learning Specialization (Coursera)", "Fast.ai - Practical Deep Learning", "Kaggle - Competitions & Datasets", "Stanford CS229 - Machine Learning (free lectures)", "Papers with Code - Latest research implementations"],
        "jobKeywords": ["Machine Learning", "Predictive Modeling", "Deep Learning", "Neural Networks", "A/B Testing", "Experimentation", "Feature Engineering", "Model Training", "Algorithm Development", "Statistical Modeling", "Classification/Regression", "Computer Vision", "NLP", "Model Evaluation", "Production ML", "MLOps"]
    },
    "business_partner": {
        "title": "Business Analytics Partner",
        "emoji": "📊",
        "description": "You're the strategist who translates between data and business. You focus on what decisions matter, frame problems correctly, and ensure insights actually drive action.",
        "whatYouDo": "Define metrics and KPIs, align analyses with business goals, advise on strategy, prioritize analyses based on impact, drive adoption of data insights",
        "dayToDay": "Discussing strategy with leadership, defining what to measure, conducting analyses that inform decisions, translating between business and data",
        "skills": ["SQL", "Business acumen", "Strategic thinking", "Problem framing", "Stakeholder management", "Data storytelling"],
        "tools": ["SQL", "Excel", "Tableau/Power BI", "Python (light)", "BI tools"],
        "bestFor": "People who care about business impact, want to influence strategy, and are energized by understanding what decisions matter",
        "careerPath": ["Analyst (1-2 years) → Senior Analytics Manager (3-5 years) → Director of Analytics (5+ years) → VP of Analytics → Chief Analytics Officer"],
        "companies": "Fortune 500 companies across all industries, Private equity firms, Consulting firms (Accenture, Bain), Tech companies, E-commerce (Amazon, Shopify), Financial services",
        "challenges": ["Getting stakeholders to act on insights", "Defining metrics that actually matter", "Balancing multiple competing priorities", "Proving ROI of analytics investments", "Explaining complex data in simple terms"],
        "resources": ["'Lean Analytics' by Alistair Croll & Benjamin Yoskovitz", "Google Analytics IQ Certification (free)", "Coursera - Business Analytics", "Mode Analytics - Analytics Mindset", "Reforge - Analytics for Executives"],
        "jobKeywords": ["Strategic Analysis", "Business Metrics", "KPI Development", "Stakeholder Alignment", "Performance Analytics", "Growth Analysis", "Financial Analysis", "Competitive Analysis", "Market Analysis", "Decision Support", "Business Intelligence", "Reporting to C-suite", "Revenue Analytics", "Cost Analysis", "ROI Measurement"]
    },
    "communicator": {
        "title": "Analytics Communicator",
        "emoji": "📈",
        "description": "You're the translator who makes data accessible. You excel at crafting narratives, creating compelling visualizations, and helping people actually understand and act on insights.",
        "whatYouDo": "Create dashboards and reports, design data visualizations, build narratives around findings, present to executives, teach others to interpret data",
        "dayToDay": "Creating dashboards, designing visualizations, writing reports, presenting findings, iterating on clarity",
        "skills": ["Visualization", "Storytelling", "Communication", "SQL", "Design thinking", "Audience awareness"],
        "tools": ["Tableau", "Power BI", "Excel", "SQL", "Design tools", "Presentation tools"],
        "bestFor": "People who are energized by clarity, care deeply about how people interpret information, and love making complex things understandable",
        "careerPath": ["Analyst/Designer (1-2 years) → Senior Data Communicator (3-5 years) → Analytics Manager (5+ years) → Head of Data Communication → Chief Data Officer"],
        "companies": "Tech companies (Google, Apple, Microsoft), Design-focused firms (Figma, Adobe), Consulting (Mckinsey, BCG), Media/Publishing (Medium, Substack), BI platforms (Tableau, Looker)",
        "challenges": ["Making complex data understandable to diverse audiences", "Designing dashboards that people actually use", "Balancing aesthetics with accuracy", "Presenting to C-level executives", "Keeping data visualization best practices in mind"],
        "resources": ["'Storytelling with Data' by Cole Nussbaumer Knaflic", "Edward Tufte - 'The Visual Display of Quantitative Information'", "Tableau Public Gallery - Best practices", "Google Slides Design Tips", "Nielsen Norman Group - Data Visualization"],
        "jobKeywords": ["Data Visualization", "Dashboard Design", "Executive Reporting", "Data Storytelling", "Presentation Design", "Information Architecture", "Visual Communication", "Report Generation", "User Experience Design", "Tableau Expert", "Power BI Design", "Data-Driven Narratives", "Infographic Design", "Interactive Dashboards", "Audience Analysis"]
    }
}

# -------------------------------------------------
# SESSION STATE
# -------------------------------------------------
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
    st.session_state.scores = {role: 0 for role in roles}
    st.session_state.compare_mode = False
    st.session_state.share_mode = False

# -------------------------------------------------
# HEADER
# -------------------------------------------------
st.markdown("""
    <div class="header-title">
        <h1>📊 Data Career Navigator</h1>
        <p>An interactive assessment to explore where you fit in the data world.</p>
    </div>
""", unsafe_allow_html=True)

# -------------------------------------------------
# QUIZ LOGIC
# -------------------------------------------------
current = st.session_state.current_question
total = len(quiz)

if current < total:
    # QUIZ IN PROGRESS
    q = quiz[current]
    
    # Progress bar
    progress = (current / total) * 100
    st.markdown(f"""
        <div class="progress-section">
            <div class="progress-text">Question {current + 1} of {total}</div>
            <div class="progress-bar">
                <div class="progress-fill" style="width: {progress}%;"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Question
    st.markdown(f"""
        <div class="question-number">Question {current + 1}</div>
        <div class="question-text">{q['question']}</div>
    """, unsafe_allow_html=True)
    
    # Answer buttons
    for idx, ans in enumerate(q["answers"]):
        if st.button(ans["text"], key=f"q{current}_a{idx}", use_container_width=True):
            st.session_state.scores[ans["role"]] += 1
            st.session_state.current_question += 1
            st.rerun()

else:
    # RESULTS
    top_role = max(st.session_state.scores, key=st.session_state.scores.get)
    role_info = roles[top_role]
    total_score = sum(st.session_state.scores.values())
    
    # Title
    st.markdown(f"<h1 class='result-title'>{role_info['emoji']} {role_info['title']}</h1>", unsafe_allow_html=True)
    
    # Description
    st.markdown(f"<div class='result-description'>{role_info['description']}</div>", unsafe_allow_html=True)
    
    # Score breakdown
    st.markdown("<div class='section-title'>Your Score Breakdown</div>", unsafe_allow_html=True)
    
    sorted_scores = sorted(st.session_state.scores.items(), key=lambda x: x[1], reverse=True)
    
    for role_key, score in sorted_scores:
        percent = int((score / total_score) * 100) if total_score > 0 else 0
        role_title = roles[role_key]["title"]
        
        score_item_html = f"""
        <div class="score-item">
            <div class="score-label">{role_title}</div>
            <div class="score-bar-container">
                <div class="score-bar-fill" style="width: {percent}%;"></div>
            </div>
            <div class="score-percent">{percent}%</div>
        </div>
        """
        st.markdown(score_item_html, unsafe_allow_html=True)
    
    # What you'll do
    st.markdown("<div class='section-title'>What You'll Do</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='section-content'>{role_info['whatYouDo']}</div>", unsafe_allow_html=True)
    
    # Day to day
    st.markdown("<div class='section-title'>Day-to-Day Work</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='section-content'>{role_info['dayToDay']}</div>", unsafe_allow_html=True)
    
    # Skills
    st.markdown("<div class='section-title'>Key Skills</div>", unsafe_allow_html=True)
    skills_html = " ".join([f"<span class='tag'>{skill}</span>" for skill in role_info["skills"]])
    st.markdown(f"<div class='tags'>{skills_html}</div>", unsafe_allow_html=True)
    
    # Tools
    st.markdown("<div class='section-title'>Common Tools</div>", unsafe_allow_html=True)
    tools_html = " ".join([f"<span class='tag'>{tool}</span>" for tool in role_info["tools"]])
    st.markdown(f"<div class='tags'>{tools_html}</div>", unsafe_allow_html=True)
    
    # Best for
    st.markdown("<div class='section-title'>Best For</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='section-content'>{role_info['bestFor']}</div>", unsafe_allow_html=True)
    
    # Real-world challenges
    st.markdown("<div class='section-title'>Real-World Challenges You'll Face</div>", unsafe_allow_html=True)
    challenges_text = ", ".join(role_info['challenges']) if isinstance(role_info['challenges'], list) else role_info['challenges']
    st.markdown(f"<div class='section-content'>{challenges_text}</div>", unsafe_allow_html=True)
    
    # Beyond the Title - Job Keywords
    st.markdown("<div class='section-title'>🔍 Beyond the Title: What to Look For in Job Descriptions</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-content' style='font-size: 14px; color: #999; margin-bottom: 15px;'>When job hunting, look for these keywords and phrases in job postings that match this role:</div>", unsafe_allow_html=True)
    keywords_html = " ".join([f"<span class='tag'>{keyword}</span>" for keyword in role_info['jobKeywords']])
    st.markdown(f"<div class='tags'>{keywords_html}</div>", unsafe_allow_html=True)
    
    # Learning resources with links
    st.markdown("<div class='section-title'>Learning Resources & Certifications</div>", unsafe_allow_html=True)
    
    resources_with_links = {
        "engineer": {
            "Apache Spark & PySpark Documentation": "https://spark.apache.org/docs/latest/",
            "dbt Fundamentals Course (free)": "https://courses.getdbt.com/courses/fundamentals",
            "DataCamp - Data Engineering Track": "https://www.datacamp.com/courses/data-engineering",
            "Cloud certifications (AWS Solutions Architect, GCP Associate)": "https://aws.amazon.com/certification/"
        },
        "analyst": {
            "Mode Analytics - SQL Tutorial (free)": "https://mode.com/sql-tutorial/",
            "Tableau Public - Gallery & Learning": "https://public.tableau.com/",
            "Google Analytics Academy (free certification)": "https://analytics.google.com/analytics/academy/",
            "DataCamp - Data Analysis with Python": "https://www.datacamp.com/courses/data-analysis-in-python",
            "Coursera - Business Analytics Specialization": "https://www.coursera.org/specializations/business-analytics"
        },
        "scientist": {
            "Andrew Ng - Machine Learning Specialization (Coursera)": "https://www.coursera.org/specializations/machine-learning-introduction",
            "Fast.ai - Practical Deep Learning": "https://www.fast.ai/",
            "Kaggle - Competitions & Datasets": "https://www.kaggle.com/",
            "Stanford CS229 - Machine Learning (free lectures)": "http://cs229.stanford.edu/",
            "Papers with Code - Latest research implementations": "https://paperswithcode.com/"
        },
        "business_partner": {
            "'Lean Analytics' by Alistair Croll & Benjamin Yoskovitz": "https://www.oreilly.com/library/view/lean-analytics/9781449368661/",
            "Google Analytics IQ Certification (free)": "https://analytics.google.com/analytics/academy/",
            "Coursera - Business Analytics": "https://www.coursera.org/specializations/business-analytics",
            "Mode Analytics - Analytics Mindset": "https://mode.com/analytics-mindset/",
            "Reforge - Analytics for Executives": "https://www.reforge.com/courses"
        },
        "communicator": {
            "'Storytelling with Data' by Cole Nussbaumer Knaflic": "https://www.storytellingwithdata.com/",
            "Edward Tufte - 'The Visual Display of Quantitative Information'": "https://www.edwardtufte.com/tufte/books_vdqi",
            "Tableau Public Gallery - Best practices": "https://public.tableau.com/",
            "Google Slides Design Tips": "https://support.google.com/docs/answer/1696717",
            "Nielsen Norman Group - Data Visualization": "https://www.nngroup.com/articles/data-visualization/"
        }
    }
    
    role_resources = resources_with_links.get(top_role, {})
    resources_html = ""
    for resource, url in role_resources.items():
        resources_html += f"<a href='{url}' target='_blank' style='display: inline-block; background: white; border: 1px solid #ddd; color: #667eea; padding: 8px 16px; border-radius: 20px; font-size: 14px; margin-bottom: 8px; margin-right: 8px; text-decoration: none;'>{resource}</a>"
    
    st.markdown(f"<div style='display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 20px;'>{resources_html}</div>", unsafe_allow_html=True)
    
    # Action buttons section
    st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📊 Compare Roles", use_container_width=True):
            st.session_state.compare_mode = True
            st.session_state.compare_role = None
            st.rerun()
    
    with col2:
        if st.button("📤 Share Result", use_container_width=True):
            st.session_state.share_mode = True
            st.rerun()
    
    st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
    if st.button("🔄 Retake Quiz", use_container_width=True):
        st.session_state.current_question = 0
        st.session_state.scores = {role: 0 for role in roles}
        st.session_state.compare_mode = False
        st.session_state.share_mode = False
        st.rerun()

# -------------------------------------------------
# COMPARE ROLES MODE
# -------------------------------------------------
if "compare_mode" in st.session_state and st.session_state.compare_mode:
    top_role = max(st.session_state.scores, key=st.session_state.scores.get)
    top_role_info = roles[top_role]
    
    st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>📊 Compare Roles</div>", unsafe_allow_html=True)
    
    # Role selection
    available_roles = [r for r in roles.keys() if r != top_role]
    compare_role = st.selectbox(
        "Select a role to compare with " + top_role_info['title'],
        available_roles,
        format_func=lambda x: roles[x]['title']
    )
    
    if compare_role:
        compare_role_info = roles[compare_role]
        
        # Comparison sections
        comparison_data = {
            "What You'll Do": {
                top_role: top_role_info['whatYouDo'],
                compare_role: compare_role_info['whatYouDo']
            },
            "Day-to-Day Work": {
                top_role: top_role_info['dayToDay'],
                compare_role: compare_role_info['dayToDay']
            },
            "Skills": {
                top_role: top_role_info['skills'],
                compare_role: compare_role_info['skills']
            },
            "Tools": {
                top_role: top_role_info['tools'],
                compare_role: compare_role_info['tools']
            },
            "Real-World Challenges": {
                top_role: top_role_info['challenges'],
                compare_role: compare_role_info['challenges']
            }
        }
        
        for section_title, section_data in comparison_data.items():
            st.markdown(f"<div class='section-title'>{section_title}</div>", unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"<div style='font-weight: 600; color: #667eea; margin-bottom: 8px;'>{top_role_info['emoji']} {top_role_info['title']}</div>", unsafe_allow_html=True)
                
                if isinstance(section_data[top_role], list):
                    content = ", ".join(section_data[top_role])
                else:
                    content = section_data[top_role]
                st.markdown(f"<div class='section-content'>{content}</div>", unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"<div style='font-weight: 600; color: #667eea; margin-bottom: 8px;'>{compare_role_info['emoji']} {compare_role_info['title']}</div>", unsafe_allow_html=True)
                
                if isinstance(section_data[compare_role], list):
                    content = ", ".join(section_data[compare_role])
                else:
                    content = section_data[compare_role]
                st.markdown(f"<div class='section-content'>{content}</div>", unsafe_allow_html=True)
        
        # Back button
        st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)
        if st.button("← Back to Results", use_container_width=True):
            st.session_state.compare_mode = False
            st.rerun()

# -------------------------------------------------
# SHARE MODE
# -------------------------------------------------
if "share_mode" in st.session_state and st.session_state.share_mode:
    top_role = max(st.session_state.scores, key=st.session_state.scores.get)
    top_role_info = roles[top_role]
    
    st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>📤 Share Your Result</div>", unsafe_allow_html=True)
    
    share_text = f"I took the Data Career Quiz and got: {top_role_info['emoji']} {top_role_info['title']}! Find out which data career path fits you best at: [quiz-link]"
    
    # Share options
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <a href="https://twitter.com/intent/tweet?text={share_text.replace(' ', '%20').replace('!', '%21').replace(':', '%3A')}" target="_blank" style='display: block; text-align: center; padding: 12px; background: #1DA1F2; color: white; border-radius: 8px; text-decoration: none; font-weight: 600;'>𝕏 Twitter</a>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <a href="https://www.linkedin.com/sharing/share-offsite/?url=[quiz-link]" target="_blank" style='display: block; text-align: center; padding: 12px; background: #0A66C2; color: white; border-radius: 8px; text-decoration: none; font-weight: 600;'>💼 LinkedIn</a>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <a href="mailto:?subject=Check%20Out%20My%20Data%20Career%20Quiz%20Result&body={share_text}" target="_blank" style='display: block; text-align: center; padding: 12px; background: #667eea; color: white; border-radius: 8px; text-decoration: none; font-weight: 600;'>✉️ Email</a>
        """, unsafe_allow_html=True)
    
    # Copy to clipboard
    st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Or Copy This Text</div>", unsafe_allow_html=True)
    st.text_area("Share text:", value=share_text, height=80, disabled=True)
    
    # Back button
    st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
    if st.button("← Back to Results", use_container_width=True):
        st.session_state.share_mode = False
        st.rerun()

# ============================
# Footer
# ============================
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #a0aec0; margin-top: 2rem;">
    <p style="font-size: 0.85rem; color: #718096;">
        Built by Evelyn | 
        <a href="https://evelyntc.streamlit.app" target="_blank" style="color:#ff4b4b; text-decoration:none;">
            View Full Portfolio
        </a>
    </p>
</div>
""", unsafe_allow_html=True)