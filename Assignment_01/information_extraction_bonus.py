from __future__ import print_function
import re
import spacy

###Hao Cheng--assignment_01_bonus


nlp = spacy.load('en')
re_spaces = re.compile(r'\s+')


class Person(object):
    def __init__(self, name, likes=None, has=None, travels=None):
        """
        :param name: the person's name
        :type name: basestring
        :param likes: (Optional) an initial list of likes
        :type likes: list
        :param dislikes: (Optional) an initial list of likes
        :type dislikes: list
        :param has: (Optional) an initial list of things the person has
        :type has: list
        :param travels: (Optional) an initial list of the person's travels
        :type travels: list
        """
        self.name = name
        self.likes = [] if likes is None else likes
        self.has = [] if has is None else has
        self.travels = [] if travels is None else travels

    def __repr__(self):
        return self.name


class Pet(object):
    def __init__(self, pet_type, pet_owner, name=None):
        self.name = name
        self.type = pet_type
        self.owner = pet_owner

    def __repr__(self):
        return "%s's %s: %s " % (self.owner, self.type, self.name)


class Trip(object):
    def __init__(self, time, name, destination_to):

        self.departs_to = destination_to
        self.time = time
        self.name = name

    def __repr__(self):
        return "%s's trip to : %s: in: %s " % (self.name, self.departs_to, self.time)

persons = []
pets = []
trips = []
root = None



def select_person(name):
    for person in persons:
        if person.name == name:
            return person


def add_person(name):
    person = select_person(name)

    if person is None:
        new_person = Person(name)
        persons.append(new_person)

        return new_person

    return person


def select_pet_owner(owner):
    for pet in pets:
        if pet.owner == owner:
            return pet


def add_pet(type, owner, name=None):


    pet = select_pet_owner(owner)

    if pet is None:
        new_pet = Pet(type, owner,name)
        pets.append(new_pet)
        return new_pet

    return pet


def get_persons_pet(person_name):

    person = select_person(person_name)

    for thing in person.has:
        if isinstance(thing, Pet):
            return thing


def select_trip(time,name):
    for trip in trips:
        if trip.name==name and trip.time==time:
            return trip

def add_trip(time, name, destination_to=None):
    trip = select_trip(time,name)

    if trip is None:
        new_trip=Trip(time, name, destination_to)
        trips.append(new_trip)

        return new_trip

    return trip




##def process_relation_triplet(triplet):
    """
    find relations of types:
    (PERSON, likes, PERSON)
    (PERSON, has, PET)
    (PET, has_name, NAME)
    (PERSON, travels, TRIP)
    (TRIP, departs_on, DATE)
    (TRIP, departs_to, PLACE)

    :param triplet: The relation triplet from ClausIE
    :type triplet: tuple
    :return: a triplet in the formats specified above
    :rtype: tuple
    """

    ###sentence = triplet.subject + ' ' + triplet.predicate + ' ' + triplet.object
def process_data_from_input_file(file_path = './assignment_01.txt'):
    with open(file_path) as infile:
        cleaned_lines = [line.strip() for line in infile if not line.startswith(('$$$', '###', '==='))]


    for sentence in cleaned_lines:
        print(sentence)
        doc = nlp(unicode(sentence))

        for t in doc:
            if t.pos_ == 'VERB' and t.head == t:
               root = t



    # CURRENT ASSUMPTIONS:
    # - People's names are unique (i.e. there only exists one person with a certain name).
    # - Pet's names are unique
    # - The only pets are dogs and cats
    # - Only one person can own a specific pet
    # - A person can own only one pet



    # Process (PERSON, likes, PERSON) relations
        if root.lemma_ == 'like' and 'does' not in sentence:
            for f in doc:
                if f.dep_ == 'nsubj':
                    if f.text in[e.text for e in doc.ents if e.label_ == 'PERSON' or e.label_ == 'ORG']:
                        s = add_person(f.text)
            for g in doc:
                if g.dep_ == 'pobj':
                    if g.text in [e.text for e in doc.ents if e.label_ == 'PERSON'or (e.label_ == 'ORG')]:
                        o = add_person(g.text)
                        s.likes.append(o)



        if root.lemma_ == 'be':
            for h in doc:
                if h.dep_ == 'attr' and h.text == 'friends' and 'with' in sentence:
                    fw_doc = nlp(unicode(sentence))
                    with_token = [t for t in fw_doc if t.text == 'with'][0]
                    fw_who = [t for t in with_token.children if t.dep_ == 'pobj'][0].text

            for n in doc:
                 if n.dep_ == 'nsubj':
                     if n.text in [e.text for e in doc.ents if e.label_ == 'PERSON'] and fw_who in [e.text for e in doc.ents if e.label_ == 'PERSON']:
                         s = add_person(n.text)
                         o = add_person(fw_who)
                         s.likes.append(o)
                         o.likes.append(s)




        # Process (PERSON, has, PET)
        if root.lemma_ == 'have':
            for m in doc:
                # print(list(m.rights))
                if m.dep_ == 'dobj' and (m.text == 'dog' or m.text == 'cat'):
                    subject = list(root.lefts)[0]
                    print(subject)
                    if len(list(m.rights))>0:
                        object = list(m.rights)[0]
                        if 'named' == object.text:
                            x = add_person(subject.text)
                            pet_name = list(object.rights)[0].text
                            x_pet_type = 'dog' if m.text == 'dog' else 'cat'
                            pet = add_pet(x_pet_type, x, pet_name)
                            x.has.append(pet)

                        else:
                            x = add_person(subject.text)
                            x_pet_type = 'dog' if m.text == 'dog' else 'cat'
                            pet = add_pet(x_pet_type, x)
                            x.has.append(pet)

                        print(object)
                        print(list(object.rights)[0])


        if root.lemma_ == 'be':
            for m in doc:
                print(m.text, ':', m.dep_, m.ent_type_)
                if m.dep_ == 'nsubj' and m.text == 'name':
                    if 'dog' in sentence or 'cat' in sentence:
                        s_people = [token.text for token in doc if token.ent_type_ == 'PERSON']
                        print(s_people[0])
                        person1 = add_person(s_people[0])
                        pet_name = [token.text for token in doc if token.ent_type_ == 'PERSON'][1]
                        s_pet_type = 'dog' if 'dog' in sentence else 'cat'
                        pet = add_pet(s_pet_type, person1, pet_name)

                        person1.has.append(pet)



        # Process(Person, departs_to, place)
        if [e.text for e in doc.ents if e.label_ == 'GPE']:
            personname = [e.text for e in doc.ents if e.label_ == 'PERSON' or e.label_ == 'ORG']
            date = [str(e.text) for e in doc.ents if e.label_ == 'DATE']
            place = [str(e.text) for e in doc.ents if e.label_ == 'GPE']
            for person in personname:
                s = add_person(person)
                o = add_trip(date, s.name, place)
                s.travels.append(o)



