import csv
from io import StringIO


def handle_notification_row(row):
    sku, code, state, errors, row_number, piece_barcode = row
    print(
        f"SKU: {sku}, Code: {code}, State: {state}, Errors: {errors}, "
        f"Row Number: {row_number}, Piece Barcode: {piece_barcode}"
    )


def handle_full_catalog_row(row):
    sku, barcode, price, active, max_sales_quantity = row
    print(
        f"SKU: {sku}, Barcode: {barcode}, Price: {price}, Active: {active}, "
        f"Maximum Sales Quantity: {max_sales_quantity}"
    )


class CsvHandler:
    def __init__(self, job_id, csv_content):
        self.job_id = job_id
        self.csv_content = csv_content
        self.is_notification_csv = None

    def determine_csv_type(self):
        csv_buffer = StringIO(self.csv_content)
        csv_reader = csv.reader(csv_buffer)
        header = next(csv_reader, None)

        if header:
            self.is_notification_csv = len(header) == 6
        else:
            self.is_notification_csv = False

    def handle_notification_csv(self):
        if self.is_notification_csv is None:
            self.determine_csv_type()

        if self.is_notification_csv:
            csv_buffer = StringIO(self.csv_content)
            csv_reader = csv.reader(csv_buffer)

            header = next(csv_reader, None)
            if header:
                print("job_id_csv: ", self.job_id)
                print(', '.join(header))

            for row in csv_reader:
                handle_notification_row(row)

    def handle_full_catalog_csv(self):
        if self.is_notification_csv is None:
            self.determine_csv_type()

        if not self.is_notification_csv:
            csv_buffer = StringIO(self.csv_content)
            csv_reader = csv.reader(csv_buffer)

            header = next(csv_reader, None)
            if header:
                print("job_id_csv: ", self.job_id)
                print(', '.join(header))

            for row in csv_reader:
                handle_full_catalog_row(row)
