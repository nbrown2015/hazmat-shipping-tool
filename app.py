import streamlit as st

# Minimal UN data set
UN_DATABASE = {
    "UN1987": {
        "name": "Alcohols, n.o.s.",
        "class": 3,
        "pg": "II or III",
        "iata_pi": "355",
        "labels": ["Flammable Liquid"],
        "air_limit": 5.0,
        "absorbent_required": True
    },
    "UN1170": {
        "name": "Ethanol Solution",
        "class": 3,
        "pg": "II",
        "iata_pi": "355",
        "labels": ["Flammable Liquid"],
        "air_limit": 5.0,
        "absorbent_required": True
    }
}

# App title and intro
st.set_page_config(page_title="HAZMAT Shipping Tool", layout="centered")
st.title("📦 HAZMAT Shipping Guidance Tool")
st.markdown("Get packaging and compliance guidance for common flammable liquids.")

# Input form
un_number = st.selectbox("Select UN Number", list(UN_DATABASE.keys()))
quantity = st.number_input("Quantity per container (liters)", min_value=0.1, max_value=60.0, step=0.1)
packaging = st.selectbox("Packaging Type", ["Plastic bottle", "Glass bottle", "Metal drum"])
mode = st.selectbox("Mode of Transport", ["Air", "Ground", "Ocean"])

# Show guidance
if st.button("Get Guidance"):
    data = UN_DATABASE.get(un_number)
    if data:
        st.subheader("Regulatory Overview")
        st.markdown(f"**Proper Shipping Name:** {data['name']}")
        st.markdown(f"**Hazard Class:** {data['class']}")
        st.markdown(f"**Packing Group:** {data['pg']}")
        st.markdown(f"**IATA Packing Instruction:** {data['iata_pi']}")

        st.subheader("Packaging Guidance")
        if quantity > data['air_limit'] and mode == "Air":
            st.warning("⚠️ Quantity exceeds IATA limit for inner packagings. Must use cargo aircraft and compliant packaging.")
        if data['absorbent_required']:
            st.info("✅ Absorbent material (e.g., vermiculite, pads) is required for combination packaging.")
        if packaging == "Glass bottle":
            st.info("💡 Glass bottles should be placed in a liner with absorbent and cushioning material.")

        st.subheader("Required Labels and Marks")
        st.markdown(", ".join(data['labels']))
        if mode == "Air":
            st.markdown("✈️ 'Cargo Aircraft Only' label required")
        st.markdown("⬆️ Orientation arrows required on outer packaging")

        st.success("✅ Always verify details against the current IATA DGR and 49 CFR.")
    else:
        st.error("UN number not found.")

