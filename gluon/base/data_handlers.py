from os.path import splitext
import csv

from zope.interface import Interface, Attribute, invariant, implementer
from zope.component import getGlobalSiteManager, createObject
from zope.component.factory import Factory
from zope.component.interfaces import IFactory


def data_handler_invariant(obj):
    if not (obj.extension and obj.mime):
        raise Exception("Both extension and MIME type are required")


class IDataHandler(Interface):
    extension = Attribute("Filename extension")
    mime = Attribute("Filename MIME type")
    invariant(data_handler_invariant)


gsm = getGlobalSiteManager()


@implementer(IDataHandler)
class CSVHandler(object):

    extension = ".csv"
    mime = "text/csv"

    @staticmethod
    def import_data(filename):
        # Get data from CSV file
        with open(str(filename)) as f:
            dialect = csv.Sniffer().sniff(f.readline())
            f.seek(0)
            data = csv.DictReader(f, dialect=dialect)
            return data.fieldnames, list(data)

    @staticmethod
    def export_data(filename, data, fieldnames):
        with open(filename, "w") as f:
            dialect = csv.unix_dialect
            writer = csv.DictWriter(f, dialect=dialect, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

gsm.registerUtility(Factory(CSVHandler), IFactory, ".csv")


def get_data_handler(filename):
        return createObject(splitext(str(filename))[-1])
