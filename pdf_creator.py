from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)


def create_news_section(data):
    print("NEWS SECTION")
    # print(data)
    pdf.set_font(family="Times", style="B", size=20)
    pdf.cell(w=30, h=10, txt="News: ", align="L", ln=1)

    for category in data:
        for key, value in category.items():
            pdf.set_font(family="Times", style="B", size=16)
            pdf.cell(w=30, h=10, txt=key.title(), align="L", ln=1)

            if len(value) == 0:
                pdf.set_font(family="Times", style="B", size=12)
                pdf.cell(w=0, h=10, txt=f"There is no news this week for {key}...", align='L', ln=1)
            else :
                for news in value:
                  print(news)
                  pdf.set_font(family="Times", style="B", size=12)
                  pdf.cell(w=0, h=8, txt=news['title'], align='L', ln=1)
                  pdf.set_font(family="Times", style="I", size=8)
                  pdf.cell(w=0, h=8, txt=f"Author: {news['author']}", align='L', ln=1)
                  pdf.set_font(family="Times", style="B", size=8)
                  pdf.cell(w=50, h=8, txt=f"News Source: {news['source']}", align='L', ln=0)
                  pdf.set_font(family="Times", style='B', size=8)
                  pdf.cell(w=0, h=8, txt=news['publishedDate'], align='L', ln=1)
                  pdf.set_font(family="Times", style="BUI", size=8)
                  pdf.cell(w=0, h=8, txt=news['url'], align='L', ln=1)
                  pdf.set_font(family="Times", size=8)
                  pdf.cell(w=0, h=10, txt=news['description'], align='L', ln=1)
                  pdf.set_font(family="Times", size=8)
                  pdf.cell(w=0, h=10, txt=news['content'], align='L', ln=1)

                  # !!! unicode error for some symbols

def create_house_section(data):
    pass

def create_stock_section(data):
    pass

def create_crypto_section(data):
    pass

def create_pdf(data):
    print("PDFF")
    # print(data)
    pdf.add_page()

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