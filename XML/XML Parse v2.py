import xml.etree.ElementTree as ET

serial_number = ""
station_id = ""
operator = ""
uut_result = ""
test_type = ""
uut_part = ""

#tree = ET.parse('Report[P200005 3-2 final][11 39 23 AM][1 27 2020].xml')
#tree = ET.parse('Report[S200001 RMR 2-1 cold][10 33 24 AM][2 10 2020].xml')
#tree = ET.parse('Report[S200001][5 51 04 AM][2 10 2020].xml')
#tree = ET.parse('Report[S200020 4-2 cold][3 36 28 PM][1 29 2020].xml')
#tree = ET.parse('Report[S200020 4-2 pre][12 04 48 PM][1 29 2020].xml')

root = tree.getroot()

for report in root:  # parsing into first <Report> layer under <Reports>
    test_type = report.get('Type')
    uut_result = report.get('UUTResult')
    for prop in report:  # parsing into parent list of <Prop>
        if prop[0].get('Name') == 'SerialNumber':
            serial_number = prop[0][0].text
        elif prop.get('Name') == 'StationInfo':
            station_id = prop[0][0].text
            operator = prop[1][0].text
        elif prop.get('Type') == 'TEResult':
            if prop[0].get('Name') == 'TS':
                if prop[0][0].get('Name') == 'SequenceCall':
                    if prop[0][0][0].get('Name') == 'ResultList':
                        for value in prop[0][0][0]:
                            if value.get('ID') == '[0]':
                                for subprop in value:
                                    if subprop.get("Type") == "TEResult":
                                        for subsubprop in subprop:
                                            if subsubprop.get('Name') == 'ReportText':
                                                x = subsubprop[0].text
                                                y = x.replace('<b>', '\'')
                                                y = y.replace('</b>', '')
                                                y = y.replace('\n', '')
                                                z = y.split("'")
                                                uut_part = z[2]

print(f"Test Type: {test_type}")
print(f"UUT Result: {uut_result}")
print(f"Serial Number: {serial_number}")
print(f"Station ID: {station_id}")
print(f"Operator: {operator}")
print(uut_part)
