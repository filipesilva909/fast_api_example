import streamlit as st
import pandas as pd
import requests

# API base URL
API_URL = "http://localhost:8080"

st.title("FastAPI Item Manager")

# -------------------------
# Form to create a new item
# -------------------------
st.header("Create a New Item")
with st.form("create_item_form"):
    name = st.text_input("Name")
    description = st.text_input("Description")
    price = st.number_input("Price", min_value=0.0, step=0.01)
    in_stock = st.checkbox("In stock", value=True)
    submit_button = st.form_submit_button("Create Item")

if submit_button:
    item_data = {
        "name": name,
        "description": description,
        "price": price,
        "in_stock": in_stock
    }
    response = requests.post(f"{API_URL}/items", json=item_data)
    if response.status_code == 201:
        st.success("Item created successfully!")
    else:
        st.error(f"Failed to create item: {response.text}")

# -------------------------
# Display all items
# -------------------------
st.header("All Items")
response = requests.get(f"{API_URL}/items")
if response.status_code == 200:
    items = response.json()
    if items:
        for item in items:
            st.subheader(f"{item['name']} (ID: {item['id']})")
            st.write(f"Description: {item.get('description', 'N/A')}")
            st.write(f"Price: ${item['price']}")
            st.write(f"In stock: {'Yes' if item['in_stock'] else 'No'}")
            # Optional: delete button
            if st.button(f"Delete {item['name']}", key=item['id']):
                del_resp = requests.delete(f"{API_URL}/items/{item['id']}")
                if del_resp.status_code == 200:
                    st.success(f"Item {item['name']} deleted successfully!")
                else:
                    st.error(f"Failed to delete {item['name']}")
    else:
        st.info("No items found in the database.")
else:
    st.error("Failed to fetch items from the API.")
