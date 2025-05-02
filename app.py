import streamlit as st
from PIL import Image

st.title("Hola Mundo")

st.header("Bienvenidos a mi primera app!!")
st. write("Bien puedan")
image = Image.open('conejito.jpg')

st.image(image, caption='Lindo conejito')


texto = st.text_input('Dime algo curioso:', '¿Ya escuchaste la del gato y el zapato?')
st.write('Tú dijiste:', texto)

st.subheader("Amo los conejitos")

col1, col2 = st.columns(2)

with col1:
  st.subheader("Razón 1: Son muy lindos")
  st.write("¿No?")
  resp = st.checkbox('deacuerdo')
  if resp: 
    st.write("SIZAAAA")

with col2:
  st.subheader("Razón 2: Son muy:")
  modo = st.radio("digame", ('cariñosos', 'suaves', 'tiernos'))
  if modo == 'cariñosos':
    st.write('totalmente')
  if modo == 'suaves':
    st.write('parecen una nube')
  if modo == 'tiernos':
    st.write('confirmo')

st.subheader("Oprime para acariciar el conejito")
if st.button("caricias y amor"):
  st.write("WIIIII")
else:
  st.write("WIIIIII")

st.subheader("Elige el nombre de tu conejito")
in_mod = st.selectbox(
  "Que sea bonito", 
  ("Nube", "Algodoncito", "Piojito"),
)
if in_mod == "Nube":
  set_mod = "Muy cursi"
elif in_mod == "Algodoncito":
  set_mod = "Muy mañe"
elif in_mod == "Piojito":
  set_mod = "ESE FUE"
st.write("Dejame pienso,", set_mod)
