# qGanq
Deep Convolutional Generative Adversarial Network utilised to simulate dijet events at detector level. The use of GAN could resolution in a substantial reduction of time required to generate simulated events.

## Download
```
git clone https://github.com/GiacomoBoldrini/qGanq.git
```

## Mg5+Pythia Simulations
This project relies on ones ability to run bash script and a proper installation of MadGraph, Pythia (or some other tool for the non-perturbative calculation) and Delphes.
In the folder named "generation" you will find two bash scripts: mg_simu_starter.sh and delphes_simu_starter.sh.

Run the script:
```
chmod 777 mg_simu_starter.sh 
source mg_simu_starter.sh 
```


You will be asked to choose a number n of cycles of 50k event generation of events p p > q q where q stands for the four light quark/anti-quark (udcs). Pythia does not yield accurate calculation when n > 50k.
You are then asked to choose a name for the output folder of the generation. Insert please the full path either in the current folder or in some other folder.

The 6th line of mg_simu_starter opens the MG consolle with its alias. Substitute "mg5" with your alias for MadGraph.
```
mg5 <<-EOF
```

The lines:
```
set ptj 1000
set ptjmax 1100
```

do impose cuts on the transverse momentum of outgoing partons of madgraph at [1000,1100]GeV.

## Run Delphes

Once you have your particle level samples you have to run Delphes with your favourite cards. This is done by the delphes_simu_starter.sh
You will be asked to specify the full path to the .hepmc file and the full path of the .root output.
Change the last lines with the position of the Delphes executable DelphesHepMC (...Delphes/DelphesHepMC), the path to the selected card (e.g. ...Delphes/DelphesHepMC/cards/delphes_card_CMS.tcl) in your system.

```
chmod 777 delphes_simu_starter.sh
source delphes_simu_starter.sh
```

## Running Image creators

To create images for the whole events for the GAN to emulate you will need to generate some .npy arrays with the energy distributions in the detector. You can do this using Analysis.py 
```
python3 Analysis.py

```


A TChain is used to link all the .root with 50k events, you will need to specify the paths to all of them (or using glob libraries)

```
path_to_events = ['/Users/bcoder/qGanq/generation/pp_qq_jet_events/pp_qq_1.root']
```

The following line saves in an array the eta phi and pt variables for every constituents of each jet inside an event:
```

event_info = image_creator.Jet_Pt_dist(path_to_events, n_ev = 10000)
```


The following line actually creates the image as a eta-phi-pt surface. The image is intended of the whole event:
```

event_im = image_creator.create_CMS_image(event_info , bins=240, eta=[-3, 3], phi=[-3.14, 3.14])
``
