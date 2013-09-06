import os
print "os.path.abspath:", os.path.abspath(__file__)
print "os.path.split:", os.path.split(os.path.abspath(__file__))
print "os.path.split[0]:", os.path.split(os.path.abspath(__file__))[0]
print "os.path.dirname:", os.path.dirname(os.path.split(os.path.abspath(__file__))[0])
print "os.path.join:", os.path.join(os.path.dirname(os.path.split(os.path.abspath(__file__))[0]),
                                                    "outputs")
