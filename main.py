import os
import sys
import hashlib
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem, QFileDialog
from ui.file_dialoge import Ui_File_dialoge
from ui.setting import Ui_Setting

# Initiate varieties
settingPath = './setting.set'
setting = ''
allFiles = []
labels = []
path = ''
num = 0


class mainWin(QWidget, Ui_File_dialoge):
    def __init__(self):
        global num, labels
        super().__init__()
        self.setupUi(self)
        self.filePath = []
        self.dir_path = None
        self.path.setReadOnly(True)
        self.exit.clicked.connect(self.pushExit)
        self.sort.clicked.connect(self.getResult)
        self.select.clicked.connect(self.getPath)
        self.search.clicked.connect(self.showTable)
        self.labelWrite.clicked.connect(self.writeLabel)
        self.table.cellDoubleClicked.connect(self.openFolder)
        self.goToSetting.clicked.connect(showSetting)
        self.setWindowTitle("File Management System (Ver: 1.0)")

        # Load setting if .txt exist
        if checkFile(settingPath, 0):
            settingT = readSetting()
            num = int(settingT[0])
            for i in range(1, int(settingT[0]) + 1):
                self.labelSelect.addItem(settingT[i])
                labels.append(settingT[i])

    def getPath(self):
        self.filePath.clear()
        path1 = QFileDialog.getExistingDirectory()
        self.path.setText(path1)
        self.filePath.append(path1)

    # Read data & print it in the table
    def showTable(self):
        global path
        try:
            self.warning.clear()
            path = self.filePath[0]
            getFiles(path)
            if num != 0 and labels != []:
                row = len(allFiles)
                col = len(labels)
                self.table.setRowCount(row + 1)
                self.table.setColumnCount(col + 1)
                self.table.setItem(0, 0, QTableWidgetItem('Filename\\Label name'))
                # Set label name
                for r in range(0, row):
                    for c in range(0, col):
                        if r == 0 and c == 0:
                            newItem1 = QTableWidgetItem(labels[0])
                            newItem2 = QTableWidgetItem(allFiles[0][0])
                            self.table.setItem(0, 1, newItem1)
                            self.table.setItem(1, 0, newItem2)
                        else:
                            if r == 0:
                                newItem = QTableWidgetItem(labels[c])
                                self.table.setItem(0, c + 1, newItem)
                            elif c == 0:
                                newItem = QTableWidgetItem(allFiles[r][0])
                                self.table.setItem(r + 1, 0, newItem)
                            else:
                                pass
                if checkFile(path, 1):
                    for r in range(row):
                        for c in range(col):
                            try:
                                sett = getData(path)
                                newItem = QTableWidgetItem(sett[r][c])
                                self.table.setItem(r + 1, c + 1, newItem)
                            except IndexError:
                                pass
                else:
                    for r in range(row):
                        for c in range(col):
                            newItem = QTableWidgetItem(' ')
                            self.table.setItem(r + 1, c + 1, newItem)
                self.table.resizeColumnsToContents()
                allFiles.clear()
            else:
                self.warning.setText('No label was set!')
        except IndexError:
            self.warning.setText('No path was selected!')

    # Record all the entered values
    def writeLabel(self):
        saving = [[]]
        row = self.table.rowCount()
        col = self.table.columnCount()
        for r in range(2, row+1):
            for c in range(2, col+1):
                try:
                    content = self.table.item(r-1, c-1).text()
                    saving[r-2].append(content)
                except AttributeError:
                    saving[r-2].append(' ')
            saving.append([])
        saveData(path, saving)

    def openFolder(self):
        row = self.table.currentRow()
        if row != 0:
            fileName = self.table.item(row, 0).text()
            if self.filePath:
                temPath = self.filePath[0] + '/' + fileName
                os.startfile(temPath)
        else:
            pass

    def getResult(self):
        record = []         # Ture row count
        tempRecord = []     # Row count - 2
        wants = str(self.nozomi.text())
        if wants != '':
            count = 0
            choice = self.labelSelect.currentIndex() + 1
            row = self.table.rowCount() + 1
            col = self.table.columnCount() + 1
            for r in range(1, row+1):
                try:
                    currentData = str(self.table.item(r, choice).text())
                    if wants in currentData:
                        record.append(r)
                except AttributeError:
                    pass
            for r in range(1, row+1):
                tempRecord.append([])
                for c in range(col+1):
                    try:
                        content = self.table.item(r, c).text()
                        tempRecord[r-1].append(content)
                    except AttributeError:
                        pass
            for r in record:
                tempItem = tempRecord[r-1]
                tempRecord.pop(r-1)
                tempRecord.insert(count, tempItem)
                count += 1
            for i in range(1, row-1):
                for j in range(1, col):
                    try:
                        con = QTableWidgetItem(tempRecord[i-1][j-1])
                        self.table.setItem(i, j-1, con)
                    except IndexError:
                        pass
            self.table.resizeColumnsToContents()
        else:
            pass

    def pushExit(self):
        self.close()


class settingWin(QWidget, Ui_Setting):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setting.clicked.connect(self.set)
        self.setWindowTitle("Setting")

    # Amounts and names of the label
    def set(self):
        if self.labelName.text() != '':
            global num, labels, setting
            string = self.labelName.text()
            num = len(string.split())
            setting = str(num) + ' ' + string
            labels = string.split()
            self.settingInfo.setText('Succeed！')
            saveSetting(setting)
            window.labelSelect.clear()
            for i in range(num):
                window.labelSelect.addItem(labels[i])
            self.close()
        else:
            self.settingInfo.setText('No info！')


def showSetting():
    settingWindow.show()


# Record the files' name and store them in a list
def getFiles(temPath):
    global allFiles
    files = os.listdir(temPath)
    for file in files:
        allFiles.append([f'{file}'])


def checkFile(temPath, mode):
    if mode == 1:
        temPath = "./data/" + f"{getFileName(temPath)}.hashname"
    return os.path.exists(temPath)


def saveSetting(data):
    with open(settingPath, 'w', encoding='utf-8') as s:
        for d in data:
            s.write(d)
        s.close()


def readSetting():
    with open(settingPath, 'r', encoding='utf-8') as s:
        settingT = s.read()
        settingT = settingT.split()
        return settingT


def saveData(temPath, data):
    temPath = getFileName(temPath)
    with open(f'./data/{temPath}.hashname', 'w', encoding='utf-8') as f:
        for i in range(len(data)):
            for j in range(len(data[i])):
                try:
                    f.write(data[i][j])
                    if j != len(data[i]) - 1:
                        f.write(',')
                except IndexError:
                    pass
            f.write('\n')
        f.close()


def getData(temPath):
    setLabel = []
    temPath = getFileName(temPath)
    with open(f'./data/{temPath}.hashname', 'r', encoding='utf-8') as f:
        data = f.read()
        data = data.splitlines()
        for line in data:
            setLabel.append(line.split(','))
        f.close()
    return setLabel


def getFileName(string):
    return hashlib.sha224(string.encode('utf-8')).hexdigest()


if __name__ == "__main__":
    if not os.path.exists("./data"):
        os.mkdir("./data")

    app = QApplication(sys.argv)
    window = mainWin()
    settingWindow = settingWin()
    window.show()
    sys.exit(app.exec())
