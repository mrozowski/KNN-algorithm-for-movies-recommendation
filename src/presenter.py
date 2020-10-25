from PyQt5 import QtWidgets

from KNN import knn
import sys


class Presenter:
    def __init__(self, _view):
        self.raw_data = []
        self.view = _view
        self.load_raw_data()
        self.movies_list = []
        self.recommended = []

    def load_raw_data(self):
        """"Load movies data from csv file"""
        path = "../Data/movies_list.csv"
        with open(path, 'r') as md:
            next(md)  # read the headings
            for line in md.readlines():
                data_row = line.strip().split(',')
                self.raw_data.append(data_row)

    def set_list(self):
        """get the title from raw data and add it to widget list"""
        for a in self.raw_data:
            self.movies_list.append(a[1])
        self.view.listWidget.addItems(self.movies_list)

    def on_button_clicked(self):
        selected_item = self.view.listWidget.currentItem().text()  # get title of selected movie
        index = self.movies_list.index(selected_item)              # get the index if this movie
        prepared_data = self.prepare_data()                        # process raw data for KNN
        result = self.get_recommended_movies(prepared_data, prepared_data[index])
        self.save_recommendation(result)
        self.show_result()

    def prepare_data(self):
        """Delete id and title of movie from database"""
        processed_data = []
        for row in self.raw_data:
            data_row = list(map(float, row[2:]))
            processed_data.append(data_row)
        return processed_data

    def show_result(self):
        """Show result on the GUI"""
        i = 0
        for a in self.recommended:
            self.view.recom[i].setText(a)
            self.view.recom[i].show()
            i += 1

    def get_recommended_movies(self, data, fav_movie):
        """Run the k-nearest neighbors algorithm"""
        recommended_movies = knn(data, fav_movie, k=5)
        return recommended_movies

    def save_recommendation(self, result):
        """Save recommended movie titles to local variable"""
        self.recommended = []
        for a in result:
            self.recommended.append(self.movies_list[a[1]])
            #print(a)

    def run(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.view.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())