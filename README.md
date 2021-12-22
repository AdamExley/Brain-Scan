# Brain-Scan
 
This repository is designed to facilitate creating 3D brain representations from fMRI scan videos.

It is *very* basic and many things are hard-coded.


## Use

Place a .mp4 file of an fMRI scan in `/scans/`.

In `run.py`, change the Extractor's args for `run_and_cvt` to your file.

The second arg is the crop factor, this is best changed with trial and error (change crop and run until you get expected area extracted)

This will then bring up a 3D model of your brain. Slicing the `frames` variable will slice this model.
