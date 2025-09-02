# Process Log – Research Task 6

This file documents the step-by-step process of creating the AI-generated deep fake interview.

## Step 1: Project Setup
- Created folder structure (`deepfake_task6` with subfolders: outputs, segments, logs).
- Installed dependencies: `edge-tts`, `pydub`, and `ffmpeg`.

## Step 2: Script Creation
- Wrote dialogue between INTERVIEWER and EXPERT in `script_example.txt`.
- Script was based on Formula 1 sprint race dataset analysis.

## Step 3: Audio Generation
- Ran `tts_generate.py` with two neural voices.
- Generated per-line segments in `segments/` and combined them into one file in `outputs/interview_mix.mp3`.

## Step 4: Challenges
- Voice timing between segments required manual pauses (added 500ms silence).
- Installing ffmpeg was necessary for audio processing.

## Step 5: Results
- Successfully generated a 1–2 minute AI interview in audio form.
- Interview realistically mimics a Q&A session.

## Step 6: Next Steps
- Optionally add background noise or video overlay to simulate a street interview.
- Explore free tools for lip-sync video if time allows.

