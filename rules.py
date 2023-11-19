from durable.lang import *


with ruleset('heart'):

    def assert_absence(c, subject):
        c.assert_fact({'subject' : subject, 'predicate' : 'has', 'object' : 'heart disease'})
    
    def assert_presence(c, subject):
        c.assert_fact({'subject' : subject, 'predicate' : 'has', 'object' : 'not heart disease'})

#Rule 1
#if (majorv <= 0.5) and (oldp <= 2.45) and (sc <= 272.0) and (maxhra > 143.5) then class: 1 
    @when_any(all(c.first << ((m.predicate == 'has_majorRv') & (m.object <= 0.5)),
            c.second << ((m.predicate == 'has_oldp') & (m.object <= 2.45) & (m.subject == c.first.subject)),           
            c.third << ((m.predicate == 'has_maxHeartRate') & (m.object > 143.5) & (m.subject == c.first.subject)), 
            c.fourth << ((m.predicate == 'serumChol') & (m.object <= '272') & (m.subject == c.first.subject))))
    def absence_heart_desease(c):
        #c.assert_fact({'subject' : c.m.subject, 'predicate' : 'desease', 'object' : 'absence of heart desease'})
        assert_absence(c, c.first.subject)
    
    @when_all(+s.exception)
    def second(c):
        print(c.s.exception)
        c.s.exception = None

    @when_all(+m.subject)
    def output(c):
            if c.m.predicate == 'has':
                print('Fact: {0} {1} {2}'.format(c.m.subject, c.m.predicate, c.m.object))


#Rule 2
#if (majorv > 0.5)  and (oldp > 0.5)   and (cp > 3.5)    and (sc <= 301.0) then class: 2  

    @when_any(all(c.first << ((m.predicate == 'has_majorRv') & (m.object > 0.5)),
            c.second << ((m.predicate == 'has_oldp') & (m.object > 0.5) & (m.subject == c.first.subject)),           
            c.third << ((m.predicate == 'has_ChestPain') & (m.object == 'asympomatic') & (m.subject == c.first.subject))))
    def presence_heart_desease(c):
        #c.assert_fact({'subject' : c.m.subject, 'predicate' : 'desease', 'object' : 'absence of heart desease'})
        assert_presence(c, c.first.subject)

#Rule 3 
#if (majorv <= 0.5) and (oldp <= 2.45) and (sc <= 272.0) and (maxhra <= 143.5) then class: 1 

    @when_any(all(c.first << ((m.predicate == 'has_majorRv') & (m.object <= 0.5)),
            c.second << ((m.predicate == 'has_oldp') & (m.object <= 2.45) & (m.subject == c.first.subject)),           
            c.third << ((m.predicate == 'has_maxHeartRate') & (m.object > 143.5) & (m.subject == c.first.subject)), 
            c.fourth << ((m.predicate == 'has_rBloodPress') & (m.object > 111) & (m.subject == c.first.subject))),
            c.fifth << ((m.predicate == 'serumChol') & (m.object <= '272') & (m.subject == c.first.subject)))
    def absence_heart_desease(c):
        #c.assert_fact({'subject' : c.m.subject, 'predicate' : 'desease', 'object' : 'absence of heart desease'})
        assert_absence(c, c.first.subject)
    
    @when_all(+s.exception)
    def second(c):
        print(c.s.exception)
        c.s.exception = None

    @when_all(+m.subject)
    def output(c):
            if c.m.predicate == 'has':
                print('Fact: {0} {1} {2}'.format(c.m.subject, c.m.predicate, c.m.object))

    
#Rule 4
#if (majorv <= 0.5) and (oldp <= 2.45) and (sc > 272.0)  and (cp <= 3.5) then class: 1 

    @when_any(all(c.first << ((m.predicate == 'has_majorRv') & (m.object <= 0.5)),
            c.second << ((m.predicate == 'has_oldp') & (m.object <= 2.45) & (m.subject == c.first.subject)),           
            c.third << ((m.predicate == 'has_ChestPain') & (m.object <= 3.5) & (m.subject == c.first.subject)), 
            c.fourth << ((m.predicate == 'serumChol') & (m.object > '272') & (m.subject == c.first.subject))))
    def absence_heart_desease(c):
        #c.assert_fact({'subject' : c.m.subject, 'predicate' : 'desease', 'object' : 'absence of heart desease'})
        assert_absence(c, c.first.subject)
    
    @when_all(+s.exception)
    def second(c):
        print(c.s.exception)
        c.s.exception = None

    @when_all(+m.subject)
    def output(c):
            if c.m.predicate == 'has':
                print('Fact: {0} {1} {2}'.format(c.m.subject, c.m.predicate, c.m.object))


