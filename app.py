import os
import gradio as gr

PLATFORM_LIMITS = {'Google Ads Headline': 30, 'Google Ads Description': 90, 'Meta Ad Primary Text': 125, 'Meta Ad Headline': 40, 'Meta Ad Link Description': 30}

def check_ad_copy(text, platform):
    limit = PLATFORM_LIMITS.get(platform, 30)
    length = len(text)
    fits = length <= limit
    remaining = limit - length
    status = 'FITS' if fits else 'TOO LONG'
    report = 'Platform: ' + platform + ' | Limit: ' + str(limit) + ' chars | Your length: ' + str(length) + ' | Status: ' + status + ' | Remaining: ' + str(remaining)
    return report

demo = gr.Interface(fn=check_ad_copy, inputs=[gr.Textbox(placeholder='Enter your ad headline or copy...', label='Ad Copy'), gr.Dropdown(choices=list(PLATFORM_LIMITS.keys()), value='Google Ads Headline', label='Platform')], outputs=gr.Textbox(label='Result'), title='Ad Copy Length Checker', description='Check if ad headlines or copy fit platform character limits for Google Ads and Meta Ads')

demo.launch(mcp_server=True, server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 7860)))
