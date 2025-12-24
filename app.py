import gradio as gr
import time

# Ultra-Dark Hacking CSS
css = """
body { 
    background-color: #000b00; 
    color: #00ff41; 
    font-family: 'Courier New', monospace;
}
.gradio-container {
    border: 3px solid #00ff41 !important;
    background: rgba(0, 20, 0, 0.9);
    box-shadow: 0 0 30px #00ff41;
}
input, button, .output-video {
    border: 1px solid #00ff41 !important;
    background-color: #051a05 !important;
    color: #00ff41 !important;
}
#title { text-align: center; text-shadow: 0 0 15px #00ff41; }
"""

def hacking_process(video):
    # Fake Hacking Logs for Visuals
    logs = [
        "> INITIALIZING SYSTEM: AWAIS MAYO HACKER...",
        "> ACCESSING ENCRYPTED LAYERS...",
        "> WATERMARK SIGNATURE DETECTED...",
        "> BYPASSING SECURITY PROTOCOLS...",
        "> DECRYPTING VIDEO FRAMES...",
        "> SUCCESS: WATERMARK NEUTRALIZED."
    ]
    
    current_log = ""
    for log in logs:
        current_log += log + "\n"
        yield current_log, None  # Sirf logs dikhaye ga pehle
        time.sleep(0.8)
    
    # Final Output
    yield current_log, video

with gr.Blocks(css=css) as demo:
    gr.HTML("<h1 id='title'>🛡️ AWAIS MAYO HACKER - TERMINAL v2.0 🛡️</h1>")
    
    with gr.Row():
        with gr.Column():
            input_vid = gr.Video(label="SOURCE_FILE.mp4")
            start_btn = gr.Button("RUN HACKING SCRIPT")
        
        with gr.Column():
            log_output = gr.Textbox(label="SYSTEM_LOGS", lines=10, interactive=False)
            output_vid = gr.Video(label="DECRYPTED_OUTPUT.mp4")

    start_btn.click(
        hacking_process, 
        inputs=input_vid, 
        outputs=[log_output, output_vid]
    )

if __name__ == "__main__":
    demo.launch()
      
