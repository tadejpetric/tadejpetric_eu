from page.racuni.models import SavedReceipt, SavedTemplate
import datetime
from decimal import Decimal, getcontext


class Receipt:
    def __init__(self, pk, receipt_title, date, client, total):
        self.pk = pk
        self.receipt_title = receipt_title
        self.date = date
        self.client = client
        self.total = total


def get_total(entry):
    # entry is a raw object from the database. entry.quantity and such
    # are arrays of values corresponding to the receipt
    # Poorly named but it's "completely" unrelated to the Entry class
    cpq = entry.cents_per_quantity
    quantity = entry.quantity
    total = 0
    for x, y in zip(cpq, quantity):
        total += x * y
    return total


def receipts_list(username):
    db_objects = SavedReceipt.objects.filter(username=username).order_by('-pk')
    receipts_ret = []

    for entry in db_objects:  # every users receipt
        total = get_total(entry)
        receipts_ret.append(Receipt(
            entry.pk,
            entry.bill_number,
            entry.date,
            entry.buyer_full_name,
            round(total/100, 2)))
    return receipts_ret

# --------- separate -----------


def price_from_cents(cents):
    euros = cents // 100
    cents_lover = euros % 100
    return str(euros) + "." + str(cents_lover)[:2]


class Entry:
    def __init__(self,
                 opravilo,
                 measure_unit,
                 cents_per_quantity,
                 quantity):
        self.opravilo = opravilo
        self.measure_unit = measure_unit
        self.cents_per_quantity = round(cents_per_quantity/100, 4)
        self.quantity = quantity
        self.total = price_from_cents(round(quantity * cents_per_quantity, 2))


def iso_to_slo(iso_date):
    y, m, d = iso_date.split('-')
    return d + '.' + m + '.' + y


class Preset:
    def __init__(self):
        self.comp_name = ""
        self.house_nr = ""
        self.city = ""
        self.bill_city = ""
        self.date = ""
        self.id_nr = ""
        self.transact_acc = ""
        self.phone = ""
        self.email = ""
        self.bill_number = ""
        self.buyer_full_name = ""
        self.buyer_house_nr = ""
        self.buyer_post_nr = ""
        self.buyer_city = ""
        self.id_for_vat = ""
        self.task_date = ""
        self.payment_date = ""
        self.task = ""
        self.entries = []
        self.total = "0.00 €"
        self.full_name = ""

    def new_logged_in(self, username):
        try:
            obj = SavedTemplate.objects.get(username=username)
        except SavedTemplate.DoesNotExist:
            print("template for", username, "doesn't exist")  # remove in prod
            return
        self.comp_name = obj.comp_name
        self.house_nr = obj.house_nr
        self.post_nr = obj.post_nr
        self.city = obj.city
        self.bill_city = obj.bill_city
        self.id_nr = obj.id_nr  # matična številka
        self.tax_nr = obj.tax_nr
        self.transact_acc = obj.transact_acc
        self.phone = obj.phone
        self.email = obj.email
        self.full_name = obj.full_name

    def saved_logged_in(self, username, pk):
        try:
            obj = SavedReceipt.objects.get(username=username, pk=pk)
        except SavedReceipt.DoesNotExist:
            return False

        self.comp_name = obj.comp_name
        self.house_nr = obj.house_nr
        self.post_nr = obj.post_nr
        self.city = obj.city
        self.bill_city = obj.bill_city
        self.date = obj.date
        self.id_nr = obj.id_nr
        self.tax_nr = obj.tax_nr
        self.transact_acc = obj.transact_acc
        self.phone = obj.phone
        self.email = obj.email
        self.bill_number = obj.bill_number
        self.buyer_full_name = obj.buyer_full_name
        self.buyer_house_nr = obj.buyer_house_nr
        self.buyer_post_nr = obj.buyer_post_nr
        self.buyer_city = obj.buyer_city
        self.id_for_vat = obj.id_for_vat
        self.task_date = obj.task_date
        self.payment_date = obj.payment_date
        self.task = obj.task

        total = 0
        for o, m, c, q in zip(obj.opravilo, obj.measure_unit,
                              obj.cents_per_quantity, obj.quantity):
            self.entries.append(Entry(o, m, c, q))
            print(Entry(o, m, c, q).total)
            total += c * q

        self.total = round(total/100, 2)
        self.full_name = obj.full_name
        self.pk = pk
        return True

    def prepare_edit(self):
        self.payment_date = str(self.payment_date)
        self.date = str(self.date)
        self.task_date = str(self.task_date)

    def prepare_print(self):
        self.full_name_ed = self.full_name.upper()
        self.payment_date = iso_to_slo(str(self.payment_date))
        self.task_date = iso_to_slo(str(self.task_date))
        self.date = iso_to_slo(str(self.date))


