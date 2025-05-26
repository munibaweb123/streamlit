import streamlit as st

# commands that are called without explicit need of st.write() function
def magic():
    "Welcome to streamlit"
    """
    # Good day
    ## sub heading
    ### this is __magic__
    """
    st.code("""
    import pandas as pd
    pd.dataftame({"col1":[1,2,3],"col2":['a','b','c']})
    """)
    import pandas as pd
    df = pd.DataFrame({"col1":[1,2,3],"col2":['a','b','c']})
    df

    import pandas as pd
    df : pd.DataFrame = pd.DataFrame({'col1':[10,20,30], 'col2':['apple','mango','banana'],'col3':list('abc')})
    df # 👈 Draw the dataframe

    z:int = 100
    'z=',z # 👈 Draw the string 'z' then the value of z

    # Also work with most supported chart types
    import matplotlib.pyplot as plt
    import numpy as np
    arr = np.random.normal(1,1,size=50)
    fig,ax = plt.subplots()
    ax.hist(arr, bins=10)

    fig # 👈 Draw the matplotlib chart

    # You can just plot using matplotlib or seaborn, and Streamlit will render it automatically.
    # plot without st.plot()

    
   

    st.title("📈 Sine Wave Graph")

    # generate data
    x = np.linspace(0, 10, 100) # start, stop , num to generate
    y = np.sin(x)

    # make graph
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title("Sine Wave")

    # show graph
    fig# Magic rendering of matplotlib figure


    # 3. Display Variables Automatically
    user_name = "Muniba"
    user_name  # Gets displayed as-is

    # 4. Multiple Return Values
    def person_info(name,course):
        return name,course

    info = person_info("Muniba","GIAIC")
    info

    # 5. Read text file
    with open("python.txt", "r") as file:
        text_file_content = file.read()
    text_file_content

    # 6. upload file
    from docx import Document
    # pip install python-docx

    st.title("📄 Word (.docx) File Reader")

    uploaded_file = st.file_uploader("Upload a .docx file", type="docx")

    if uploaded_file is not None:
        doc = Document(uploaded_file)

        st.subheader("📃 File Content:")
        for para in doc.paragraphs:
            if para.text.strip():  # Empty lines skip
                para.text
magic()