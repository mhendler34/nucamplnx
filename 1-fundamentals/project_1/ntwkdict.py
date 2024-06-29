#!/usr/bin/python3

# File for all dictionaries in class_networking_app.py

# MODULE 1
dictionary_1 = {}
with open('/home/mitchell/Code/projects/networking/text_files/mod1_terms.txt', 'r') as m:
    lines = m.readlines()

    for line in lines:
        key, value = line.split(':')
        value = value.strip()
        dictionary_1[key] = value

sbj_mod1td = "Module 1: OSI Reference Model"
dict_mod1td = dictionary_1


# MODULE 2

# MODULE 3
sbj_prv = "Private IP Address Ranges"
dict_prv = {'Class-A start': '10.0.0.0', 'Class-A end': '10.255.255.255',
            'Class-B start': '172.16.0.0', 'Class-B end': '172.31.255.255',
            'Class-C start': '192.168.0.0', 'Class-C end': '192.168.255.255'}

sbj_res = "Reserved IP Addresses"
dict_res = {'broadcast': '255.255.255.255',
            'unassigned': '0.0.0.0', 'loopback-start': '127.0.0.1',
            'loopback-end': '127.255.255.254',
            'APIPA-start': '169.254.0.1', 'APIPA-end': '169.254.255.254'}
# MODULE 4
sbj_npp = "network ports and protocols"
dict_npp = {20: 'ftp-data', 21: 'ftp-control', 22: 'ssh', 23: 'telnet',
            25: 'smtp', 67: 'dhcp-server', 68: 'dhcp-client', 69: 'tftp',
            80: 'http', 110: 'pop3', 123: 'ntp', 143: 'imap4',
            161: 'snmp', 162: 'snmp', 389: 'ldap', 443: 'https',
            445: 'smb', 514: 'syslog', 587: 'smtp-tls', 636: 'ldap-ssl',
            993: 'imap4-ssl', 995: 'pop3-ssl', 1433: 'sql',
            1521: 'sqlnet', 2427: 'mgcp', 2727: 'mgcp', 3306: 'mysql',
            3389: 'rdp', 5004: 'rtp', 5005: 'rtp', 5060: 'sip', 5061: 'sip'}

dictionary_4b = {}
with open('/home/mitchell/Code/projects/networking/text_files/protocols.txt', 'r') as m:
    lines = m.readlines()

    for line in lines:
        key, value = line.split(':')
        value = value.strip()
        dictionary_4b[key] = value

sbj_proto = "Module 4: Acronyms and Protocols"
dict_proto = dictionary_4b
# MODULE 5
sbj_ecs = "ethernet cable standards"
dict_ecs = {'10BASE-T-Mbps': '10mbps', '10BASE-T-dist': '100m',
            '10BASET-media': 'cat3', '10BASET-pairs': '2',
            '100BASET-Mbps': '100mbps', '100BASET-dist': '100m',
            '100BASET-media': 'cat5', '100BASET-pairs': '2',
            '100BASETX-Mbps': '100mbps', '100BASETX-dist': '100m',
            '100BASETX-media': 'cat6', '100BASETX-pairs': '2',
            '1000BASET-Mbps': '1000mbps', '1000BASET-dist': '100m',
            '1000BASET-media': 'cat5', '1000BASET-pairs': '4',
            '2.5GBASET-Mbps': '2500mbps', '2.5GBASET-dist': '100m',
            '2.5GBASET-media': 'cat5e', '2.5GBASET-pairs': '4',
            '5GBASET-Mbps': '5000mbps', '5GBASET-dist': '100m',
            '5GBASET-media': 'cat6', '5GBASET-pairs': '4',
            '10GBASET-Mbps': '10000mbps', '10GBASET-dist': '100m',
            '10GBASET-media': 'cat6/7', '10GBASET-pairs': '4',
            '40GBASET-Mbps': '40000mbps', '40GBASET-dist': '30m',
            '40GBASET-media': 'cat8', '40GBASET-pairs': '4'}

sbj_efs = "ethernet fiber standards"
dict_efs = {'100BASE-SX-Mbps': '100mbps', '100BASE-SX-dist': '300m',
            '100BASE-SX-media': 'mmf', '100BASE-FX-Mbps': '100mbps',
            '100BASE-FX-dist': '2000m', '100BASE-FX-media': 'mmf',
            '1000BASE-SX-Mbps': '1000mbps', '1000BASE-SX-dist': '550m',
            '1000BASE-LX-Mbps': '1000mbps', '1000BASE-LX-dist-mmf':
            '550m', '1000BASE-LX-dist-smf': '5000m',
            '1000BASE-LX-media': 'mmf/smf', '10GBASE-SR-Mbps': '10000mbps',
            '10GBASE-SR-dist': '300m', '10GBASE-SR-media': 'mmf',
            '10GBASE-LR-Mbps': '10000mbps', '10GBASE-LR-dist': '10000m',
            '10GBASE-LR-media': 'smf'}

sbj_twps = "twisted pair standards"
dict_twps = {'cat3-mbps': '10mbps', 'cat5-mbps': '100mbps',
             'cat5e-mbps': '1000mbps', 'cat6-mbps': '1gbps/10gbps',
             'cat6a-mbps': '10gbps', 'cat7-mbps': '10gbps/100gbps',
             'cat8-mbps': '25gbps/40gbps'}

sbj_t568a = "T568A pin out colored wires"
dict_t568a = {'T568A-1': 'white/green', 'T568A-2': 'green',
              'T568A-3': 'white/orange', 'T568A-4': 'blue',
              'T568A-5': 'white/blue', 'T568A-6': 'orange',
              'T568A-7': 'white/brown', 'T568A-8': 'brown'}

sbj_t568b = "T568B pin out colored wires"
dict_t568b = {'T568B-1': 'white/orange', 'T568B-2': 'orange',
              'T568B-3': 'white/green', 'T568B-4': 'blue',
              'T568B-5': 'white/blue', 'T568B-6': 'green',
              'T568B-7': 'white/brown', 'T568B-8': 'brown'}

dictionary_5 = {}
with open('/home/mitchell/Code/projects/networking/text_files/mod5_cabling.txt', 'r') as m:
    lines = m.readlines()

    for line in lines:
        key, value = line.split(':')
        value = value.strip()
        dictionary_5[key] = value

sbj_mod5td = "Module 5: Cabling Terms and Definitions"
dict_mod5td = dictionary_5

# MODULE 6
dictionary_6 = {}
with open('/home/mitchell/Code/projects/networking/text_files/mod6_wireless.txt', 'r') as m:
    lines = m.readlines()

    for line in lines:
        key, value = line.split(':')
        value = value.strip()
        dictionary_6[key] = value

sbj_mod6td = "Module 6: Wireless Networking Terms and Definitions"
dict_mod6td = dictionary_6

# MODULE 7
dictionary_7 = {}
with open('/home/mitchell/Code/projects/networking/text_files/mod7_architecture.txt', 'r') as m:
    lines = m.readlines()

    for line in lines:
        key, value = line.split(':')
        value = value.strip()
        dictionary_7[key] = value

sbj_mod7td = "Module 7: Networking Architecture Terms and Definitions"
dict_mod7td = dictionary_7


dictionary_20 = {}
with open('/home/mitchell/Code/projects/networking/text_files/pqf1.txt', 'r') as m:
    lines = m.readlines()

    for line in lines:
        key, value = line.split(':')
        value = value.strip()
        dictionary_20[key] = value

sbj_pqf1 = "Practice Questions: Fundamentals 1-99"
dict_pqf1 = dictionary_20
