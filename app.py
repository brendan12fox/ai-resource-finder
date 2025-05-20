# -*- coding: utf-8 -*-
import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("AI Resource Finder")

zip_code = st.text_input("Enter ZIP Code")
need = st.text_input("What is the patient's need?", placeholder="e.g. food, housing, legal help")

if st.button("Search"):
    with st.spinner("Searching..."):
        prompt = f"""
        Provide 3-5 real, local services in ZIP code {zip_code} that can help with the following need: {need}.
        For each service, include:
        - Name
        - One-sentence description
        - Address with ZIP code
        - Phone number
        - Website (if available)
        Only return clean, specific, local services. No national hotlines.
        Format as bullet points.
        """

        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You help clinicians find local social resources."},
                    {"role": "user", "content": prompt}
                ]
            )
            st.markdown(response.choices[0].message.content)
        except Exception as e:
            st.error(f"Error: {e}")

