## Workflow Summary

The project follows a four-step workflow:

1. **Prepare Input Data**  
   - Collect text inputs for the interview.  
   - Place all text files in the `data/` folder.

2. **Generate TTS Segments**  
   - Run `tts_generate.py` to convert text into individual audio files.  
   - Ensure all dependencies like `edge_tts` are installed.

3. **Combine Audio Segments**  
   - Run `mix_interviews.py` to merge all TTS segments into a single audio file.  
   - Output is saved in the `data/output/` folder.

4. **Verify Output**  
   - Listen to the final audio mix.  
   - Ensure all segments are included and properly synchronized.

