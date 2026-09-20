from pyscript import display, document

def ordering(e):
    prod1 = document.getElementById("pen")
    prod2 = document.getElementById("pencil")
    prod3 = document.getElementById("eraser")
    prod4 = document.getElementById("notes")
    prod5 = document.getElementById("noteb")
    subtotal = float(prod1.value) * prod1.checked + float(prod2.value) * prod2.checked + float(prod3.value) * prod3.checked + float(prod4.value) * prod4.checked + float(prod5.value) * prod5.checked
    
    VAT = subtotal * .12
    total = subtotal + VAT

    display(f'===Receipt===', target='result')
    display(f'Subtotal: Php {subtotal}', target='result')
    display(f'VAT: Php {VAT}', target='result')
    display(f'Total amount: Php {total}', target='result')