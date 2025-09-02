# Research Task 6 — AI “Deep Fake” Interview 

## Overview
This project demonstrates the process of generating interview mixes using Python scripts. The goal of this assignment was to automate the creation of interview audio files by combining multiple text-to-speech segments. It involves handling dependencies, running scripts, and troubleshooting errors during execution.

## Workflow Summary

The project follows a four-step workflow:

1. **Prepare Input Data**  
   - Collect text inputs for the interview.  
   - Place all text files in the `data/` folder.

2. **Generate TTS Segments**  
   - Run `tts_generate.py` to convert text into individual audio files.
   - Install 'e
   - Ensure all dependencies like `edge_tts` are installed.

3. **Combine Audio Segments**  
   - Run `tts_generate.py` to merge all TTS segments into a single audio file.  
   - Output is saved in the `data/output/` folder.

4. **Verify Output**  
   - Listen to the final audio mix.  
   - Ensure all segments are included and properly synchronized.

