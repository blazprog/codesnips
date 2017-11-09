import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from PyQt5.QtSql import *

class WReferences(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        
        self.adding_flag = False
        self.edit_layout = QGridLayout()
        self.setEditControls()

        table_layout = QHBoxLayout()
        self.view = QTableView(self)
        self.model = QSqlTableModel(self)
        self.model.setTable("ref_table")
        self.model.select()
        self.view.setModel(self.model)
        self.view.setSelectionMode(QTableView.SingleSelection)
        self.view.setSelectionBehavior(QTableView.SelectRows)
        self.view.resizeColumnsToContents()
        table_layout.addWidget(self.view)   
        self.setMappings()            
        self.view.selectionModel().currentRowChanged.connect(self.row_changed)        

        buttons_layout = QHBoxLayout()
        self.pbAdd = QPushButton("Add new")
        self.pbAdd.clicked.connect(self.add_record)
        self.pbSave = QPushButton("Save")
        self.pbSave.clicked.connect(self.save_record)
        self.pbDelete = QPushButton("Delete")
        self.pbDelete.clicked.connect(self.delete_record)
        self.pbSort = QPushButton("Sort")
        self.pbSort.clicked.connect(self.sort_record)
        self.pbClose = QPushButton("Close")
        self.pbClose.clicked.connect(self.close_window)
        buttons_layout.addWidget(self.pbAdd)
        buttons_layout.addWidget(self.pbSave)
        buttons_layout.addWidget(self.pbDelete)
        buttons_layout.addWidget(self.pbSort)
        buttons_layout.addWidget(self.pbClose)
        buttons_layout.addStretch()

        main_layout = QVBoxLayout()
        main_layout.addLayout(self.edit_layout)
        main_layout.addLayout(table_layout)
        main_layout.addLayout(buttons_layout)
        self.setLayout(main_layout)
        
        self.view.setFocus()
        self.setGeometry(20,20,600,400)
    
    def setEditControls(self):
        lblid = QLabel("Refrence id")
        self.leref_id = QLineEdit()
        lblcategory = QLabel("Category")
        self.lecategory = QLineEdit()
        lblshortdesc = QLabel("Short description")
        self.leshort_description = QLineEdit()
        lbllongdesc = QLabel("Long description")
        self.lelong_description = QLineEdit()
        self.edit_layout.addWidget(lblid,0,0)
        self.edit_layout.addWidget(self.leref_id,0,1)
        self.edit_layout.addWidget(lblcategory,1,0)
        self.edit_layout.addWidget(self.lecategory,1,1)
        self.edit_layout.addWidget(lblshortdesc,2,0)
        self.edit_layout.addWidget(self.leshort_description,2,1)
        self.edit_layout.addWidget(lbllongdesc,3,0)
        self.edit_layout.addWidget(self.lelong_description,3,1)

    def setMappings(self):
        self.mapper = QDataWidgetMapper(self)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(self.model)
        self.mapper.addMapping(self.leref_id,0)
        self.mapper.addMapping(self.lecategory,1)
        self.mapper.addMapping(self.leshort_description,2)
        self.mapper.addMapping(self.lelong_description,3)
        self.mapper.toFirst()



    # Slots
    def add_record(self):
        self.adding_flag = True
        row = self.model.rowCount()
        self.mapper.submit()
        self.model.insertRow(row)
        self.mapper.setCurrentIndex(row)
        self.leref_id.setText("{}".format(row + 1))
        self.lecategory.setFocus()
    def delete_record(self):
        if QMessageBox.question(self,"Confirm", "Delete selected record",
                QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
            return

        row = self.mapper.currentIndex()
        self.model.removeRow(row)
        self.model.submitAll()
        #After deleting current record we navigate to the next record
        #if possible
        if row + 1 >= self.model.rowCount():
            row = self.model.rowCount() - 1
        self.mapper.setCurrentIndex(row)
        self.view.setModel(self.model)
        self.view.selectRow(row)

    def save_record(self):
        row = self.mapper.currentIndex()
        self.mapper.submit()
        self.mapper.setCurrentIndex(row)
        if self.adding_flag:
            self.view.selectRow(row)
        self.adding_flag = False

    def sort_record(self):
        print("Sorting records")

    def close_window(self):
        self.close()

    def row_changed(self, index):
        self.adding_flag = False
        if index.isValid():
            row = index.row()
            self.mapper.setCurrentIndex(row)
        else:
            Print("Something wrong with app and the guy who program it")
def main():
    qapp = QApplication(sys.argv)
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("pos.db")
    if not db.open():
        QMessageBox.warning(None,"References table",db.lastError.text())
        sys.exit(1)
    wrefrences = WReferences()
    wrefrences.show()
    sys.exit(qapp.exec_())

if __name__ == '__main__':
    main()


