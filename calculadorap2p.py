import streamlit as st

st.set_page_config(page_title="Calculadora P2P", page_icon="💰", layout="centered")

# CSS para reducir el tamaño de los números en los widgets 'metric'
st.markdown("""
    <style>
    [data-testid="stMetricValue"] {
        font-size: 20px !important;
    }
    .block-container { padding-top: 1rem; padding-bottom: 1rem; }
    </style>
""", unsafe_allow_html=True)

st.title("💰 Calculadora P2P")

niveles = {"Sin verif.": 0.0, "Bronce": 0.20, "Plata": 0.30, "Oro": 0.50}

nivel = st.radio("Nivel Binance", list(niveles.keys()), horizontal=True)
cantidad_usdt = st.number_input("Cantidad USDT a vender", value=1000.000, format="%.3f")
tasa_venta = st.number_input("Tasa Venta (VES x USDT)", value=833.000, format="%.3f")
tasa_compra = st.number_input("Tasa Recompra (VES x USDT)", value=812.123, format="%.3f")

descuento = niveles[nivel]
comision_final = 0.0025 * (1 - descuento)

if cantidad_usdt > 0 and tasa_venta > 0 and tasa_compra > 0:
    monto_bruto = cantidad_usdt * tasa_venta
    recibes_neto = monto_bruto * (1 - comision_final)
    usdt_final = recibes_neto / tasa_compra
    ganancia = usdt_final - cantidad_usdt

    st.divider()
    
    st.subheader("⬇️ Etapa: Venta (USDT a VES)")
    c1, c2 = st.columns(2)
    c1.metric("Monto Bruto", f"{monto_bruto:,.3f} VES")
    c2.metric("Recibes (Neto)", f"{recibes_neto:,.3f} VES")
    
    st.subheader("⬆️ Etapa: Recompra (VES a USDT)")
    c3, c4 = st.columns(2)
    c3.metric("Usas para comprar", f"{recibes_neto:,.3f} VES")
    c4.metric("USDT obtenidos", f"{usdt_final:,.3f} USDT")
    
    st.divider()
    
    if ganancia > 0:
        st.success(f"### Ganancia Neta: +{ganancia:,.3f} USDT")
    else:
        st.error(f"### Ganancia Neta: {ganancia:,.3f} USDT")
    
    st.caption(f"Comisión aplicada: {comision_final*100:.3f}%")
else:
    st.warning("Completa los valores para calcular.")
