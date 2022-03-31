import streamlit as st
import yaml

def data_page():
    with open(r'C:\Users\skurt\PycharmProjects\StreamlitProject\venv\share\configuration.yaml') as file:
        dictionary = yaml.safe_load(file)

    st.header('Data')
    st.write('\n')

    data_platform_dict = dictionary['data']['data_platform']
    data_platform = st.selectbox('Data_platform:',
                                 (data_platform_dict, "local", "sql", "azure_ml", "azure_datalake", "docker"))
    dictionary['data']['data_platform'] = data_platform

    account_name_dict = dictionary['data']['account_name']
    account_name = st.text_input('Account_name:', account_name_dict)
    dictionary['data']['account_name'] = account_name

    production_dict = dictionary['data']['production']
    if production_dict == True:
        production = st.radio('Locally:', (production_dict, False))
        dictionary['data']['production'] = production
    elif production_dict == False:
        production = st.radio('Locally:', (production_dict, True))
        dictionary['data']['production'] = production

    sales_quantity_dict = dictionary['data']['aggregations']['sales_quantity']
    sales_quantity = st.selectbox('Select_sales_quantity:', (sales_quantity_dict, 'sum', 'main', 'std','max','median'))
    dictionary['data']['aggregations']['sales_quantity'] = sales_quantity

    submit = st.button('Submit')

    def write_to_file():
        with open(r'C:\Users\skurt\PycharmProjects\StreamlitProject\venv\share\configuration.yaml','w') as file:
            documents = yaml.dump(dictionary, file, sort_keys=False, default_flow_style=False,allow_unicode = True, encoding = None)

    if submit:
       write_to_file()
