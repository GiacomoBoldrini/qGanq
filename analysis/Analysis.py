import numpy as np
import math as mt
from Creators.image_creator import image_creator
from Utils.plot_image import plot_image, plot_images
from Utils.generic_utils import mkdir_p
import ROOT 

#creating saving repo

save_path = "./data_general"
mkdir_p(save_path)

#importing libraries to read Delphes tree
ROOT.gSystem.Load("/Users/bcoder/MG5_aMC_v2_6_6/Delphes/libDelphes.so")
ROOT.gSystem.Load("/Users/bcoder/MG5_aMC_v2_6_6/Delphes/libDelphes.so")
ROOT.gSystem.Load("/Users/bcoder/MG5_aMC_v2_6_6/Delphes/external/libExRootAnalysis.so")
ROOT.gInterpreter.Declare('#include "/Users/bcoder/MG5_aMC_v2_6_6/ExRootAnalysis/ExRootAnalysis/ExRootTreeReader.h"')
ROOT.gInterpreter.Declare('#include "/Users/bcoder/MG5_aMC_v2_6_6/Delphes/classes/SortableObject.h"')
ROOT.gInterpreter.Declare('#include "/Users/bcoder/MG5_aMC_v2_6_6/Delphes/classes/DelphesClasses.h"')
ROOT.gInterpreter.Declare('#include "/Users/bcoder/MG5_aMC_v2_6_6/ExRootAnalysis/ExRootAnalysis/ExRootTreeReader.h"')
ROOT.gInterpreter.Declare('#include "/Users/bcoder/MG5_aMC_v2_6_6/ExRootAnalysis/ExRootAnalysis/ExRootTask.h"')
ROOT.gInterpreter.Declare('#include "/Users/bcoder/MG5_aMC_v2_6_6/Delphes/classes/SortableObject.h"')
ROOT.gInterpreter.Declare('#include "/Users/bcoder/MG5_aMC_v2_6_6/Delphes/classes/DelphesClasses.h"')

path_to_events = ['/Users/bcoder/qGanq/generation/pp_qq_jet_events/pp_qq_1.root']

event_info = image_creator.Jet_Pt_dist(path_to_events, n_ev = 10000)

#ECAL Pseudorapidity coverage in the endcap 1 < |eta| < 3
event_im = image_creator.create_CMS_image(event_info , bins=240, eta=[-3, 3], phi=[-3.14, 3.14])
np.save(save_path+"/events_im.npy", event_im)

mkdir_p("./images")

plot_images(event_im, normalized = False, Save = True, outpath = "./images", title = "event jet energy dist")




