#     |               |                                 |
                
#                 |                                                |            |                                   |                               |                           |                               |                           |                               |                                |                               |
#          |                                  |                                     |
                
#                 |                     |                                                     |                                   |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
#  |                          |                       |                    |
#          |                                    |                                         |     |                    |                                    | |     |                    |                                    | |     |                    |                                    |      |     |                                                        |
#     |                        |                                 |      |                                |                       |                    |                |                       |                    |                |                       |                    |                     |                       |                    |
                
#                     |                                                |      |                                   |                               |                         |                               |                         |                               |                              |                               |
#          |                                   |                               |                   |                                |                       |                    |          |                                |                       |                    |          |                                |                       |                    |               |                                |                                        |
                
#                 |                     |
#  |                                |                       |                    |            |                                |                       |                    |     |                                |                       |                    |     |                                |                       |                              |                                |
#          |                               |                                         |                              |                       |                    |                           |                       |                    |                           |                       |                    |                                |                       |                    |
                
#  |         |                                   PRESENTATION                                                |                                |                    |   |                                |                    |   |                                |                    |        |                                |                    |
#                                                                                                                              |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
#               |                             /                 \                          |                                                                              |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
                
#       |                               convert images between various 

#                                   formats. Users can select a single file,  
              
#                            an entire folder, or all subfolders for conversion, 

#                       retaining the same folder architecture in the output directory.                                                                       |               |                                           |               |                                           |                    |                                           |
#                          /                      |    v    |                    \
#                            
#                https://github.com/SECRET-GUEST/tiny-scripts/tree/ALL/python/Photos/Converter |                                |                                          |      |                                |                                          |      |                                |                                          |           |                                |  
#     |                  !      |                                   |     |                                |                       |                    |                |                       |                    |                |                       |                    |                    |                                           |
#                               |                                   |     |                  
#                  |            |                   Anyway          !                        |                                         |                                |                       |                    |                |                       |                    |                |                       |                    |                    |
                
#             |                      |                 have                                                 |                        |                                         |                                |                       |                    |                |                       |                    |                |                       |                    |                     |                                           |
                

#                |                                  FUN         |                        |                                         |                                |                       |                    |                |                       |                    |                |                       |                    |                    |                                                                      |
                
#                                                        =)
                
#
#                               |                      or                                       |                                                            |                    |                |                       |                    |                |                       |                    |                    |                                           |
                

#             |                              |       DIE ! ! !        |                       |                            |                |                       |                    |                |                       |                    |                    |                                           |#     |                        |                                         |                                |
                
#
#                                                    !                                       |                                |                    |  |                                |                    |  |                                |                    |       |                                |                    |
                
#     |               |                                 !
                
#                 |                                                |            |                                   |                               |                           |                               |                           |                               |                                |                               |
#          |                                  !                                     |
                
#                 |                     |                                                     |                                   |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
#  |                          |                       |                    !
#          |                                    |                                         |     |                    |                                    | |     |                    |                                    | |     |                    |                                    |      |     |                    |                                    |
#     |                        |                                 |      |                                |                       |                    |                |                       |                    |                |                       |                    |                    |                                           |
                
#                     |                                                |      |                                   |                               |                         |                               |                         |                               |                              |                               |
#          |                                   |                               |                   |                                |                       |                    |          |                                |                       |                    |          |                                |                       |                    |               |                                                                |
              
#_ _  _ ____ ___ ____ _    _    ____ ___ _ ____ _  _
#| |\ | [__   |  |__| |    |    |__|  |  | |  | |\ |
#| | \| ___]  |  |  | |___ |___ |  |  |  | |__| | \|
        

import os, rawpy
from PIL import Image
from PyQt5.QtWidgets import  QFileDialog, QVBoxLayout, QPushButton, QWidget, QLabel, QComboBox,QMessageBox,QHBoxLayout #,QApplication


#___  ____ _ _ _ ____ ____    ___  _    ____ _  _ ___
#|__] |  | | | | |___ |__/    |__] |    |__| |\ |  |
#|    |__| |_|_| |___ |  \    |    |___ |  | | \|  |
                
#OPENING | https://www.youtube.com/watch?v=_85LaeTCtV8 :3


