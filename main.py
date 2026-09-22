from pyscript import display, document

def create_order (e):
    prod1 = document.getElementById("item1")
    prod2 = document.getElementById("item2")
    prod3 = document.getElementById("item3")
    prod4 = document.getElementById("item4")
    prod5 = document.getElementById("item5")

    subtotal = (float(prod1.value) * prod1.checked) + (float(prod2.value) * prod2.checked) + (float(prod3.value) * prod3.checked) + (float(prod4.value) * prod4.checked) + (float(prod5.value) * prod5.checked) 

    tax = (subtotal * 0.12)

    total = float(subtotal + tax)

    display(f'Subtotal: ₱{subtotal}', target="show-subtotal")
    display(f'Tax: ₱{tax}', target="show-tax")
    display(f'Total: ₱{total}', target="show-total")


def generate_sku(e):
    cat = document.querySelector('input[name="cat"]:checked')
    cat_final = cat.value

    prodname = document.getElementById("productname")
    qnty = document.getElementById("quantity")

    product_code = prodname.value[:3].upper()
    quantity = qnty.value

    sku = f"{cat_final.upper()}-{product_code}-{quantity}"

    display(sku, target="show-sku")
