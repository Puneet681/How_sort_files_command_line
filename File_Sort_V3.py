# working on version 3 (have a bug)

import os
import time
import shutil
import logging
import sys

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
    for dir in os.listdir(path):
        if os.path.isdir(path+"\\"+dir):
            dirs[path].append(path+"\\"+dir)
        else:
            pass
    if path in dirs:
        for dir in dirs[path]:
            find_dirs(dir)
    else:
        pass
    log_file = open("log.log", "a")
    find_dirs_log = setup_logger("find_dirs",log_file= "log.log", level = logging.INFO)
    find_dirs_log.log(level=logging.INFO,msg="all Dirs Found")
    log_file.close()
    return list(dirs.keys())


# Fuction to make dir with date and path 
def mapping(all_dirs):

    file_location = []
    for i in all_dirs:
        a = os.listdir(i)
        for j in range(len(a)):
            if os.path.isdir(a[j]):
                pass
            else:               
                file_path = i + "\\" + a[j]
                if os.path.isdir(file_path):
                    pass
                else:
                    file_location.append(file_path)
    log_file = open("log.log", "a")
    mapping_log = setup_logger("mapping",log_file= "log.log", level = logging.INFO)
    mapping_log.log(level=logging.INFO,msg="all Files Found")
    log_file.close()
    return(file_location)


# use the dir list to find dates of file in them
def chr_date(map):
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
    log_file = open("log.log", "a")
    chr_date_log = setup_logger("Chr_date",log_file= "log.log", level = logging.INFO)
    chr_date_log.log(level=logging.INFO,msg="all files Found with path and cr_dates")
    log_file.close()
    return(cr_date)

