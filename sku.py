from pyscript import display, document

def generate(e):
    prod1 = document.getElementById("pen")
    prod2 = document.getElementById("penc")
    prod3 = document.getElementById("eraser")
    prod4 = document.getElementById("stick")
    prod5 = document.getElementById("book")

    material1 = document.getElementById("write")
    material2 = document.getElementById("paper")


    type = (material1.value) * material1.selected + (material2.value) * material2.selected 
    object = (prod1.value) * prod1.selected + (prod2.value) * prod2.selected + (prod3.value) * prod3.selected + (prod4.value) * prod4.selected + (prod5.value) * prod5.selected
    
    quantity = (document.getElementById('number').value)


    display(f'{type}-{object}-{quantity}', target='result')