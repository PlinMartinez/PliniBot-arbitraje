# AQUI VAMOS A IR PONIENDO LAS FUNCIONES QUE NECESITA EL HILO PRINCIPAL PARA IR HACIENDO LO NECESARIO


def medio(par):

    libro = exchange.fetch_order_book(par)
    ask = libro['asks'][0][0]
    bid = libro['bids'][0][0]
    spread = ask - bid
    medio = (ask + bid) / 2
    compra = medio * 0.98
    venta = medio * 1.02

