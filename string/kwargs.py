"""kwargs :-  It's datatype is dict.
In function it returns all dict. elements """


def fun(**d):
    print(d)   # convert input elements in dict form
    for i, j in d.items():
        print(i, j)


fun(ram=1, shyam=2, roy=3, mohan=4)
