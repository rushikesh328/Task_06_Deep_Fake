import argparse
import edge_tts
import asyncio
import os
from pydub import AudioSegment

async def generate_tts(script_file, voice_a, voice_b, out_file):
    os.makedirs("segments", exist_ok=True)
    with open(script_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    segments = []
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue

        if line.startswith("INTERVIEWER:"):
            voice = voice_a
            text = line.replace("INTERVIEWER:", "").strip()
        elif line.startswith("EXPERT:"):
            voice = voice_b
            text = line.replace("EXPERT:", "").strip()
        else:
            continue

        out_segment = f"segments/seg_{i}.mp3"
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(out_segment)
        segments.append(out_segment)

    # Combine all audio segments
    final_audio = AudioSegment.empty()
    for seg in segments:
        final_audio += AudioSegment.from_mp3(seg) + AudioSegment.silent(duration=500)

    os.makedirs("outputs", exist_ok=True)
    final_audio.export(out_file, format="mp3")
    print(f"Interview audio saved to {out_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--script", required=True, help="Path to the script file")
    parser.add_argument("--voice_a", default="en-US-JennyNeural", help="Voice for INTERVIEWER")
    parser.add_argument("--voice_b", default="en-GB-RyanNeural", help="Voice for EXPERT")
    parser.add_argument("--out", default="outputs/interview_mix.mp3", help="Final output file")
    args = parser.parse_args()

    asyncio.run(generate_tts(args.script, args.voice_a, args.voice_b, args.out))
