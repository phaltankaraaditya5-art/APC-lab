class Printer:
    def print_document(self):
        print("Printing document...")


class Scanner:
    def scan_document(self):
        print("Scanning document...")


class MultifunctionDevice(Printer, Scanner):
    def copy_document(self):
        self.scan_document()
        self.print_document()


mfd = MultifunctionDevice()
mfd.copy_document()