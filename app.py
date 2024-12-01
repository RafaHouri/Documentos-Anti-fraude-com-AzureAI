import streamlit as st
from services.blob_services import upload_blob
from services.credit_card_services import analyze_credit_card


def configure_interface():
    st.title("Upload de Arquivos DIO - Desafio 1 - Azure - Fake Docs")
uploaded_file = st.file_uploader("Escolha um arquivo", type=["jpg", "png", "jpeg"])


if uploaded_file is not None:
  fileName = uploaded_file.name
  blob_url = upload_blob(uploaded_file, fileName)
  if blob_url:
     st.write(f"Arquivo {fileName} enviado com sucesso para o Azure Blob Storge")
     credit_card_info = analyze_credit_card(blob_url)
     show_image_and_validation(blob_url, credit_card_info)
  else:
    st.write(f"Erro ao enviar o {fileName} para o Azure Blob Storge")


def show_image_and_validation(blob_url, credit_card_info):    
  st.image(blob_url, caption="Imagem enviada", use_column_width=True)
  st.write("Informações de cartão encontradas:")
  st.write(credit_card_info)
if credit_card_info and credit_card_info["card_name"]:
  st.markdown(f"<h1 style='color:green;'>Cartão válido</h1>", unsafe_allow_html=True)
  st.write(f"Nome do Titular: {credit_card_info['card name']}")
  st.write(f"Banco Emissor: {credit_card_info['bank name']}")
  st.write(f"Data de Validade: {credit_card_info['expity date']}")
else:
  st.markdown(f"<h1 style='color:red;'>Cartão inválido</h1>" , unsafe_allow_html=True)
  st.write("Cartão Inválido")

  if __name__ == "__main__":  
    configure_interface()
    

        
