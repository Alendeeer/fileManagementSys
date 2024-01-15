***
# File Management System (ver1.0)

## Main Window  
### Buttons
- **setting**  
`Use to enter the Setting UI, where labels could be setup.`
- **Select folder**  
`To select the folder tent to manage.`
- **Scan**  
`List all the files in the selected folder.`
- **Record**  
`Recording wrote data, stored under ./data folder. Record file end up with ".hashname".`
- **Reorder**  
`Reorder the list of files due to targeting label and expecting value. (descending order)`
- **Exit**  
`Exit the system.`
### Text lines
- **Path**  
`Can not be edited. Auto-updated after selecting folder.`
- **Expectation**  
`Enter the expecting value.`
### Drop-down menu
- **Label**  
`Select target label.`
### Table
- **Folder table**  
`First column shows all the contents inside the folder, the rest of column are set as empty. Single click one of them and enter the information directly. Also, double click each single blank could open the file/folder in the first column.`

## Setting Window
- **Text line**  
`Enter the label name. Notes that the label names should be separated by space. Here's an example of setting labels for a folder storing research articles: `
    >Genre PublishingTime CitationTimes
- **"Confirm" Button**  
`Storing set label to "setting.set" files under the root path of the programm.`

This programme has been tested under Python 3.12.1, all the required packages are summa rized in requirements.txt. 

---
## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
