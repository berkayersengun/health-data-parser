# import os
# entries = os.listdir('resources/')

import xml.etree.ElementTree as ET
import datetime

tree = ET.parse('resources/export.xml')
root = tree.getroot()

def parseTime(time):
    timeFormat = '%Y-%m-%d %H:%M:%S %z'
    return datetime.datetime.strptime(time, timeFormat)

# total entries in xml file
def totalEntriesInFile(root):
    lastIndex = len(list(enumerate(root))) - 1

    for idx, item in enumerate(root):
        if idx == lastIndex:
            print('total entries: ', idx + 1)


# get all info
def printAllData(root):
    for child in enumerate(root):
        if child.get('type') == 'HKQuantityTypeIdentifierBodyMass':
            print(child.get('value'), child.get('creationDate'), child.get('startDate'), child.get('endDate'), sep=' ')
            print(child.get('value'), child.get('startDate'), sep=' ')
    if child.get('type') == 'HKQuantityTypeIdentifierBasalEnergyBurned':
        print(child.get('value'), child.get('creationDate'), child.get('startDate'), child.get('endDate'), sep=' ')
        print(child.get('value'), child.get('startDate'), sep=' ')


# total energy burned in oct
def totalEnergyBurned(month, root):
    total = 0
    for child in root:
        if child.get('type') == 'HKQuantityTypeIdentifierBasalEnergyBurned':
            # print(child.get('value'), child.get('creationDate'), child.get('startDate'), child.get('endDate'), sep=' ')
            date = parseTime(child.get('startDate')).date()
            if date.month == 11:
                # print(child.get('value'), date, sep=' ')
                total += float(child.get('value'))

    print('total energy burned in oct: ', total, sep=' ')


# list all record types
def listAllRecordTypes(root):
    types = []
    for child in root:
        if child.get('type') not in types:
            types.append(child.get('type'))

    for type in types:
        print(type)