#Rule 5
#if (majorv > 0.5)  and (oldp <= 0.5)  and (sex > 0.5)   and (maxhra <= 172.0) then class: 2 

    @when_any(all(c.first << ((m.predicate == 'has_majorRv') & (m.object > 0.5)),
            c.second << ((m.predicate == 'has_oldp') & (m.object <= 0.5) & (m.subject == c.first.subject)),           
            c.third << ((m.predicate == 'is') & (m.object == 'Male') & (m.subject == c.first.subject))),
            c.fourth << ((m.predicate == 'has_MaxHeartRate') & (m.object <= 172.0) & (m.subject == c.first.subject)))
    def presence_heart_desease(c):
        #c.assert_fact({'subject' : c.m.subject, 'predicate' : 'desease', 'object' : 'absence of heart desease'})
        assert_presence(c, c.first.subject) 




#Rule 6
#if (majorv <= 0.5) and (oldp <= 2.45) and (sc > 272.0)  and (cp > 3.5) then class: 2 

    @when_any(all(c.first << ((m.predicate == 'has_majorRv') & (m.object <= 0.5)),
            c.second << ((m.predicate == 'has_oldp') & (m.object <= 2.45) & (m.subject == c.first.subject)),           
            c.third << ((m.predicate == 'has_ChestPain') & (m.object == 'asympomatic') & (m.subject == c.first.subject))))
    def presence_heart_desease(c):
        #c.assert_fact({'subject' : c.m.subject, 'predicate' : 'desease', 'object' : 'absence of heart desease'})
        assert_presence(c, c.first.subject)



#Rule 7
#if (majorv > 0.5)  and (oldp > 0.5)  and (cp <= 3.5)   and (oldp <= 1.9) then class: 1 

    @when_any(all(c.first << ((m.predicate == 'has_majorRv') & (m.object > 0.5)),
            c.second << ((m.predicate == 'has_oldp') & (m.object > 0.5) & (m.subject == c.first.subject)),           
            c.third << ((m.predicate == 'has_oldp') & (m.object <= 1.9) & (m.subject == c.first.subject)), 
            c.fourth <<  ((m.predicate == 'has_ChestPain') & (m.object == 'Typical Angina')|  (m.object == 'Atypical Angina')|(m.object == 'Non-Anginal Pain') & (m.subject == c.first.subject))))
    def absence_heart_desease(c):
        #c.assert_fact({'subject' : c.m.subject, 'predicate' : 'desease', 'object' : 'absence of heart desease'})
        assert_absence(c, c.first.subject)
    
    @when_all(+s.exception)
    def second(c):
        print(c.s.exception)
        c.s.exception = None

    @when_all(+m.subject)
    def output(c):
            if c.m.predicate == 'has':
                print('Fact: {0} {1} {2}'.format(c.m.subject, c.m.predicate, c.m.object))


#Rule 8
#if (majorv > 0.5)  and (oldp <= 0.5) and (sex <= 0.5)   and (sc <= 318.5) then class: 1  

    @when_any(all(c.first << ((m.predicate == 'has_majorRv') & (m.object > 0.5)),
            c.second << ((m.predicate == 'has_oldp') & (m.object <= 0.5) & (m.subject == c.first.subject)),           
            c.third << ((m.predicate == 'is') & (m.object == 'Female') & (m.subject == c.first.subject)), 
            c.fourth << ((m.predicate == 'serumChol') & (m.object <= 318.5) & (m.subject == c.first.subject))))
    def absence_heart_desease(c):
        #c.assert_fact({'subject' : c.m.subject, 'predicate' : 'desease', 'object' : 'absence of heart desease'})
        assert_absence(c, c.first.subject)
    
    @when_all(+s.exception)
    def second(c):
        print(c.s.exception)
        c.s.exception = None

    @when_all(+m.subject)
    def output(c):
            if c.m.predicate == 'has':
                print('Fact: {0} {1} {2}'.format(c.m.subject, c.m.predicate, c.m.object))



