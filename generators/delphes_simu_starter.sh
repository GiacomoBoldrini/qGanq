echo "insert path to .hepmc"
read in_hepmc_path

echo "insert full path to output .root"
echo out_root_path

/Users/bcoder/MG5_aMC_v2_6_6/Delphes/DelphesHepMC /Users/bcoder/MG5_aMC_v2_6_6/Delphes/cards/delphes_card_CMS.tcl out_root_path in_hepmc_path
