#!/usr/bin/python3

import sys
import image2video as i2v

def main(img_dir, img_type, vid_name, vid_type):
    movie_maker = i2v.Image2Video(img_dir, img_type, vid_name, vid_type)
    movie_maker.convert()

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
