#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import locale

def main():
    glasn = list(u'ауоыиэяюёеАУОЫИЭЯЮЁЕ')
    soglasn = list(u'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ')
    graf = list(u'ьъЬЪ')
    if sys.stdin.encoding: encoding = sys.stdin.encoding
    else: encoding = locale.getdefaultlocale()[1]
    print u"Введите предложение 1"
    predloj1 = raw_input().decode(encoding)
    print predloj1
    pred1_count = counter(predloj1,glasn,soglasn,graf)
    print "chislo_glasn = " + str(pred1_count[0]) + "\nchislo_soglasn = " + str(pred1_count[1]) + "\nchislo_graf = " + str(pred1_count[2])
    print u"Введите предложение 2"
    predloj2  = raw_input().decode(encoding)
    print predloj2
    pred2_count = counter(predloj2,glasn,soglasn,graf)
    print "chislo_glasn = " + str(pred2_count[0]) + "\nchislo_soglasn = " + str(pred2_count[1]) + "\nchislo_graf = " + str(pred2_count[2])
    if pred1_count[0] == pred2_count[0]: print u'Число слогов равно'
    else: print u'Число слогов не равно'

def counter(predloj,glasn,soglasn,graf):
    chislo_glasn,chislo_soglasn,chislo_graf = 0,0,0
    while predloj:
        bukva = predloj[0]
        predloj = predloj[1:]
        if bukva in glasn: chislo_glasn+=1
        if bukva in soglasn: chislo_soglasn+=1
        if bukva in graf: chislo_graf+=1
    return chislo_glasn,chislo_soglasn,chislo_graf

if __name__ == '__main__':
    main()
