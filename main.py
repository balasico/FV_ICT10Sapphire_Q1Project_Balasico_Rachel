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


def generate_sku (e):
    cat1 = document.getElementById("bev_id")
    cat2 = document.getElementById("topps_id")
    cat3 = document.getElementById("bkedgds_id")
    cat4 = document.getElementById("othr_id")

    cat_final = (float(cat1.value) * cat1.checked) + (float(cat2.value) * cat2.checked) + (float(cat3.value) * cat3.checked) + (float(cat4.value) * cat4.checked)

    prodname = document.getElementById("productname")
    qnty = document.getElementById("quantity")

    final_prodname = (prodname[1]) + (prodname[2]) + (prodname[3])

    display(f'Your Generated SKU: {cat_final}-{final_prodname}-{qnty}', target="show-sku")
