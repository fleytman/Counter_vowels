#! /usr/bin/env python
# -*- coding: utf-8 -*-

def main():
##    glasn = [u'а', u'у', u'о', u'ы', u'и', u'э', u'я', u'ю', u'ё', u'е', u'А', u'У', u'О', u'Ы', u'И', u'Э', u'Я', u'Ю', u'Ё', u'Е']
##    soglasn = [u'б', u'в', u'г', u'д', u'ж', u'з', u'й', u'к', u'л', u'м', u'н', u'п', u'р', u'с', u'т', u'ф', u'х', u'ц', u'ч', u'ш', u'щ',u'Б', u'В', u'Г', u'Д', u'Ж', u'З', u'Й', u'К', u'Л', u'М', u'Н', u'П', u'Р', u'С', u'Т', u'Ф', u'Х', u'Ц', u'Ч', u'Ш', u'Щ']
##    graf = [u'ь',u'ъ',u'Ь',u'Ъ']
    glasn = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е', 'А', 'У', 'О', 'Ы', 'И', 'Э', 'Я', 'Ю', 'Ё', 'Е']
    soglasn = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ','Б', 'В', 'Г', 'Д', 'Ж', 'З', 'Й', 'К', 'Л', 'М', 'Н', 'П', 'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ']
    graf = ['ь','ъ','Ь','Ъ']
    predloj1 = raw_input("Vvedite predloj 1")
    print predloj1
    pred1_count = counter(predloj1,glasn,soglasn,graf)
    print "chislo_glasn = " + str(pred1_count[0]) + "\nchislo_soglasn = " + str(pred1_count[1]) + "\nchislo_graf = " + str(pred1_count[2])
    predloj2  = raw_input("Vvedite predloj 2")
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
