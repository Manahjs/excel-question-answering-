# -*- coding: utf-8 -*-
"""extract answer from pdf.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AzQJLlbNXsupLIid8meFHX6_w0W1M2mz
"""

!pip install streamlit pandas openpyxl transformers

pip install streamlit

!pip install pymupdf
# !pip install streamlit
# import streamlit as st
# import fitz  # PyMuPDF
# from transformers import pipeline
# from transformers import pipeline

# import pandas as pd

# def read_excel(file):
#     # Open the Excel file and read its content
#     excel_data = pd.read_excel(file)
#     text = ""  # Initialize an empty string to store text
#     for index, row in excel_data.iterrows():
#         # Convert each row into a string and append it to the text
#         text += " ".join(map(str, row.values)) + "\n"
#     return text

# def main():
#     st.title("EXCEL Question-Answering App")
#     st.sidebar.header("User Input")

#     # Upload Excel file
#     uploaded_file = st.sidebar.file_uploader("/content/vehical_owner.xlsx", type=["xlsx", "xls"])

#     if uploaded_file:
#         st.sidebar.subheader("Excel Preview")
#         excel_text = read_excel(uploaded_file)
#         st.sidebar.text(excel_text[:5000])  # Display a snippet of the Excel text

#         # User input for question
#         user_question = st.text_input("Ask a question about the Excel content:")

#         if st.button("Get Answer"):
#             if user_question:
#                 # Use a pre-trained question-answering model (DistilBERT in this case)
#                 question_answering = pipeline("question-answering")
#                 answer = question_answering(question=user_question, context=excel_text)

#                 st.subheader("Answer:")
#                 st.write(answer['answer'])
#             else:
#                 st.warning("Please enter a question.")

# if __name__ == "__main__":
#     main()

!wget  -q -O - ipv4.icanhazip.com

! streamlit run app.py & npx localtunnel --port 8501