import cv2
import os

class Image2Video(object):
    def __init__(self, img_dir, img_type, vid_name, vid_type):
        self.img_dir = img_dir
        self.img_type = img_type
        self.vid_name = vid_name
        self.vid_type = vid_type

    def convert(self):
        images = [img for img in os.listdir(self.img_dir) if img.endswith('.' + self.img_type)]
        os.chdir(self.img_dir)
        print('gathering images...')
        images.sort(key=lambda x: os.path.getmtime(x))
        os.chdir('..')

        frame = cv2.imread(os.path.join(self.img_dir, images[0]))
        height, width, layers = frame.shape

        video = cv2.VideoWriter(self.vid_name + '.' + self.vid_type, 0, 1, (width,height))

        print('writting video...')
        for image in images:
            video.write(cv2.imread(os.path.join(self.img_dir, image)))

        cv2.destroyAllWindows()
        video.release()

        print('image2video complete')