#Rule 9
#if (majorv > 0.5)  and (oldp > 0.5)  and (cp <= 3.5)    and (oldp > 1.9) then class: 2 

    @when_any(all(c.first << ((m.predicate == 'has_majorRv') & (m.object > 0.5)),
            c.second << ((m.predicate == 'has_oldp') & (m.object > 0.5) & (m.subject == c.first.subject)),  
            c.third << ((m.predicate == 'has_oldp') & (m.object > 1.9) & (m.subject == c.first.subject)),         
            c.fourth << ((m.predicate == 'has_ChestPain') & (m.object == 'Typical Angina')|(m.object == 'Atypical Angina')|(m.object == 'Non-Anginal Pain') & (m.subject == c.first.subject))))
    def presence_heart_desease(c):
        #c.assert_fact({'subject' : c.m.subject, 'predicate' : 'desease', 'object' : 'absence of heart desease'})
        assert_presence(c, c.first.subject)


#Rule 10
#if (majorv <= 0.5) and (oldp > 2.45) and (oldp <= 4.0)  then class: 2  

    @when_any(all(c.first << ((m.predicate == 'has_majorRv') & (m.object <= 0.5)),
            c.second << ((m.predicate == 'has_oldp') & (m.object > 2.45) & (m.subject == c.first.subject)),           
            c.third <<((m.predicate == 'has_oldp') & (m.object <= 4.0) & (m.subject == c.first.subject))))
    def presence_heart_desease(c):
        #c.assert_fact({'subject' : c.m.subject, 'predicate' : 'desease', 'object' : 'absence of heart desease'})
        assert_presence(c, c.first.subject)


#Rule 11
#if (majorv > 0.5)  and (oldp > 0.5)  and (cp > 3.5) and (sc > 301.0) then class: 2 

    @when_any(all(c.first << ((m.predicate == 'has_majorRv') & (m.object > 0.5)),
            c.second << ((m.predicate == 'has_oldp') & (m.object > 0.5) & (m.subject == c.first.subject)),           
            c.third << ((m.predicate == 'has_ChestPain') & (m.object == 'asympomatic') & (m.subject == c.first.subject)),
            c.fourth << ((m.predicate == 'serumChol') & (m.object > 301.0) & (m.subject == c.first.subject))))
    def presence_heart_desease(c):
        #c.assert_fact({'subject' : c.m.subject, 'predicate' : 'desease', 'object' : 'absence of heart desease'})
        assert_presence(c, c.first.subject)


#Rule 12
#if (majorv > 0.5)  and (oldp <= 0.5) and (sex > 0.5)    and (maxhra > 172.0) then class: 1 

    @when_any(all(c.first << ((m.predicate == 'has_majorRv') & (m.object > 0.5)),
            c.second << ((m.predicate == 'has_oldp') & (m.object <= 0.5) & (m.subject == c.first.subject)),           
            c.third << ((m.predicate == 'has_maxHeartRate') & (m.object > 172.0) & (m.subject == c.first.subject)), 
            c.fourth << ((m.predicate == 'is') & (m.object == 'Male') & (m.subject == c.first.subject))))
    def absence_heart_desease(c):
        #c.assert_fact({'subject' : c.m.subject, 'predicate' : 'desease', 'object' : 'absence of heart desease'})
        assert_absence(c, c.first.subject)
    
    @when_all(+s.exception)
    def second(c):
        print(c.s.exception)
        c.s.exception = None

    @when_all(+m.subject)
    def output(c):
            if c.m.predicate == 'has':
                print('Fact: {0} {1} {2}'.format(c.m.subject, c.m.predicate, c.m.object))



#Rule 13
#if (majorv > 0.5)  and (oldp <= 0.5) and (sex <= 0.5)   and (sc > 318.5) then class: 2   

    @when_any(all(c.first << ((m.predicate == 'has_majorRv') & (m.object > 0.5)),
            c.second << ((m.predicate == 'has_oldp') & (m.object <= 0.5) & (m.subject == c.first.subject)),           
            c.third << ((m.predicate == 'is') & (m.object == 'Female') & (m.subject == c.first.subject)),
            c.fourth << ((m.predicate == 'serumChol') & (m.object > 318.5) & (m.subject == c.first.subject))))
    def presence_heart_desease(c):
        #c.assert_fact({'subject' : c.m.subject, 'predicate' : 'desease', 'object' : 'absence of heart desease'})
        assert_presence(c, c.first.subject)



