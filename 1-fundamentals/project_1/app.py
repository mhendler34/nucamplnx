#!/usr/bin/python3

from class_networking import Networking
from class_topics import Topics
import ntwkdict

while True:
    topics = Topics()
    topics.main_menu()
    response = input('> ')
    if response == '1':
        #  topics.mod1_menu()  Create this
        #  response = input('> ')
        mod1_osi = Networking()
        mod1_osi.flash_cards(ntwkdict.sbj_mod1td, ntwkdict.dict_mod1td)
    elif response == '2':
        print("TODO: Module 2")
        #  topics.mod2_menu ?
        #  mod2_infrastructure = Networking()
    elif response == '3':
        topics.mod3_menu()
        response = input('> ')
        mod3_addressing = Networking()
        if response == '1':
            mod3_addressing.bin_dec()
        elif response == '2':
            mod3_addressing.bin_hex()
        elif response == '3':
            mod3_addressing.hex_dec()
        elif response == '4':
            mod3_addressing.flash_cards(ntwkdict.sbj_prv, ntwkdict.dict_prv)
        elif response == '5':
            mod3_addressing.flash_cards(ntwkdict.sbj_res, ntwkdict.dict_res)
        elif response == '6':
            print("TODO: Module 3 terms and Definitions flash cards")
    elif response == '4':
        mod4_protocols = Networking()
        mod4_protocols.flash_cards(ntwkdict.sbj_npp, ntwkdict.dict_npp)
        mod4_protocols.flash_cards(ntwkdict.sbj_proto, ntwkdict.dict_proto)
        print("TODO: mod4_terms flash cards")
    elif response == '5':
        topics.mod5_menu()
        response = input('> ')
        mod5_cabling = Networking()
        if response == '1':
            mod5_cabling.flash_cards(ntwkdict.sbj_ecs, ntwkdict.dict_ecs)
        elif response == '2':
            mod5_cabling.flash_cards(ntwkdict.sbj_efs, ntwkdict.dict_efs)
        elif response == '3':
            mod5_cabling.flash_cards(ntwkdict.sbj_twps, ntwkdict.dict_twps)
        elif response == '4':
            mod5_cabling.flash_cards(ntwkdict.sbj_t568a, ntwkdict.dict_t568a)
        elif response == '5':
            mod5_cabling.flash_cards(ntwkdict.sbj_t568b, ntwkdict.dict_t568b)
        elif response == '6':
            mod5_cabling.flash_cards(ntwkdict.sbj_mod5td, ntwkdict.dict_mod5td)
    elif response == '6':
        mod6_wireless = Networking()
        mod6_wireless.flash_cards(ntwkdict.sbj_mod6td, ntwkdict.dict_mod6td)
    elif response == '7':
        mod7_ntwkarc = Networking()
        mod7_ntwkarc.flash_cards(ntwkdict.sbj_mod7td, ntwkdict.dict_mod7td)
    elif response == '8':
        print("TODO: Module 8")
    elif response == '9':
        print("TODO: Module 9")
    elif response == '10':
        print("TODO: Module 10")
    elif response == '11':
        print("TODO: Module 11")
    elif response == '12':
        print("Module 12")

    else:
        print("Do It Again Tomorrow!!")
        print("and Again... and Again.... and Again!!!")
        break