## Following Fuction have Bug (FIXED)
def file_scr_copy_path(copy_path, cr_date):
    new_copy_path = []
    file_name_list = []
    file_name_ext = []
    formats ={"Video" : [
    ".264", ".3g2", ".3gp", ".3gp2", ".3gpp", ".3gpp2", ".3mm", ".3p2", ".60d", ".787", ".89", ".aaf", ".aec", ".aep", ".aepx",
    ".aet", ".aetx", ".ajp", ".ale", ".am", ".amc", ".amv", ".amx", ".anim", ".aqt", ".arcut", ".arf", ".asf", ".asx", ".avb",
    ".avc", ".avd", ".avi", ".avp", ".avs", ".avs", ".avv", ".axm", ".bdm", ".bdmv", ".bdt2", ".bdt3", ".bik", ".bin", ".bix",
    ".bmk", ".bnp", ".box", ".bs4", ".bsf", ".bvr", ".byu", ".camproj", ".camrec", ".camv", ".ced", ".cel", ".cine", ".cip",
    ".clpi", ".cmmp", ".cmmtpl", ".cmproj", ".cmrec", ".cpi", ".cst", ".cvc", ".cx3", ".d2v", ".d3v", ".dat", ".dav", ".dce",
    ".dck", ".dcr", ".dcr", ".ddat", ".dif", ".dir", ".divx", ".dlx", ".dmb", ".dmsd", ".dmsd3d", ".dmsm", ".dmsm3d", ".dmss",
    ".dmx", ".dnc", ".dpa", ".dpg", ".dream", ".dsy", ".dv", ".dv-avi", ".dv4", ".dvdmedia", ".dvr", ".dvr-ms", ".dvx", ".dxr",
    ".dzm", ".dzp", ".dzt", ".edl", ".evo", ".eye", ".ezt", ".f4p", ".f4v", ".fbr", ".fbr", ".fbz", ".fcp", ".fcproject",
    ".ffd", ".flc", ".flh", ".fli", ".flv", ".flx", ".gfp", ".gl", ".gom", ".grasp", ".gts", ".gvi", ".gvp", ".h264", ".hdmov",
    ".hkm", ".ifo", ".imovieproj", ".imovieproject", ".ircp", ".irf", ".ism", ".ismc", ".ismv", ".iva", ".ivf", ".ivr", ".ivs",
    ".izz", ".izzy", ".jss", ".jts", ".jtv", ".k3g", ".kmv", ".ktn", ".lrec", ".lsf", ".lsx", ".m15", ".m1pg", ".m1v", ".m21",
    ".m21", ".m2a", ".m2p", ".m2t", ".m2ts", ".m2v", ".m4e", ".m4u", ".m4v", ".m75", ".mani", ".meta", ".mgv", ".mj2", ".mjp",
    ".mjpg", ".mk3d", ".mkv", ".mmv", ".mnv", ".mob", ".mod", ".modd", ".moff", ".moi", ".moov", ".mov", ".movie", ".mp21",
    ".mp21", ".mp2v", ".mp4", ".mp4v", ".mpe", ".mpeg", ".mpeg1", ".mpeg4", ".mpf", ".mpg", ".mpg2", ".mpgindex", ".mpl",
    ".mpl", ".mpls", ".mpsub", ".mpv", ".mpv2", ".mqv", ".msdvd", ".mse", ".msh", ".mswmm", ".mts", ".mtv", ".mvb", ".mvc",
    ".mvd", ".mve", ".mvex", ".mvp", ".mvp", ".mvy", ".mxf", ".mxv", ".mys", ".ncor", ".nsv", ".nut", ".nuv", ".nvc", ".ogm",
    ".ogv", ".ogx", ".osp", ".otrkey", ".pac", ".par", ".pds", ".pgi", ".photoshow", ".piv", ".pjs", ".playlist", ".plproj",
    ".pmf", ".pmv", ".pns", ".ppj", ".prel", ".pro", ".prproj", ".prtl", ".psb", ".psh", ".pssd", ".pva", ".pvr", ".pxv",
    ".qt", ".qtch", ".qtindex", ".qtl", ".qtm", ".qtz", ".r3d", ".rcd", ".rcproject", ".rdb", ".rec", ".rm", ".rmd", ".rmd",
    ".rmp", ".rms", ".rmv", ".rmvb", ".roq", ".rp", ".rsx", ".rts", ".rts", ".rum", ".rv", ".rvid", ".rvl", ".sbk", ".sbt",
    ".scc", ".scm", ".scm", ".scn", ".screenflow", ".sec", ".sedprj", ".seq", ".sfd", ".sfvidcap", ".siv", ".smi", ".smi",
    ".smil", ".smk", ".sml", ".smv", ".spl", ".sqz", ".srt", ".ssf", ".ssm", ".stl", ".str", ".stx", ".svi", ".swf", ".swi",
    ".swt", ".tda3mt", ".tdx", ".thp", ".tivo", ".tix", ".tod", ".tp", ".tp0", ".tpd", ".tpr", ".trp", ".ts", ".tsp", ".ttxt",
    ".tvs", ".usf", ".usm", ".vc1", ".vcpf", ".vcr", ".vcv", ".vdo", ".vdr", ".vdx", ".veg",".vem", ".vep", ".vf", ".vft",
    ".vfw", ".vfz", ".vgz", ".vid", ".video", ".viewlet", ".viv", ".vivo", ".vlab", ".vob", ".vp3", ".vp6", ".vp7", ".vpj",
    ".vro", ".vs4", ".vse", ".vsp", ".w32", ".wcp", ".webm", ".wlmp", ".wm", ".wmd", ".wmmp", ".wmv", ".wmx", ".wot", ".wp3",
    ".wpl", ".wtv", ".wve", ".wvx", ".xej", ".xel", ".xesc", ".xfl", ".xlmv", ".xmv", ".xvid", ".y4m", ".yog", ".yuv", ".zeg",
    ".zm1", ".zm2", ".zm3", ".zmv"  ],
    "Images" :  [".jpg",".jpeg",".png",".gif",".bmp",".tiff",".tif",".svg",".ico"],
    "Audio" : [".ape",".wv",".m4a",".wav",".aiff",".3gp",".aa",".aac",".aax",".act",".aiff",".alac",".amr",".ape",".au",".awb",
               ".dss",".dvf",".flac",".gsm",".iklax",".ivs",".m4a",".m4b",".m4p",".mmf",".mp3",".mpc",".msv",".nmf",".ogg",".oga",
               ".mogg",".oups",".ra",".rm",".raw",".rf64",".sln",".tta",".voc",".vox",".wav",".wma",".wv",".webm",".8svx",".cds"],
    "Basic_documents": [".pdf",".doc",".docx",".odt",".msg",".rtf",".tex",".txt",".csv",".wks",".wps",".wpd",".ods",".xlr",".xls",
                        ".xlsx",".key",".odp",".pps",".ppt",".pptx",".bak",".cab",".cfg",".cpl",".cur",".dll",".dmp",".drv",".icns",
                        ".ico",".ini",".ink",".msi",".sys",".tmp",".zip"]}
    for date , value in cr_date.items():
        for file_name in value:
            file_name_list.append([date,file_name])
        
        
        
    for i in range(len(file_name_list)):
        # print(i)
        file = file_name_list[i][1]
        if os.path.isdir(file):
            pass
        else:    
            split_tup = os.path.splitext(file)
            ext = str(split_tup[1])
            file_name_ext.append(str(ext))
            for key, value in formats.items():
                if isinstance(value, list) and ext in [i for i in value if i==str(ext)]:
                    path =copy_path+"\\"+(file_name_list[i][0])+"\\"+key
                    new_copy_path.append([file,path])
            
    log_file = open("log.log", "a")
    file_sort_log = setup_logger("File_sort",log_file= "log.log", level = logging.INFO)
    file_sort_log.log(level=logging.INFO,msg="files sorted by file type with requred copy path")
    log_file.close()
    return new_copy_path
                        

