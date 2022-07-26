import py_dss_interface

dss = py_dss_interface.DSSDLL(dll_folder_param="/home/enacom/.local/share/applications/wine/Programs")
dssfile = '/home/enacom/PycharmProjects/ufjf/PandaPower/lw05e_3f.dss'
dss.text(f"compile {dssfile}")
dss.solution_solve()
dss.text(f"")