def preprocess_question(question):
    # remove articles: a, an, the

    q_words = question.split(' ')

    # when won't this work?
    for article in ('a', 'an', 'the'):
        try:
            q_words.remove(article)
        except:
            pass

    return re.sub(re_spaces, ' ', ' '.join(q_words))



def answer_question(question=' '):
    while question[-1] != '?':
        question = raw_input("Please enter your question: ")

        if question[-1] != '?':
            print('This is not a question... please try again')

        else:
            question_over = preprocess_question(question)
            break


    doc = nlp(unicode(question_over))

    for t in doc:
        if t.pos_ == 'VERB' and t.head == t:
            root = t



    # 1) Who has a <pet_type>? (e.g. Who has a dog?)
    for m in doc:

        if m.dep_ == 'nsubj' and  m.text.lower() == 'who' and 'dog' in question_over or 'cat' in question_over:
            answer = '{} has a {} named {}.'
            pet_type = 'dog' if 'dog' in question_over else 'cat'

            for person in persons:
                # print(person)
                pet = get_persons_pet(person.name)
                if pet and pet.type == pet_type:
                    print(answer.format(person.name, pet_type, pet.name))



    # 2) Who is [going to|flying to|traveling to] <place>? (e.g. Who is flying to Japan?)
    for m in doc:
        if m.dep_ == 'nsubj' and m.text.lower() == 'who' and (root.lemma_ == 'go' or root.lemma_ ==  'fly' or root.lemma_ == 'travel'):
            answer = '{} is going to {}, time:{}'
            qdoc = nlp(unicode(question_over))
            place = [t.text for t in qdoc.ents if t.label_=='GPE']
            for trip in trips:
                if trip.departs_to [0] == place[0]:
                   print(answer.format(trip.name,trip.departs_to[0], trip.time[0]))


    # 3) Does <person> like <person>? (e.g. Does Bob like Sally?)
    for m in doc:
        if m.dep_ == 'aux' and m.text.lower() == 'does' and 'like' in question_over and 'who' not in question_over.lower():
                list = [e.text for e in doc.ents if e.label_ == 'PERSON']
                person_sub = list[0]
                person_obj = list[1]
                x = 0
                for person in persons:
                    if person.name == person_sub:
                        for person1 in person.likes:
                            if person1.name == person_obj:

                                x = 1

                if x:
                    print("Yes.")
                else:
                    print("No")



    # 4) When is <person> [going to|flying to|traveling to] <place>?
    for m in doc:
            if m.dep_ == 'advmod' and m.text.lower() == 'when' and (root.lemma_ == 'fly' or root.lemma_ == 'go' or root.lemma_ == 'travel'):
                qdoc=nlp(unicode(question_over))
                personA = [e.text for e in qdoc.ents if e.label_ == 'PERSON' or (e.label_ == 'ORG')][0]
                placeA = [e.text for e in qdoc.ents if e.label_ == 'GPE'][0]
                a = select_person(personA)
                # print(a)
                for trip in a.travels:
                    r=str(trip.departs_to[0])
                    if r == placeA and len(trip.time) >0:
                        print(trip.time)



    # 5) Who likes <person>?
    for m in doc:
            if m.dep_ == 'nsubj' and m.text.lower() == 'who' and root.lemma_ == 'like':
                qdoc = nlp(unicode(question_over))
                personB = [e.text for e in qdoc.ents if e.label_ == 'PERSON'][0]
                for person in persons:
                    for person_like in person.likes:
                        if person_like.name == personB:
                            print(person)

    # 6) Who does <person> like?
    for m in doc:
            if m.dep_ == 'aux' and m.text.lower() == 'does' and 'like' in question_over and 'who' in question_over.lower():
                qdoc=nlp(unicode(question_over))
                personD = [e.text for e in qdoc.ents if e.label_ == 'PERSON' or (e.label_ == 'ORG') ][0]
                n = add_person(personD)
                for person in n.likes:
                        print(person)



def main():

    process_data_from_input_file()
    print(persons)
    print(pets)
    print(trips)
    answer_question()
if __name__ == '__main__':
        main()