#  sorts the files by the data given by chr_date() fuction
def copy_file(n_scr_copy_path=dict,main_copy_path=str , Remove = bool):
    # print(Remove)
    for i in range(len(n_scr_copy_path)):
        scr_file = n_scr_copy_path[i][0]
        copy_file = n_scr_copy_path[i][1]
                
        if copy_file==[]:
            empty_copy_path = main_copy_path+"\\Uncertain"
            os.makedirs(empty_copy_path,exist_ok=True)
            log_file = open("log.log", "a")
            copy_file_log = setup_logger("copy_file",log_file= "log.log", level = logging.INFO)
            copy_file_log.log(level=logging.INFO,msg="nw_fol md")
            log_file.close()
            shutil.copy((scr_file),str(empty_copy_path))
            if os.stat(scr_file).st_size == os.stat(empty_copy_path).st_size:
                if Remove == True:
                    # print (True)
                    os.remove(scr_file)
                log_file = open("log.log", "a")
                copy_file_log = setup_logger("copy_file",log_file= "log.log", level = logging.INFO)
                copy_file_log.log(level=logging.INFO,msg="copy_done ")
                log_file.close()
                # print(True)
        else:
            os.makedirs(copy_file,exist_ok=True)
            log_file = open("log.log", "a")
            copy_file_log = setup_logger("copy_file",log_file= "log.log", level = logging.INFO)
            copy_file_log.log(level=logging.INFO,msg="nw_fol md")
            log_file.close()
            shutil.copy(str(scr_file),str(copy_file))
            # print(copy_file+"\\"+os.path.basename(scr_file))
            if os.stat(scr_file).st_size == os.stat(copy_file+"\\"+os.path.basename(scr_file)).st_size:
                if Remove == True:
                    # print (True)
                    os.remove(scr_file)
                log_file = open("log.log", "a")
                copy_file_log = setup_logger("copy_file",log_file= "log.log", level = logging.INFO)
                copy_file_log.log(level=logging.INFO,msg="copy_done")
                log_file.close()
                # print(True)
