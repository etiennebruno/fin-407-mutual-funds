import streamlit as st
from utils import *
from textblob import TextBlob
from termcolor import colored

PAGES = ['The pitfalls of benchmark extraction', 'benchmark sliding window']


def main():
    if 'count' not in st.session_state:
        st.session_state.count = 0

    def increment_counter():
        st.session_state.count += 1

    def decrease_counter():
        st.session_state.count -= 1

    st.title('Mutual fund deviations from their benchmarks')
    page = st.sidebar.selectbox('Select page:', PAGES)
    st.header(page)

    b1 = load_pkl('data/find_benchmark_1.pkl')[:20].to_markdown()

    df = df_from_filings()
    df = df.head(100)

    if page == PAGES[0]:
        l, r = st.columns(2)
        with l:
            st.button('previous report', on_click=decrease_counter)
        with r:
            st.button('next report', on_click=increment_counter)
        row = df.iloc[[st.session_state.count]]
        st.dataframe(row)

        benchmark_sentences = list(
            filter(lambda sentence: 'benchmark' in sentence.lower(),
                   TextBlob(row.text[st.session_state.count]).sentences))

        for b in benchmark_sentences:
            st.markdown(b.replace('benchmark', '<span style="color:red">**benchmark**</span>'), unsafe_allow_html=True)
    elif page == PAGES[1]:
        st.markdown(b1)
        # st.dataframe(b1[['potential_benchmark_occurrences']])
        pass


if __name__ == '__main__':
    main()
