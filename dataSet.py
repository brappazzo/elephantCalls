from matplotlib import pyplot as plt and import mlab as ml 
from scikits.audiolab import Sndfile


f = Sndfile('test.flac', 'r')

[spectrum, freqs, t] = specgram(f.get_frames(20000),
