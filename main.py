from browser import document # type: ignore

def SKU_generator(e):
    
    
    document.getElementById('sku-display').innerHTML = " "
    
    brand = document.getElementById('brand-select').value
    type = document.getElementById('type-select').value
    color = document.getElementById('color-select').value
    
    prod_code = type[:4].upper()
    qty = str(color)
    
    sku = brand[:3].upper() = "-" + prod_code + "-" + qty
    document.getElementById('output-zone').innerHTML = f"<strong>SKU:</strong>&nbsp;{sku}"
    
    document["SKU_generator"].bind("click", SKU_generator)

# ms. i give up