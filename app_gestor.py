import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

# layout
st.set_page_config(
    page_title = 'Gestor 360',
    page_icon = "📊",
    initial_sidebar_state = 'expanded',
)

# Título aplicativo
st.title('📊 GESTOR 360 - Relatórios Dinâmicos')
st.markdown('<br>', unsafe_allow_html=True)

# Carregar planilha
st.sidebar.title('Envie seus dados 📁')
uploaded_file = st.sidebar.file_uploader('Escolha um arquivo Excel ou CSV', type=['csv', 'xlsx'])

# Processar arquivo enviado
if uploaded_file:
    try:
        if uploaded_file.name.endswith('.csv'):
            data = pd.read_csv(uploaded_file)
        else:
            data = pd.read_excel(uploaded_file)
        
        st.success('Dados carregados com sucesso')
        st.write('Visualização inicial dos dados')
        st.dataframe(data.head())
        
        # Selecionar colunas para análise
        product_line = data['Product line']
        total_sales = data['Total Sales']
        gross_margin = data['Gross Margin Percentage']
        
        # Gráfico de vendas por produto
        fig1 = px.bar(data, x='Product line', y='Total Sales', title='Total de vendas por Produto', color='Product line')   
        st.plotly_chart(fig1, use_container_width=True)
        
        # Gráfico de margem bruta
        fig2 = px.bar(data, x='Product line', y='Gross Margin Percentage', title='Margem Bruta por Produto', color='Product line')
        st.plotly_chart(fig2, use_container_width=True)
        
        # Gráfico de distribuição de métodos de pagamento
        fig3 = px.pie(data, names='Product line', values='Total Sales', title='Distribuição de Pagamentos')
        st.plotly_chart(fig3, use_container_width=True)
    
    except Exception as e:
        st.error(f'Erro ao carregado o arquivo: {e}')
else:
    st.info('Envie um arquivo para começar.')


st.sidebar.markdown('---')
st.sidebar.write('Desenvolvido com 💻 por **Gestor360**."')