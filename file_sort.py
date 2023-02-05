# Working on parsing

import argparse
def file_sort(path,copy_path):
    import os
    import time
    import shutil
    import logging

    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
    def setup_logger(name, log_file, level=logging.INFO):
        """To set up as many loggers as you want"""
        handler = logging.FileHandler(log_file)
        handler.setFormatter(formatter)
        logger = logging.getLogger(name)
        logger.setLevel(level)
        if logger.handlers:
            logger.handlers = []
        logger.addHandler(handler)

        return logger

    dirs ={}
    def find_dirs(path):
        dirs[path] = []
        for i in os.listdir(path):
            if os.path.isdir(path+"\\"+i):
                dirs[path].append(path+"\\"+i)
            else:
                pass
        if path in dirs:
            for i in dirs[path]:
                find_dirs(i)
        else:
            pass
        
        return list(dirs.keys())
    all_dirs=find_dirs(path)
    log_file = open("log.log", "a")
    find_dirs_log = setup_logger("find_dirs",log_file= "log.log", level = logging.INFO)
    find_dirs_log.log(level=logging.INFO,msg="all Dirs Found")
    log_file.close()

    # Fuction to make dir with date and path 
    def mapping(path):
        file_location = []
        for j in all_dirs:
            a = os.listdir(j)
            for i in range(len(a)):
                if os.path.isdir(a[i]):
                    pass
                else:               
                    file_path = j + "\\" + a[i]
                    if os.path.isdir(file_path):
                        pass
                    else:
                        file_location.append(file_path)
        return(file_location)
    map = mapping(path)
    log_file = open("log.log", "a")
    mapping_log = setup_logger("mapping",log_file= "log.log", level = logging.INFO)
    mapping_log.log(level=logging.INFO,msg="all Files Found")
    log_file.close()

    # use the dir list to find dates of file in them
    def chr_date(path):
        cr_date = {}
        data = map
        for i in data:
            if os.path.isfile(i):
                cr_T=(os.path.getmtime(i))
                cr_time = time.ctime(cr_T)
                cr_t_obj = time.strptime(cr_time)
                date = time.strftime("%Y-%m-%d", cr_t_obj)
                file_path = i
                if date in cr_date.keys():
                    cr_date[date].append(file_path)
                else:
                    cr_date[date]=[file_path]
        return(cr_date)
    dates = chr_date(path)
    log_file = open("log.log", "a")
    chr_date_log = setup_logger("Chr_date",log_file= "log.log", level = logging.INFO)
    chr_date_log.log(level=logging.INFO,msg="all files Found with path and cr_dates")
    log_file.close()

    #  sorts the files by the data given by chr_date() fuction
    def copy_file(scr_path,copy_path):
        os.chdir(copy_path)
        cr_date = dates
        fol_name = list(cr_date.keys())
        for i in cr_date.keys():
            f_list = cr_date[i]
            # print(f_list)
            current_directory = os.getcwd()
            v_format=(
    '.264', '.3g2', '.3gp', '.3gp2', '.3gpp', '.3gpp2', '.3mm', '.3p2', '.60d', '.787', '.89', '.aaf', '.aec', '.aep', '.aepx',
    '.aet', '.aetx', '.ajp', '.ale', '.am', '.amc', '.amv', '.amx', '.anim', '.aqt', '.arcut', '.arf', '.asf', '.asx', '.avb',
    '.avc', '.avd', '.avi', '.avp', '.avs', '.avs', '.avv', '.axm', '.bdm', '.bdmv', '.bdt2', '.bdt3', '.bik', '.bin', '.bix',
    '.bmk', '.bnp', '.box', '.bs4', '.bsf', '.bvr', '.byu', '.camproj', '.camrec', '.camv', '.ced', '.cel', '.cine', '.cip',
    '.clpi', '.cmmp', '.cmmtpl', '.cmproj', '.cmrec', '.cpi', '.cst', '.cvc', '.cx3', '.d2v', '.d3v', '.dat', '.dav', '.dce',
    '.dck', '.dcr', '.dcr', '.ddat', '.dif', '.dir', '.divx', '.dlx', '.dmb', '.dmsd', '.dmsd3d', '.dmsm', '.dmsm3d', '.dmss',
    '.dmx', '.dnc', '.dpa', '.dpg', '.dream', '.dsy', '.dv', '.dv-avi', '.dv4', '.dvdmedia', '.dvr', '.dvr-ms', '.dvx', '.dxr',
    '.dzm', '.dzp', '.dzt', '.edl', '.evo', '.eye', '.ezt', '.f4p', '.f4v', '.fbr', '.fbr', '.fbz', '.fcp', '.fcproject',
    '.ffd', '.flc', '.flh', '.fli', '.flv', '.flx', '.gfp', '.gl', '.gom', '.grasp', '.gts', '.gvi', '.gvp', '.h264', '.hdmov',
    '.hkm', '.ifo', '.imovieproj', '.imovieproject', '.ircp', '.irf', '.ism', '.ismc', '.ismv', '.iva', '.ivf', '.ivr', '.ivs',
    '.izz', '.izzy', '.jss', '.jts', '.jtv', '.k3g', '.kmv', '.ktn', '.lrec', '.lsf', '.lsx', '.m15', '.m1pg', '.m1v', '.m21',
    '.m21', '.m2a', '.m2p', '.m2t', '.m2ts', '.m2v', '.m4e', '.m4u', '.m4v', '.m75', '.mani', '.meta', '.mgv', '.mj2', '.mjp',
    '.mjpg', '.mk3d', '.mkv', '.mmv', '.mnv', '.mob', '.mod', '.modd', '.moff', '.moi', '.moov', '.mov', '.movie', '.mp21',
    '.mp21', '.mp2v', '.mp4', '.mp4v', '.mpe', '.mpeg', '.mpeg1', '.mpeg4', '.mpf', '.mpg', '.mpg2', '.mpgindex', '.mpl',
    '.mpl', '.mpls', '.mpsub', '.mpv', '.mpv2', '.mqv', '.msdvd', '.mse', '.msh', '.mswmm', '.mts', '.mtv', '.mvb', '.mvc',
    '.mvd', '.mve', '.mvex', '.mvp', '.mvp', '.mvy', '.mxf', '.mxv', '.mys', '.ncor', '.nsv', '.nut', '.nuv', '.nvc', '.ogm',
    '.ogv', '.ogx', '.osp', '.otrkey', '.pac', '.par', '.pds', '.pgi', '.photoshow', '.piv', '.pjs', '.playlist', '.plproj',
    '.pmf', '.pmv', '.pns', '.ppj', '.prel', '.pro', '.prproj', '.prtl', '.psb', '.psh', '.pssd', '.pva', '.pvr', '.pxv',
    '.qt', '.qtch', '.qtindex', '.qtl', '.qtm', '.qtz', '.r3d', '.rcd', '.rcproject', '.rdb', '.rec', '.rm', '.rmd', '.rmd',
    '.rmp', '.rms', '.rmv', '.rmvb', '.roq', '.rp', '.rsx', '.rts', '.rts', '.rum', '.rv', '.rvid', '.rvl', '.sbk', '.sbt',
    '.scc', '.scm', '.scm', '.scn', '.screenflow', '.sec', '.sedprj', '.seq', '.sfd', '.sfvidcap', '.siv', '.smi', '.smi',
    '.smil', '.smk', '.sml', '.smv', '.spl', '.sqz', '.srt', '.ssf', '.ssm', '.stl', '.str', '.stx', '.svi', '.swf', '.swi',
    '.swt', '.tda3mt', '.tdx', '.thp', '.tivo', '.tix', '.tod', '.tp', '.tp0', '.tpd', '.tpr', '.trp', '.ts', '.tsp', '.ttxt',
    '.tvs', '.usf', '.usm', '.vc1', '.vcpf', '.vcr', '.vcv', '.vdo', '.vdr', '.vdx', '.veg','.vem', '.vep', '.vf', '.vft',
    '.vfw', '.vfz', '.vgz', '.vid', '.video', '.viewlet', '.viv', '.vivo', '.vlab', '.vob', '.vp3', '.vp6', '.vp7', '.vpj',
    '.vro', '.vs4', '.vse', '.vsp', '.w32', '.wcp', '.webm', '.wlmp', '.wm', '.wmd', '.wmmp', '.wmv', '.wmx', '.wot', '.wp3',
    '.wpl', '.wtv', '.wve', '.wvx', '.xej', '.xel', '.xesc', '.xfl', '.xlmv', '.xmv', '.xvid', '.y4m', '.yog', '.yuv', '.zeg',
    '.zm1', '.zm2', '.zm3', '.zmv'  )
            if fol_name in os.listdir():
                for j in range(len(f_list)):
                    file_name = f_list[j]
                    if os.path.isdir(file_name):
                        pass
                    else:
                        if file_name.endswith(v_format):
                            v_copy_path=copy_path + "\\"+ i+"\\video"
                            # if path exist copy the file
                            if v_copy_path in os.listdir:
                                shutil.copyfile(file_name,v_copy_path)
                                if os.stat(file_name).st_size == os.stat(i_copy_path+"\\"+os.path.basename(cr_date[i][j])).st_size:
                                    # os.remove(file_name)
                                    log_file = open("log.log", "a")
                                    copy_file_log = setup_logger("copy_file",log_file= "log.log", level = logging.INFO)
                                    copy_file_log.log(level=logging.INFO,msg="v_copy_done and Scr_file removed")
                                    log_file.close()
                                    print(True)
                        # if path does not exist make the path then copy
                            else:
                                os.makedirs(i+"\\video")
                                shutil.copyfile(file_name,v_copy_path)
                                if os.stat(file_name).st_size == os.stat(i_copy_path+"\\"+os.path.basename(cr_date[i][j])).st_size:
                                    # os.remove(file_name)
                                    log_file = open("log.log", "a")
                                    copy_file_log = setup_logger("copy_file",log_file= "log.log", level = logging.INFO)
                                    copy_file_log.log(level=logging.INFO,msg="v_fol_made_&_copy_done and Scr_file removed")
                                    log_file.close()
                                    print(True)
                        # move the file_name in fol_name\\video
                        else:
                            i_copy_path=copy_path + "\\"+ i+"\\img"
                            #  if path exist then copy
                            if i_copy_path in os.listdir:
                                shutil.copyfile(file_name,i_copy_path)
                                if os.stat(file_name).st_size == os.stat(i_copy_path+"\\"+os.path.basename(cr_date[i][j])).st_size:
                                    # os.remove(file_name)
                                    log_file = open("log.log", "a")
                                    copy_file_log = setup_logger("copy_file",log_file= "log.log", level = logging.INFO)
                                    copy_file_log.log(level=logging.INFO,msg="i_copy_done and Scr_file removed")
                                    log_file.close()
                                    print(True)
                            #  if path do not exist then make path and them copy
                            else:
                                os.mkdir(i+"\\img")
                                shutil.copyfile(file_name,i_copy_path)
                                if os.stat(file_name).st_size == os.stat(i_copy_path+"\\"+os.path.basename(cr_date[i][j])).st_size:
                                    # os.remove(file_name)
                                    log_file = open("log.log", "a")
                                    copy_file_log = setup_logger("copy_file",log_file= "log.log", level = logging.INFO)
                                    copy_file_log.log(level=logging.INFO,msg="i_fol_made_&_copy_done and Scr_file removed")
                                    log_file.close()
                                    print(True)
                            # move the file_name in fol_name\\img
            else:
                os.makedirs(i,exist_ok=True)
                log_file = open("log.log", "a")
                copy_file_log = setup_logger("copy_file",log_file= "log.log", level = logging.INFO)
                copy_file_log.log(level=logging.INFO,msg="nw_fol"+i+" md")
                log_file.close()
                for j in range(len(f_list)):
                    file_name = f_list[j]
                    if os.path.isdir(file_name):
                        pass
                    else:    
                        if file_name.endswith(v_format):
                            v_copy_path=copy_path + "\\"+i+"\\video"
                            # if path exist copy the file
                            dir_list=os.listdir()
                            if v_copy_path in dir_list:
                                shutil.copyfile(file_name,v_copy_path)
                                if os.stat(file_name).st_size == os.stat(i_copy_path+"\\"+os.path.basename(cr_date[i][j])).st_size:
                                    # os.remove(file_name)
                                    log_file = open("log.log", "a")
                                    copy_file_log = setup_logger("copy_file",log_file= "log.log", level = logging.INFO)
                                    copy_file_log.log(level=logging.INFO,msg="v_copy_done and Scr_file removed")
                                    log_file.close()
                                    print(True)
                        # if path does not exist make the path then copy
                            else:
                                os.makedirs(i+"\\video",exist_ok=True)
                                shutil.copy(file_name,v_copy_path)
                                if os.stat(file_name).st_size == os.stat(v_copy_path+"\\"+os.path.basename(cr_date[i][j])).st_size:
                                    # os.remove(file_name)
                                    log_file = open("log.log", "a")
                                    copy_file_log = setup_logger("copy_file",log_file= "log.log", level = logging.INFO)
                                    copy_file_log.log(level=logging.INFO,msg="V_fol_made_&_copy_done and Scr_file removed")
                                    log_file.close()
                                    print(True)
                            # move the file_name in fol_name\\video
                        else:
                            i_copy_path=copy_path + "\\"+i+"\\img"
                            #  if path exist then copy
                            if i_copy_path in os.listdir():
                                shutil.copyfile(file_name,i_copy_path)
                                if os.stat(file_name).st_size == os.stat(i_copy_path+"\\"+os.path.basename(cr_date[i][j])).st_size:
                                    # os.remove(file_name)
                                    log_file = open("log.log", "a")
                                    copy_file_log = setup_logger("copy_file",log_file= "log.log", level = logging.INFO)
                                    copy_file_log.log(level=logging.INFO,msg="i_copy_done and Scr_file removed")
                                    log_file.close()
                                    print(True)
                            #  if path do not exist then make path and them copy
                            else:
                                os.makedirs(i+"\\img",exist_ok=True)
                                shutil.copy(file_name,i_copy_path)
                                if os.stat(file_name).st_size == os.stat(i_copy_path+"\\"+os.path.basename(cr_date[i][j])).st_size:
                                    # os.remove(file_name)
                                    log_file = open("log.log", "a")
                                    copy_file_log = setup_logger("copy_file",log_file= "log.log", level = logging.INFO)
                                    copy_file_log.log(level=logging.INFO,msg="i_fol_made_&_copy_done and Scr_file removed")
                                    log_file.close()
                                    print(True)
                                # move the file_name in fol_name\\img
    copy_file(scr_path= path,copy_path=copy_path)
    log_file = open("log.log", "a")
    file_sort_log = setup_logger("File_sort",log_file= "log.log", level = logging.INFO)
    file_sort_log.log(level=logging.INFO,msg="all files from scr_path are moved and are sorted in copy_path")
    log_file.close()
pars = argparse.ArgumentParser()
pars.add_argument("-p" , "--path" , action='append', help='provide the absolute path of the source folder and copy folder in a list as -p "SOURCE PATH" -p "COPY PATH"')
args = pars.parse_args()
print(args)
scrpath = args.path[0]
copypath = args.path[1]

file_sort(path= str(scrpath),copy_path=str(copypath))

# command to run the program in cmd
# pushd <absuloute path of this file> & python file_sort.py -p "D:\test" -p "D:\copy path test"  (geralized)
# pushd D:\python scripts\.pyfiles & python file_sort.py -p "D:\test" -p "D:\copy path test" (personal)