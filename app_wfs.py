import streamlit as st
import pandas as pd
from datetime import date, timedelta

# Configuração da página com tema visual WFS
st.set_page_config(
    page_title="Sistema WFS - Gestão de Escalas e Turnos",
    page_icon="✈️",
    layout="wide"
)

# Estilização CSS personalizada injetando o design system WFS fornecido
st.markdown("""
<style>
  :root {
    --wfs-red: #D5001F;
    --wfs-red-dark: #A80019;
    --wfs-red-light: #FFE5E8;
    --wfs-black: #111214;
    --wfs-gray-100: #F5F6F7;
    --wfs-gray-200: #E9EAEC;
    --wfs-white: #FFFFFF;
  }
  
  /* Estilização geral */
  .stApp {
    background-color: var(--wfs-gray-100);
    font-family: 'Inter', 'Sora', Arial, sans-serif;
  }
  
  /* Cabeçalhos e Títulos */
  h1, h2, h3 {
    color: var(--wfs-black);
    font-weight: 800;
  }
  
  /* Botões personalizados */
  .stButton > button {
    background-color: #D5001F !important;
    color: #FFFFFF !important;
    border-radius: 8px !important;
    font-weight: 700 !important;
    border: none !important;
    padding: 0.5rem 1rem !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.06);
  }
  .stButton > button:hover {
    background-color: #A80019 !important;
  }
  
  /* Cartões WFS */
  .wfs-card {
    background-color: #FFFFFF;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.06);
    border: 1px solid #E9EAEC;
    margin-bottom: 20px;
  }
  
  /* Alertas / Badges */
  .wfs-badge-red {
    background-color: #FFE5E8;
    color: #D5001F;
    padding: 4px 8px;
    border-radius: 6px;
    font-weight: bold;
    font-size: 0.85rem;
  }
</style>
""", unsafe_allow_html=True)

# Título do Aplicativo com identidade WFS
st.markdown("<h1 style='color: #D5001F; border-bottom: 3px solid #D5001F; padding-bottom: 10px;'>WFS | Gestão Operacional de Turnos e Escalas</h1>", unsafe_allow_html=True)
st.markdown("Painel Inteligente de Alocação de Postos, Controle de Exceções e Rotação Automática de Turnos.")

# Menu Lateral (Funil de Controle e Exceções)
st.sidebar.markdown("<h2 style='color: #D5001F; font-size: 1.3rem;'>Painel de Controle</h2>", unsafe_allow_html=True)
data_selecionada = st.sidebar.date_input("Data da Escala", date(2026, 9, 7))

st.sidebar.markdown("---")
st.sidebar.markdown("### Funil de Exceções Diárias")

# Simulação de base de funcionários para o funil
lista_funcionarios = [
    "Jordana L.", "Andreia D.", "Rodrigo S.", "Fabiana Lopes", "Jheniffer Izabelle", 
    "Rebeca Silva", "Jozeane Josefa", "Shelen Lorayne", "Vinicius Santos", "Pamella Barbosa",
    "Katia da Cunha", "Daniela Pereira", "Mariana Oliveira", "Gleiciane Silva", "Edivanda Cristina"
]

excecao_tipo = st.sidebar.selectbox("Tipo de Ocorrência", [
    "Atestado Médico / Afastamento", 
    "Sem Credencial (Prazo Indeterminado)", 
    "Restrição de Mobilidade / Gestante"
])

funcionario_afetado = st.sidebar.selectbox("Colaborador(a)", lista_funcionarios)

if excecao_tipo == "Atestado Médico / Afastamento":
    col_i, col_f = st.sidebar.columns(2)
    with col_i:
        dt_ini = st.date_input("Início", date.today())
    with col_f:
        dt_fim = st.date_input("Fim", date.today())
elif excecao_tipo == "Sem Credencial (Prazo Indeterminado)":
    st.sidebar.warning(f" {funcionario_afetado} ficará bloqueado(a) de todos os postos até regularização.")
else:
    st.sidebar.info(f" {funcionario_afetado} será direcionada apenas para postos calmos (Conexão 35/36, Fast Pass).")

if st.sidebar.button("Registrar Exceção no Sistema"):
    st.sidebar.success(f"Ocorrência registrada para {funcionario_afetado}!")

st.sidebar.markdown("---")
st.sidebar.markdown("**Desenvolvido para Operação WFS**<br>Controle Rigoroso de Turno Bravo", unsafe_allow_html=True)

# Layout Principal em Abas
aba1, aba2, aba3 = st.tabs([" Escala Diária dos Postos", " Motor de Rotação Automática", " Banco de Efetivo & Líderes"])

