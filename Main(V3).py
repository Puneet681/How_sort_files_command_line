import File_Sort_V3 as FS
import argparse

def main(path,main_copy_path,Remove):
    all_dirs = FS.find_dirs(path)
    maped = FS.mapping(all_dirs=all_dirs)
    cr_date = FS.chr_date(maped)
    n_scr_copy_path = FS.file_scr_copy_path(copy_path=main_copy_path, cr_date=cr_date)
    FS.copy_file(n_scr_copy_path,main_copy_path,Remove)
    log_file = open("log.log", "a")
    file_sort_log = FS.setup_logger("File_sort",log_file= "log.log", level = FS.logging.INFO)
    file_sort_log.log(level=FS.logging.INFO,msg="all files from scr_path are moved and are sorted in copy_path")
    log_file.close()
    


pars = argparse.ArgumentParser()
pars.add_argument("-p" , "--path" , action='append', help='provide the absolute path of the source folder and copy folder in a list as -p "SOURCE PATH" -p "COPY PATH"')
args = pars.parse_args()
print(args)
s_path = args.path[0]
c_path = args.path[1]


if __name__ =='__main__':
    s_path = "d:\\test"
    c_path="d:\\copy_path_test"
    main(path=s_path ,main_copy_path=c_path,Remove=True)



# command to run the program in cmd
# pushd <absuloute path of this file> & python Main.py -p "D:\test" -p "D:\copy path test"  (geralized)

# pushd D:\python scripts\projects\How_sort_files_from_command_line & python Main.py -p "D:\test" -p "D:\copy path test" (Only for personal Use)
 