import streamlit as st

st.set_page_config(page_title="Calculadora P2P Pro", page_icon="💰", layout="centered")

st.markdown("""
    <style>
    [data-testid="stMetricValue"] { font-size: 26px !important; font-weight: bold !important; color: #ffffff !important; }
    [data-testid="stMetricLabel"] { font-size: 16px !important; }
    .stDivider { margin: 1rem 0; }
    </style>
""", unsafe_allow_html=True)

st.title("💰 Calculadora P2P Pro")

niveles_info = {
    "Sin verif.": 0.0025, 
    "Bronce": 0.0020, 
    "Plata": 0.00175, 
    "Oro": 0.00125
}

nivel = st.radio("Nivel Binance", list(niveles_info.keys()), horizontal=True)
cantidad_usdt = st.number_input("Cantidad USDT a vender", value=100.0, format="%.3f")
tasa_venta = st.number_input("Tasa Venta (VES x USDT)", value=833.0, format="%.3f")
tasa_compra = st.number_input("Tasa Recompra (VES x USDT)", value=813.0, format="%.3f")

comision = niveles_info[nivel]

if cantidad_usdt > 0 and tasa_venta > 0 and tasa_compra > 0:
    # --- ETAPA 1: VENTA (USDT -> VES) ---
    bruto_venta = cantidad_usdt * tasa_venta
    ves_tras_comision_venta = bruto_venta * (1 - comision)
    
    # --- ETAPA 2: RECOMPRA (VES -> USDT) ---
    ves_neto_para_recompra = ves_tras_comision_venta * (1 - comision)
    usdt_final_neto = ves_neto_para_recompra / tasa_compra
    
    ganancia = usdt_final_neto - cantidad_usdt

    st.divider()
    
    st.subheader("⬇️ Etapa 1: Venta (USDT a VES)")
    c1, c2 = st.columns(2)
    # Etiquetas solicitadas
    c1.metric("VES obtenidos", f"{bruto_venta:,.2f}") 
    c2.metric("VES tras comisiones", f"{ves_tras_comision_venta:,.2f}")
    
    st.subheader("⬆️ Etapa 2: Recompra (VES a USDT)")
    c3, c4 = st.columns(2)
    c3.metric("VES para recompra tras com.", f"{ves_neto_para_recompra:,.2f}")
    c4.metric("USDT Final Neto", f"{usdt_final_neto:,.3f}")
    
    st.divider()
    
    if ganancia >= 0:
        st.success(f"### Ganancia Neta: +{ganancia:,.3f} USDT")
    else:
        st.error(f"### Ganancia Neta: {ganancia:,.3f} USDT")
        
    st.caption(f"Comisión del {comision*100:.3f}% aplicada en cada ciclo de forma independiente.")
else:
    st.warning("Completa los valores para calcular.")