class imgConverter(QWidget):
    def __init__(self):
        super().__init__()

        # Supported image formats
        self.supported_formats = ["arw", "jpg", "png", "tiff", "ico", "bmp"]
        self.supported_output_formats = ["jpg", "png", "tiff", "ico", "bmp"] 

        self.GUI()



    # Select the source file or folder
    def select_source(self):
        conversion_mode = self.conversion_mode_combobox.currentText()
        if conversion_mode == "File":
            self.source_path, _ = QFileDialog.getOpenFileName(self, "Choose file", "", "Images (*.arw *.jpg *.png *.tiff *.ico *.bmp)")
        elif conversion_mode == "Folder" or conversion_mode == "All subfolders":
            self.source_path = QFileDialog.getExistingDirectory(self, "Input folder")

        # Check if source_path is defined
        if hasattr(self, 'source_path') and self.source_path:
            self.start_conversion_button.setEnabled(True)   



    def convert_single(self, file_path, input_format, output_format):

        # Construisez le chemin de sortie en utilisant le même nom de fichier que l'entrée, mais avec la nouvelle extension
        output_path = os.path.join(self.output_directory, os.path.basename(file_path))
        output_path = os.path.splitext(output_path)[0] + '.' + output_format

        # If either input or output format is not selected, show a message and exit
        if not input_format or not output_path:
            QMessageBox.information(self, "Information", "No format selected")
            return  

        # If the input format is 'arw', use rawpy to process it, else use PIL
        if input_format == 'arw':
            with rawpy.imread(file_path) as raw:
                image_data = raw.postprocess()
        else:
            image_data = Image.open(file_path)  

        # Save the image using output_path
        image_data.save(output_path)    



    def conversion(self):
        self.start_conversion_button.setEnabled(False)
        format_out = self.output_format_combobox.currentText()  # Output Format
        mode_conversion = self.conversion_mode_combobox.currentText()  # Conversion Mode

        # Ask the user to select an output directory
        self.output_directory = QFileDialog.getExistingDirectory(self, "Output folder")
        if not self.output_directory:
            self.start_conversion_button.setEnabled(True)
            return


        if mode_conversion == "File":  # Single File
            input_format = os.path.splitext(self.source_path)[1].lower()[1:]
            self.convert_single(self.source_path, input_format, format_out)


        else:
            input_format = self.input_format_combobox.currentText()  # Input Format
            if mode_conversion == "Folder":  # Folder
                for file in os.listdir(self.source_path):
                    if file.lower().endswith(f".{input_format}"):
                        file_path = os.path.join(self.source_path, file)  # File Path
                        self.convert_single(file_path, input_format, format_out)

            else:  # All Subfolders
                for root, _, files in os.walk(self.source_path):
                    for file in files:
                        if file.lower().endswith(f".{input_format}"):
                            file_path = os.path.join(root, file)  # File Path
                            relative_path = os.path.relpath(file_path, self.source_path) # Relative Path from the source directory
                            output_relative_path = os.path.splitext(relative_path)[0] + '.' + format_out # Add the output extension
                            output_path = os.path.join(self.output_directory, output_relative_path)
                            output_folder = os.path.dirname(output_path)

                            # Create the folder if it doesn't exist
                            if not os.path.exists(output_folder):
                                os.makedirs(output_folder)

                            self.convert_single(file_path, input_format, format_out)  # Pass the output path instead of the format



        self.start_conversion_button.setEnabled(True)
        QMessageBox.information(self, "Information", "Done !")






#____ ____ ____ ___  _  _ _ ____ ____ _       _  _ ____ ____ ____    _ _  _ ___ ____ ____ ____ ____ ____ ____ 
#| __ |__/ |__| |__] |__| | |    |__| |       |  | [__  |___ |__/    | |\ |  |  |___ |__/ |___ |__| |    |___ 
#|__] |  \ |  | |    |  | | |___ |  | |___    |__| ___] |___ |  \    | | \|  |  |___ |  \ |    |  | |___ |___ 
   

    def GUI(self):

        #Widgets
        self.select_source_button = QPushButton('Folder source', self)
        self.select_source_button.clicked.connect(self.select_source)

        self.start_conversion_button = QPushButton('Convert', self)
        self.start_conversion_button.clicked.connect(self.conversion)
        self.start_conversion_button.setEnabled(False)

        self.conversion_mode_combobox = QComboBox(self)
        self.conversion_mode_combobox.addItems(["File", "Folder", "All subfolders"])

        self.input_format_combobox = QComboBox(self)
        self.input_format_combobox.addItems(self.supported_formats)
        self.input_format_combobox.setToolTip("Input")


        self.output_format_combobox = QComboBox(self)
        self.output_format_combobox.addItems(self.supported_output_formats)  
        self.output_format_combobox.setToolTip("Output")

        #Layout
        self.HLayConverter = QHBoxLayout()
        self.HLayConverter.addWidget(self.input_format_combobox)
        self.HLayConverter.addStretch(1)
        self.HLayConverter.addWidget(QLabel('<b>> >>> ></b>'))
        self.HLayConverter.addStretch(1)
        self.HLayConverter.addWidget(self.output_format_combobox)

        self.VLayConverter = QVBoxLayout()
        self.VLayConverter.addWidget(self.select_source_button)
        self.VLayConverter.addWidget(self.conversion_mode_combobox)
        self.VLayConverter.addLayout(self.HLayConverter) 
        self.VLayConverter.addWidget(self.start_conversion_button)

        self.setLayout(self.VLayConverter)



#____ ____ ____ _  _ ____ ___    _    ____ _  _ _  _ ____ _  _
#|__/ |  | |    |_/  |___  |     |    |__| |  | |\ | |    |__|
#|  \ |__| |___ | \_ |___  |     |___ |  | |__| | \| |___ |  |
                
#ENDING | https://www.youtube.com/watch?v=CgZVrvQZB6U&ab_channel=SECRETGUEST :3

#if __name__ == '__main__':
#    app = QApplication([])
#    converter = imgConverter()
#    converter.show()
#    app.exec_()