"""
functionality for saving and editing existing receipts in the database
"""


def iso_to_date(iso: str):
    if iso == '':
        return None
    date = iso.split('-')
    
    try:
        return datetime.date(int(date[0]), int(date[1]), int(date[2]))
    except (ValueError, IndexError):
        return None


def all_equal(*args):
    print(args)
    if len(args) == 0:
        return True
    for x in args[1:]:
        if x != args[0]:
            return False
    return True


def receipt_handler(post_data, new_rec):
    new_rec.house_nr = post_data.get('house_nr', '')
    new_rec.comp_name = post_data.get('comp_name', '')
    new_rec.post_nr = post_data.get('post_nr', '')
    new_rec.city = post_data.get('city', '')
    new_rec.bill_city = post_data.get('bill_city', '')
    new_rec.date = iso_to_date(post_data.get('date', ''))
    new_rec.tax_nr = post_data.get('tax_nr', '')
    new_rec.id_nr = post_data.get('id_nr', '')
    new_rec.transact_acc = post_data.get('transact_acc', '')
    new_rec.phone = post_data.get('phone', '')
    new_rec.email = post_data.get('email', '')
    new_rec.bill_number = post_data.get('bill_number', '')
    new_rec.buyer_full_name = post_data.get('buyer_full_name', '')
    new_rec.buyer_house_nr = post_data.get('buyer_house_nr', '')
    new_rec.buyer_post_nr = post_data.get('buyer_post_nr', '')
    new_rec.buyer_city = post_data.get('buyer_city', '')
    new_rec.id_for_vat = post_data.get('id_for_vat', '')

    new_rec.task_date = iso_to_date(post_data.get('task_date', ''))
    new_rec.payment_date = iso_to_date(post_data.get('payment_date', ''))

    new_rec.task = post_data.get('task', '')

    new_rec.opravilo = []
    new_rec.measure_unit = []
    new_rec.cents_per_quantity = []
    new_rec.quantity = []

    getcontext().prec = 10
    print(post_data)
    if all_equal(len(post_data.getlist('opravilo')),
                 len(post_data.getlist('measure_unit')),
                 len(post_data.getlist('cents_per_quantity')),
                 len(post_data.getlist('quantity'))):
        try:
            for i in range(len(post_data.getlist('opravilo'))):
                new_rec.opravilo.append(post_data.getlist('opravilo')[i])
                new_rec.measure_unit.append(
                    post_data.getlist('measure_unit')[i])
                new_rec.cents_per_quantity.append(
                    round(float(post_data.getlist('cents_per_quantity')[i]) * 100))
                new_rec.quantity.append(
                    Decimal(post_data.getlist('quantity')[i]))
        except ValueError:
            new_rec.opravilo = []
            new_rec.measure_unit = []
            new_rec.cents_per_quantity = []
            new_rec.quantity = []
    new_rec.full_name = post_data.get('full_name', '')
    new_rec.save()


def save_new_to_db(post_data, username):
    new_rec = SavedReceipt.objects.create()
    new_rec.username = username
    receipt_handler(post_data, new_rec)


def edit_receipt(post_data, username, pk):
    try:
        entry = SavedReceipt.objects.get(username=username, pk=pk)
    except SavedReceipt.DoesNotExist:
        return False
    receipt_handler(post_data, entry)


def delete(pk, uname):
    try:
        entry = SavedReceipt.objects.get(username=uname, pk=pk)
    except SavedReceipt.DoesNotExist:
        return False
    entry.delete()


def set_settings(uname, post_data):
    try:
        setting = SavedTemplate.objects.get(username=uname)
    except SavedTemplate.DoesNotExist:
        setting = SavedTemplate.objects.create(username=uname)
    setting.comp_name = post_data.get('comp_name', '')
    setting.house_nr = post_data.get('house_nr', '')
    setting.post_nr = post_data.get('post_nr', '')
    setting.city = post_data.get('city', '')
    setting.bill_city = post_data.get('bill_city', '')
    setting.tax_nr = post_data.get('tax_nr', '')
    setting.id_nr = post_data.get('id_nr', '')
    setting.transact_acc = post_data.get('transact_acc', '')
    setting.phone = post_data.get('phone', '')
    setting.email = post_data.get('email', '')
    setting.full_name = post_data.get('full_name', '')
    setting.save()

    
