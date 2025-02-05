from enum import Enum

Usage = Enum("Usage", ["SINGLE_CELL", "MULTI_CELL"])

### WARNING: DO NOT EDIT THIS FILE ABOVE THIS LINE! ###

usage = Usage.SINGLE_CELL
acquisition_frequency = 50
pacing_frequency = 1
apply_photo_bleach_correction = True
beginning_frames_removed = 1
max_pacing_deviation = 0.1
good_snr = False
quiet = True
save_tau_fittings = True

extract_traces = True

videos_directory = "samples/dataset1_RGECO_SingleCell"

trace_path = "samples/dataset1_RGECO_SingleCell/pycaltrack_analysis/calcium_traces.xlsx"
