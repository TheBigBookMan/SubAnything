from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)


def create_news_section(data):
    print("NEWS SECTION")
    print(data)


def create_house_section(data):
    pass

def create_stock_section(data):
    pass

def create_crypto_section(data):
    pass

def create_pdf(data):
    print("PDFF")
    # print(data)

    for key, value in data.items():
        if key == 'house':
            create_house_section(value)
        elif key == 'news':
            create_news_section(value)
        elif key == 'stocks':
            create_stock_section(value)
        elif key == 'crypto':
            create_crypto_section(value)



    pdf.output('temp.pdf')