import logging

logging.basicConfig(filename="test.log",level=logging.INFO)
logging.info = "This is my Information."
logging.error = "This is my error."
logging.critical = "This is my critical."
logging.noset = "this is my notset"
logging.warning = "This is my warning"
logging.debug = "this is my debug."

logging.shutdown()

##############################
logging.basicConfig(filename = "shally.log", level=logging.DEBUG, format="%(asctime)s %(message)s")
logging.debug = "this is my debug."
logging.warning = "This is my warning"
logging.info = "This is my Information."

###############################
logging.basicConfig(filename = "shally.log", level=logging.DEBUG, format="%(asctime)s %(name)s %(levelname)s %(message)s")
logging.debug = "this is my debug."
logging.warning = "This is my warning"
logging.info = "This is my Information."

################################
l = [1,2,3,[4,5,6,7,8],"shally","harpreet"]
l1_int = []
l2_str = []
for i in l : 
    logging.info("this is the start of my first for loop {}".format(l))
    logging.info("this is the value of i am logging {}".format(i))
    if type(i) == list:
        for j in i :
            logging.info("logggin my j {j} and i is {i}".format(i = i ,j = j))
            if type(j) == int :
                l1_int.append(j)
    elif type(i) == int :
        l1_int.append(i)
        
    else :
        if type(i) == str:
            l2_str.append(i)
logging.info("this is my final result  with all int {l1} ,with all str{l2}".format(l1 =l1_int ,l2 =l2_str ))





