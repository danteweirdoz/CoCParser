import sys
from skimage import data, io, filter
import numpy as np

def parse(filename):
    image = io.imread(filename, as_grey = True)

    ff = filter.canny(image)
    # io.imshow(ff)

    pi = 0
    for i in xrange(len(ff)):
        cnt = np.count_nonzero(ff[i])
        if cnt > 800:
            diff = i - pi
            if diff > 50 and diff < 60:
                slit = image[i-52:i]
                yield slit
                # data = slit.flatten()
                # yield data
                # io.imshow(slit)
            if __name__ == "__main__":
                print i, cnt, i-pi
            pi = i
        # , ff[i].choose(set([True]))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit(-1)
    for row in parse(sys.argv[-1]):
        print row