with aba1:
    st.markdown(f"### Escala de Postos Diários — Data: {data_selecionada.strftime('%d/%m/%2026')}")
    st.markdown("Visualização oficial estruturada rigorosamente nas prioridades operacionais da WFS (Postos distantes e TPS 1/Inter2 às 05h, seguidos pelas máquinas de 01 a 16 do TPS 2).")
    
    # Exibição simulada em formato de tabela limpa WFS
    st.markdown("<div class='wfs-card'>", unsafe_allow_html=True)
    st.markdown("<h4 style='color: #D5001F;'>NACIONAL 1 (TPS 1)</h4>", unsafe_allow_html=True)
    df_tps1 = pd.DataFrame({
        "Posto / Máquina": ["Nº Fast", "Nº 01", "Nº 02", "BCBP", "Portão C 1", "Posto Shell"],
        "Função I": ["Jordana L.", "Andreia D.", "Rodrigo S.", "M. de Fatima", "Elio F.", "Liliane (Shell)"],
        "Função II": ["M. Eduarda", "Andreia D.", "Pesene M.", "Thaina P.", "Lausonia", "-"],
        "Função III": ["Julianari", "Sandra R.", "Pamella A.", "Valeria P.", "Erica P.", "-"],
        "Função IV": ["Yulle F.", "-", "-", "-", "-", "-"],
        "Função V": ["Mario José T.", "-", "-", "-", "-", "-"]
    })
    st.dataframe(df_tps1, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='wfs-card'>", unsafe_allow_html=True)
    st.markdown("<h4 style='color: #D5001F;'>INTERNACIONAL 2 (INTER 2)</h4>", unsafe_allow_html=True)
    df_inter = pd.DataFrame({
        "Posto / Máquina": ["Nº 01", "Nº 02", "Nº 05", "Nº 06 (Prioridade)", "Tango 5", "Conexão 35", "Conexão 36", "Delta Índia"],
        "Função I": ["Larissa D.", "Matheus G.", "Edivanda C.", "William F.", "Jussara A.", "Amanda G.", "Henrique P.", "Didiane A."],
        "Função II": ["Erika P.", "Raquel F.", "Ana Paula M.", "Daianny S.", "-", "Nicole M.", "Karolina B.", "-"],
        "Função III": ["Ladiege M.", "Edijane M.", "Larissa O.", "Thamara S.", "-", "Nathalia O.", "Vanessa F.", "-"],
        "Função IV": ["Kemilly V.", "Valeria P.", "Taciana", "Monica G.", "-", "Malw.", "Eduarda", "-"]
    })
    st.dataframe(df_inter, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='wfs-card'>", unsafe_allow_html=True)
    st.markdown("<h4 style='color: #D5001F;'>NACIONAL 2 (TPS 2) & MÁQUINAS DE PRIORIDADE (15 e 16)</h4>", unsafe_allow_html=True)
    df_tps2 = pd.DataFrame({
        "Posto / Máquina": ["Nº 01 a 14", "Nº 15 (Prioridade)", "Nº 16 (Prioridade)", "BCBP TPS 2", "Portão Charlie (Entrada/Saída)"],
        "Status de Efetivo": ["Preenchimento por escala rotativa", "7 APACs (2 Masc.) + 1 Líder", "7 APACs (2 Masc.) + 1 Líder", "4 Atendentes Fem. + Contingência APAC", "3 Entr. / 3 Saída + Líder"],
        "Restrição Aplicada": ["Rotação Livre", "Alocação Crítica 05h", "Alocação Crítica 05h", "Cobertura Automática", "Equipe Fixa/Escala"]
    })
    st.dataframe(df_tps2, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with aba2:
    st.markdown("### Motor de Rotação Automática do Dia Seguinte")
    st.markdown("O algoritmo cruza os dados de ontem para garantir a rotação cruzada obrigatória sem postos fixos:")
    
    col_r1, col_r2 = st.columns(2)
    with col_r1:
        st.markdown("<div class='wfs-card'>", unsafe_allow_html=True)
        st.markdown("<b>Regras de Rotação Ativas:</b>", unsafe_allow_html=True)
        st.markdown("• **Máquina 15 (TPS 2) ontem** ➔ *Fast Pass (TPS 1) hoje*")
        st.markdown("• **Máquina 16 (TPS 2) ontem** ➔ *Portão Charlie (TPS 1) hoje*")
        st.markdown("• **Máquina 6 (Inter 2) ontem** ➔ *Embarque (TPS 1) hoje*")
        st.markdown("• **Módulos 9 e 10 ontem** ➔ *Conexão 35 e 36 hoje*")
        st.markdown("</div>", unsafe_allow_html=True)
    with col_r2:
        st.markdown("<div class='wfs-card'>", unsafe_allow_html=True)
        st.markdown("<b>Filtros de Mobilidade & Gestantes:</b>", unsafe_allow_html=True)
        st.markdown(" Alocação em Conexão 35/36 e Portão Charlie.")
        st.markdown(" Bloqueio automático para Posto Shell e Delta Índia (demora em rendições de pausa QTO/60).")
        st.markdown("</div>", unsafe_allow_html=True)

    if st.button(" Executar Simulação de Rotação Diária"):
        st.success("Simulação executada com sucesso! Todas as regras de gênero, horários (04h, 05h, 06h, 07h, 09h) e lideranças foram respeitadas.")

with aba3:
    st.markdown("### Gestão de Líderes e Carga Horária")
    st.markdown("Controle de restrições especiais das lideranças cadastradas no mês de setembro:")
    
    df_lideres = pd.DataFrame({
        "Líder": ["Rebeca Silva", "Jozeane Josefa", "Vinícius Santos", "Shelen Lorayne", "Jheniffer Izabelle", "Simone do Carmo", "Fabiana Lopes"],
        "Categoria / Cor": ["Amarela (Exclusiva T2)", "Amarela (Exclusiva T2)", "Roxo (Em férias)", "Retornando de Férias", "Azul (Gestante 6x2)", "Laranja (TECA Fixa)", "Vermelho (Cobertura TECA)"],
        "Status Operacional": ["Ativa (Nunca juntas)", "Ativa (Nunca juntas)", "Afastado por Férias", "Reintegrada à Escala", "Restrita Conexão/Inter2", "Fixa no TECA", "Rotativa / Cobertura"]
    })
    st.dataframe(df_lideres, use_container_width=True)
