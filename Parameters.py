import os

class Parameters:
    def __init__(self):
        self.base_dir = 'data'
        self.gui_elements_path = os.path.join(self.base_dir, 'gui_elements')
        self.state_change_inputs_path = os.path.join(self.base_dir, 'state_change_inputs')
        self.save_directory = 'saved_data'
        self.video_directory = os.path.join(self.base_dir, 'videos')