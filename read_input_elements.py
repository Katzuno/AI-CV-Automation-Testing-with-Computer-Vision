from Parameters import *
import numpy as np
import glob
import cv2 as cv


class Reader:
    def __init__(self):
        self.params: Parameters = Parameters()
        self.gui_elements_path_npy = os.path.join(self.params.save_directory, 'gui_descriptors.npy')
        self.gui_elements = []

        self.state_change_inputs_path_npy = os.path.join(self.params.save_directory, 'input_descriptors.npy')
        self.state_change_inputs = []

        self.video_file_frames_path_npy = os.path.join(self.params.save_directory, 'video_frames.npy')
        self.video_frames = []

    def read_gui_elements(self):
        images_path = os.path.join(self.params.gui_elements_path, '*.png')
        files = glob.glob(images_path)
        num_images = len(files)
        self.gui_elements = []
        for i in range(num_images):
            print('Citim elementul GUI numarul %d...' % i)
            img = cv.imread(files[i])
            self.gui_elements.append(img)
        self.gui_elements = np.array(self.gui_elements)

    def read_state_change_inputs(self):
        inputs_path = os.path.join(self.params.state_change_inputs_path, '*.png')
        files = glob.glob(inputs_path)
        num_images = len(files)
        self.state_change_inputs = []
        for i in range(num_images):
            print('Citim input-ul schimbator numarul %d...' % i)
            img = cv.imread(files[i])
            self.state_change_inputs.append(img)
        self.state_change_inputs = np.array(self.state_change_inputs)

    def load_gui_elements(self):
        if os.path.exists(self.gui_elements_path_npy):
            self.gui_elements = np.load(self.gui_elements_path_npy, allow_pickle=True)
            print('Am incarcat descriptorii pentru elementele de GUI')
        else:
            print('Citim descriptorii pentru elementele de GUI:')
            self.read_gui_elements()
            np.save(self.gui_elements_path_npy, self.gui_elements)
            print('Am salvat elementele de GUI in fisierul %s' % self.gui_elements_path_npy)

        if os.path.exists(self.state_change_inputs_path_npy):
            self.state_change_inputs = np.load(self.state_change_inputs_path_npy, allow_pickle=True)
            print('Am incarcat descriptorii pentru inputurile de stare')
        else:
            print('Citim descriptorii pentru inputurile de stare:')
            self.read_state_change_inputs()
            np.save(self.state_change_inputs_path_npy, self.state_change_inputs)
            print('Am salvat inputurile de stare in fisierul %s' % self.state_change_inputs_path_npy)

    def read_video(self, filename):
        vidcap = cv.VideoCapture(os.path.join(self.params.video_directory, filename))
        success, image = vidcap.read()
        count = 0
        while success:
            self.video_frames.append(image)
            cv.imwrite("saved_data/frames/frame_%d.jpg" % count, image)  # save frame as JPEG file
            success, image = vidcap.read()
            # print('Read a new frame: ', success)
            count += 1
        self.video_frames = np.array(self.video_frames)

    def load_video(self, filename):
        if os.path.exists(self.video_file_frames_path_npy):
            self.video_frames = np.load(self.video_file_frames_path_npy, allow_pickle=True)
            print('Am incarcat frame-urile videoului')
        else:
            print('Citim descriptorii pentru frame-urile din video:')
            self.read_video(filename)
            np.save(self.video_file_frames_path_npy, self.video_frames)
            print('Am salvat frameurile video in fisierul %s' % self.video_file_frames_path_npy)


