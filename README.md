# Research Task 6 — AI “Deep Fake” Interview 

## Overview
This project demonstrates the process of generating interview mixes using Python scripts. The goal of this assignment was to automate the creation of interview audio files by combining multiple text-to-speech segments. It involves handling dependencies, running scripts, and troubleshooting errors during execution.

## Workflow Summary

The project follows a four-step workflow:

1. **Draft your interview script**
- Keep it **60–120 seconds** (8–16 lines total).
- Use clear speaker labels: `INTERVIEWER:` / `EXPERT:`
- Put your script into `script_example.txt` or replace it with your own.

2. **Generate audio with `edge-tts`**
- Install dependencies (in a fresh virtual environment is recommended):

```bash
pip install edge-tts pydub
# pydub needs ffmpeg on your system PATH (download/install ffmpeg, then reopen terminal)
```

3. **Generate TTS Segments**  
- Run `tts_generate.py` to convert text into individual audio files.
- Ensure all dependencies like `edge_tts` are installed.

4. **Combine Audio Segments**  
- Run the script:
```bash
python tts_generate.py --script script_example.txt   --voice_a en-US-JennyNeural --voice_b en-GB-RyanNeural   --out         outputs/interview_mix.mp3
```
- Output is saved in the `data/output/` folder.

5. **Verify Output**  
- Listen to the final audio mix.  
- Ensure all segments are included and properly synchronized.

## Ethics & Disclosure (include in video/audio description)

- “This interview is **AI-generated** for academic purposes.”  
- “No private individual’s identity was used without consent.”  
- “Voices are synthetic; any resemblance is coincidental.”
