# import time
# from multiprocessing.pool import ThreadPool as Pool
# # from multiprocessing import Pool
# from random import randint
# from time import sleep
#
#
# def process_line(l):
#     #print ( "started", l)
#     sleep(2)
#     #print ("done", l)
#
#
# def get_next_line():
#     with open("/Users/rahul.prajapati/rahul/out.csv", 'r') as f:
#         for line in f:
#             yield line

# def run():
#     f = get_next_line()
#
#     t = Pool(processes=4)
#
#     for i in f:
#         t.map(process_line, (i,))
#     t.close()
#     t.join()
#
# print('starting itme ')
# t1 = time.time()
# run()
# t2 = time.time()
# print('total time ', t2-t1)
#





import os, multiprocessing as mp
import time


# process file function
import csv
def processfile(file, start=0, stop=0):
    results = []
    with open(file, 'r') as fh:

        if start == 0 and stop == 0:
            for line in fh:
                #time.sleep(1)
                #results[line] = (line, 'yes', 'yes]')
                results.append((line, 'yes', 'yes]'))
                #yield line
        else:
            fh.seek(start)
            lines = fh.readlines(stop - start)
            print('processin===', len(lines))
            for line in lines:
                #time.sleep(1)
                #results.append(line)
                #results[line] = 'yes'
                results.append((line, 'yes', 'yes'))
                #yield line
    return results
    #
    # if
    #     #... process entire file...
    # else:
    #
    #         #... process these lines ...
    #
    # return results

def run():
    filename = '/Users/rahul.prajapati/rahul/out.csv'
    filesize = os.path.getsize(filename)
    #split_size = 100*1024*1024
    split_size = 700
    #assert False, f' '
    # determine if it needs to be split
    if filesize > split_size:

        # create pool, initialize chunk start location (cursor)
        pool = mp.Pool(4)
        cursor = 0
        results = []
        with open(filename, 'r') as fh:

            # for every chunk in the file...

            #assert False, f'=== {filesize // split_size}, {filesize} ,  {split_size}'
            for chunk in range(filesize // split_size):

                # determine where the chunk ends, is it the last one?
                if cursor + split_size > filesize:
                    end = filesize
                else:
                    end = cursor + split_size

                # seek to end of chunk and read next line to ensure you
                # pass entire lines to the processfile function
                fh.seek(end)
                fh.readline()

                # get current file location
                end = fh.tell()

                # add chunk to process pool, save reference to get results
                proc = pool.apply_async(processfile, args=[filename, cursor, end])
                results.append(proc)
                #assert False, '='
                # setup next chunk
                cursor = end

        # close and wait for pool to finish
        pool.close()
        pool.join()

        # iterate through results
        with open('/Users/rahul.prajapati/rahul/output.csv', 'w') as h:
            for proc in results:
                assert False, proc.get()
#                processfile_result = proc.get()

                assert  False, processfile_result
                h.write(len(processfile_result))
                #assert False, processfile_result

#     #else:
t1 = time.time()
run()
t2 = time.time()
print('---unning time ', t2-t1)


# def run1():
#     #f = get_next_line()
#     processfile('/Users/rahul.prajapati/rahul/out.csv')
#
# print('\n\nstarting itme 222222')
# t1 = time.time()
# run1()
# t2 = time.time()
# print('total time ', t2-t1)


# with open('/Users/rahul.prajapati/rahul/output.csv', 'r') as h:
#     line = h.readlines()
#     with open('/Users/rahul.prajapati/rahul/out.csv', 'r') as h1:
#         line2 = h1.readlines()
#         for i in line:
#             print(i)
#             break
#         for i in line2:
#             print(i)
#             if i not in line:
#                 print('invalid')
#                 break
