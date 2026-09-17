from pyscript import display, document

def create_order (e):
    prod5 = document.getElementById("item5")

    subtotal = float(prod5.value) * prod5.checked
    display(subtotal, target="show")