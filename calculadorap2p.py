
import streamlit as st

st.set_page_config(page_title="Calculadora P2P", page_icon="💰", layout="centered")

st.markdown("""
    <style>
    .block-container { padding-top: 1rem; padding-bottom: 1rem; }
    [data-testid="stMetricValue"] { font-size: 18px; }
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
    # Cálculos
    bruto_venta = cantidad_usdt * tasa_venta
    neto_venta = bruto_venta * (1 - comision_final)
    
    bruto_recompra_usdt = neto_venta / tasa_compra
    neto_recompra_usdt = bruto_recompra_usdt * (1 - comision_final)
    
    ganancia = neto_recompra_usdt - cantidad_usdt

    st.divider()
    
    # Sección Venta
    st.subheader("⬇️ Venta (USDT a VES)")
    c1, c2 = st.columns(2)
    c1.metric("Bruto (Sin com.)", f"{bruto_venta:,.2f}")
    c2.metric("VES tras comisiones", f"{neto_venta:,.2f}")
    
    # Sección Recompra
    st.subheader("⬆️ Recompra (VES a USDT)")
    c3, c4 = st.columns(2)
    c3.metric("VES para recompra", f"{neto_venta:,.2f}")
    c4.metric("USDT final neto", f"{neto_recompra_usdt:,.3f}")
    
    st.divider()
    
    st.success(f"### Ganancia Neta: {'+' if ganancia > 0 else ''}{ganancia:,.3f} USDT")
    st.caption(f"Comisión aplicada: {comision_final*100:.3f}%")
else:
    st.warning("Completa los valores para calcular.")
