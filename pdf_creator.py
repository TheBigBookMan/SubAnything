from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

def create_pdf(data):
    print("PDFF")
    print(data)

    news_category = data['news']
    print(news_category)