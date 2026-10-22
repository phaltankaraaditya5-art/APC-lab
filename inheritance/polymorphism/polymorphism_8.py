class Report:
    def generate(self):
        print("Generating report...")


class PDFReport(Report):
    def generate(self):
        print("Generating PDF report")


class ExcelReport(Report):
    def generate(self):
        print("Generating Excel report")


class HTMLReport(Report):
    def generate(self):
        print("Generating HTML report")


def create_report(report):
    report.generate()


create_report(PDFReport())
create_report(ExcelReport())
create_report(HTMLReport())