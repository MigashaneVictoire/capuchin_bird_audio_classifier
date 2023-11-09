import tansorflow as tf
import matplotlib.pyblot as plt
import tensorflow_io as tfio
import os

def load_wave_16hz_mono(filename):
    # read encoded wave file
    file_content = tf.io.read_file(filename)
    # decode wav file in single channel
    wav, sample_rate = tf.audio.decode_wav(file_content, desired_channels=1)
    # remove trailing axis
    wav = tf.squeeze(wav, axis= -1)
    sample_rate = tf.cast(sample_rate, dtype=tf.int64)
    
    wav = tfio.audio.resample(waav, rate_im=sample_rate, rate_out=18000)
    return wav
    
    