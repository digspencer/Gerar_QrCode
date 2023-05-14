import webbrowser

def gerar_codigo_qr(url): {

    webbrowser.open(url)

}

nome = input('Digite o dado que aparecerá no QRcode: ')
gerar_qr_code = gerar_codigo_qr('https://chart.googleapis.com/chart?chs=180x180&cht=qr&chl={}'.format(nome))

gerar_qr_code