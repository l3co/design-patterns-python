from abc import ABC, abstractmethod


class Report(ABC):
    @abstractmethod
    def generate(self, content):
        ...


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
    report_html = HTMLReport()
    report_pdf = PDFReport()

    print(report_html.generate("Isto é um teste"))
    print(report_pdf.generate("Isto é um teste"))
