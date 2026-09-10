"""
HubX AI Applications Suite - Verification & Example Usage
"""
from client import HubXClient

def main():
    print("==========================================================")
    print("  TESTING HUBX AI APPS SUITE AGENT SKILL")
    print("==========================================================")
    client = HubXClient()

    # 1. Nova Chatbot
    print("\n[1/5] Testing Nova All-in-One AI Chatbot...")
    nova_res = client.nova_chat(
        prompt="Explain the key benefits of agentic commerce in 2 sentences.",
        model="gpt-4o"
    )
    print(f"  App      : {nova_res['app']}")
    print(f"  Model    : {nova_res['model_routed']}")
    print(f"  Response : {nova_res['response']}")

    # 2. PlantApp Botanical Identifier
    print("\n[2/5] Testing PlantApp Botanical Diagnosis...")
    plant_res = client.plant_identify(
        image_url="https://images.unsplash.com/photo-1545241047-6083a3684587?w=600",
        check_disease=True
    )
    print(f"  Identified Species : {plant_res['species']} (Confidence: {plant_res['confidence_score']*100}%)")
    print(f"  Diagnosis          : {plant_res['health_status']}")
    print(f"  First Treatment    : {plant_res['treatment_suggestions'][0]}")

    # 3. DaVinci AI Art Generator
    print("\n[3/5] Testing DaVinci AI Art Generator...")
    art_res = client.davinci_generate_art(
        prompt="Futuristic botanical conservatory inside a glass dome on Mars",
        style="Cyberpunk Synthwave",
        aspect_ratio="1:1"
    )
    print(f"  Artwork ID  : {art_res['artwork_id']}")
    print(f"  Render URL  : {art_res['image_url']}")
    print(f"  Gallery Link: {art_res['community_share_url']}")

    # 4. NoteAI Meeting Intelligence
    print("\n[4/5] Testing NoteAI Meeting Summarization...")
    note_res = client.noteai_summarize_meeting(
        meeting_title="HubX Ecosystem Expansion Strategy",
        transcript_or_audio_url="https://storage.hubx.co/recordings/expansion_call.wav"
    )
    print(f"  Meeting : {note_res['meeting_title']}")
    print(f"  Summary : {note_res['executive_summary']}")
    print(f"  Action 1: {note_res['action_items'][0]['task']} -> {note_res['action_items'][0]['assignee']}")

    # 5. BetterSpeak Language Practice
    print("\n[5/5] Testing BetterSpeak Language Tutor...")
    speak_res = client.betterspeak_evaluate_dialogue(
        user_audio_text="Buenos días, me gustaría un café con leche y una tostada por favor.",
        target_language="Spanish",
        scenario="Cafe Breakfast"
    )
    print(f"  Scenario     : {speak_res['scenario']}")
    print(f"  Fluency Score: {speak_res['fluency_score_pct']}%")
    print(f"  Avatar Reply : {speak_res['avatar_reply']}")

    print("\n==========================================================")
    print("  ALL 5 HUBX AI APPS TESTED AND OPERATIONAL ✓")
    print("==========================================================")

if __name__ == "__main__":
    main()
