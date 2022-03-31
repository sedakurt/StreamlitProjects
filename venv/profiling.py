import streamlit as st
import yaml
import datetime

def profiling():
    with open(r'C:\Users\skurt\PycharmProjects\StreamlitProject\venv\share\configuration.yaml') as file:
        dictionary = yaml.safe_load(file)

    st.header('Profiling:')
    st.write('\n')

    profiling_group_cols_dict = dictionary['profiling']['profiling_group_cols']
    profiling_group_cols = st.text_input('Profiling_group_cols:', profiling_group_cols_dict)
    dictionary['profiling']['profiling_group_cols'] = profiling_group_cols

    sales_profiling_gap_dict = dictionary['profiling']['sales_profiling_gap']
    sales_profiling_gap = st.text_input('Sales_profiling_gap:', sales_profiling_gap_dict)
    dictionary['profiling']['sales_profiling_gap'] = sales_profiling_gap

    profiling_month_dict = dictionary['profiling']['profiling_month']
    profiling_month = st.number_input('Profiling_month:', 1, 24, profiling_month_dict, 1)
    dictionary['profiling']['profiling_month'] = profiling_month

    date_start_dict = dictionary['profiling']['clustering']['date_start']
    date_start = st.date_input('Date_start:', value=date_start_dict, min_value=datetime.date(2012, 1, 1),
                               max_value=datetime.date(2029, 1, 1))
    dictionary['profiling']['clustering']['date_start'] = date_start

    submit = st.button('Submit')

    def write_to_file():
        with open(r'C:\Users\skurt\PycharmProjects\StreamlitProject\venv\share\configuration.yaml','w') as file:
            documents = yaml.dump(dictionary, file, sort_keys=False, default_flow_style=False,allow_unicode = True, encoding = None)

    if submit:
       write_to_file()
