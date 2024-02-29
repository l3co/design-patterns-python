class Report:
    def generate(self, content):
        return f"Text Report: {content}"


class HTMLReport(Report):
    def generate(self, content):
        return f"""
        <html>
            <body>
                <p>{content}</p>
            </body>
        </html>"""


class PDFReport(Report):
    def generate(self, content):
        return f"PDF(bytes): Relatório em PDF: {content}"


if __name__ == '__main__':
    report_txt = Report()
    report_html = HTMLReport()
    report_pdf = PDFReport()

    print(report_txt.generate("Isto é um teste"))
    print(report_html.generate("Isto é um teste"))
    print(report_pdf.generate("Isto é um teste"))
