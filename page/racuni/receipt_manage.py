from page.racuni.models import SavedReceipt


class Receipt:
    def __init__(self, pk, receipt_title, date, client, total):
        self.pk = pk
        self.receipt_title = receipt_title
        self.date = date
        self.client = client
        self.total = total


def get_total(entry):
    cpq = entry.cents_per_quantity
    quantity = entry.quantity
    total = 0
    for x, y in zip(cpq, quantity):
        total += x * y
    return total


def receipts_list(username):
    db_objects = SavedReceipt.objects.filter(username=username)
    receipts_ret = []

    for entry in db_objects:
        total = get_total(entry)
        receipts_ret.append(Receipt(
            entry.pk,
            entry.bill_number,
            entry.date,
            entry.buyer_full_name,
            total))
    return receipts_ret
