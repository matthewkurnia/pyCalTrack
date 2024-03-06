from enum import Enum

Usage = Enum("Usage", ["SINGLE_CELL", "MULTI_CELL"])

### WARNING: DO NOT EDIT THIS FILE ABOVE THIS LINE! ###

usage = Usage.SINGLE_CELL
extract_traces = True
acquisition_frequency = 50
pacing_frequency = 1
beginning_frames_removed = 1
max_pacing_deviation = 0.1
good_snr = True
quiet = True

videos_directory = (
    "/home/mkurnia/uni/fyp/PyCalTrack/sample_videos/dataset1_RGECO_SingleCell"
)
