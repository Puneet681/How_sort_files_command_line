from flask import Flask, render_template, request
import webbrowser
import File_Sort_V3 as FS

app = Flask(__name__)


def main(path=str,main_copy_path=str, Remove = bool):
    all_dirs = FS.find_dirs(path)
    maped = FS.mapping(all_dirs=all_dirs)
    cr_date = FS.chr_date(maped)
    n_scr_copy_path = FS.file_scr_copy_path(copy_path=main_copy_path, cr_date=cr_date)
    FS.copy_file(n_scr_copy_path,main_copy_path,Remove)
    log_file = open("log.log", "a")
    file_sort_log = FS.setup_logger("File_sort",log_file= "log.log", level = FS.logging.INFO)
    file_sort_log.log(level=FS.logging.INFO,msg="all files from scr_path are moved and are sorted in copy_path")
    log_file.close()
    scr_files_count = len([n_scr_copy_path[i][0] for i in range(len(n_scr_copy_path))])
    scr_files_count = len([n_scr_copy_path[i][1] for i in range(len(n_scr_copy_path))])
    if Remove == True:
        return (f"Files Count: {scr_files_count} Copied Files Count: {scr_files_count} and Source Files have been Removed")
    else:
        return (f"Files Count: {scr_files_count} Copied Files Count: {scr_files_count}")
    # return Remove


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        str1 = request.form['string1']
        str2 = request.form['string2']
        Remove = 'Remove' in request.form
        result = main(str1, str2, Remove)
        # main(str1, str2)
        return render_template('index.html', result=result)
    else:
        return render_template('index.html', result=None)

if __name__ == '__main__':
    webbrowser.open_new('http://127.0.0.1:5000/')
    app.run() 