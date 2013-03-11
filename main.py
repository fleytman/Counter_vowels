#! /usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    predloj = raw_input(u"Введите предложение")
    print predloj
    glasn = [u'а', u'у', u'о', u'ы', u'и', u'э', u'я', u'ю', u'ё', u'е']
    soglasn = [u'б', u'в', u'г', u'д', u'ж', u'з', u'й', u'к', u'л', u'м', u'н', u'п', u'р', u'с', u'т', u'ф', u'х', u'ц', u'ч', u'ш', u'щ']
    graf = [u'ь',u'ъ']
    counter(predloj,glasn,soglasn,graf)

def counter(predloj,glasn,soglasn,graf):
    chislo_glasn,chislo_soglasn,chislo_graf = 0,0,0
    while predloj:
        bukva = predloj[0]
        predloj = predloj[1:]
        if bukva in glasn: chislo_glasn+=1
        if bukva in soglasn: chislo_soglasn+=1
        if bukva in graf: chislo_graf+=1
    print "chislo_glasn = " + unicode(chislo_glasn) + "\nchislo_soglasn = " + unicode(chislo_soglasn) + "\nchislo_graf = " + unicode(chislo_graf)

if __name__ == '__main__':
    main()
