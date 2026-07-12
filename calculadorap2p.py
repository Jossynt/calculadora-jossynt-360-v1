import streamlit as st

st.set_page_config(page_title="Calculadora P2P", page_icon="💰")

st.title("💰 Calculadora P2P")
st.subheader("Simula tu operación como maker")

# Configuración de tarifas
tarifa_base = 0.0025  # 0.25% tarifa maker en Venezuela
niveles = {
    "Sin verificar": 0.0,
    "Bronce": 0.20,
    "Plata": 0.30,
    "Oro": 0.50
}

# Inputs
nivel = st.radio("Nivel Binance", list(niveles.keys()), horizontal=True)
cantidad_usdt = st.number_input("Cantidad USDT a vender", min_value=0.0, value=1000.0)
tasa_venta = st.number_input("Tasa de venta (fiat x USDT)", min_value=0.0, value=833.0)
tasa_compra = st.number_input("Tasa de compra (recompra)", min_value=0.0, value=812.123)

# Lógica de cálculo
descuento = niveles[nivel]
comision_final = tarifa_base * (1 - descuento)

# Validación: Solo calcular si hay datos válidos
if cantidad_usdt > 0 and tasa_venta > 0 and tasa_compra > 0:
    monto_bruto = cantidad_usdt * tasa_venta
    comision_dinero = monto_bruto * comision_final
    recibes_neto = monto_bruto - comision_dinero
    
    usdt_recuperados = recibes_neto / tasa_compra
    ganancia_neta_usdt = usdt_recuperados - cantidad_usdt

    # Interfaz de resultados
    st.divider()
    st.subheader("📊 Resultado del Ciclo")
    
    col1, col2 = st.columns(2)
    col1.metric("Recibes en VES", f"{recibes_neto:,.2f} VES")
    col2.metric("USDT Recuperados", f"{usdt_recuperados:,.4f} USDT")
    
    st.markdown("---")
    st.subheader("🚀 Ganancia Neta del Ciclo")
    
    if ganancia_neta_usdt > 0:
        st.success(f"### Has ganado: +{ganancia_neta_usdt:,.4f} USDT")
    else:
        st.error(f"### Resultado: {ganancia_neta_usdt:,.4f} USDT (Pérdida)")
    
    st.caption(f"Comisión aplicada: {comision_final*100:.3f}%")
else:
    st.warning("Por favor, completa los campos con valores mayores a cero para ver el resultado.")