#Rule 14
#if (majorv <= 0.5) and (oldp > 2.45) and (oldp > 4.0)   then class: 1  

    @when_any(all(c.first << ((m.predicate == 'has_majorRv') & (m.object <= 0.5)),
            c.second << ((m.predicate == 'has_oldp') & (m.object > 2.45) & (m.subject == c.first.subject)),           
            c.third << ((m.predicate == 'has_oldp') & (m.object > 4.0) & (m.subject == c.first.subject))))
    def absence_heart_desease(c):
        #c.assert_fact({'subject' : c.m.subject, 'predicate' : 'desease', 'object' : 'absence of heart desease'})
        assert_absence(c, c.first.subject)
    
    @when_all(+s.exception)
    def second(c):
        print(c.s.exception)
        c.s.exception = None

    @when_all(+m.subject)
    def output(c):
            if c.m.predicate == 'has':
                print('Fact: {0} {1} {2}'.format(c.m.subject, c.m.predicate, c.m.object))


##Patient Examples
# Patient 262
assert_fact('heart', {'subject': '262', 'predicate': 'has_oldp', 'object': 1.8})
assert_fact('heart', {'subject': '262', 'predicate': 'has_maxHeartRate', 'object': 160})
assert_fact('heart', {'subject': '262', 'predicate': 'has_majorRv', 'object': 0})
assert_fact('heart', {'subject': '262', 'predicate': 'has_rBloodPress', 'object': 120})
assert_fact('heart', {'subject': '262', 'predicate': 'age', 'object': 58})
assert_fact('heart', {'subject': '262', 'predicate': 'is', 'object': 'Male' })
assert_fact('heart', {'subject': '262', 'predicate': 'has_ChestPain', 'object': 'atypical angina'})
assert_fact('heart', {'subject': '262', 'predicate': 'serumChol', 'object': 284})
assert_fact('heart', {'subject': '262', 'predicate': 'has_rECG', 'object': 'hypertrophy'})
assert_fact('heart', {'subject': '262', 'predicate': 'has_exia', 'object': 'No'})
assert_fact('heart', {'subject': '262', 'predicate': 'has_slope', 'object': 'flat'})
assert_fact('heart', {'subject': '262', 'predicate': 'has_thal', 'object': 'normal'})

#Patient 216
assert_fact('heart', {'subject': '216', 'predicate': 'hasAge', 'object': 63})
assert_fact('heart', {'subject': '216', 'predicate': 'is', 'object': 'Female'})
assert_fact('heart', {'subject': '216', 'predicate': 'has_ChestPain', 'object': 'non anginal pain'})
assert_fact('heart', {'subject': '216', 'predicate': 'has_rBloodPress', 'object': 135})
assert_fact('heart', {'subject': '216', 'predicate': 'has_serumChol', 'object': 252})
assert_fact('heart', {'subject': '216', 'predicate': 'has_rECG', 'object': 'hypertrophy'})
assert_fact('heart', {'subject': '216', 'predicate': 'has_maxHeartRate', 'object': 172})
assert_fact('heart', {'subject': '216', 'predicate': 'has_exia', 'object': 'No'})
assert_fact('heart', {'subject': '216', 'predicate': 'has_oldp', 'object': 0})
assert_fact('heart', {'subject': '216', 'predicate': 'has_slope', 'object': 'upsloping'})
assert_fact('heart', {'subject': '216', 'predicate': 'has_majorRv', 'object': 0})
assert_fact('heart', {'subject': '216', 'predicate': 'has_thal', 'object': 'normal'})

# Patient 194
assert_fact('heart', {'subject': '194', 'predicate': 'hasAge', 'object': 48})
assert_fact('heart', {'subject': '194', 'predicate': 'is', 'object': 'Male'})
assert_fact('heart', {'subject': '194', 'predicate': 'has_ChestPain', 'object': 'non anginal pain'})
assert_fact('heart', {'subject': '194', 'predicate': 'has_rBloodPress', 'object': 124})
assert_fact('heart', {'subject': '194', 'predicate': 'has_serumChol', 'object': 255})
assert_fact('heart', {'subject': '194', 'predicate': 'has_rECG', 'object': 'normal'})
assert_fact('heart', {'subject': '194', 'predicate': 'has_maxHeartRate', 'object': 175})
assert_fact('heart', {'subject': '194', 'predicate': 'has_exia', 'object': 'No'})
assert_fact('heart', {'subject': '194', 'predicate': 'has_oldp', 'object': 0})
assert_fact('heart', {'subject': '194', 'predicate': 'has_slope', 'object': 'upsloping'})
assert_fact('heart', {'subject': '194', 'predicate': 'has_majorRv', 'object': 2})
assert_fact('heart', {'subject': '194', 'predicate': 'has_thal', 'object': 'normal'})
