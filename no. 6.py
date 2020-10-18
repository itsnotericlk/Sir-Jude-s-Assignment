#def converter(histogram):
    #for i in histogram:
        #a = print('*' * i)
    #return a

#def main():
    #histogram = [int(x) for x in input("Input numbers:").split()]
    #print(histogram)
    #converter(histogram)

def histogram( items ):
    for n in items:
        output = ''
        times = n
        while( times > 0 ):
          output += '*'
          times = times - 1
        print(output)
        histogram = [4, 9, 7]